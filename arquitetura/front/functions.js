/*
 Desenvolvido por Thiago Fernandes	
 AC99dc@gmail.com - thiago_rainmaker@hotmail.com
*/

console.log(config.calc)
const http  = new XMLHttpRequest();


jQuery.support.cors = true; 
$.ajax({ 
	url: "https://kne3fkjbwc.execute-api.us-east-1.amazonaws.com/default/calc", 
	type: "GET", 
	dataType: "json", 
	contentType: "application/x-www-form-urlencoded", 

	// data: { order: orderData }, 
	success: function (response) { 
		alert(response); 
		// orderId = data; 
	} 

});

http.onreadystatechange = (e) => {

	if (http.readyState === XMLHttpRequest.DONE) {
		// Everything is good, the response was received.
  		console.log(http.responseText)
	} else {
		// Not ready yet.
	}

}

function setValue(value){
	obj = document.getElementById('visor');
	obj.value = obj.value+value;
}
function limpar(){
	obj = document.getElementById('visor');	
	obj.value = '';
}
function cont(value){
	obj = document.getElementById('visor');
	objNum = document.getElementById('num');
	objOperacao = document.getElementById('operacao');
	objNum.value = obj.value;
	obj.value = '';
	objOperacao.value = value;
}

function exe(){
	obj = document.getElementById('visor');
	objNum = document.getElementById('num');
	objOperacao = document.getElementById('operacao');
	var	params = "op1="+objNum.value+"&op2="+obj.value;
	console.log(params);
	switch (objOperacao.value){
		case "+":
			url = config.soma;
			result = parseFloat(obj.value) + parseFloat(objNum.value);
			http.open("GET", url, true);
  
		break;
		case "-":
			result = parseFloat(objNum.value) - parseFloat(obj.value);
		break;
		case "*":
			result = parseFloat(obj.value)*parseFloat(objNum.value);
		break;
		case "/":
			result = parseFloat(objNum.value)/parseFloat(obj.value);
		break;
	}
	//http.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
	http.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http.setRequestHeader("Access-Control-Allow-Headers","x-requested-with")
	http.setRequestHeader("contentType", "application/x-www-form-urlencoded")


	http.send(params)
	objNum.value = '';
	objOperacao.value = '';
	obj.value = result;
}


