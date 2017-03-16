global.jQuery = require("jquery");

export function disableEnable(event, store){


    //selectors
    let $accountData = $('.account-data-div');
    let $levelSelect = $accountData.find('.level-select');
    let $parentAccount = $accountData.find('.accounts-select');
    let $code = $accountData.find('.code-field');
    let $nature = $accountData.find('.nature-select');
    let $name = $accountData.find('.name-field');
    let $active = $accountData.find('.active-checkbox');
    let $movement = $accountData.find('.movement-checkbox');


    $(".account-data-div :input").removeClass("error-field");


    //swith of events
    switch(event){

        case 'level-selected':

            $parentAccount.attr('disabled', false);
            break;

        case 'parent-selected':

            $code.attr('disabled', false);
            $nature.val(store.selectedParentAccount.nature);
            $name.attr('disabled', false);
            $active.attr('disabled', false);
            $movement.attr('disabled', false);

            break;

        case 'no-parent':

            $parentAccount.attr('disabled', true);
            $code.attr('disabled', false);
            $nature.attr('disabled', false);
            $name.attr('disabled', false);
            $active.attr('disabled', false);
            $movement.attr('disabled', false);

            break;

        case 'remove-parent':

            $code.attr('disabled', true);
            $nature.attr('disabled', true);
            $name.attr('disabled', true);
            $active.attr('disabled', true);
            $movement.attr('disabled', true);

            break;

        case 'remove-level':

            $parentAccount.attr('disabled', true);
            $code.attr('disabled', true);
            $nature.attr('disabled', true);
            $name.attr('disabled', true);
            $active.attr('disabled', true);
            $movement.attr('disabled', true);

            break;

    }

}
