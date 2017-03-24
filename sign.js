function gatherInfo() {
	username = document.getElementById("username").value;
	firstname = document.getElementById("firstname").value;
	//if(!validateName(firstname)) {
		//Fizza will add the warning
//	}
	lastname = document.getElementById("lastname").value;
//	if(!validateName(lastname)) {
		//Fizza will add the warning
//	}
	mobile = document.getElementById("mobile").value;
//	if(!validateMobile(mobile)) {
		//Fizza will add the warning
//	}
	email = document.getElementById("email").value;
//	if(!validateEmail(email)) {
		//Fizza will add the warning
//	}
	password = document.getElementById("password").value;
//	if(!validatePassword(password)) {
		//Fizza will add the warning
//	}
	repassword = document.getElementById("repassword").value;
//	if(!validatePassword(repassword)) {
		//Fizza will add the warning
//	}
    alert('ceva');
	/*if(!matchPasswords(password, repassword)) {
		alert("Passwords entered do not match");
	}*/
	sendInformation(username, firstname, lastname, mobile, email, password);
}

function sendInformation(username, firstname, lastname, mobile, email, password) {
	var jsonObject = new Object();
	jsonObject.type = "register";
	jsonObject.username = username
   	jsonObject.firstname = firstname;
   	jsonObject.lastname  = lastname;
   	jsonObject.mobile = mobile;
   	jsonObject.email = email;
   	jsonObject.password = password;
   	alert(firstname);
   	alert('ceva1');
   	var jsonString= JSON.stringify(jsonObject);
   	ws = new WebSocket("ws://127.0.0.1:9001");
	ws.onopen = function(){
	   ws.send(jsonString);
    };
    ws.onmessage = function(msg) {
    	alert(msg.data);
    };
    
}

function matchPasswords(password, repassword) {
	if(password.localeCompare(repassword)) {
		return True;
	} else {
		return False;
	}
}
