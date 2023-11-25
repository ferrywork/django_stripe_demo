function FirstNameValidate(){
    var firstname_value = $("#firstname").val()
    var regex_var =/^[ A-Za-z]*$/;

    if (firstname_value){
		if (firstname_value.match(regex_var)) {

	    	if(firstname_value.length <= 2 || firstname_value.length > 100){
				$("#firstname").addClass('has-error');
				$("#firstname").removeClass('has-success');
				$("#firstname").text("It must contain minimum 3 characters")
				return false;
			}
			else{
				$("#firstname").text("");
				$("#firstname").removeClass('has-error');
				$("#firstname").addClass('has-success');
				return true;


			}


		}

		else{
			$("#firstname").addClass('has-error');
			$("#firstname").removeClass('has-success');
			$("#firstname").text("Invalid username")
			return false;

		}
	}
	else{

		$("#firstname_label").text("Please fill out this Field")
		$("#firstname").addClass('has-error');
		$("#firstname").removeClass('has-success');
		}  
	}

function LastNameValidate(){
    var lastname_value = $("#lastname").val()
    var regex_var =/^[ A-Za-z]*$/;
    

    if (lastname_value){
        if (lastname_value.match(regex_var)) {

            if(lastname_value.length <= 2 || lastname_value.length > 100){
                $("#lastname").addClass('has-error');
                $("#lastname").removeClass('has-success');
                $("#lastname").text("It must contain minimum 3 characters")
                return false;
            }
            else{
                $("#lastname").text("");
                $("#lastname").removeClass('has-error');
                $("#lastname").addClass('has-success');
                return true;
            }
        }

        else{
            $("#lastname").addClass('has-error');
            $("#lastname").removeClass('has-success');
            $("#lastname").text("Invalid username")
            return false;
        }
    }
    else{

        $("#lastname_label").text("Please fill out this Field")
        $("#lastname").addClass('has-error');
        $("#lastname").removeClass('has-success');
        }  
    }
    
function PhoneNumberValidate(){
    var phonenumber_value = $("#phonenumber").val()
    var regex_var =/^[ 0-9]*$/;
    
    if (phonenumber_value){
        if (phonenumber_value.match(regex_var)) {

            if(phonenumber_value.length <= 10 || phonenumber_value.length > 14){
                $("#phonenumber").addClass('has-error');
                $("#phonenumber").removeClass('has-success');
                $("#phonenumber").text("It must contain minimum 3 characters")
                return false;
            }
            else{
                $("#phonenumber").text("");
                $("#phonenumber").removeClass('has-error');
                $("#phonenumber").addClass('has-success');
                return true;
            }
        }

        else{
            $("#phonenumber").addClass('has-error');
            $("#phonenumber").removeClass('has-success');
            $("#phonenumber").text("Invalid username")
            return false;

        }
    }
    else{

        $("#phonenumber_label").text("Please fill out this Field")
        $("#phonenumber").addClass('has-error');
        $("#phonenumber").removeClass('has-success');
        }  
    }

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


//NEXT PAGE LOAD, THE USERNAME & PASSWORD WILL BE SHOWN IN THEIR FIELDS
$(document).ready(function(){
    var usename_val = localStorage.getItem("username_id"); //"USERNAME" COOKIE
    var password_val = localStorage.getItem("registerPassword"); //"PASSWORD" COOKIE

    $("#username_id").val(usename_val); //FILLS WITH "USERNAME" COOKIE
    $("#registerPassword").val(password_val); //FILLS WITH "PASSWORD" COOKIE
})

