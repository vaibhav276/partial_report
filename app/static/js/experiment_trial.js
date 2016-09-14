
settings = {
  elemWidth: 100,
  elemHeight: 100,
  textWidth: 20,
  displayDuration: 150
}

function showTrialMatrix(canvas,
    response,
    matrix,
    size,
    cue_row,
    duration) {

  var width = size * settings.elemWidth;
  var height = size * settings.elemHeight;
  canvas.width(width);
  canvas.height(height);

  var elementPositions = findElementPositions(matrix.length, size);
  /*
  var canvasElem = canvas.get(0);
  var ctx = canvasElem.getContext('2d');
  ctx.font = "48px courier";
  for(var i = 0; i < elementPositions.length; i++) {
    ctx.fillText(matrix[i], elementPositions[i].x, elementPositions[i].y);
  }
  */

  console.debug('calling hide');
  window.setTimeout(hideTrialMatrix(canvas), 1500);
}

function hideTrialMatrix(canvas) {
  console.debug('hide called');
  /*
  var canvasElem = canvas.get(0);
  var ctx = canvasElem.getContext('2d');
  ctx.fillRect(0, 0, canvas.width(), canvas.height());
  */
}

function findElementPositions(numElements, size) {
  var offsetX = (settings.elemWidth / 2) - settings.textWidth ;
  var offsetY = settings.elemHeight / 2;

  var positions = [];
  for(var i = 0; i < size; i++) {
    for(var j = 0; j < size; j++) {
      positions.push({x: offsetX + (j * settings.elemWidth), y: offsetY + (i * settings.elemHeight)});
    }
  }

  return positions;
}
