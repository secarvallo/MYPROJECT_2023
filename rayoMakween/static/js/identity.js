$(document).ready(function(){
  
    $("#btnlogin").click(function(){
        $("#txtcorreo").blur(function(){
                alert("el input de correo ha perdido el foco");
        
        });
        
        var email = $("#txtcorreo").val();
        var clave = $("#txtclave").val();

        if(email == "" || clave == ""){
            Swal.fire({
                title: 'Error',
                text: 'Campos Vacios',
                imageUrl: 'https://cdn.pixabay.com/photo/2023/05/23/20/29/rayo-makween-8013448_150.png',
                icon: 'error',
                width: 400,
                imageAlt: 'Custom image',
                }
            );
        }else{
            if(email === "se.carvallo@duocuc.cl" && clave === "duoc"){
                Swal.fire({
                    title: 'Felicitaciones!',
                    text: 'Usuario correcto.',
                    imageUrl: 'https://cdn.pixabay.com/photo/2023/05/23/20/29/rayo-makween-8013448_150.png',
                    icon: 'success',
                    width: 400,
                    imageAlt: 'Custom image',
                
                } );           
                $("#error").addClass("d-none");   
                $("#correcto").removeClass("d-none");
            } else{
                Swal.fire({
                    title: 'Uuuuupss!',
                    text: 'Usuario incorrecto.',
                    imageUrl: 'https://cdn.pixabay.com/photo/2023/05/23/20/29/rayo-makween-8013448_150.png',
                    icon: 'warning',
                    width: 400,
                    imageAlt: 'Custom image',
                });
            }
        }
    });
});


/*const form = document.getElementById("form1");

form.addEventListener("submit", function(event){
    event.preventDefault();
        console.log(event);
        alert("Se detecto un evento")
});*/
