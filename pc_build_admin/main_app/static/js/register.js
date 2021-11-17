$('#registerForm').on('submit', function(e){

    var formData = new FormData();

    formData.append('email', $('#registerEmail').val());
    formData.append('password', $('#password').val());
    formData.append('confirm_password', $('#confirm_password').val());
    formData.append('first_name', $('#first_name').val());
    formData.append('last_name', $('#last_name').val());
    formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  
    e.preventDefault();
    console.log("1");
    $.ajax({
        type: 'post',
        url: "/register_admin_firebase/",
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        data: formData,
        success: function(data){

            if(data == 'Email Already Exists!'){
              Swal.fire({
                  icon: 'error',
                  title: 'Oops...',
                  text: data,
                })
            }
            else if(data == 'Password Do not Match!'){
              Swal.fire({
                  icon: 'error',
                  title: 'Oops...',
                  text: data,
                })
            }
            else if(data == 'New User Registered Successfully!'){
              Swal.fire({
                  position: 'middle',
                  icon: 'success',
                  title: 'Success!',
                  text: 'New User Registered Successfully!',
                  showConfirmButton: true,
                  confirmButtonText: 'PROCEED',
                }).then((result) => {
                  if (result.isConfirmed) {
                      location.reload();
                  }
                })
            }
  
        },
        error: function(data){

            Swal.fire({
                  icon: 'error',
                  title: 'Oops...',
                })
        }
  
    });
  });