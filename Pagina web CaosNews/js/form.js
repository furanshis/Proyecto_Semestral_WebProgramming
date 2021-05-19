$(document).ready(
    function(){
        $("#form-motivo").submit(function(){
            var comuna = $("#comuna").val()
            if(comuna.length == 0){
                $('#p-comuna').html("*Este campo no debe estar vacío")
                $("#comuna").css("border-color", "red");
                event.preventDefault()
            }else{
                $('#p-comuna').html("*")
            }

            if($('#direccion').val().length == 0){
                $('#p-direccion').html("*Este campo no debe estar vacío")
                $("#direccion").css("border-color", "red");
                event.preventDefault()
            }else{
                $('#p-direccion').html('')
            }

            if($('#nombre').val().length == 0){
                $('#p-nombre').html("*Este campo no debe estar vacío")
                $("#nombre").css("border-color", "red");
                event.preventDefault()
            }else{
                $('#p-nombre').html('')
            }

            if($('#app').val().length == 0){
                $('#p-app').html("*Este campo no debe estar vacío")
                $("#app").css("border-color", "red");
                event.preventDefault()
            }else{
                $('#p-app').html('')
            }

            if($('#apm').val().length == 0){
                $('#p-apm').html("*Este campo no debe estar vacío")
                $("#apm").css("border-color", "red");
                event.preventDefault()
            }else{
                $('#p-apm').html('')
            }

            if($('#email').val().length == 0){
                $('#p-email').html("*Este campo no debe estar vacío")
                $("#email").css("border-color", "red");
                event.preventDefault()
            }else{
                $('#p-email').html('')
            }
            

        });
    }
)