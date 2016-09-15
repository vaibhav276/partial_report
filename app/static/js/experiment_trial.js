
settings = {
  elemWidth: 100,
  elemHeight: 100,
  textWidth: 20,
  fixationDuration: 2000,
  displayDuration: 150,
  frequencies: [640, 440, 340, 240]
}

var canvas = $('#trial_canvas');
var responseCanvas = $('#response_canvas');

function startTrial(
    matrix,
    size,
    cueRow,
    duration) {
  console.debug(matrix);
  console.debug(size);
  console.debug(cueRow);
  console.debug(duration);
  showFixationPoint(matrix, size, cueRow, duration);
}

function showFixationPoint( matrix, size, cueRow, duration) {
  var canvasElem = canvas.get(0);
  var ctx = canvasElem.getContext('2d');
  ctx.fillRect(canvas.width()/2 - 5, canvas.height()/2 - 5, 10, 10);
  window.setTimeout(showTrialMatrix, settings.fixationDuration, canvas, matrix, size, cueRow, duration);
}

function showTrialMatrix( matrix,
    size,
    cueRow,
    duration) {

  //var width = size * settings.elemWidth;
  //var height = size * settings.elemHeight;
  //canvas.width(width);
  //canvas.height(height);

  var elementPositions = findElementPositions(matrix.length, size);
  var canvasElem = canvas.get(0);
  var ctx = canvasElem.getContext('2d');
  ctx.font = "48px courier";
  ctx.clearRect(0, 0, canvas.width(), canvas.height());
  for(var i = 0; i < elementPositions.length; i++) {
    ctx.fillText(matrix[i], elementPositions[i].x, elementPositions[i].y);
  }

  window.setTimeout(hideTrialMatrix, settings.displayDuration, canvas, cueRow, duration);
}

function hideTrialMatrix(canvas, cueRow, duration) {
  var canvasElem = canvas.get(0);
  var ctx = canvasElem.getContext('2d');
  ctx.clearRect(0, 0, canvas.width(), canvas.height());

  window.setTimeout(playTone, duration, cueRow);
}

function playTone(cueRow) {
	audio.draw_and_play(settings.frequencies[cueRow]);
}

var audio = {
	 draw_and_play: function(frequency) {

		sampleRate = 44100;
		//  var samples_length = sampleRate; // divide by 2 ???
		var samples = [] //new Float32Array(samples_length);

		// var frequency = 440;                      // 440 Hz = "A" note
		var samples_length = 44100;               // Plays for 1 second (44.1 KHz)
		for (var i=0; i < samples_length ; i++) { // fills array with samples
			var t = i/samples_length;               // time from 0 to 1
			samples[i] = Math.sin( frequency * 2*(Math.PI)*t ); // wave equation (between -1,+1)
			samples[i] *= (1-t);                    // "fade" effect (from 1 to 0)
		}

		if (samples.length==0) {
			alert("ERROR: No values in array 'samples'");
			return;
		}

		this.normalize_invalid_values(samples); // keep samples between [-1, +1]

		var wave = new RIFFWAVE();
		wave.header.sampleRate = sampleRate;
		wave.header.numChannels = 1;
		var audio = new Audio();
		var samples2=this.convert255(samples);
		wave.Make(samples2);
		audio.src=wave.dataURI;
		// setTimeout(function() { audio.play(); }, 10); // page needs time to load?
		audio.play();
	},

	normalize_invalid_values: function(samples) {
		for (var i=0, len=samples.length; i<len; i++) {
			if (samples[i]>1) {
				samples[i] = 1;
			} else if (samples[i]<-1) {
				samples[i] = -1;
			}
		}
	},

	convert255: function(data) {
		var data_0_255=[];
		for (var i=0;i<data.length;i++) {
			data_0_255[i]=128+Math.round(127*data[i]);
		}
		return data_0_255;
	}
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
