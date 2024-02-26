document.addEventListener("DOMContentLoaded", function () {
  var messageElement = document.querySelector(".alert");

  if (messageElement) {
    setTimeout(function () {
      messageElement.style.display = "none";
    }, 5000);
  }
});
