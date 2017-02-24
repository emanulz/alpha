global.jQuery = require("jquery");
var alertify = require('alertifyjs');

// select2 = require('select2');
import $ from 'jquery';
import 'select2';                       // globally assign select2 fn to $ element

let currencySymbol = ''

export function getData(){

    //DOM CACHE
    let $general = $('.general-block');

    //SELECTORS
    let $date = $general.find('.date');
    let $currency = $general.find('.currency');


    let $exchangeRate = $general.find('.exchange-rate');

    let company = $('#id_company').val();

    let $select = $('.select-account');

    let $accountCell = $('.account-cell');

    let $table = $('.table-entry');


    setDateToday($date);

    loadData(company);

    addNewRow();

    currenciesToSelect($currency);

    $('.new-line-btn').on("click", function () {
        addNewRow();
        refreshCurrencySymbol($currency);
    });


    $table.on("select2:select",".account-cell", function (e) {

        let text = e.params.data.text
        $(this).closest('td').prepend(`<div class="account-text">
                                        <span class="account-text-span">${text}</span>
                                        <span class="glyphicon glyphicon-remove-circle remove-item" aria-hidden="true"></span>
                                      </div>`);

        $(this).closest('td').find('.detail-input').show();
        $(this).find('select').select2('destroy')
        $(this).find('select').remove();

        //test.show();

    });

    $('.currency-div').on("select2:select",".currency", function (e) {

        refreshCurrencySymbol($currency);

    });

    $table.on('click', '.remove-row', function(e){
        removeRow(this);
    });

    $table.on("click",".remove-item", function () {

        $(this).closest('td').find('.detail-input').hide();

        $(this).closest('tr').find('input').val('');

        let $td = $(this).closest('td');

        $td.append(`<select class='form-control input-sm select-account'></select>`);

        let $selectCreated = $td.find('select');

        accountsToSelect($selectCreated);

        $(this).parent().remove();

    });

    $table.on("change","input", function () {

        scanTable($table);
    });
}

function scanTable($table){

    let $rows = $table.find('tbody > tr');
    let data = []
    $rows.splice(0,1);
    $.each($rows, function (i) {

        let detail = $($rows[i]).find('.detail-input').val();
        let accountText = $($rows[i]).find('.account-text-span').html();
        let documentText = $($rows[i]).find('.document-cell input').val();
        let debe = $($rows[i]).find('.debe-cell input').val();
        let haber = $($rows[i]).find('.haber-cell input').val();

        if(debe != 0 || haber != 0){

            data.push([accountText, detail, documentText, debe, haber]);

        }

    });

    updateTotals(data);

    return data;


}

function updateTotals(data){

    let totalDebe = 0;
    let totalHaber = 0;
    let diferrence = 0;

    $.each(data, function (i) {

        totalDebe = totalDebe + parseFloat(data[i][3]);
        totalHaber = totalHaber + parseFloat(data[i][4]);
    });

    diferrence = totalDebe - totalHaber;

    $('.total-debe-val').html(totalDebe);
    $('.total-haber-val').html(totalHaber);
    $('.total-difference-val').html(diferrence);

}

function setDateToday($dateField){

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
    dd='0'+dd
    }

    if(mm<10) {
    mm='0'+mm
    }

    today = yyyy+'-'+mm+'-'+dd;

    $dateField.val(today);

}

function loadData(company){

    $.get(`/accounting/api/account_categories/?company=${company}`, function (data) {

       localStorage.account_categories = JSON.stringify(data);

    });

    $.get(`/accounting/api/accounts/?company=${company}`, function (data) {

       localStorage.accounts = JSON.stringify(data);

    });

    $.get(`/accounting/api/subaccounts/?company=${company}`, function (data) {

       localStorage.subaccounts = JSON.stringify(data);

    });

    $.get(`/accounting/api/detailaccounts/?company=${company}`, function (data) {

       localStorage.detailaccounts = JSON.stringify(data);

    });

    $.get(`/general/api/currencies/?company=${company}`, function (data) {

       localStorage.currencies = JSON.stringify(data);

    });

}

