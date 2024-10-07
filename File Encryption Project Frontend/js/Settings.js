// Function to update profile information
function updateProfile() {
  const username = document.getElementById("username").value;
  const email = document.getElementById("email").value;
  const currentPassword = document.getElementById("currentPassword").value;
  const newPassword = document.getElementById("newPassword").value;
  const confirmPassword = document.getElementById("confirmPassword").value;

  // Basic validation
  if (newPassword && newPassword !== confirmPassword) {
    alert("New passwords do not match.");
    return;
  }

  // Simulate updating profile (replace with actual logic)
  alert(
    `Profile updated for ${username}!\nEmail: ${email}\nPassword: ${
      newPassword ? "Changed" : "Not changed"
    }`
  );
  resetForm();
}

// Function to reset the form fields
function resetForm() {
  document.getElementById("username").value = "";
  document.getElementById("email").value = "";
  document.getElementById("currentPassword").value = "";
  document.getElementById("newPassword").value = "";
  document.getElementById("confirmPassword").value = "";
}

// Function to upgrade storage plan
function upgradePlan() {
  alert("Redirecting to upgrade plan page..."); // Replace with actual upgrade logic
}
