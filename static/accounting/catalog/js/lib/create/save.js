var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

var alertify = require('alertifyjs');

$.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if(settings.type == "POST"){
                    xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
                }
                if(settings.type == "PUT"){
                    xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
                }
                if(settings.type == "PATCH"){
                    xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
                }
            }
        });//ajax setup


export function save(store){

    let parent = (store.selectedParentAccount ? store.selectedParentAccount.id : null)

    let company = $('#id_company').val();

    let $accountData = $('.account-data-div');
    let $code = $accountData.find('.code-field');
    let $nature = $accountData.find('.nature-select');
    let $name = $accountData.find('.name-field');
    let $active = $accountData.find('.active-checkbox');
    let $movement = $accountData.find('.movement-checkbox');

    let data = JSON.stringify({

        "company": company,
        "name": $name.val(),
        "identifier": $code.val(),
        "nature": $nature.val(),
        "level": store.selectedLevel.id,
        "parent": parent,
        "active": $active.is(":checked"),
        "movements": $movement.is(":checked")
    });

    console.log(data);

    let savePromise = saveAccount(data);

    savePromise.then((data)=>{


        alertify.alert('Completado',`La cuenta "${data.name}" ha sido guardada correctamente`,
        function(){

            location.reload();
        });

    })
    .catch((err)=>{
        alertify.alert('Error',`Error al crear la cuenta, por favor intente de nuevo,(LOG: ${err})`);
    })


}

function saveAccount(data){

    return new Promise((resolve, reject)=>{

        $.ajax({
            type: "POST",
            url: '/accounting/api/accounts/',
            data: data,
            contentType:"application/json; charset=utf-8",
            dataType:"json"
        })
        .success((data)=>{
            resolve(data);
        })
        .fail((xhr, status, err)=>{
            console.log(xhr.responseText);
            reject(`${status}, ${err}`)
        });

    });

}
