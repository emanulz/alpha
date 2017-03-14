global.jQuery = require("jquery");

// select2 = require('select2');
import $ from 'jquery';
import 'select2';                       // globally assign select2 fn to $ element


export function dataToSelect(data, className, idField, codeField, nameField){

    let $select = $(`.${className}`);

    $select.html('');

    $select.append($('<option>', {

    }));

    $.each(data, function (i) {

        $select.append(`<option value=${data[i][idField]}>
                            ${data[i][codeField]} - ${data[i][nameField]}
                        </option>`);

    });

    $(() => {
      $select.select2({ placeholder: 'Seleccione un elemento', width: '100%' });
    });


}
