var $ = require('jquery');
var alertify = require('alertifyjs');
const company = $("#id_company").val();
import {blockCheck} from './blockCheck'
import {parseBlockData} from './parseBlockData'

export let productData={};

export function save(){

    productData.company = company;

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

    //CACHE DOM
    let $save = $('.save');
    let $saveBtn = $save.find('.save--btn-save');

    //EVENTS
    //$saveBtn.on('click', saveProduct);

}


function saveProduct(ev) {

    ev.preventDefault();

    let errors = blockCheck('.general-block', '.required');

    // if (errors){
    //     alertify.alert('Error','Hay errores en el formulario, por favor corrija los campos marcados.');
    //     return false;
    //
    // }

    productData = parseBlockData('.general-block', '.field', productData);
    productData = parseBlockData('.sale-block', '.field', productData);
    productData = parseBlockData('.inventory-block', '.field', productData);


    console.log(JSON.stringify(productData));


    $.ajax({
        method: "POST",
        url: "/products/add/",
        data:JSON.stringify(productData),
        contentType:"application/json; charset=utf-8",
        dataType:"json"
    })
    .fail(function(data){
        console.log('fail');
        console.log(data)
    })
    .success(function(data){
        console.log('success');
        console.log(data)
    });//ajax

}