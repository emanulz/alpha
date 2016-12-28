var $ = require('jquery');

export function saleData(){

    //DOM CACHE
    let $sale = $('.sale-block');

    //SELECTORS
    let $hasforsale = $sale.find('.hasforsale');

    //EVENTS
    $hasforsale.change({$sale:$sale },hasforsale);

    initialDisables($sale);
}

function hasforsale(e) {

     //Selectors
    let $sale = e.data.$sale;
    let $saleInputs = $sale.find('input');
    let $hasforsale = $sale.find('.hasforsale');

    if(e.target.checked) {
        $saleInputs.attr("disabled", false);
    }

    if(!e.target.checked) {
        $saleInputs.attr("disabled", true);
    }

   $hasforsale.attr("disabled", false);
}


function initialDisables($sale){

    //Selectors
    let $saleInputs = $sale.find('input');
    let $hasforsale = $sale.find('.hasforsale');

    //Actions
    if(!$hasforsale[0].checked){


        $saleInputs.attr("disabled", true);
        $hasforsale.attr("disabled", false);

        return true;
    }

    $saleInputs.attr("disabled", false);
    $hasforsale.attr("disabled", false);

}
