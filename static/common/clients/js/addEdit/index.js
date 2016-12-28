
global.jQuery = require("jquery");
var $ = require('jquery');

window.$ = $;
window.jQuery = jQuery;

var bootstrap = require('bootstrap');

require('controller');

var qtip = require("qtip");
window.qtip = qtip;

import {creditData} from './credit';

$(document).on('ready', mainCreateProduct );

//MAIN
//------------------------------------------------------------------------------------------
function mainCreateProduct() {

    $('.hasTooltip').each(function() { // Notice the .each() loop, discussed below
        $(this).qtip({
            content: {
                text: $(this).next('div').html() // Use the "div" element next to this for the content
            },
            position: {
                my: 'bottom left',
                at: 'top left'
            },
            style: {
                classes: 'qtip-red qtip-shadow'
            }
        });
    });


    creditData();

}//MAIN FUNCTION
