var $ = require('jquery');

export function composedData(){

    //DOM CACHE
    let $composed = $('.composed');

    //SELECTORS
    let $isComposed = $composed.find('.isComposed');

    //EVENTS
    $isComposed.change({$composed:$composed }, isComposed);

    initialDisables($composed);
}

function isComposed(e) {

     //Selectors
    let $composed = e.data.$composed;
    let $composedInputs = $composed.find('input');
    let $isComposed = $composed.find('.isComposed');

    if(e.target.checked) {
        $composedInputs.attr("disabled", false);
    }

    if(!e.target.checked) {
        $composedInputs.attr("disabled", true);
    }

   $isComposed.attr("disabled", false);
}


function initialDisables($composed){

    //Selectors
    let $composedInputs = $composed.find('input');
    let $isComposed = $composed.find('.isComposed');

    //Actions
    if(!$isComposed[0].checked){


        $composedInputs.attr("disabled", true);
        $isComposed.attr("disabled", false);

        return true;
    }

    $composedInputs.attr("disabled", false);
    $isComposed.attr("disabled", false);

}
