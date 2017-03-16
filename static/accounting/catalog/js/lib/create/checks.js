var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

var alertify = require('alertifyjs');


export function checks(store){

    //vars

    let accounts = JSON.parse(localStorage.accounts);
    let accountlevels = JSON.parse(localStorage.accountlevels);

    //selectors

    let $accountData = $('.account-data-div');
    let $levelSelect = $accountData.find('.level-select');
    let $accountsSelect = $accountData.find('.accounts-select');
    let $code = $accountData.find('.code-field');
    let $name = $accountData.find('.name-field');


    //check Level

    if(!store.selectedLevel){

        alertify.alert('Error','Debe seleccionar un Nivel para la cuenta');

        $($levelSelect.data('select2').$container).addClass('error-field')

        return false;
    }

    //ckeck Parent Account

    if(!store.selectedParentAccount){

        let levelSelected = ((store.selectedLevel.level == 0) ? true : false)

        if(!levelSelected){
            alertify.alert('Error','Debe seleccionar una cuenta padre');
            $($accountsSelect.data('select2').$container).addClass('error-field')

            return false;
        }
    }

    //check code

    if(!$code.val()){

        alertify.alert('Error','Debe digitar un código');
        $code.addClass('error-field');

        return false;
    }


    //check code not repeated

    let codeVal = $code.val()

    let parentAccountId = (store.selectedParentAccount ? store.selectedParentAccount.id : null);

    let filteredAccounts = accounts.filter(function( obj ) {
        return (obj.level_num == store.selectedLevel.level)&&(obj.parent == parentAccountId);
    });


    let checkedCode = filteredAccounts.filter((obj)=>{
        return obj.identifier == (codeVal);
    })

    console.log(checkedCode);

    if(checkedCode.length){

        let parentAccountName = (store.selectedParentAccount ? `de ${store.selectedParentAccount.name}` : 'de nivel 0');

        alertify.alert('Error',`Ya existe una cuenta ${parentAccountName}, con el código ${codeVal},
                        llamada "${checkedCode[0].name}", seleccione un código válido.`);

        $code.addClass('error-field');

        checkedCode = [];

        return false;
    }

    //check name

    if(!$name.val()){

        alertify.alert('Error','Debe digitar un nombre para la cuenta');
        $name.addClass('error-field');

        return false;
    }


    return true;


}
