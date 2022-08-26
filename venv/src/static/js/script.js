function spin(){


	let x = 1024; //min value
	let y = 9999; // max value

	let deg = Math.floor(Math.random() * (x - y)) + y;

	document.getElementById('box').style.transform = "rotate("+deg+"deg)";

	let element = document.getElementById('mainbox');
	element.classList.remove('animate');
	setTimeout(function(){
		element.classList.add('animate');
	}, 8000); //5000 = 5 second
}