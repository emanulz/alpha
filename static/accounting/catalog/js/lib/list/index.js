var $ = require('jquery');
var jQuery = require('jquery');

window.$ = $;
window.jQuery = jQuery;


$(document).on('ready', mainListCatalog );

import {listData} from './listData';


//------------------------------------------------------------------------------------------
function mainListCatalog() {
    listData();

}//MAIN FUNCTION
