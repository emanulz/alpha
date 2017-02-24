global.jQuery = require("jquery");

export function listData(){

    let $main = $('.main-table');
    let company = $('#id_company').val();

    getData(company);

    console.log(JSON.parse(localStorage.accounts));

    dataToHTML($main);

}

function getData( company){

    $.get(`/accounting/api/account_categories/?company=${company}`, function (data) {

       localStorage.account_categories = JSON.stringify(data);

    });

    $.get(`/accounting/api/account_groups/?company=${company}`, function (data) {

       localStorage.account_groups = JSON.stringify(data);

    });

    $.get(`/accounting/api/accounts/?company=${company}`, function (data) {

       localStorage.accounts = JSON.stringify(data);

    });

    $.get(`/accounting/api/subaccounts/?company=${company}`, function (data) {

       localStorage.subaccounts = JSON.stringify(data);

    });

    $.get(`/accounting/api/detailaccounts/?company=${company}`, function (data) {

       localStorage.detailaccounts = JSON.stringify(data);

    });


}

function dataToHTML($main){

    let categories = JSON.parse(localStorage.account_categories);
    let groups = JSON.parse(localStorage.account_groups);
    let accounts = JSON.parse(localStorage.accounts);
    let subaccounts = JSON.parse(localStorage.subaccounts);
    let detailaccounts = JSON.parse(localStorage.detailaccounts);


    $.each(categories, function (i) {

        $main.append(`<tr class='account-category'>
                        <td><a href='/admin/accounting/accountcategory/${categories[i].id}/'> ${categories[i].identifier}. </a></td>
                        <td>${categories[i].name}</td>
                        <td>
                            Tipo de cuenta
                        </td>
                      </tr>`)

        let grepGroups = $.grep(groups, function (element, index) {
            return element.category == categories[i].id;
        });

        let $this = this;

        $this.categoryId = categories[i].identifier;

        $.each(grepGroups, function (i) {

            $main.append(`<tr class='account-group'>
                            <td>
                                <a href='/admin/accounting/accountgroup/${grepGroups[i].id}/'>
                                ${$this.categoryId}.${grepGroups[i].identifier}
                                </a>
                            </td>
                            <td>
                                ${grepGroups[i].name}
                            </td>
                            <td>
                                Grupo de cuenta
                            </td>
                         </tr>`)

            let grepAccounts = $.grep(accounts, function (element, index) {
                return element.group == grepGroups[i].id;
            });

            $this.groupId = grepGroups[i].identifier;

            $.each(grepAccounts, function (i) {


                $main.append(`<tr class='account'>
                                <td>
                                    <a href='/admin/accounting/account/${grepAccounts[i].id}/'>
                                    ${$this.categoryId}.${$this.groupId}.${grepAccounts[i].identifier}
                                    </a>
                                </td>
                                <td>
                                    ${grepAccounts[i].name}
                                </td>
                                <td>
                                    Cuenta Mayor
                                </td>
                              </tr>`)

                let grepSubAccounts = $.grep(subaccounts, function (element, index) {
                    return element.account == accounts[i].id;
                });

                $this.accountId = accounts[i].identifier;

                $.each(grepSubAccounts, function (i) {

                    $main.append(`<tr class='subaccount'>
                                    <td>
                                        <a href='/admin/accounting/subaccount/${grepSubAccounts[i].id}/'>
                                        ${$this.categoryId}.${$this.groupId}.${$this.accountId}.${grepSubAccounts[i].identifier}
                                        </a>
                                    </td>
                                    <td>
                                        ${grepSubAccounts[i].name}
                                    </td>
                                    <td>
                                        Sub-cuenta
                                    </td>
                                  </tr>`)

                    let grepDetailAccounts = $.grep(detailaccounts, function (element, index) {
                        return element.subaccount == grepSubAccounts[i].id;
                    });

                    $this.subaccountId = grepSubAccounts[i].identifier;

                    $.each(grepDetailAccounts, function (i) {

                        console.log($this);

                        $main.append(`<tr class='detailaccount'>
                                        <td>
                                            <a href='/admin/accounting/detailaccount/${grepDetailAccounts[i].id}/'>
                                            ${$this.categoryId}.${$this.groupId}.${$this.accountId}.${$this.subaccountId}.${grepDetailAccounts[i].identifier}
                                            </a>
                                        </td>
                                        <td>
                                            ${grepDetailAccounts[i].name}
                                        </td>
                                        <td>
                                            Cuenta Detalle
                                        </td>
                                      </tr>`)

                    }); //each Account details


                });// Each Grep SubAccounts

            }); // Each Grep Accounts


        });// Each grep groups

    });//Each categories

}
