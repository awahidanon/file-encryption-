const fileList = document.getElementById("fileList");

function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  if (file) {
    const fileItem = document.createElement("div");
    fileItem.className = "file-item";
    fileItem.textContent = file.name;
    fileList.appendChild(fileItem);
    fileInput.value = ""; // Clear input
  } else {
    alert("Please select a file to upload.");
  }
}
