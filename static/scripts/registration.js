let submit_button = document.querySelector('.submit-button');

function validateForm(){

	let registration = document.querySelector('.registration');

	let email = document.querySelector('.email');
	let login = document.querySelector('.login');
	let password = document.querySelector('.password');
	let repassword = document.querySelector('.repassword');

	registration.submit();

	alert(123);

}

submit_button.onclick = validateForm;