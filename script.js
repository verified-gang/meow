
document.getElementById("uploadForm").onsubmit = async (e) => {
  e.preventDefault();
  
  const formData = new FormData();
  const imageFile = document.getElementById("imageUpload").files[0];
  formData.append("image", imageFile);

  const response = await fetch("/process-image", {
    method: "POST",
    body: formData,
  });
  
  const data = await response.blob();
  document.getElementById("outputImage").src = URL.createObjectURL(data);
};
