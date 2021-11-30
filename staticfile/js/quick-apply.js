const diciplineBox = document.getElementById('dicipline-box')
const levelBox = document.getElementById('level-box')
const specialtyBox = document.getElementById('specialty-box')
const programBox = document.getElementById('program-box')
const countryBox = document.getElementById('country-box')
const universityBox = document.getElementById('university-box')
const dicipline = document.getElementById('dicipline')
const level = document.getElementById('level')
const specialty = document.getElementById('specialty')
const program = document.getElementById('program')
const country = document.getElementById('country')
const csrfTokenmiddleware = document.getElementsByName('csrfmiddlewaretoken');
const resetBtn = document.getElementById('reset-btn')
const quickApplyForm = document.getElementById('quick-apply')
const url = window.location.href
const formBox = document.getElementById('form-box')


level.onchange = function() {
    resetBtn.classList.remove('visually-hidden')
    const diciplineValue = dicipline.value;
    const levelValue = level.value;
    levelBox.innerHTML = `
        <h6 class="">
            Level:  <br><span class = "fw-600 text-dark">${levelValue}</span>
        </h6>
    `;
    if (diciplineValue != 0) {
        getDiciplineLEvel()
    }
}

function getDiciplineLEvel() {
    const diciplineValue = dicipline.value;
    const levelValue = level.value;
    diciplineBox.innerHTML = `
        <h6 class="">
            Dicipline:  <br><span class = "fw-600 text-dark">${diciplineValue}</span>
        </h6>
    `;
    $.ajax({
        type: 'POST',
        url: '/get-in-touch/get-dicipline/',
        data: {
            'csrfmiddlewaretoken': csrfTokenmiddleware,
            'level': levelValue,
            'dicipline': diciplineValue,
        },
        success: function(response) {
            console.log(response.get_specialty)
        },
        error: function(error) {
            console.log(error)
        },
    })
}


specialty.onchange = function() {
    const specialtyValue = specialty.value;
    specialtyBox.innerHTML = `
        <h6 class="">
            Specialty:  <br><span class = "fw-600 text-dark">${specialtyValue}</span>
        </h6>
    `;

    $.ajax({
        type: 'POST',
        url: '/get-in-touch/get-specialty/',
        data: {
            'specialty': specialtyValue,
        },
        success: function(response) {
            console.log(response.program_name)
        },
        error: function(error) {
            console.log(error)
        },
    })
}

program.onchange = function() {
    const programValue = program.value;
    programBox.innerHTML = `
        <h6 class="">
            Program:  <br><span class = "fw-600 text-dark">${programValue}</span>
        </h6>
    `;

    $.ajax({
        type: 'POST',
        url: url,
        data: {
            'program': programValue,
        },
        success: function(response) {
            console.log(response.university_name)
        },
        error: function(error) {
            console.log(error)
        },
    })
}

country.onchange = function() {
    const countryValue = country.value;
    countryBox.innerHTML = `
        <h6 class="">
            Country:  <br><span class = "fw-600 text-dark">${countryValue}</span>
        </h6>
    `;

    // $.ajax({
    //     type: 'POST',
    //     url: url,
    //     data: {
    //         'csrfmiddlewaretoken': csrfToken[0].value,
    //         'full_name': fullName.value,
    //     },
    //     success: function(response) {
    //         infoBox.innerHTML += `
    //             <h6 class="">
    //               You have selected:  ${diciplineValue}
    //             </h6>
    //         `
    //     },
    //     error: function(error) {
    //         console.log(error)
    //     },
    // })
}

function getUniversity() {
    universityBox.classList.add('visually-hidden')
    formBox.classList.remove('visually-hidden')
}

function resetForm() {
    quickApplyForm.reset()
}

// quickApplyForm.addEventListener('submit', e => {
//     e.preventDefault()
//     console.log('Test submit apply')
// })