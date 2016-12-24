global.jQuery = require("jquery");

export function messages(){

    let $messages = $('.messagelist');
    $messages.find('li').append('<button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>');

    $messages.find('.error').addClass('alert alert-danger alert-dismissible');
    $messages.find('.success').addClass('alert alert-success alert-dismissible');

}
