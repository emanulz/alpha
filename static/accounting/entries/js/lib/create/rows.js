global.jQuery = require("jquery");

import {accountsToSelect} from './accounts';

export function addNewRow(){

    let template = `<tr>
                        <td class='input-cell account-cell'>
                            <select class='form-control input-sm select-account'></select>
                            <input type="text" hidden placeholder='Ingrese el detalle del asiento' class='detail-input'>
                        </td>
                        <td class='input-cell document-cell'>
                            <input type="text" class='form-control input'>
                        </td>
                        <td class='input-cell debe-cell'>
                            <div class='currency-cell'>
                                <span class="currency-symbol"> </span>
                                <input type="number" value="0" class='form-control input'>
                            </div>
                        </td>
                        <td class='input-cell haber-cell'>
                            <div class='currency-cell'>
                                <span class="currency-symbol"> </span>
                                <input type="number" value="0" class='form-control input'>
                            </div>
                            <div class='remove-row-div'>
                                <div class='remove-row-container'>
                                    <span class="glyphicon glyphicon-remove-sign remove-row" aria-hidden="true"></span>
                                </div class='form-control input'>
                            </div>
                        </td>
                    </tr>`

    $('.table-entry').append(template);

    let $addedSelect = $('.table-entry').find('tr:last').find('.select-account');

    accountsToSelect($addedSelect);

}

export function removeRow($this){

    $this.closest('tr').remove();
}
