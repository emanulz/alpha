
export function setClient(code){

    var clients = JSON.parse(localStorage.Clients);
    var control = -1;
    var name;
    var hasCredit;
    var debt;

    $.each(clients, function(i) {

        if(code == clients[i].code.toLowerCase()){
            control=i;
            return false
        }

    });

    if (control != -1){

        name = clients[control].name.toString() + ' ' +clients[control].last_name.toString();
        hasCredit = clients[control].has_credit;
        debt = clients[control].debt;

        $('.client-name-span').html(name);

        if(hasCredit){
            $('.client-credit-span').removeClass('fa-times-circle');
            $('.client-credit-span').addClass('fa-check-square');
        }
        else{
            $('.client-credit-span').removeClass('fa-check-square');
            $('.client-credit-span').addClass('fa-times-circle');
        }

        $('.debt-amount-span').html(parseFloat(debt).toFixed(2));
        $('.debt-amount-span').addClass('credit-negative')



    }
    else{
        $('.client-name-span').html('Cliente de Contado');

        $('.client-credit-span').removeClass('fa-check-square');
        $('.client-credit-span').addClass('fa-times-circle');

        $('.debt-amount-span').html('-');

        alertify.alert('Error', 'No existe un cliente con ese código');
    }

}
