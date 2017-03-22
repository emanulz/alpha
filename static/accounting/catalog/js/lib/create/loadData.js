var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

import 'select2';

var bootstrap = require('bootstrap');
var alertify = require('alertifyjs');
require('controller');

let store = {};

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

import {drawTable} from './drawTable';
import {dataToSelect} from './dataToSelect';
import {filterLevel} from './filterLevel';
import {actions} from './actions';

export function loadData(){

    localStorage.clear();

    let loadAccounts = loadApi('accounts');
    let loadAccountLevels = loadApi('accountlevels');

    let $accountData = $('.account-data-div');
    let $level = $accountData.find('.level-select');


    //Initial Disables

    $(".account-data-div :input").attr("disabled", true);


    //Initial Draws after promise resolve
    loadAccounts.then((accounts)=>{


        drawTable(accounts);


        loadAccountLevels.then((accountLevels)=>{
            filterLevel(accounts, accountLevels);
            store = actions(store);
            $level.attr("disabled", false);

        })
        .catch((err)=>{
            alertify.alert('Error',`Error al cargar los niveles, por favor recargue la página e intente de nuevo,(LOG: ${err})`);
        });

    })
    .catch((err)=>{
        alertify.alert('Error',`Error al cargar las cuentas, por favor recargue la página e intente de nuevo,(LOG: ${err})`);
    });


}

function loadApi(api){

    let company = $('#id_company').val();

    return new Promise((resolve, reject)=>{

        $.get(`/accounting/api/${api}/?company=${company}`)

        .done((data)=>{
            localStorage[api] = JSON.stringify(data);
            resolve(data);
        })

        .fail((xhr, status, err)=>{
            reject(`${status}, ${err}`)
        })

    });


}
