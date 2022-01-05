
function deleteProduct(product_id, img_directory){

    Swal.fire({
        icon: 'question',
        title: 'Do you Really Want to Delete this Product?',
        text: 'This Cannot Be Undone!',
        showDenyButton: true,
        showCancelButton: true,
        showConfirmButton: false,
        denyButtonText: `Delete`,
      }).then((result) => {
          if (result.isDenied) {
            var url = "/delete_Product";

            // Construct the full URL with "id"
            document.location.href = url + "?product_id=" + product_id+ "&img_directory=" + img_directory;
        }
      })

}