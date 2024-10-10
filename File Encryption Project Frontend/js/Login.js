let isLogin = true;

function toggleForm() {
  isLogin = !isLogin;
  const formTitle = document.getElementById("formTitle");
  const submitButton = document.getElementById("submitButton");
  const usernameField = document.getElementById("username");

  if (isLogin) {
    formTitle.textContent = "Login";
    submitButton.textContent = "Login";
    usernameField.type = "text";
    usernameField.placeholder = "Username";
  } else {
    formTitle.textContent = "Sign Up";
    submitButton.textContent = "Sign Up";
    usernameField.type = "email";
    usernameField.placeholder = "Email";
  }
}

function handleSubmit() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;
  alert(`Submitting: ${isLogin ? "Login" : "Signup"} for ${username}`);
  // Handle submission logic here
}
