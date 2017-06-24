/**
 * Created by chico_percedes on 2017-06-24.
 */

$(function() {
    var params = {
        // Request parameters
    };

    $.ajax({
               url: "https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize?" + $.param(params),
               beforeSend: function(xhrObj){
                   // Request headers
                   xhrObj.setRequestHeader("Content-Type","application/json");
                   xhrObj.setRequestHeader("Ocp-Apim-Subscription-Key","3fab902b4add4555bfd10686842091ee");
               },
               type: "POST",
               // Request body
               data: '{ "url" : "http://static2.businessinsider.com/image/5087f99369bedd394700000d/obama-press-conference-obamacare-sad.jpg" }',
           })
        .done(function(data) {
            console.log(data);
        })
        .fail(function(data) {
            console.log(data);
        });
});