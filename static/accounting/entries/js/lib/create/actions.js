global.jQuery = require("jquery");
var alertify = require('alertifyjs');

// select2 = require('select2');
import $ from 'jquery';
import 'select2';

import{addNewRow} from './rows'
import {currenciesToSelect} from './currencies';
import {refreshCurrencySymbol} from './currencies';
import {accountsToSelect} from './accounts';

let data = []

export function actions(){

    //DOM CACHE
    let $general = $('.general-block');

    //SELECTORS

    let $exchangeRate = $general.find('.exchange-rate');

    let $currency = $general.find('.currency');

    let $select = $('.select-account');

    let $accountCell = $('.account-cell');

    let $table = $('.table-entry');


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

        data = scanTable($table);
        updateTotals(data);
    });
}

function scanTable($table){

    data = [];

    let $rows = $table.find('tbody > tr');

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
