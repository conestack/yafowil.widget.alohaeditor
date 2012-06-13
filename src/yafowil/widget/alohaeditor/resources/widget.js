/*
 * yafowil alohaeditor widget
 *
 * Optional: bdajax
 */

if (typeof(window['yafowil']) == "undefined") yafowil = {};

(function($) {

    $(document).ready(function() {
        // initial binding
        yafowil.alohaeditor.binder();

        // add after ajax binding if bdajax present
        if (typeof(window['bdajax']) != "undefined") {
            $.extend(bdajax.binders, {
                alohaeditor_binder: yafowil.alohaeditor.binder
            });
        }
    });

    $.extend(yafowil, {
        alohaeditor: {
            binder: function(context) {
                Aloha.ready( function(){
                    $('textarea.alohaeditor', context).each(function(event) {
                        var id = $(this).attr('id');
                        var alohajq = Aloha.jQuery;
                        alohajq('#'+id).aloha();
                    });
                });
            }
        }
    });

})(jQuery);
