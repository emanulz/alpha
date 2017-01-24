var $ = require('jquery');
var alertify = require('alertifyjs');

import { updateTotals } from "./updateTotals"
import { rowUpdate } from "./rowUpdate"

//ACTION FUNCTIONS FUNCTIONS
//------------------------------------------------------------------------------------------
export function handleCode(codeStr, store) {

    var products = JSON.parse(localStorage.Products);

    var code = codeStr.split('*')[0];
    var qty = codeStr.split('*')[1];

    if( qty === 0){
        alertify.alert('Error','La Cantidad no puede ser Cero');
        return false;
    }

    if( qty === undefined){
        qty=1;
    }

    var isOnArray = isCodeOnArray(store.saleList,code);

    if(isOnArray === -1){
        //filter product by code
        products = $.grep(products, function(element){
            return element.code == code;
        });

        if (products.length){

           store = prepareNewRow(products, qty, store);

        }
        else{
            products = $.grep(products, function(element){
                return element.barcode == code;
            });

            if (products.length){
                store = prepareNewRow(products, qty, store);
            }
            else{
                alertify.alert('Error','No existe un producto con el código seleccionado.')
            }
        }
    }//if

    else{

        store.saleList = rowUpdate(isOnArray, code, qty, store.saleList, 1,0);
        store = updateTotals(store);

    }//else

    return store;


}


function isCodeOnArray(array , code){

    var control = -1;

    $.each(array, function(i) {

        if (array[i][0]==code || array[i][1]==code){ // Eval Code and Barcode
            control = i;
            return false;
        }
    });

    return control;
} //IS ON ARRAY FUNCTION

function prepareNewRow(products, qty, store) {

    console.log(products);

    var subt = (products[0].price*qty)*((100-products[0].discount)/100);

    var iv=0;

    if( products[0].usetaxes){
        iv=products[0].taxes;
    }

    store = addNewRow(products[0].code, products[0].barcode, products[0].description, qty, products[0].price , subt,
                      products[0].id, products[0].discount, iv, store);

    return store;


}

function addNewRow(code, barcode, desc, qty, uprice, subt, id, disc, iv, store){

    store.saleList.push([code, barcode, qty, parseFloat(uprice), subt, desc, id, disc, iv]);
    // code, barcode, qty, unit price, subt, discount %, id, iv,

    var newRow=`<tr class="${code} product_row">
                    <td>${code}</td>
                    <td>${desc}</td>
                    <td style="padding:0; width:10%"><input type="number" style="width:100%;border:0px; padding: 0; text-align: center"
                    class="form-control ${code}_product_qty product_qty"/></td>
                    <td class="${code}_product_uprice price" >${parseFloat(uprice).toFixed(2)}</td>
                    <td style="padding:0; width:10%"><input value="${disc}" type="number" style="width:100%;border:0px; padding:0;text-align: center"
                    class="form-control ${code}_product_disc product_disc"/></td>
                    <td class="${code}_product_iv" >${iv}%</td>
                    <td class="${code}_product_subt price" >${subt.toFixed(2)}</td>
                    <td style="text-align: center; padding:0; width:5%" class="inner-addon">
                    <i class="fa fa-minus remove_row"></i></td>
                </tr>`;

    $('.table-body').append(newRow);

    $(`.${code}_product_qty`).val(qty);

    store = updateTotals(store);

    return store;
}