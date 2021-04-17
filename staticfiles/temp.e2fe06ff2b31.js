let videos = document.getElementsByClassName('video-js')
let tolerancePixel = 40
let doc = document.documentElement;
const month = document.getElementById("month");
let monthLabel = document.getElementById("mlabel");

const day = document.getElementById("day");
let dayLabel = document.getElementById("dlabel");

const year = document.getElementById("year");
let yearLabel = document.getElementById("ylabel");

document.getElementById("login").addEventListener("click", () => {
    let leftPos = (window.pageXOffset || doc.scrollLeft) - (doc.clientLeft || 0);
    let topPos = (window.pageYOffset || doc.scrollTop)  - (doc.clientTop || 0);
    console.log(topPos, leftPos)
})

month.onchange = (ev) => monthLabel.classList.add("hidden");
day.onchange = (ev) => dayLabel.classList.add("hidden");
year.onchange = (ev) => yearLabel.classList.add("hidden");

