$('#add_product_form').on('submit', function(e){
    var formData = new FormData();
  
    formData.append('product_name', $('#product_name').val());
    formData.append('product_part', $('#product_part').val());
    formData.append('product_price', $('#product_price').val());
    formData.append('stocks', $('#stocs').val());

    formData.append('csrfmiddlewaretoken', $("input[name='csrfmiddlewaretoken']").val());
  
    e.preventDefault();
    console.log("1");
    $.ajax({
        type: 'post',
        url: "/add_product/",
        enctype: 'multipart/form-data',
        processData: false,
        contentType: false,
        data: formData,
        success: function(data){

            if(data == 'Product Already Exists!'){
              Swal.fire({
                  icon: 'error',
                  title: 'Oops...',
                  text: data,
                })
            }
            else if(data == 'Success!'){
              Swal.fire({
                  icon: 'success',
                  title: 'Product Successfully Added!',
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