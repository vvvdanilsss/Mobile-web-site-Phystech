let result = [0, 0, 0];

function marker(text) {
    let level = ["Бакалавриат", "Магистратура"],
        group = ["V3103", "V3203", "V3303", "V3403"],
        day = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"],
        x = document.getElementById('cl2'),
        y = document.getElementById('cl3');
    if (level.includes(text)) {
        result[0] = text;
    } else if (group.includes(text)) {
        result[1] = text;
    } else if (day.includes(text)) {
        result[2] = text;
    }
    if (result[1] === 0) {
        x.className += " on";
    } else if (result[2] === 0) {
        y.className += " on";
    } else if (result[2] !== 0) {
        alert("Вы нажали такую комбинацию кнопок: " + result.join('→'));
        result = [0, 0, 0];
        x.className = "click2";
        y.className = "click3";
    }
}

baka.addEventListener('click', function () {
    marker("Бакалавриат");
});
maga.addEventListener('click', function () {
    marker("Магистратура");
});

v31.addEventListener('click', function () {
    marker("V3103");
});
v32.addEventListener('click', function () {
    marker("V3203");
});
v33.addEventListener('click', function () {
    marker("V3303");
});
v34.addEventListener('click', function () {
    marker("V3403");
});

pn.addEventListener('click', function () {
    marker("Понедельник");
});
vt.addEventListener('click', function () {
    marker("Вторник");
});
sr.addEventListener('click', function () {
    marker("Среда");
});
cht.addEventListener('click', function () {
    marker("Четверг");
});
pt.addEventListener('click', function () {
    marker("Пятница");
});
sb.addEventListener('click', function () {
    marker("Суббота");
});