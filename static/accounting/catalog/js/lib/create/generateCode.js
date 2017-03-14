global.jQuery = require("jquery");
import {disableEnable} from './disableEnable'


export function generateCode(store, $codeField, accounts){

    let code = 1;
    let filteredAccounts = [];


    if(store.selectedParentAccount){
        let parentAccount = store.selectedParentAccount.id

        filteredAccounts = accounts.filter(function( obj ) {
            return obj.parent == parentAccount;
        });

        //disable enable fields
        disableEnable('parent-selected', store);


    }
    else{
        filteredAccounts = accounts.filter(function( obj ) {
            return obj.parent == null;

        });
    }

    if(filteredAccounts.length!=0){

        let sortedAccounts = filteredAccounts.sort(function (a, b) {

            if(a.identifier < b.identifier) return 1;
            if(a.identifier > b.identifier) return -1;
            return 0;
        });

        code = ((sortedAccounts.length!=0) ? parseInt(sortedAccounts[0].identifier) + 1 : 1);

    }

    $codeField.val(code);
    $codeField.attr("disabled", false);



}
