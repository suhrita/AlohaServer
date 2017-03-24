function gatherInfo() {
	alert("hei");
	username = document.getElementById("username").value;
	password = document.getElementById("password").value;
	alert(username+password);
	sendInformation(username, password);
}

function sendInformation(username, password) {
	var jsonObject = new Object();
	jsonObject.type = "authenticate";
	jsonObject.username = username;
   	jsonObject.password = password;
   	var jsonString= JSON.stringify(jsonObject);
   	//ws = new WebSocket("ws://ec2-52-40-170-181.us-west-2.compute.amazonaws.com:9001");
   	ws = new WebSocket("ws://127.0.0.1:9001");
	ws.onopen = function(){
	   ws.send(jsonString);
    };
}
