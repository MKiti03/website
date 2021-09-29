const getForm = document.getElementById('get-in-touch');
const firstName = document.getElementById('first_name');
const lastName = document.getElementById('last_name');
const getEmailAddress = document.getElementById('get_email');
const getphoneNumber = document.getElementById('get_phone');
const nationality = document.getElementById('nationality');
const countryOfResident = document.getElementById('country_of_resident');
const graduationYear = document.getElementById('graduation_year');
const programCategory = document.getElementById('category');
const programName = document.getElementById('program_name');
const educationalQualification = document.getElementById('educational_qualification');
const csrftoken = document.getElementsByName('csrfmiddlewaretoken')

function getProgram() {
    var selectedValue = programCategory.options[programCategory.selectedIndex].value;

    $.ajax({
        type: 'POST',
        url: '/get-in-touch/get-program-ajax/',
        data: {
            'program': selectedValue,
        },

        success: function(response) {
            console.log(response.text)
        },

        error: function(error) {
            console.log(error)
        }
    })

}