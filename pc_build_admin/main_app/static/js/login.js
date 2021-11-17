$('#loginForm').on('submit', function(e){

    $('#loginBtn').prop('disabled', true);
    e.preventDefault();
    console.log("1");
    
    $.ajax({
        type: 'post',
        url: "/login_validation/",
        data: {
          login_email: $('#email').val(),
          login_password: $('#password').val(),
          csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
          },
        success: function(data){
            if(data=="Invalid Email or Password!"){
                //  $('#responseMessage').html(data);
                $('#loginBtn').prop('disabled', false);
                 Swal.fire({
                    icon: 'error',
                    title: data,
                    confirmButtonText: 'OKAY',
                  })
            }else if (data == 'Success!'){
                $('#loginBtn').prop('disabled', false);
                location.reload();
            }
        },
        error: function(data){
            $('#loginBtn').prop('disabled', false);
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
              })
        },
  
    });
});