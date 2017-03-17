global.jQuery = require("jquery");
var alertify = require('alertifyjs');

// select2 = require('select2');
import $ from 'jquery';
import 'select2';                       // globally assign select2 fn to $ element

import{addNewRow} from './rows'
import {currenciesToSelect} from './currencies';
import {refreshCurrencySymbol} from './currencies';
import {actions} from './actions';


export function loadData(){

    localStorage.clear();

    let $general = $('.general-block');

    let $currency = $general.find('.currency');

    //load currencies
    let loadCurrencies = loadApi('currencies', '/general/api/');

    let loadAccounts = loadApi('accounts', '/accounting/api/');

    loadAccounts.then((accounts)=>{

        addNewRow();

        actions();

        loadCurrencies.then((currencies)=>{
            currenciesToSelect($currency, currencies);
            refreshCurrencySymbol($currency, currencies);
        })
        .catch((err)=>{
            alertify.alert('Error',`Error al cargar las monedas, por favor recargue la página e intente de nuevo,(LOG: ${err})`);
        });

    })
    .catch((err)=>{
        alertify.alert('Error',`Error al cargar las cuentas, por favor recargue la página e intente de nuevo,(LOG: ${err})`);
    });

}


function loadApi(api, baseUrl){

    let company = $('#id_company').val();

    return new Promise((resolve, reject)=>{

        $.get(`${baseUrl}${api}/?company=${company}`)

        .done((data)=>{
            localStorage[api] = JSON.stringify(data);
            resolve(data);
        })

        .fail((xhr, status, err)=>{
            reject(`${status}, ${err}`)
        })

    });


}
