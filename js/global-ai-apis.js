/**
 * Created by chico_percedes on 2017-06-24.
 */

$(function() {
    var params = {
        // Request parameters
    };

    var instagram_clientid = "cdb6ebd6ab4841d3a518e9ecaef9213d";
    var instagram_secretkey = "43ef1a2a7c484f17aeede55a343ba6fc";

    var jsonresults;

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
            paramupdate(data);
            appendhtml();
        })
        .fail(function(data) {
            console.log(data);
        });

    function paramupdate(value){
        jsonresults = value;
    }

    function appendhtml(){
        $('#hashtag').html("<p>Anger:" + jsonresults[0].scores.anger + "</p>");
    };

});