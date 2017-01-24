var $ = require('jquery');

export function parseBlockData(blockClass, fieldClass, object){

    //DOM CACHE
    let $block = $(blockClass);

    let $fields = $block.find(fieldClass);

    $.each($fields,(i, $field)=>{

        let name = $field.classList[0];

        if($field.type == 'checkbox'){
            object[name] = $field.checked;
        }
        else{
            object[name] = $field.value;
        }

    });

    return object;


}
