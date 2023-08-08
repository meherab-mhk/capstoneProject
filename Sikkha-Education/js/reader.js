const one = document.getElementById('one');
const switchBox = document.getElementById('is_checked');
var ctrlPressed = false; // flag to track if Ctrl key is currently pressed
var doubleCtrlPress = false; // flag to track if Ctrl key was double pressed
var pressCount = 0; // variable to store the number of presses
var pressTimeout; // variable to store the ID of the timeout
var pressInterval = 300; // time interval in milliseconds to count presses
let newelement;
const body = document.getElementById('indexBody');
const onRead = "Screen Reader On, press enter to close popup";
const offRead = "Screen Reader Off, press enter to close popup";

const synth = window.speechSynthesis;
const alertReadOn = new SpeechSynthesisUtterance(onRead);
const alertReadOff = new SpeechSynthesisUtterance(offRead);
const menubar = "select menu bar";
const talk_menubar = new SpeechSynthesisUtterance(menubar);
document.addEventListener('keydown', function (event) {
    if (event.key === 'R') {

        if (ctrlPressed && !doubleCtrlPress) {
            pressCount++; // increment the press count if Ctrl is pressed again within the time interval
        } else {
            ctrlPressed = true; // set the flag to true when Ctrl key is pressed for the first time
            doubleCtrlPress = false; // reset the double press flag
            pressCount = 1; // set the press count to 1
        }

        // start a timeout to reset the press count after the time interval
        clearTimeout(pressTimeout);
        pressTimeout = setTimeout(function () {
            pressCount = 0;
        }, pressInterval);

        // check if the press count is 2 to indicate a double press
        if (pressCount === 1) {
            switchBox.checked = !switchBox.checked; // toggle the checked state of the checkbox
            if (switchBox.checked) {
                synth.speak(alertReadOn);
                alert("Screen Reader On, press enter to close!");
                newelement = document.createElement("script");
                const savedText = localStorage.getItem("savedText");
                newelement.textContent = savedText || 'System.load("Main")';
                body.appendChild(newelement);
                localStorage.setItem("savedText", newelement.textContent);
            } else if (!switchBox.checked) {
                synth.speak(alertReadOff);
                alert("Screen Reader Off, press enter to close!");
                body.removeChild(newelement);
                localStorage.removeItem("savedText");
                location.reload();
            }
            doubleCtrlPress = true; // set the double press flag to true
            pressCount = 0; // reset the press count
        }

    }

});

document.addEventListener('keyup', function (event) {
    if (event.key === 'R') {
        ctrlPressed = false; // set the flag to false when Ctrl key is released
        clearTimeout(pressTimeout); // clear the timeout when the key is released
        pressCount = 0; // reset the press count
    }
});

switchBox.addEventListener("change", () => {
    if (switchBox.checked) {
        synth.speak(alertReadOn);
        alert("Screen Reader On, press enter to close!");
        newelement = document.createElement("script");
        const savedText = localStorage.getItem("savedText");
        newelement.textContent = savedText || 'System.load("Main")';
        body.appendChild(newelement);
        localStorage.setItem("savedText", newelement.textContent);

    } else if (!switchBox.checked) {
        synth.speak(alertReadOff);
        alert("Screen Reader Off, press enter to close!");
        body.removeChild(newelement);
        localStorage.removeItem("savedText");
        location.reload();
    }
});
window.addEventListener("load", function () {
    const savedText = localStorage.getItem("savedText");
    if (savedText) {
        switchBox.checked = true;
        newelement = document.createElement("script");
        newelement.textContent = savedText;
        body.appendChild(newelement);
    }
});

document.addEventListener("keydown", function (event) {
    if (event.key === "m") { // Check if the pressed key is M
        if (switchBox.checked) {
            var myDiv = document.getElementById("navMenu");
            myDiv.focus();
            synth.speak(talk_menubar);
        }

    }
});

// select all tag ... press by tab button
// const elements = document.querySelectorAll('p, h1, h2, h3, h4, h5, h6, button, a, span, img,td');
// for (var i = 0; i < elements.length; i++) {
//     elements[i].setAttribute('tabindex', i + 1);
//     elements[i].focus();
// }