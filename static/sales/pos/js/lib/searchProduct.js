export function searchProduct(text){

    $('.table-body-product-search').html('');

    var products = JSON.parse(localStorage.Products);
    var description;

    text = text.split('%');

    $.each(products, function(i) {

        description = products[i].description.toString();
        var control = true;

        $.each(text, function(i) {

        var index = description.toLowerCase().indexOf(text[i].toLowerCase());

        if (index == -1){
            control = false;
            return false;
        }

        });

        if (control == true){
            addToSearchProductTable(products[i]);
        }

    });
    
}