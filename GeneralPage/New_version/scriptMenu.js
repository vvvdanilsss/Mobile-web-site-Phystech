menu.onclick = function menuFunction() {
    var x = document.getElementById('myTopnav');
    x.className += " responsive";
    var y = document.getElementById('menu');
    y.className += " responsive";
    var z = document.getElementById('clos');
    z.className += " responsive";
    clos.onclick = function closFunction() {
        var x = document.getElementById('myTopnav');
        x.className = "topnav";
        var y = document.getElementById('menu');
        y.className = "iconMenu";
        var z = document.getElementById('clos');
        z.className = "iconClos";
    }
    document.addEventListener('click', e => {
        const target = e.target;
        if (!target.closest('.head')) {
            var x = document.getElementById('myTopnav');
            x.className = "topnav";
            var y = document.getElementById('menu');
            y.className = "iconMenu";
            var z = document.getElementById('clos');
            z.className = "iconClos";
        }
    })
}

function clickMenu(element, mainElement) {
    var x = document.getElementById(element);
    if (x.className === element) {
        x.className += " click";
    } else {
        x.className = element;
    }
    document.addEventListener('click', e => {
        const target = e.target;
        if (!target.closest(mainElement)) {
            x.className = element;
        }
    })
}

abit.addEventListener('click', function () {
    clickMenu("abitur", '#abit')
})

sotr.addEventListener('click', function () {
    clickMenu("sotrud", '#sotr')
})

quick.addEventListener('click', function () {
    clickMenu("quickl", '#quick')
})

issl.addEventListener('click', function () {
    clickMenu("issled", '#issl')
})

onas.addEventListener('click', function () {
    clickMenu("abitur", '#onas')
})