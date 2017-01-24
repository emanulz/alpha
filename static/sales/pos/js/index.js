/**
 * Created by emanuelziga on 14/12/16.
 */

var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

var mouseTrap = require('mouseTrap');
var alertify = require('alertifyjs');

window.alertify = alertify;

import {browserObjectEvents} from "./lib/browserEvents";
import {loadToLocalStorage} from  "./lib/loadToLocalStorage";

//STORE VAR
//------------------------------------------------------------------------------------------
var store = {saleList:[],total:0,subtotal:0,iv_amount:0,companyId:$('#company-id').html()};
//------------------------------------------------------------------------------------------

$(document).on('ready',()=>{mainSales(store)} );

//------------------------------------------------------------------------------------------
//MAIN
//------------------------------------------------------------------------------------------
function mainSales(store) {

    //EVENTS
    browserObjectEvents(store);

    //LOAD TO LOCAL STORAGE
    loadToLocalStorage(store);

}//MAIN FUNCTION
//------------------------------------------------------------------------------------------
