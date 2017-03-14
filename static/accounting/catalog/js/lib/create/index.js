var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

import 'select2';

var bootstrap = require('bootstrap');

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

import {loadData} from './loadData';
import {drawTable} from './drawTable';
import {dataToSelect} from './dataToSelect';
import {filterLevel} from './filterLevel';
import {actions} from './actions';

$(document).on('ready', mainCreateCatalog);

//------------------------------------------------------------------------------------------
function mainCreateCatalog() {

    //Selectors
    let accounts = loadData('accounts');
    let accountlevels = loadData('accountlevels');
    let $accountData = $('.account-data-div');
    let $level = $accountData.find('.level-select');

    //Initial Disables

    $(".account-data-div :input").attr("disabled", true);

    $level.attr("disabled", false);

    //Initial Draws

    drawTable(accounts);
    //dataToSelect(accounts, 'accounts-select', 'id','identifier', 'name');
    // dataToSelect(accountlevels, 'level-select', 'id','level', 'name');
    filterLevel(accounts, accountlevels);

    store = actions(store);

}//MAIN FUNCTION
