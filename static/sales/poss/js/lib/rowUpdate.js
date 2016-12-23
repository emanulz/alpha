export function rowUpdate(row, code, qty, array, ctrl, disc){

    var actualQty = 0;
    var actualUprice = 0;
    var newQty = 0;
    var newSubt = 0;
    var newDisc = 0;

    if (ctrl == 1){//means add already existing product on table

        actualQty = array[row][2];
        actualUprice = array[row][3];
        newDisc =  array[row][7];

        newQty = parseFloat(actualQty) + parseFloat(qty);

        newSubt = (actualUprice*newQty)*(1-(newDisc/100));


    }

    if(ctrl == 2){//means update qty



        actualUprice = array[row][3];
        newDisc =  array[row][7];

        newQty = parseFloat(qty);

        newSubt = (actualUprice*newQty)*(1-(newDisc/100));

    }

    if(ctrl == 4){//means update discount

        actualUprice = array[row][3];

        newQty = array[row][2];

        newDisc =  disc;

        newSubt = (actualUprice*newQty)*(1-(newDisc/100));

    }

    if(newQty <= 0){

        alertify.alert('Error', 'La cantidad no puede ser cero, ni menor a cero, el valor volverá a 1');

        rowUpdate(row, code, 1, saleList, 2,0);

        updateTotals();

        return array;

    }

    //update values

    $(`.${code}_product_qty`).val(newQty);
    $(`.${code}_product_subt`).text(newSubt.toFixed(2));

    array[row][2] = newQty;
    array[row][4] = newSubt;
    array[row][7] = newDisc;

    return array;

}