function currenciesToSelect($select) {

    let currencies = JSON.parse(localStorage.currencies);

    $.each(currencies, function (i) {

        $select.append($('<option>', {
            value: currencies[i].id,
            text: `${currencies[i].symbol} - ${currencies[i].name}`
        }));
    });

    $(() => {
      $select.select2({height:'200px'});
    });

    refreshCurrencySymbol($select);
}

function refreshCurrencySymbol($select){

    let selectedCurrency = $select.val();
    let currencies = JSON.parse(localStorage.currencies);

    let currency = $.grep(currencies, function (element, index) {
        return element.id == selectedCurrency;
    });

    $('.currency-symbol').html(currency[0].symbol)

}

function accountsToSelect($select){


    let accounts = JSON.parse(localStorage.accounts);
    let subaccounts = JSON.parse(localStorage.subaccounts);
    let detailaccounts = JSON.parse(localStorage.detailaccounts);

    $select.append($('<option>', {

    }));

    $.each(accounts, function (i) {


        let accountsDisabled = (accounts[i].movements ? '':'disabled')

        $select.append(`<option value=${accounts[i].id} ${accountsDisabled}>
                            ${accounts[i].identifier}-00-00  - ${accounts[i].name}
                            </option>`);

        let grepSubAccounts = $.grep(subaccounts, function (element, index) {
            return element.account == accounts[i].id;
        });

        let $this = this

        $this.accountId = accounts[i].identifier;

        $.each(grepSubAccounts, function (i) {

            let subAccountsDisabled = (grepSubAccounts[i].movements ? '':'disabled')


            $select.append(`<option value=${grepSubAccounts[i].id} ${subAccountsDisabled}>
                                ${$this.accountId}-${grepSubAccounts[i].identifier}-00  - ${grepSubAccounts[i].name}
                            </option>`);


            let grepDetailAccounts = $.grep(detailaccounts, function (element, index) {
                return element.subaccount == grepSubAccounts[i].id;
            });

            $this.subaccountId = grepSubAccounts[i].identifier;

            $.each(grepDetailAccounts, function (i) {

                let detailAccountsDisabled = (grepDetailAccounts[i].movements ? '':'disabled')


                $select.append(`<option value= grepDetailAccounts[i].id ${detailAccountsDisabled}>
                                    ${$this.accountId}-${$this.subaccountId}-${grepDetailAccounts[i].identifier}  - ${grepDetailAccounts[i].name}
                                </option>`);

            })

        })


    })

    $(() => {
      $select.select2({ placeholder: 'Seleccione una cuenta', width: '100%' });
    });

}

function addNewRow(){

    let template = `<tr>
                        <td class='input-cell account-cell'>
                            <select class='form-control input-sm select-account'></select>
                            <input type="text" hidden placeholder='Ingrese el detalle del asiento' class='detail-input'>
                        </td>
                        <td class='input-cell document-cell'>
                            <input type="text" class='form-control input'>
                        </td>
                        <td class='input-cell debe-cell'>
                            <div class='currency-cell'>
                                <span class="currency-symbol"> </span>
                                <input type="number" value="0" class='form-control input'>
                            </div>
                        </td>
                        <td class='input-cell haber-cell'>
                            <div class='currency-cell'>
                                <span class="currency-symbol"> </span>
                                <input type="number" value="0" class='form-control input'>
                            </div>
                            <div class='remove-row-div'>
                                <div class='remove-row-container'>
                                    <span class="glyphicon glyphicon-remove-sign remove-row" aria-hidden="true"></span>
                                </div class='form-control input'>
                            </div>
                        </td>
                    </tr>`

    $('.table-entry').append(template);

    let $addedSelect = $('.table-entry').find('tr:last').find('.select-account');

    accountsToSelect($addedSelect);


}

function removeRow($this){

    $this.closest('tr').remove();
}
