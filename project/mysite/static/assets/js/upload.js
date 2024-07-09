const dropArea = document.querySelector(".drop_box"),
  button = dropArea.querySelector("button"),
  dragText = dropArea.querySelector("header"),
  input = dropArea.querySelector("input");
let file;
var filename;

button.onclick = () => {
  input.click();
};

input.addEventListener("change", function (e) {
  uploadFile(file);
});

function uploadFile(file) {
    const xhr = new XMLHttpRequest();
    const url = "{% url 'admin' %}"; // Replace with your server endpoint
  
    xhr.open("POST", url, true);
  
    xhr.upload.onprogress = function (e) {
      const percentComplete = (e.loaded / e.total) * 100;
      progressBar.style.width = percentComplete.toFixed(2) + "%";
    };
  
    xhr.onload = function () {
      if (xhr.status === 200) {
        alert("File uploaded successfully!");
      } else {
        alert("File upload failed!");
      }
    };
  
    const formData = new FormData();
    formData.append("file", file);
  
    xhr.send(formData);
  }
