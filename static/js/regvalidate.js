$.validator.addMethod("nowhitespace", function(value, element) {
    return this.optional(element) || /^\S+$/i.test(value);
}, "Username cannot contain white space.");
$("#regform").validate({
    rules: {
        regemail: {
            required: true,
            email: true,
        },
        password: {
            required: true,
            minlength: 4,
            maxlength: 12,
        },
        repeat_password: {
            required: true,
            minlength: 4,
            maxlength: 12,
            equalTo: "#floating_password",
        },
        first_name: {
            required: true,
        },
        last_name: {
            required: true,
        },
        phone: {
            required: true,
            minlength: 10,
            maxlength: 10,
            digits: true,
        },
        username: {
            required: true,
            nowhitespace: true, // Use 'nowhitespace: true' to disallow white space
        },
    },
    messages: {
        regemail: {
            required: "Please enter your email address.",
            email: "Please enter a valid email address.",
        },
        password: {
            required: "Please enter your password.",
            minlength: "Password must be at least 4 characters long.",
            maxlength: "Password must not exceed 12 characters.",
        },
        repeat_password: {
            required: "Please repeat your password.",
            minlength: "Password must be at least 4 characters long.",
            maxlength: "Password must not exceed 12 characters.",
            equalTo: "Passwords do not match.",
        },
        first_name: {
            required: "Please enter your first name.",
        },
        last_name: {
            required: "Please enter your last name.",
        },
        phone: {
            required: "Please enter your phone number.",
            minlength: "Phone number must be 10 digits long.",
            maxlength: "Phone number must be 10 digits long.",
            digits: "Please enter only digits.",
        },
        username: {
            required: "Please enter your username.",
            nowhitespace: "Username cannot contain white space.",
        },
    },
    errorPlacement: function (error, element) {
        error.insertAfter(element); // Show error below each input field
        error.css("color", "red"); // Style error message with red color
    },
    submitHandler: function (form) {
        form.submit(); // Submit the form if it's valid
    },
});
