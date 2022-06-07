function open(idElement) {
    var x = document.getElementById(idElement);
    x.className += ' open';
}

function close(idName, className) {
    var x = document.getElementById(idName);
    x.className = className;
}

function openMenu() {
    open('myBurger');
    open('myBottom');
    open('mySite');
}

function closeMenu() {
    close('myBurger', 'up__burger');
    close('myBottom', 'head__bottom');
    close('mySite', 'body__site');
}

myBurger.addEventListener('click', e => {
    var x = document.getElementById('myBurger');
    if (x.className === 'up__burger') {
        openMenu()
    } else {
        closeMenu()
    }
    document.addEventListener('click', e => {
        const target = e.target;
        if (!target.closest('.head')) {
            closeMenu()
        }
    })
})

function clickMenu(element, mainElement) {
    var x = document.getElementById(element);
    if (x.className === element) {
        x.className += ' click';
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

abit.addEventListener('click', e => {
    clickMenu('abitur', '#abit')
})

sotr.addEventListener('click', e => {
    clickMenu('sotrud', '#sotr')
})

quick.addEventListener('click', e => {
    clickMenu('quickl', '#quick')
})

issl.addEventListener('click', e => {
    clickMenu('issled', '#issl')
})

onas.addEventListener('click', e => {
    clickMenu('onewph', '#onas')
})

window.addEventListener('scroll', e => {
    var scroll = document.querySelector('.scrollTop')
    scroll.classList.toggle('active', window.scrollY > 100)
})

function myScrollTop() {
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    })
}