global.jQuery = require("jquery");

export function generalData(){

    //DOM CACHE
    let $general = $('.general-block');

    //SELECTORS
    let $department = $general.find('.department');

    //EVENTS
    //$department.change({$general:$general},departmentChange);

    // $department.trigger("change");


function departmentChange(e) {

    //SELECTORS
    let $general = e.data.$general;
    let $subdepartment = $general.find(".subdepartment");
    let $department = $general.find(".department");

    $subdepartment.find('option').hide();
    $subdepartment.find(`option[department=${$department.val()}]`).show();

    $subdepartment.each(function () {
        if ($(this).css('display') != 'none') {
            $(this).prop("selected", true);
            return false;
        }
    });
}
