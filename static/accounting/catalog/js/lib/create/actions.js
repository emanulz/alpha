global.jQuery = require("jquery");
import {accountsToSelect} from './accoutsToSelect';

export function actions(){

    //Selectors

    let $accountData = $('.account-data-div');
    let $level = $accountData.find('.level-select');

    //click on select level

    $accountData.on("select2:select",".level-select", function (e) {

        let text = e.params.data.text
        $(this).closest('div').append(`<div class="level-text selected-div">
                                        <span class="account-text-span">${text}</span>
                                        <span class="glyphicon glyphicon-remove-circle remove-item remove-level" aria-hidden="true"></span>
                                      </div>`);

        $(this).closest('select').select2('destroy');
        $(this).closest('select').remove();
        $('.accounts-select').attr("disabled", false);

    });

    //click on select account

    $accountData.on("select2:select",".accounts-select", function (e) {

        let text = e.params.data.text
        $(this).closest('div').append(`<div class="level-text selected-div">
                                        <span class="account-text-span">${text}</span>
                                        <span class="glyphicon glyphicon-remove-circle remove-item remove-account" aria-hidden="true"></span>
                                      </div>`);

        $(this).closest('select').select2('destroy');
        $(this).closest('select').remove();
        $('.code-div :input').attr("disabled", false);

    });

    //click on remove level
    $accountData.on("click",".remove-level", function () {

        $(this).closest('.level-div').append(`<select class="form-control level-select">
                                                  <option></option>
                                                  <option value="0">0 - Categoría</option>
                                                  <option value="1">1 - Grupo</option>
                                                  <option value="2">2 - Cuenta</option>
                                                  <option value="3">3 - Sub-Cuenta</option>
                                                  <option value="4">4 - Cuenta Auxiliar</option>
                                                </select>`);
       $(this).closest('div').remove();

       $(() => {
         $('.level-select').select2({ placeholder: 'Seleccione un nivel', width: '100%' });
       });

    });

    //click on remove account
    $accountData.on("click",".remove-account", function () {

       $(this).closest('.parent-account-div').append(`<select class="form-control accounts-select"></select>`);
       $(this).closest('div').remove();

       accountsToSelect(JSON.parse(localStorage.accounts));

       $(() => {
         $('.accounts-select').select2({ placeholder: 'Seleccione una cuenta', width: '100%' });
       });

    });


}
