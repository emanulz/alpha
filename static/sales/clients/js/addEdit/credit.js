var $ = require('jquery');

export function creditData(){

    //DOM CACHE
    let $credit = $('.credit-block');

    //SELECTORS
    let $hasCredit = $credit.find('.has-credit');

    //EVENTS
    $hasCredit.change({$credit:$credit}, hasCredit);

    initialDisables($credit);
}


function hasCredit(e) {

    //SELECTORS
    let $credit = e.data.$credit;
    let $creditInputs = $credit.find('input');
    let $hasCredit = $credit.find('.has-credit');

    //ACTIONS
    if(e.target.checked) {
        $creditInputs.attr("disabled", false);
    }

    if(!e.target.checked) {
        $creditInputs.attr("disabled", true);
    }

    $hasCredit.attr("disabled", false);
}


function initialDisables($credit){

    //SELECTORS
    let $creditInputs = $credit.find('input');
    let $hasCredit = $credit.find('.has-credit');

    //ACTIONS
    $creditInputs.attr("disabled", true);
    $hasCredit.attr("disabled", false);
}
