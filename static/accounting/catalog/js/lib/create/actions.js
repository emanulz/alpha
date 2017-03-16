global.jQuery = require("jquery");
import {dataToSelect} from './dataToSelect';
import {filterLevel} from './filterLevel';
import {filterParentAccount} from './filterParentAccount';
import {generateCode} from './generateCode';
import {disableEnable} from './disableEnable';
import {drawTable} from './drawTable';
import {checks} from './checks';
import {save} from './save';

export function actions(store){

    //Selectors

    let $accountData = $('.account-data-div');
    let accounts = JSON.parse(localStorage.accounts);
    let accountlevels = JSON.parse(localStorage.accountlevels);

    //click on select level

    $accountData.on("select2:select",".level-select", function (e) {

        let text = e.params.data.text
        $(this).closest('div').append(`<div class="level-text selected-div">
                                        <span class="account-text-span">${text}</span>
                                        <span class="glyphicon glyphicon-remove-circle remove-item remove-level" aria-hidden="true"></span>
                                      </div>`);

        let $this = this;

        let selectedLevel = accountlevels.filter((obj)=>{
            return obj.id == $($this).closest('select').val();
        })

        store.selectedLevel = selectedLevel[0];

        $(this).closest('select').select2('destroy');
        $(this).closest('select').remove();
        $('.accounts-select').attr("disabled", false);

        filterParentAccount(accounts, store);

    });


    //click on select account

    $accountData.on("select2:select",".accounts-select", function (e) {

        let $this = this;

        let selectedParentAccount = accounts.filter((obj)=>{
            return obj.id == $($this).closest('select').val();
        })

        store.selectedParentAccount = selectedParentAccount[0];


        let text = e.params.data.text

        $(this).closest('div').append(`<div class="level-text selected-div">
                                        <span class="account-text-span">${text}</span>
                                        <span class="glyphicon glyphicon-remove-circle remove-item remove-account" aria-hidden="true"></span>
                                      </div>`);

        $(this).closest('select').select2('destroy');
        $(this).closest('select').remove();
        let $codeField = $('.code-div :input');

        generateCode(store, $codeField, accounts);

    });

    //click on remove level
    $accountData.on("click",".remove-level", function () {

        $(this).closest('.level-div').append(`<select class="form-control level-select"></select>`);
        $(this).closest('div').remove();

        store.selectedLevel = '';

        $('.account-data-div .remove-account').trigger('click');

        disableEnable('remove-level', store)

        filterLevel(accounts, accountlevels);

    });

    //click on remove account
    $accountData.on("click",".remove-account", function () {

       $(this).closest('.parent-account-div').append(`<select class="form-control accounts-select"></select>`);
       $(this).closest('div').remove();

       store.selectedParentAccount='';

       disableEnable('remove-parent', store)

       filterParentAccount(accounts, store);

    });

    $('.save--btn-save').on('click', (ev)=>{

        ev.preventDefault();

        let check = checks(store);

        if(check){
            save(store);
        }
    })

    $( ".account-filter" ).on('keyup',function(ev) {


        if(ev.keyCode == 13) {
          ev.preventDefault();
          return false;
        }

        let text = $( ".account-filter" ).val().toUpperCase();
        let filteredAccounts = accounts.filter((obj)=>{

            return obj.name.toUpperCase().includes(text);

        })

        drawTable(filteredAccounts);

        filteredAccounts =[];

    });

return store;

}
