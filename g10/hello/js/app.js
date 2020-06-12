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

// Ex10
/*function updatePhoto(event){
    var reader = new FileReader();
    reader.onload = function(event){
        //Criar uma imagem
        var img = new Image();
        img.onload = function(){
            //Colocar a imagem no ecrã
            canvas = document.getElementById("photo");
            ctx = canvas.getContext("2d");
            ctx.drawImage(img,0,0,img.width,img.height,0,0,530, 400);
        }
        img.src = event.target.result;
    }
    //Obter o ficheiro
    reader.readAsDataURL(event.target.files[0]);
    sendFile(event.target.files[0]);
}*/

// Ex11
function sendFile(file) {
    var data = new FormData();
    data.append("myFile", file);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "upload");
    xhr.upload.addEventListener("progress", updateProgress, false);
    xhr.send(data);
    }

    function updateProgress(evt){
    if(evt.loaded == evt.total)
    alert("OK!");
    }

    function updatePhoto(evt){
        var reader = new FileReader();
        reader.onload = function(event){
            //Criar uma imagem
            var img = new Image();
            img.onload = function(){
                //Colocar a imagem no ecrã
                canvas = document.getElementById("photo");
                ctx = canvas.getContext("2d");
                ctx.drawImage(img,0,0,img.width,img.height,0,0,530, 400);
            }
            img.src = event.target.result;
        }
        
        //Obter o ficheiro
        reader.readAsDataURL(event.target.files[0]);
        sendFile(image[0]);
        //Libertar recursos da imagem seleccionada
        windowURL.revokeObjectURL(picURL);
    }
    

$( document ).ready(function() {
    $("#refresh").on("click",refresh);
});