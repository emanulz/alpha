global.jQuery = require("jquery");

// todo: rewrite this function
export function accountsToSelect($select, accountsRecieved){

    let accounts = accountsRecieved ? accountsRecieved : JSON.parse(localStorage.accounts);

    $select.append($('<option>', {

    }));

    let dataToSelect = [];

    //filter accounts and annd code to new array
    $.each(accounts, function (i) {

        let code = getCode(accounts[i]);

        dataToSelect.push([code, accounts[i].name, accounts[i].id, accounts[i].movements])

    });

    //sort accounts by code

    let sortedAccounts = dataToSelect.sort(function (a, b) {

        if(a[0] < b[0]) return -1;
        if(a[0] > b[0]) return 1;
        return 0;
    });


    //add rows to select
    $.each(sortedAccounts, function (i) {

        let accountsDisabled = (sortedAccounts[i][3] ? '':'disabled')

        $select.append(`<option value=${sortedAccounts[i][2]} ${accountsDisabled}>
                            ${sortedAccounts[i][0]}  - ${sortedAccounts[i][1]}
                            </option>`);

    })

    $(() => {
      $select.select2({ placeholder: 'Seleccione una cuenta', width: '100%' });
    });

}

//generate code recursively
function getCode(account){

    let accounts = JSON.parse(localStorage.accounts);

    if (account.parent == null){
        return `${account.identifier}.`
    }
    else{
        let parentAccount = accounts.filter((obj)=>{
            return obj.id == account.parent
        })

        return getCode(parentAccount[0]) + account.identifier+'.'

    }

}
