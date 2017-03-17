global.jQuery = require("jquery");

export function currenciesToSelect($select, currenciesRecieved) {

    let currencies = currenciesRecieved ? currenciesRecieved : JSON.parse(localStorage.currencies);

    $.each(currencies, function (i) {

        $select.append($('<option>', {
            value: currencies[i].id,
            text: `${currencies[i].symbol} - ${currencies[i].name}`
        }));
    });

    $(() => {
      $select.select2({height:'200px'});
    });

}

export function refreshCurrencySymbol($select, currenciesRecieved){

    let currencies = currenciesRecieved ? currenciesRecieved : JSON.parse(localStorage.currencies);

    let selectedCurrency = $select.val();

    let currency = $.grep(currencies, function (element, index) {
        return element.id == selectedCurrency;
    });

    $('.currency-symbol').html(currency[0].symbol)

}
