$(document).ready(
    function(){
        $("#form-login").submit(function(){
            if($("#user").val().length == 0){
                $("#p-user").html("este campo no debe estar vacio")
                $("#user").css("border-color", "red");
                event.preventDefault()
            }else{
                $("#p-user").html("")
            }
            if($("#password").val().length == 0){
                $("#p-password").html("este campo no debe estar vacio")
                $("#password").css("border-color", "red");
                event.preventDefault()
            }else{
                $("#p-password").html("")
            }
        })
    }
)