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
        const target = e.target
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
abit.onclick = function clickAbit() {
    var x = document.getElementById('abitur');
    if (x.className === "abitur") {
        x.className += " click";
    } else {
        x.className = "abitur";
    }
    document.addEventListener('click', e => {
            const target = e.target
            if (!target.closest('#abit')) {
                var x = document.getElementById('abitur');
                x.className = "abitur";
            }
        }
    )
}
sotr.onclick = function clickAbit() {
    var x = document.getElementById('sotrud');
    if (x.className === "sotrud") {
        x.className += " click";
    } else {
        x.className = "sotrud";
    }
    document.addEventListener('click', e => {
            const target = e.target
            if (!target.closest('#sotr')) {
                var x = document.getElementById('sotrud');
                x.className = "sotrud";
            }
        }
    )
}
quick.onclick = function clickAbit() {
    var x = document.getElementById('quickl');
    if (x.className === "quickl") {
        x.className += " click";
    } else {
        x.className = "quickl";
    }
    document.addEventListener('click', e => {
            const target = e.target
            if (!target.closest('#quick')) {
                var x = document.getElementById('quickl');
                x.className = "quickl";
            }
        }
    )
}
issl.onclick = function clickAbit() {
    var x = document.getElementById('issled');
    if (x.className === "issled") {
        x.className += " click";
    } else {
        x.className = "issled";
    }
    document.addEventListener('click', e => {
            const target = e.target
            if (!target.closest('#issl')) {
                var x = document.getElementById('issled');
                x.className = "issled";
            }
        }
    )
}
onas.onclick = function clickAbit() {
    var x = document.getElementById('onewph');
    if (x.className === "onewph") {
        x.className += " click";
    } else {
        x.className = "onewph";
    }
    document.addEventListener('click', e => {
            const target = e.target
            if (!target.closest('#onas')) {
                var x = document.getElementById('onewph');
                x.className = "onewph";
            }
        }
    )
}