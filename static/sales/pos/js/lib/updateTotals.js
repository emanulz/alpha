
export function updateTotals(store) {

    var subtotal=0;
    var iv_amount= 0;
    var saleList = store.saleList;
    var total;

    var generalDiscount ;

    if ($('.sale_global_discount_input').val()){

        generalDiscount = parseFloat($('.sale_global_discount_input').val());

    }
    else{
        generalDiscount = 0;
    }


    // code, barcode, qty, unit price, subt, discount %, id, iv,
    $.each(store.saleList, function(i) {

        subtotal = subtotal+saleList[i][4];//saleList[i][4] is the subt amount.
        iv_amount=iv_amount+(saleList[i][4]*(saleList[i][8]/100));//saleList[i][8] is the IV


    });

    subtotal = subtotal*(1-(generalDiscount/100));
    iv_amount=iv_amount*(1-(generalDiscount/100));

    total = subtotal+iv_amount;

    iv_amount = parseFloat(iv_amount).toFixed(2);
    subtotal = parseFloat(subtotal).toFixed(2);
    total = total.toFixed(2);

    $('.sale_subtotal').text(subtotal);
    $('.sale_iv_amount').text(iv_amount);
    $('.sale_total').text(total);

    $('.product_code_field').val('');


    $('.price').priceFormat({
        prefix: '₡ ',
        centsSeparator: ',',
        thousandsSeparator: '.'
    });

    store.total = total;
    store.subtotal = subtotal;
    store.iv_amount = iv_amount;

    return store;
}
