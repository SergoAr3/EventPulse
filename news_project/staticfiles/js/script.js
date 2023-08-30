function checkEmail() {
    var email = $('#email').val()
    var pattern = $('#email').attr('pattern');
    var regex = new RegExp(pattern);

    if (regex.test(email)) {
        $('#submit').removeAttr('disabled');
    } else {
        $('#submit').attr('disabled', 'disabled');
    }
}

const COLOR_RED = "#eb2940";
const COLOR_WHITE = "#f7fafe";
const DURATION_MULTIPLIER = 20;

const button = document.querySelector(".btn-like");

const moTimeline = new mojs.Timeline();
const moScaleCurve = mojs.easing.path("M0 100H15.5C51 54.5 14.5 7.5 100 0");

const moTween1 = new mojs.Burst({
    parent: button,
    angle: {0: 45},
    y: -10,
    count: 8,
    radius: 130,
    children: {
        shape: "circle",
        radius: 28,
        fill: [COLOR_RED, COLOR_WHITE],
        duration: 60 * DURATION_MULTIPLIER
    }
});

const moTween2 = new mojs.Tween({
    duration: 90 * DURATION_MULTIPLIER,
    onUpdate: (progress) => {
        const moScaleProgress = moScaleCurve(progress);
        button.style.transform = `translate(-50%, -50%) scale3d(${moScaleProgress}, ${moScaleProgress}, 1)`;
    }
});

moTimeline.add(moTween1, moTween2);

button.addEventListener("click", () => {
    if (button.classList.contains("liked")) {
        button.classList.remove("liked");
    } else {
        moTimeline.play();
        button.classList.add("liked");
    }
});

// function submitForm() {
//     document.getElementById('submitFlag').value = 'true';
//     document.getElementById('cityForm').submit();
// }