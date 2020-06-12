// Ex7
function dst(position){
    $.get("/dst",{lat:position.coords.latitude, lon: position.coords.longitude},function(response){
        var text ="<h2> Estádio dos Lampiões a " +response.distance+" km</h2>";
        $("#dst").html(text);
    });
}

// Ex6
function refresh(){
    $.get("/time",function(response){
        var text="<h2>"+response.date+"</h2><br /><h2>"+response.time+"</h2>";
        $("#clock").html(text);
    });
    // Ex7
    navigator.geolocation.getCurrentPosition(dst)
}

$( document ).ready(function() {
    $("#refresh").on("click",refresh);
});