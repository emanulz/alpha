global.jQuery = require("jquery");

export function loadData(){

    let company = $('#id_company').val();

    $.get(`/accounting/api/accounts/?company=${company}`, function (data) {

       localStorage.accounts = JSON.stringify(data);

    });

    return JSON.parse(localStorage.accounts);

}
