const fileList = document.getElementById("fileList");
const uploadModal = document.getElementById("uploadModal");
const progressContainer = document.getElementById("progressContainer");
const progressBar = document.getElementById("progressBar");

function openModal() {
  uploadModal.style.display = "block";
}

function closeModal() {
  uploadModal.style.display = "none";
  resetUpload();
}

function resetUpload() {
  document.getElementById("fileInput").value = "";
  progressContainer.style.display = "none";
  progressBar.style.width = "0%";
}

function startUpload() {
  const fileInput = document.getElementById("fileInput");
  const file = fileInput.files[0];

  if (file) {
    const fileItem = document.createElement("div");
    fileItem.className = "file-item";
    fileItem.textContent = file.name;
    fileList.appendChild(fileItem);

    // Simulate upload process
    progressContainer.style.display = "block";
    let progress = 0;

    const interval = setInterval(() => {
      if (progress >= 100) {
        clearInterval(interval);
        closeModal();
      } else {
        progress += 10; // Simulate progress
        progressBar.style.width = progress + "%";
      }
    }, 300); // Simulate upload time
  } else {
    alert("Please select a file to upload.");
  }
}

window.onclick = function (event) {
  if (event.target == uploadModal) {
    closeModal();
  }
};
