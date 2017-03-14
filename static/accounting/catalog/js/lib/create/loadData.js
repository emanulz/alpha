global.jQuery = require("jquery");

export function loadData(api){


    let company = $('#id_company').val();

    $.get(`/accounting/api/${api}/?company=${company}`, function (data) {

       localStorage[api] = JSON.stringify(data);

    });

    return JSON.parse(localStorage[api]);

}
