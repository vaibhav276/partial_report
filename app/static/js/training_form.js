$(document).ready(function() {
  applyPreset(1);
  $('#preset1').click(function() { applyPreset(1); });
  $('#preset2').click(function() { applyPreset(2); });
  $('#preset3').click(function() { applyPreset(3); });
  $('#preset4').click(function() { applyPreset(4); });
});

function applyPreset(preset) {
  if (preset == 1) {
    $('#matrix_size').val(3); 
    $('#data_type').val(1); 
    $('#num_trials').val(5);
  } else if (preset == 2) {
    $('#matrix_size').val(3); 
    $('#data_type').val(2); 
    $('#num_trials').val(5);
  } else if (preset == 3) {
    $('#matrix_size').val(2); 
    $('#data_type').val(1); 
    $('#num_trials').val(5);
  } else if (preset == 4) {
    $('#matrix_size').val(2); 
    $('#data_type').val(2); 
    $('#num_trials').val(5);
  }
}

