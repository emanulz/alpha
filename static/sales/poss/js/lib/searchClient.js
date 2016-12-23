export function searchClient(text){

    $('.client-search-table-body').html('');

    var clients = JSON.parse(localStorage.Clients);
    var name;

    text = text.split('%');

    $.each(clients, function(i) {

        name = clients[i].name.toString() + ' ' +clients[i].last_name.toString();
        var control = true;

        $.each(text, function(i) {

        var index = name.toLowerCase().indexOf(text[i].toLowerCase());

        if (index == -1){
            control = false;
            return false;
        }

        });

        if (control == true){
            addToSearchClientTable(clients[i]);
        }

    });

}
