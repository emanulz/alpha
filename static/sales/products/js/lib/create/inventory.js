var $ = require('jquery');

export function inventoryData(){

    //DOM CACHE
    let $inventory = $('.inventory-block');

    //SELECTORS
    let $useInventory = $inventory.find('.useinventory');

    //EVENTS
    $useInventory.change({$inventory:$inventory}, useInventory);

    initialDisables($inventory);
}


function useInventory(e) {

    //SELECTORS
    let $inventory = e.data.$inventory;
    let $inventoryInputs = $inventory.find('input');
    let useInventory = $inventory.find('.useinventory');

    //ACTIONS
    if(e.target.checked) {
        $inventoryInputs.attr("disabled", false);
    }

    if(!e.target.checked) {
        $inventoryInputs.attr("disabled", true);
    }

    useInventory.attr("disabled", false);
}


function initialDisables($inventory){

    //SELECTORS
    let $inventoryInputs = $inventory.find('input');
    let $useInventory = $inventory.find('.useinventory');

    //ACTIONS
    $inventoryInputs.attr("disabled", true);
    $useInventory.attr("disabled", false);
}



