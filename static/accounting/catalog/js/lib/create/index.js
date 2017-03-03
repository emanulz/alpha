var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

import 'select2';

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
            }
        });//ajax setup

import {loadData} from './loadData';
import {drawTable} from './drawTable';
import {accountsToSelect} from './accoutsToSelect';

$(document).on('ready', mainCreateCatalog);

//------------------------------------------------------------------------------------------
function mainCreateCatalog() {

    //Selectors
    let accounts = loadData();
    let $accountData = $('.account-data-div');
    let $level = $accountData.find('.level-select');

    //Initial Disables

    $(".account-data-div :input").attr("disabled", true);

    $level.attr("disabled", false);

    //Initial Draws
    drawTable(accounts);
    accountsToSelect(accounts);

    $(() => {
      $level.select2({ placeholder: 'Seleccione un nivel', width: '100%' });
    });

    actions();


}//MAIN FUNCTION


function actions(){

    //Selectors

    let $accountData = $('.account-data-div');
    let $level = $accountData.find('.level-select');

    $accountData.on("select2:select",".level-select", function (e) {

        

    });



}
