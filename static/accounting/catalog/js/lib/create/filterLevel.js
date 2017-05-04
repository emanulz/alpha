global.jQuery = require("jquery");
import {dataToSelect} from './dataToSelect';

export function filterLevel(accounts, accountlevels){

    console.log(accounts);

    let sortedAccounts = accounts.sort(function (a, b) {

        if(a.level < b.level) return 1;
        if(a.level > b.level) return -1;
        return 0;
    });


    let maxLevel =  ((accounts.length) ? sortedAccounts[0].level_num+1 : 0);

    let filteredLevels = accountlevels.filter(function( obj ) {
    return obj.level <= maxLevel;
    });


    $(".level-select").html('');

    dataToSelect(filteredLevels, 'level-select', 'id','level', 'name');


}
