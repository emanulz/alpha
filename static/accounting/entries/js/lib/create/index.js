var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

var bootstrap = require('bootstrap');

require('controller');

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
            if(settings.type == "DELETE"){
                xhr.setRequestHeader("X-CSRFToken", $('[name="csrfmiddlewaretoken"]').val());
            }
        }
    });//ajax setup

$(document).on('ready', mainCreateEntry );

import {loadData} from './loadData';


//------------------------------------------------------------------------------------------
function mainCreateEntry() {

    let $general = $('.general-block');

    let $date = $general.find('.date');

    setDateToday($date);

    loadData();

    $('#createForm').on('keyup keypress', function(e) {
        var keyCode = e.keyCode || e.which;
        if (keyCode === 13) {
            e.preventDefault();
            return false;
        }
    });

}//MAIN FUNCTION


function setDateToday($dateField){

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

    $dateField.val(today);

}
