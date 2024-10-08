// Example shared files data
const sharedFiles = [
  { name: "Report.pdf", sharedWith: "User A", permissions: "View" },
  {
    name: "Presentation.pptx",
    sharedWith: "User B",
    permissions: "Edit",
  },
  { name: "Budget.xlsx", sharedWith: "User C", permissions: "View" },
  { name: "Design.png", sharedWith: "User D", permissions: "Edit" },
];

const fileList = document.getElementById("fileList");

// Function to display shared files
function displaySharedFiles() {
  fileList.innerHTML = ""; // Clear previous items
  sharedFiles.forEach((file) => {
    const fileItem = document.createElement("div");
    fileItem.className = "file-item";
    fileItem.innerHTML = `
            <strong>${file.name}</strong><br>
            Shared with: ${file.sharedWith}<br>
            Permissions: ${file.permissions}<br>
            <button class="button" onclick="managePermissions('${file.name}')">Manage Permissions</button>
          `;
    fileList.appendChild(fileItem);
  });
}

// Function to manage shared permissions
function managePermissions(fileName) {
  const newPermission = prompt(
    `Change permissions for ${fileName} (View/Edit):`,
    "View"
  );
  if (newPermission === "View" || newPermission === "Edit") {
    const file = sharedFiles.find((f) => f.name === fileName);
    if (file) {
      file.permissions = newPermission;
      alert(`Permissions for ${fileName} updated to ${newPermission}`);
      displaySharedFiles(); // Refresh to show updated permission
    }
  } else {
    alert('Invalid permission. Please enter "View" or "Edit".');
  }
}

// Load shared files on page load
window.onload = displaySharedFiles;
