var $ = require('jquery');

import { blurElement } from "./blurElement"
import { handleCode } from "./handleCode"

import { updateTotals } from "./updateTotals"
import { rowUpdate } from "./rowUpdate"

import { setClient } from "./setClient"

//------------------------------------------------------------------------------------------
//SELECTORS
//------------------------------------------------------------------------------------------

var html = $('html');
var product_panel = $('.cd-panel-search-product');
var client_panel = $('.cd-panel-search-client');
var pay_panel = $('.cd-panel-pay');

var btn_product_search = $('.product-search-btn');
var btn_client_search = $('.btn-client-search');
var btn_pay = $('.btn-pay');

var product_code_field = $('.product_code_field');
var client_code_field = $('.client_code_field');

//------------------------------------------------------------------------------------------
//BROWSER EVENTS FUNCTIONS
//------------------------------------------------------------------------------------------
export function browserObjectEvents(store){
    //--------------------------------------------------------------------------------------
    //EVENTS PRODUCT SEARCH PANEL
    //--------------------------------------------------------------------------------------

    btn_product_search.on('click', function(event){
        event.preventDefault();
        product_panel.addClass('is-visible');
        blurElement('.blur-div',2);

    });

    product_panel.on('click', function(event){
        if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
            product_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
        }
    });

    $('#btncerrarbuscar').on('click', function(event){
            product_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
    });

    //---------------------------------------------------------------------------------------
    //EVENTS CLIENT SEARCH PANEL
    //---------------------------------------------------------------------------------------

    btn_client_search.on('click', function(event){
        event.preventDefault();
        client_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });

    client_panel.on('click', function(event){
        if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
            client_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
        }
    });

    $('#btncerrarbuscarcliente').on('click', function(event){
            client_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
    });

    //---------------------------------------------------------------------------------------
    //EVENTS PAY PANEL
    //---------------------------------------------------------------------------------------

    btn_pay.on('click', function(event){
        event.preventDefault();
        pay_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });

    pay_panel.on('click', function(event){
        if( $(event.target).is('.cd-panel') || $(event.target).is('.cd-panel-close') ) {
            pay_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
        }
    });

    $('#btncerrarbuscarpay').on('click', function(event){
            pay_panel.removeClass('is-visible');
            blurElement('.blur-div',0);
            event.preventDefault();
    });
    //---------------------------------------------------------------------------------------

    //EVENTS PRODUCT CODE

    product_code_field.on('keypress', function (e) {
         if(e.which === 13){
             store = handleCode(product_code_field.val(),store);
         }
    });

    // EVENTS PRODUCT SEARCH ACTIONS
    //---------------------------------------------------------------------------------------

    $('#btnbusqueda').on('click', function(event){

        event.preventDefault();
        searchProduct($('#busqueda').val());

    });

    $('#busqueda').on('keypress', function (e) {

        if(e.which === 13){
            e.preventDefault();
            searchProduct($('#busqueda').val());
        }



    });

    html.on('click','.select_product_search_row', function (){

        event.preventDefault();

        var row=$(this).closest("tr");

        var productId = row.attr('class');

        product_code_field.val(productId);

        product_panel.removeClass('is-visible');

        blurElement('.blur-div',0);

        $('.table-body-product-search').html('');

        $('#busqueda').val('');

        product_code_field.focus();

    });
    //---------------------------------------------------------------------------------------

    // EVENTS CLIENT SEARCH ACTIONS
    //---------------------------------------------------------------------------------------

    $('#client-search-btn').on('click', function(event){

        event.preventDefault();
        searchClient($('#client-search-input').val());

    });

    $('#client-search-input').on('keypress', function (e) {

        if(e.which === 13){
            e.preventDefault();
            searchClient($('#client-search-input').val());
        }

    });

    html.on('click','.select_client_search_row', function (){

        event.preventDefault();

        var row=$(this).closest("tr");

        var clientCode = row.attr('class');

        client_code_field.val(clientCode);

        client_panel.removeClass('is-visible');

        blurElement('.blur-div',0);

        $('.client-search-table-body').html('');

        $('#client-search-input').val('');

        client_code_field.trigger('change');

        product_code_field.focus();

    });

    html.on('change','.client_code_field', function () {

        setClient(client_code_field.val());

    });

    //---------------------------------------------------------------------------------------
    html.on('change','.product_qty', function () {

        event.preventDefault();
        var row = $(this).closest("tr");
        var rowIndex = row.index();

        var code = saleList[rowIndex][0];
        var qty = $(`.${code}_product_qty`).val();
        var disc = saleList[rowIndex][5];

        store = rowUpdate(rowIndex, code, qty, saleList, 2,disc, store);

        store = updateTotals(store);

    });

    html.on('change','.product_disc', function () {

        event.preventDefault();
        let row = $(this).closest("tr");
        let rowIndex = row.index();

        var code = saleList[rowIndex][0];
        var qty = saleList[rowIndex][2];
        var disc = $(`.${code}_product_disc`).val();

        rowUpdate(rowIndex, code, qty, saleList, 4, disc);

        updateTotals();

    });

     html.on('change','.sale_global_discount_input', function () {
         console.log('entro');
         updateTotals();
     });


    html.on('click','.remove_row', function () {

        event.preventDefault();
        var row=$(this).closest("tr");
        var rowIndex = row.index();

        store.saleList.splice( rowIndex,1 );

        $(this).parent().parent().remove();

        updateTotals();

        if (store.saleList.length==0){

        }

    });

    //---------------------------------------------------------------------------------------


    // MOUSETRAP SHORTCUTS
    //---------------------------------------------------------------------------------------

    Mousetrap.bind('mod p', function (e) {
        e.preventDefault();
        product_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });

    Mousetrap.bind('mod c', function (e) {
        e.preventDefault();
        client_panel.addClass('is-visible');
        blurElement('.blur-div',2);
    });
    //---------------------------------------------------------------------------------------

    // KEYBOARD SHORTCUTS
    //---------------------------------------------------------------------------------------

    html.on('click','.product_row', function (){
        $('.table-product-selected').removeClass('table-product-selected');
        $(this).addClass("table-product-selected");
    });

    $(document).on('keydown', function (e) {

        var row=$('.table-product-selected');
        var rowIndex = row.index();
        var code;

        if(e.which == 46){//MEAN DELETE KEY

            if(rowIndex != -1){
                store.saleList.splice( rowIndex,1 );

                row.remove();

                store = updateTotals(store);

                if (store.saleList.length==0){

                }
            }

        }

        if(e.which == 107){//MEAN PLUS KEY

            if(rowIndex != -1){

                code = row.attr('class').split(' ')[0];

                store = rowUpdate(rowIndex, code, 1, saleList, 1,0, store);

                store = updateTotals(store);

            }

        }

        if(e.which == 109){//MEAN PLUS KEY

            if(rowIndex != -1){

                code = row.attr('class').split(' ')[0];

                store = rowUpdate(rowIndex, code, -1, saleList, 1,0, store);

                store = updateTotals(store);

            }

        }

    });

    $(':input').focusin(function () {///ON ANY INPUT FOCUS DESELECT ALL ROWS
        $('.table-product-selected').removeClass('table-product-selected');
    });

    return store;


}// BROWSER EVENTS ENDS
//------------------------------------------------------------------------------------------
