const contactForm = document.getElementById('contact-form');
const fullName = document.getElementById('id_full_name');
const phoneNumber = document.getElementById('id_phone_number');
const emailAdddress = document.getElementById('id_email');
const subject = document.getElementById('id_object');
const message = document.getElementById('id_message');
const csrfToken = document.getElementsByName('csrfmiddlewaretoken');
const messageBox = document.getElementById('message-box');

contactForm.addEventListener('submit', e => {
    e.preventDefault()

    $.ajax({
        type: 'POST',
        url: '/contact-us/',
        data: {
            'csrfmiddlewaretoken': csrfToken[0].value,
            'full_name': fullName.value,
            'phone_number': phoneNumber.value,
            'email': emailAdddress.value,
            'object': subject.value,
            'message': message.value,
        },
        success: function(response) {
            messageBox.innerHTML += `
                <div class="alert alert-success alert-dismissible fade show" role="alert">
                    ${response.message}
                    <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
                </div>
            `
            contactForm.reset()
        },
        error: function(error) {
            messageBox.innerHTML += `
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                And error occured while submiting your form, please try again latter
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `
            console.log(error)
        },
    })
})