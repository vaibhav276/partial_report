
function populateForm() {
  var preset = parseInt($('#preset').val(), 10);
  if (preset == 1) {
    $('#matrix_size').val(2); //.prop('disabled', true);
    $('#data_type').val(1); //.prop('disabled', true);
    $('#num_trials').val(1); //.prop('disabled', true);
  }
}

populateForm();
