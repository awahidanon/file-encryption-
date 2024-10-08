const folderList = document.getElementById("folderList");

function openModal(modalId) {
  document.getElementById(modalId).style.display = "block";
}

function closeModal(modalId) {
  document.getElementById(modalId).style.display = "none";
  resetModal();
}

function resetModal() {
  document.getElementById("folderName").value = "";
}

function createFolder() {
  const folderNameInput = document.getElementById("folderName");
  const folderName = folderNameInput.value.trim();

  if (folderName) {
    const folderItem = document.createElement("div");
    folderItem.className = "folder-item";
    folderItem.textContent = folderName;

    folderItem.onclick = () => openFolder(folderName);

    const deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    deleteButton.onclick = (e) => {
      e.stopPropagation();
      deleteFolder(folderItem);
    };

    folderItem.appendChild(deleteButton);
    folderList.appendChild(folderItem);

    closeModal("createModal");
  } else {
    alert("Please enter a folder name.");
  }
}

function openFolder(folderName) {
  alert(`Opening folder: ${folderName}`);
}

function deleteFolder(folderItem) {
  if (confirm("Are you sure you want to delete this folder?")) {
    folderList.removeChild(folderItem);
  }
}

window.onclick = function (event) {
  const modals = document.querySelectorAll(".modal");
  modals.forEach((modal) => {
    if (event.target == modal) {
      closeModal(modal.id);
    }
  });
};
