
function editProduct(product_id, product_name, product_part, edit_manufacturer,product_price, stocks, old_directory,generation, socket_type){
   
    $('#product_id_edit').val(product_id);
    $('#product_name_edit').val(product_name);
    $('#product_part_edit').val(product_part);
    $('#edit_manufacturer').val(edit_manufacturer);
    $('#product_price_edit').val(product_price);
    $('#generation_edit').val(generation);
    $('#frequency_edit').val(socket_type);
    $('#stocks_edit').val(stocks);

    $('#old_img_directory').val(old_directory);
    $('#hello').html(old_directory);
    
}