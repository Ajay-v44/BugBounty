$.validator.addMethod(
  "nowhitespace",
  function (value, element) {
    return this.optional(element) || /^\S+$/i.test(value);
  },
  "Username cannot contain white space."
);
$.validator.addMethod(
  "passwordComplexity",
  function (value, element) {
    return (
      this.optional(element) ||
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/.test(
        value
      )
    );
  },
  "Password must contain at least one lowercase letter, one uppercase letter, one digit, one special character, and be at least 8 characters long."
);
$.validator.addMethod("emailChecker", function (value, element) {
  return (
    this.optional(element) ||
    /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(
      value
    )
  );
});
$("#regform").validate({
  rules: {
    regemail: {
      required: true,
      email: true,
      emailChecker: true,
    },
    password: {
      required: true,
      minlength: 8,
      maxlength: 12,
      passwordComplexity: true,
    },
    repeat_password: {
      required: true,
      minlength: 8,
      maxlength: 12,
      passwordComplexity: true,
      equalTo: "#floating_password",
    },
    first_name: {
      required: true,
      minlength: 4,
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
      minlength: 4,
      nowhitespace: true, // Use 'nowhitespace: true' to disallow white space
    },
  },
  messages: {
    regemail: {
      required: "Please enter your email address.",
      email: "Please enter a valid email address.",
      emailChecker: "Please enter a valid email",
    },
    password: {
      required: "Please enter your password.",
      minlength: "Password must be at least 8 characters long.",
      maxlength: "Password must not exceed 12 characters.",
      passwordComplexity:
        "Password must contain at least one lowercase letter, one uppercase letter, one digit, one special character, and be at least 8 characters long.",
    },
    repeat_password: {
      required: "Please repeat your password.",
      minlength: "Password must be at least 8 characters long.",
      maxlength: "Password must not exceed 12 characters.",
      equalTo: "Passwords do not match.",
      passwordComplexity:
        "Password must contain at least one lowercase letter, one uppercase letter, one digit, one special character, and be at least 8 characters long.",
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
