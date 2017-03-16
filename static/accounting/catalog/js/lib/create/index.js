var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;

require('controller');

import {loadData} from './loadData';


$(document).on('ready', mainCreateCatalog);

//------------------------------------------------------------------------------------------
function mainCreateCatalog() {

    //Initial Disables

    $(".account-data-div :input").attr("disabled", true);


    loadData();


}//MAIN FUNCTION
