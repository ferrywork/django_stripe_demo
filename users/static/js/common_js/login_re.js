
// validations applying on Username
function UserNameValidate() {
    var user_value = $("#username").val()
    var regex_var =/^[ A-Za-z0-9-@&_.]*$/;

    if (user_value){
		if (user_value.match(regex_var)) {

	    	if(user_value.length <= 7 || user_value.length >25){
				$("#username").addClass('has-error');
				$("#username").removeClass('has-success');
				$("#user_label").text("It must contain minimum 8 characters")
				return false;
			}
			else{
				$("#user_label").text("");
				$("#username").removeClass('has-error');
				$("#username").addClass('has-success');
				return true;


			}


		}

		else{
			$("#username").addClass('has-error');
			$("#username").removeClass('has-success');
			$("#user_label").text("Invalid username")
			return false;

		}
	}
	else{

		$("#user_label").text("Please fill out this Field")
		$("#username").addClass('has-error');
		$("#username").removeClass('has-success');
		}  
	}

// validations applying on username ends here

// validations applying on password_label
function PasswordValidate() {
    password_value = $("#password").val();
    var regex_var = /^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=])(?=\S+$).{8,}$/
    if (password_value){
		if (password_value.match(regex_var)) {
				$("#password_label").text("")
				$("#password").removeClass('has-error');
				$("#password").addClass('has-success');
				return true;
		}
		else {
			$("#password_label").text("It must contain one lowercase,uppercase,digit and one special character")
			$("#password").addClass('has-error');
			$("#password").removeClass('has-success');
			return false;
		    }
		}
    else {
        $("#password_label").text("Please fill out this Field")
        $("#password").addClass('has-error');
        $("#password").removeClass('has-success');

        return false;
    }
}

// validations applying on password_label ends here


$(document).on('submit', '#loginform', function(){
	if (UserNameValidate() && Password_Register() == true){
		return true;
	}
	else{
		UserNameValidate();
		Password_Register();
		return false;
	}

})



// making function here for remember me functionality
function remember_me_hit_while_submitting() {
    var checkbox_value = $("#remember_me");
    if (checkbox_value.is(":checked")) {
        var usename_val = $('#username_id').val(); //VALUE OF USERNAME
        var password_val = $('#registerPassword').val(); //VALUE OF PASSWORD

        console.log("password_val is ----->", password_val)

        localStorage.setItem('username_id', usename_val); //SETTING VALUE IN LOCAL STORAGE
        localStorage.setItem('registerPassword', password_val); //SETTING VALUE IN LOCAL STORAGE
    } else {
        localStorage.setItem('username_id', ''); //SETTING VALUE IN LOCAL STORAGE i.e None
        localStorage.setItem('username_id', ''); //SETTING VALUE IN LOCAL STORAGE i.e None
    }
}
// ends here making function here for remember me functionality

//NEXT PAGE LOAD, THE USERNAME & PASSWORD WILL BE SHOWN IN THEIR FIELDS
$(document).ready(function(){
    var usename_val = localStorage.getItem("username_id"); //"USERNAME" COOKIE
    var password_val = localStorage.getItem("registerPassword"); //"PASSWORD" COOKIE

    $("#username_id").val(usename_val); //FILLS WITH "USERNAME" COOKIE
    $("#registerPassword").val(password_val); //FILLS WITH "PASSWORD" COOKIE
})

