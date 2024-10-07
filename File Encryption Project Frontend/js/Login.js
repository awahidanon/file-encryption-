let isLogin = true;

function toggleForm() {
  isLogin = !isLogin;
  const formTitle = document.getElementById("formTitle");
  const submitButton = document.getElementById("submitButton");

  if (isLogin) {
    formTitle.textContent = "Login";
    submitButton.textContent = "Login";
    document.getElementById("username").placeholder = "Username";
  } else {
    formTitle.textContent = "Sign Up";
    submitButton.textContent = "Sign Up";
    document.getElementById("username").placeholder = "Email";
  }
}

function handleSubmit() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  if (isLogin) {
    // Simulate login (replace with actual login logic)
    alert(`Logging in as ${username}`);
  } else {
    // Simulate signup (replace with actual signup logic)
    alert(`Signing up with ${username}`);
  }

  // Reset fields after submission
  document.getElementById("username").value = "";
  document.getElementById("password").value = "";
}
