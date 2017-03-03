global.jQuery = require("jquery");

// select2 = require('select2');
import $ from 'jquery';
import 'select2';                       // globally assign select2 fn to $ element


export function accountsToSelect(accounts){

    let $select = $('.accounts-select');

    $select.html('');

    $select.append($('<option>', {

    }));

    $.each(accounts, function (i) {


        $select.append(`<option value=${accounts[i].id}>
                            ${accounts[i].identifier}-00-00  - ${accounts[i].name}
                            </option>`);

    });

    $(() => {
      $select.select2({ placeholder: 'Seleccione una cuenta', width: '100%' });
    });


}
