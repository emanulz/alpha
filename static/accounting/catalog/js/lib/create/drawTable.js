global.jQuery = require("jquery");

export function drawTable(accounts){

    let $table = $('.accounts-table tbody');

    $table.html('');

    $.each(accounts, function (i) {

        $table.append(

        `<tr class='hola'>
            <td>
                <a href='/admin/accounting/account/${accounts[i].id}/'>
                ${accounts[i].identifier}
                </a>
            </td>
            <td>
                ${accounts[i].name}
            </td>
            <td>
                ${accounts[i].level}
            </td>
         </tr>`
     )

    });

}

function getCode(accounts, account){



}
