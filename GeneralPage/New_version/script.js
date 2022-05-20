menu.onclick = function menuFunction() {
    var x = document.getElementById('myTopnav');

    if (x.className === "topnav") {
        x.className += " responsive";
    } else {
        x.className = "topnav";
    }
    outMenu.onclick = function outFunction() {
        var y = document.getElementById('myTopnav');

        if (y.className === "topnav responsive") {
            y.className = "topnav";
        } else {
            y.className = "topnav";
        }
    }
}