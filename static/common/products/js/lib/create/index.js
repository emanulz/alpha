var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

var bootstrap = require('bootstrap');

require('controller');

var qtip = require("qtip");
window.qtip = qtip;


import {saleData} from './sale';
import {generalData} from './general';
import {inventoryData} from './inventory';
import {save} from './buttons';

$(document).on('ready', mainCreateProduct );

//MAIN
//------------------------------------------------------------------------------------------
function mainCreateProduct() {

    generalData();

    saleData();

    inventoryData();

    save();

}//MAIN FUNCTION
