$ = jQuery;
var report = 0;
$( document ).ready(function(){

    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10) {
    dd='0'+dd
    }

    if(mm<10) {
    mm='0'+mm
    }

    FOMonth = yyyy+'-'+mm+'-'+'01';

    today = yyyy+'-'+mm+'-'+dd;

    $('.date').attr('disabled', true);
    $('#generate-Btn').attr('disabled', true);

    $('#start-date').focus( function(){
        $('#start-date').css('border-color','');
    })
    $('#end-date').focus(function(){
        $('#end-date').css('border-color','');
    })

    var modal = $("#dates-modal").iziModal({
        title:'PARÁMETROS',
        subtitle:'Seleccione las fechas',
        overlayClose: false,
        width: 600,
        appendTo:'#content-main',
        overlayColor: 'rgba(0, 0, 0, 0.6)',
        transitionIn: 'bounceInDown',
        transitionOut: 'bounceOutDown',
        navigateCaption: true,
        navigateArrows: 'closeScreenEdge',
        headerColor: '#59677E',
        attached: 'top',
        top:'20%',
        onOpened: function() {

            $('#start-date').val(FOMonth);
            $('#end-date').val(today);
            $('.date').attr('disabled', false);
            $('#generate-Btn').attr('disabled', false);
            $('#start-date').focus();
            //console.log('onOpened');
            var url = $(location).attr('href');
            url = url.split('#');
            window.history.pushState("", "", url[0]);
        },
        onClosed: function() {
            //console.log('onClosed');
            $('.date').attr('disabled', true);
            $('#generate-Btn').attr('disabled', true);
        }

    });

    $('html').on('click','.buttonGenerate', function (event) {
        event.preventDefault();
        report = this.id;
        $('#start-date').css('border-color','');
        $('#end-date').css('border-color','');
        modal.iziModal('open');
    });

    $('html').on('click','#generate-Btn', function (event) {

        event.preventDefault();
        var flag = checkFields();

        if(flag){
            let params = '?dateini='+$('#start-date').val()+'&dateend='+$('#end-date').val()+'&report='+report;
            var dataUrl ='/accounting/reports/'+params
            $(location).attr('href', dataUrl);
        }

    });


});


function checkFields(){

    var startDate = $('#start-date');
    var endDate = $('#end-date');

    if(!startDate.val()){
        startDate.css('border-color','red');
        return false;
    }

    if(!endDate.val()){

        endDate.css('border-color','red');
        return false;
    }

    return true;
}
