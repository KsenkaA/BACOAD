function max() {
	var inp1 = document.getElementById('inp1').value;
	var inp2 = document.getElementById('inp2').value;
	// var checkbox = document.getElementById('toggle');
	if (Number(inp1)>Number(inp2)) {
		alert(inp1);
	}
	else {
		alert(inp2);
	}
}

function min() {
	var inp1 = document.getElementById('inp1').value;
	var inp2 = document.getElementById('inp2').value;
	// var checkbox = document.getElementById('toggle');
	if (Number(inp1)>Number(inp2)) {
		alert(Math.abs(inp2));
	}
	else {
		alert(Math.abs(inp1));
	}
}

function w() {
	var i = 0;
	while (i <= 10) {
		console.log(i);
		i++;
	}
}

var count = 0;
function plua() {
	var plus = document.getElementById('plus').value;
	var rez = document.getElementById('rez');
	count = count+1;
	rez.value = count;
}
function reset() {
	count = 0;
	document.getElementById('rez').value = 0;
}