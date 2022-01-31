
function editProduct(product_id, product_name, product_part, edit_manufacturer,product_price, stocks, old_directory){
   
    $('#product_id_edit').val(product_id);
    $('#product_name_edit').val(product_name);
    $('#product_part_edit').val(product_part);
    $('#edit_manufacturer').val(edit_manufacturer);
    $('#product_price_edit').val(product_price);
    $('#stocks_edit').val(stocks);

    $('#old_img_directory').val(old_directory);
    $('#hello').html(old_directory);
    
}