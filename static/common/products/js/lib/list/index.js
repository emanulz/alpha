var $ = require('jquery');
global.jQuery = require("jquery");

window.$ = $;
window.jQuery = jQuery;


var bootstrap = require('bootstrap');

require('controller');


$(document).on('ready', mainListProducts );


//MAIN
//------------------------------------------------------------------------------------------
function mainListProducts() {

    $('.list-table').dynatable();

}//MAIN FUNCTION
