$(document).on("submit", "#values-form", (e) => {
    e.preventDefault();
    const form = document.getElementById("values-form");
    var values = {};
    Array.from(form.elements).forEach(element => {  
        if (element.getAttribute("name") != null) {
            values[element.getAttribute("name")] = element.value;
        }
    });
    $.ajax({
        type : 'POST',
        url : window.location.href,
        data : values,
    })
})

const forcesDiv = document.getElementById("forces-div")
let forceCounter = 0;
function addForce() {
    forceCounter++;
    const timeSelect=`<option value="ms">milliseconds</option>
            <option value="s" selected="selected">seconds</option>
            <option value="m">minutes</option>
            <option value="h">hours</option>
            <option value="d">days</option>
            <option value="mo">months</option>
            <option value="y">years</option>`
    const html = `<br>
    <p>Name: </p>
    <input class="input" type="text">
    <p style="padding-left:20px;">Strength:</p>
    <input class="input" name="force-${forceCounter}" type="number" value="1">
    <p>newtons</p>
    <p style="padding-left:20px;">Angle:</p>
    <input class="input" name="force-${forceCounter}-ang" type="number" value="0">
    <select name="force-${forceCounter}-ang-units">
        <option value="rd">radians</option>
        <option value="dg">degrees</option>
    </select>
    <p style="padding-left:20px;">Interval Active:</p>
    <input class="input" name="force-${forceCounter}-start" type="number" value="0">
    <select name="force-${forceCounter}-start-units">
        ${timeSelect}
    </select>
    <p style="padding-left:10px; padding-right:10px;">to</p>
    <input class="input" name="force-${forceCounter}-end" id="force-${forceCounter}-end" type="number" value="${document.getElementById("time").value}" onchange="endChanged(${forceCounter});">
    <select name="force-${forceCounter}-end-units" id="force-${forceCounter}-end-units" onchange="endChanged(${forceCounter});">
        ${timeSelect}
    </select>
    `
    forcesDiv.innerHTML = forcesDiv.innerHTML + html;
}

function gravChanged() {
    const checkbox = document.getElementById("grav-checkbox");
    const gravDiv = document.getElementById("grav-input");
    if (checkbox.checked) {
        gravDiv.innerHTML = `<input class="input" type="number" name="grav-coeff" value="9.81">`;
    } else {
        gravDiv.innerHTML = ``;
    }
}

var toSec = {
    "ms" : 0.001,
    "s" : 1,
    "m" : 60,
    "h" : 3600,
    "d" : 86400,
    "mo" : 2628000,
    "y" : 31556952,
}

function endChanged(forceNum) {
    const endInput = document.getElementById(`force-${forceNum}-end`);
    var endInputValue = endInput.value;
    const endUnits = document.getElementById(`force-${forceNum}-end-units`).value;
    endInputValue *= toSec[endUnits];
    const timeInput = document.getElementById("time").value;
    const timeUnits = document.getElementById("time-units").value
    console.log(timeInput * toSec[timeUnits] * (1/toSec[endUnits]));
    if (endInputValue > timeInput) endInput.value = timeInput * toSec[timeUnits] * (1/toSec[endUnits]);
}