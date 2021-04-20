const month = document.getElementById("month");
let monthLabel = document.getElementById("mlabel");

const day = document.getElementById("day");
let dayLabel = document.getElementById("dlabel");

const year = document.getElementById("year");
let yearLabel = document.getElementById("ylabel");

month.onchange = (ev) => monthLabel.classList.add("hidden");
day.onchange = (ev) => dayLabel.classList.add("hidden");
year.onchange = (ev) => yearLabel.classList.add("hidden");

