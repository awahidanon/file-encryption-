// Example file data (static for demonstration)
const fileData = {
  name: "example-file.pdf",
  size: "1.2 MB",
  type: "PDF Document",
  uploadDate: "2024-10-07",
};

// Function to display file details
function displayFileDetails(file) {
  document.getElementById("fileName").textContent = file.name;
  document.getElementById("fileSize").textContent = file.size;
  document.getElementById("fileType").textContent = file.type;
  document.getElementById("uploadDate").textContent = file.uploadDate;
}

// Function to handle sharing the file
function shareFile() {
  alert("File shared successfully!"); // Placeholder for sharing logic
}

// Function to handle downloading the file
function downloadFile() {
  alert("Downloading " + fileData.name); // Placeholder for download logic
}

// Function to handle deleting the file
function deleteFile() {
  if (confirm("Are you sure you want to delete this file?")) {
    alert(fileData.name + " has been deleted."); // Placeholder for delete logic
  }
}

// Attach event listeners
document.getElementById("shareButton").onclick = shareFile;
document.getElementById("downloadButton").onclick = downloadFile;
document.getElementById("deleteButton").onclick = deleteFile;

// Display the file details when the page loads
window.onload = function () {
  displayFileDetails(fileData);
};
