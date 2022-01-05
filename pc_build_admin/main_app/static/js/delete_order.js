
function deleteOrder(order_id){

    Swal.fire({
        icon: 'question',
        title: 'Do you Really Want to Delete this Order?',
        text: 'This Cannot Be Undone!',
        showDenyButton: true,
        showCancelButton: true,
        showConfirmButton: false,
        denyButtonText: `Delete`,
      }).then((result) => {
          if (result.isDenied) {
            var url = "/delete_order";

            // Construct the full URL with "id"
            document.location.href = url + "?order_id=" + order_id;
        }
      })

}