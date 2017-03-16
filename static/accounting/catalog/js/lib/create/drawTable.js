global.jQuery = require("jquery");

export function drawTable(accounts){

    let $table = $('.accounts-table tbody');

    $table.html('');

    let dataToTable = [];


    $.each(accounts, function (i) {

        let code = getCode(accounts[i]);

        dataToTable.push([code, accounts[i].name, accounts[i].level_num, accounts[i].id])

    });

    let sortedAccounts = dataToTable.sort(function (a, b) {

        if(a[0] < b[0]) return -1;
        if(a[0] > b[0]) return 1;
        return 0;
    });


    $.each(sortedAccounts, function (i) {

        $table.append(

        `<tr class='hola'>
            <td>
                <a href='/admin/accounting/account/${sortedAccounts[i][3]}/'>
                ${sortedAccounts[i][0]}
                </a>
            </td>
            <td>
                ${sortedAccounts[i][1]}
            </td>
            <td>
                ${sortedAccounts[i][2]}
            </td>
         </tr>`
     )

    });

}

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
