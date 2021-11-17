
function deleteAdmin(user_id){

    Swal.fire({
        icon: 'question',
        title: 'Do you Really Want to Delete this Admin?',
        text: 'This Cannot Be Undone!',
        showDenyButton: true,
        showCancelButton: true,
        showConfirmButton: false,
        denyButtonText: `Delete`,
      }).then((result) => {
          if (result.isDenied) {
            var url = "/delete_Admin";

            // Construct the full URL with "id"
            document.location.href = url + "?user_id=" + user_id;
        }
      })

}