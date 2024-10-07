// Example files data
const files = [
  { name: "Report.pdf" },
  { name: "Presentation.pptx" },
  { name: "Budget.xlsx" },
  { name: "Design.png" },
  { name: "Notes.docx" },
  { name: "ProjectPlan.docx" },
  { name: "Invoice.pdf" },
  { name: "Summary.txt" },
];

const fileList = document.getElementById("fileList");

// Function to display search results
function displayFiles(fileArray) {
  fileList.innerHTML = ""; // Clear previous results
  if (fileArray.length === 0) {
    fileList.innerHTML = "<p>No files found.</p>";
    return;
  }

  fileArray.forEach((file) => {
    const fileItem = document.createElement("div");
    fileItem.className = "file-item";
    fileItem.textContent = file.name;
    fileList.appendChild(fileItem);
  });
}

// Function to search files
function searchFiles() {
  const searchInput = document
    .getElementById("searchInput")
    .value.toLowerCase();
  const filteredFiles = files.filter((file) =>
    file.name.toLowerCase().includes(searchInput)
  );
  displayFiles(filteredFiles);
}
