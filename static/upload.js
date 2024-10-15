let caption = document.getElementById("caption");
let counter = document.getElementById("counter");
caption.addEventListener("keyup", () => {
    if (caption.value.length <= 150) {
        counter.innerHTML = caption.value.length + "/150";
    } else {
        caption.value = caption.value.substring(0, caption.value.length - 1);
    }
})

let activity = document.getElementById("upload-input");
activity.onchange = (ev) => {
    if (activity.files) {
        let activityPreview = document.getElementById("activity-preview");
        document.getElementById("upload-submit").disabled = false
        document.getElementById("preview-div").classList.remove("hidden")
        document.getElementById("file-uploader").classList.add("hidden")
        document.getElementById("upload-input").classList.add("hidden")
        
        let reader = new FileReader();
        reader.readAsDataURL(activity.files[0])
        reader.onload = (e) => {
            activityPreview.src = e.target.result;
        }
    }
}

window.onload = () => {
    document.getElementById("id_privacy_settings_0").checked = true
}