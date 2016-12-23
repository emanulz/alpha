var $ = require('jquery');

export function blockCheck(blockClass, classToCheck){

    //DOM CACHE
    let $block = $(blockClass);
    let $requires = $block.find(classToCheck);
    let errors = [];

    $.each($requires,(i, $require)=>{

        let field = $require.classList[0];
         $block.find(`.${field}`).removeClass('error-field');

        if(!$require.value){
            errors.push(field);
            $block.find(`.${field}`).addClass('error-field');
        }

    });

    if(errors.length){

        return errors;
    }

    // return true;
    return false;

}