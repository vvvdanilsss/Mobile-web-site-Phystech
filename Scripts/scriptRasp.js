function levelOnClick(element, mainElement, restElement) {
    var x = document.getElementById(element);
    if (x.className === element) {
        x.className += ' on';
    } else {
        x.className = element;
    }
    document.addEventListener('click', e => {
        const target = e.target;
        if (!target.closest(mainElement)
            && !target.closest(restElement)
            && !target.closest('#myHead')) {
            x.className = element;
        }
    })
}

function groupOnClick(element, mainElement) {
    var x = document.getElementById(element);
    if (x.className === element) {
        x.className += ' on';
    } else {
        x.className = element;
    }
    document.addEventListener('click', e => {
        const target = e.target;
        if (!target.closest(mainElement)
            && !target.closest('#myHead')) {
            x.className = element;
        }
    })
}

baka.addEventListener('click', e => {
    levelOnClick('knopki__group__baka',
        '#baka', '#knopki__group__baka')
})

maga.addEventListener('click', e => {
    levelOnClick('knopki__group__maga',
        '#maga', '#knopki__group__maga')
})

z3143.addEventListener('click', e => {
    groupOnClick('pdf__z3143',
        '#z3143')
})

z3144.addEventListener('click', e => {
    groupOnClick('pdf__z3144',
        '#z3144')
})

z3243.addEventListener('click', e => {
    groupOnClick('pdf__z3243',
        '#z3243')
})

z3244.addEventListener('click', e => {
    groupOnClick('pdf__z3244',
        '#z3244')
})

z3343.addEventListener('click', e => {
    groupOnClick('pdf__z3343',
        '#z3343')
})
z41761.addEventListener('click', e => {
    groupOnClick('pdf__z41761',
        '#z41761')
})

z41762.addEventListener('click', e => {
    groupOnClick('pdf__z41762',
        '#z41762')
})

z41772.addEventListener('click', e => {
    groupOnClick('pdf__z41772',
        '#z41772')
})

z41773.addEventListener('click', e => {
    groupOnClick('pdf__z41773',
        '#z41773')
})

z41775.addEventListener('click', e => {
    groupOnClick('pdf__z41775',
        '#z41775')
})
