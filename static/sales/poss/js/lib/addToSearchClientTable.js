
export function addToSearchClientTable(client){

    var code  = client.code;
    var name = client.name.toString() + ' ' +client.last_name.toString();
    var hasCredit;
    var debt = parseFloat(client.debt).toFixed(2);


    if(client.has_credit){
        hasCredit = 'fa fa-check';
    }
    else{
        hasCredit = 'fa fa-minus';
    }

    var newRow=`<tr class="${code}">
                    <td>${code}</td>
                    <td>${name}</td>
                    <td><i class="${hasCredit}"></i></td>
                    <td class="price">${debt}</td>
                    <td style="text-align: center; padding:0; width:5%" class="inner-addon">
                    <i class="fa fa-plus select_client_search_row"></i></td>
                </tr>`;

    $('.client-search-table-body').append(newRow);

     $('.price').priceFormat({
        prefix: '₡ ',
        centsSeparator: ',',
        thousandsSeparator: '.'
    });


}
