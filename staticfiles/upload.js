let caption = document.getElementById("caption");
let counter = document.getElementById("counter");
caption.addEventListener("keyup", () => {
    if (caption.value.length <= 150) {
        counter.innerHTML = caption.value.length + "/150";
    } else {
        caption.value = caption.value.substring(0, caption.value.length - 1);
    }
})

let video = document.getElementById("upload-input");
video.onchange = (ev) => {
    if (video.files) {
        let videoPreview = document.getElementById("video-preview");
        document.getElementById("upload-submit").disabled = false
        document.getElementById("preview-div").classList.remove("hidden")
        document.getElementById("file-uploader").classList.add("hidden")
        document.getElementById("upload-input").classList.add("hidden")
        
        let reader = new FileReader();
        reader.readAsDataURL(video.files[0])
        reader.onload = (e) => {
            videoPreview.src = e.target.result;
        }
    }
}

window.onload = () => {
    document.getElementById("id_privacy_settings_0").checked = true
}