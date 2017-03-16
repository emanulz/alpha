global.jQuery = require("jquery");
import {dataToSelect} from './dataToSelect';
import {generateCode} from './generateCode';
import {disableEnable} from './disableEnable'

export function filterParentAccount(accounts, store){

    if(store.selectedLevel.level == 0){

        disableEnable('no-parent', store);

        let $codeField = $('.code-div :input');

        generateCode(store, $codeField, accounts);

    }
    else{

        let filteredAccounts = accounts.filter(function( obj ) {
        return obj.level_num == (store.selectedLevel.level-1);
        });

        $(".accounts-select").html('');

        dataToSelect(filteredAccounts, 'accounts-select', 'id','identifier', 'name');

    }

}
