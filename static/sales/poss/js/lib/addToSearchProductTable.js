export function addToSearchProductTable(product){

    var code  = product.code;
    var desc = product.description;
    var price = parseFloat(product.sellprice).toFixed(2);
    var inventory;


    if(product.useinventory){
        inventory = product.inventory;
    }
    else{
        inventory = '-';
    }

    var newRow=`<tr class="${code}">
                    <td>${code}</td>
                    <td>${desc}</td>
                    <td>${inventory}</td>
                    <td class="price">${price}</td>
                    <td style="text-align: center; padding:0; width:5%" class="inner-addon">
                    <i class="fa fa-plus select_product_search_row"></i></td>
                </tr>`;

    $('.table-body-product-search').append(newRow);

     $('.price').priceFormat({
        prefix: '₡ ',
        centsSeparator: ',',
        thousandsSeparator: '.'
    });


}
