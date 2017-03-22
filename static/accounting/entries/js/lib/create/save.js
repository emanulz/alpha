var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

var alertify = require('alertifyjs');

import {scanTable} from './actions';
import {updateTotals} from './actions';

export function save(){

    //selectors
    let $general = $('.general-block');
    let $date = $general.find('.date');
    let $table = $('.table-entry');

    //data
    let data = scanTable($table);
    let totals = updateTotals(data);
    let company = $('#id_company').val();

    if (totals.diferrence == 0){
        //entry data
        let entryData = JSON.stringify({
            "company": company,
            "date": today(),
            "entryDate": $date.val(),
            "totalDebe": totals.totalDebe,
            "totalHaber": totals.totalHaber,
            "difference": totals.diferrence
        });

        //promise objects
        let saveEntryPromise = saveApi(entryData, '/accounting/api/entries/')

        saveEntryPromise.then((entry)=>{
            //console.log(entry);
            saveDetails(data, entry)
            //alertify.alert('Correcto',`Asiento # ${data.id} creado correctamente.`);
        })
        .catch((err)=>{
            alertify.alert('Error',`Error al crear el asiento, por favor intente de nuevo,(LOG: ${err})`);
        })

    }

    else{
        alertify.alert('Error',`El asiento no está balanceado, la diferencia debe ser 0`);
    }
}

function saveApi(data, apiUrl){

    return new Promise((resolve, reject)=>{

        $.ajax({
            type: "POST",
            url: `${apiUrl}`,
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

function today(){

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
    dd='0'+dd
    }

    if(mm<10) {
    mm='0'+mm
    }

    today = yyyy+'-'+mm+'-'+dd;

    return today;



}

function saveDetails(data, entry){

    let company = $('#id_company').val();
    let entryId = entry.id;
    let urlDetails = '/accounting/api/entrydetails/'
    let $general = $('.general-block');
    let $date = $general.find('.date');

    let promises = data.map((item)=>{

        let detailData = JSON.stringify({
            "company": company,
            "entry": entryId,
            "account": item[5],
            "debe": item[3],
            "haber": item[4],
            "date": $date.val(),
            "detail": item[1],
            "document": item[2]
        });

        return saveApi(detailData, urlDetails)

    });

    Promise.all(promises)
    .then((results)=>{
        alertify.alert('Correcto',`Asiento # ${entryId} creado correctamente.`);
    })
    .catch((err)=>{
        alertify.alert('Error',`Error al crear los detalles del asiento, por favor intente de nuevo,(LOG: ${err})`);
        $.ajax({
            type: "DELETE",
            url: `/accounting/api/entries/${entryId}/`,
        })

    })


}
