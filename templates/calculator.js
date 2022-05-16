$(document).on("submit", "#values-form", (e) => {
    e.preventDefault();
    const form = document.getElementById("values-form");
    var values = {};
    Array.from(form.elements).forEach(element => {  
        if (!(element.getAttribute("name") == null)) {
            values[element.getAttribute("name")] = element.value;
        }
    });
    $.ajax({
        type : 'POST',
        url : '/',
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
    <input type="text">
    <p style="padding-left:20px;">Strength:</p>
    <input name="force-${forceCounter}" type="number" value="1">
    <p>newtons</p>
    <p style="padding-left:20px;">Angle:</p>
    <input name="force-${forceCounter}-ang" type="number" value="0">
    <select name="force-${forceCounter}-ang-units">
        <option value="rd">radians</option>
        <option value="dg">degrees</option>
    </select>
    <p style="padding-left:20px;">Interval Active:</p>
    <input name="force-${forceCounter}-start" type="number" value="0">
    <select name="force-${forceCounter}-start-units">
        ${timeSelect}
    </select>
    <p style="padding-left:10px; padding-right:10px;">to</p>
    <input name="force-${forceCounter}-end" id="force-${forceCounter}-end" type="number" value="${document.getElementById("time").value}" onchange="endChanged(${forceCounter});">
    <select name="force-${forceCounter}-end-units">
        ${timeSelect}
    </select>
    `
    forcesDiv.innerHTML = forcesDiv.innerHTML + html
}

function gravChanged() {
    const checkbox = document.getElementById("grav-checkbox");
    const gravDiv = document.getElementById("grav-input");
    if (checkbox.checked) {
        gravDiv.innerHTML = `<input type="number" name="grav-coeff" value="9.81">`;
    } else {
        gravDiv.innerHTML = ``;
    }
}
function endChanged(forceNum) {
    const endInput = document.getElementById(`force-${forceNum}-end`);
    var endInputValue = endInput.value;
    //endInputValue *= {{ toSec[document.getElementById(`force-${forceNum}-end-units`).value] }};
    const timeInput = document.getElementById("time").value;
    if (endInputValue > timeInput) endInput.value = timeInput;
}