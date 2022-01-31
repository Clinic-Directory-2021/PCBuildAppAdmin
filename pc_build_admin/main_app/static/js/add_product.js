$('#add_product_form').on('submit', function(e){
    var formData = new FormData();

    var files = $('#product_img')[0].files[0];
  
    formData.append('product_image', files);
    formData.append('fileName', files.name);

    formData.append('product_name', $('#product_name').val());
    formData.append('product_part', $('#product_part').val());
    formData.append('manufacturer', $('#manufacturer').val());
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

  $(function(){
    $('#product_img').change(function(){
      var input = this;
      var url = $(this).val();
      var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
      if (input.files && input.files[0]&& (ext == "png" || ext == "jpeg" || ext == "jpg")) 
       {
          var reader = new FileReader();
  
          reader.onload = function (e) {
             $('#product_preview_img').attr('src', e.target.result);
          }
         reader.readAsDataURL(input.files[0]);
      }
      else
      {
        $('#product_preview_img').attr('src', '../static/images/map.jpg');
      }
    });
  
  });

  $(function(){
    $('#edit_product_img').change(function(){
      var input = this;
      var url = $(this).val();
      var ext = url.substring(url.lastIndexOf('.') + 1).toLowerCase();
      if (input.files && input.files[0]&& (ext == "png" || ext == "jpeg" || ext == "jpg")) 
       {
          var reader = new FileReader();
  
          reader.onload = function (e) {
             $('#edit_product_preview_img').attr('src', e.target.result);
          }
         reader.readAsDataURL(input.files[0]);
      }
      else
      {
        $('#edit_product_preview_img').attr('src', '../static/images/map.jpg');
      }
    });
  
  });