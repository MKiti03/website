// $.ajax({
//     type: 'GET',
//     url: '/get-in-touch-ajax/',
//     success: function(response) {
//         console.log('Success', response.text)
//         messageDiv.innerHTML += `
//         <div class="alert alert-success alert-dismissible fade show" role="alert">
//             <strong>${response.text}</strong>
//             <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
//         </div>
//       `
//     },
//     error: function(error) {
//         console.log('Error', error)
//     }
// });

const formField = document.getElementById('getInTouchForm');
formField.addEventListener("submit", formSubmitHandler);


function formSubmitHandler(event) {
    event.preventDefault();
    $.ajax({
        type: 'POST',
        url: '/get-in-touch-ajax/',
        data: $(
            '#formField',
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
        ).serialize(),
        dateType: 'json',
        success: successFunction
    });
}

function successFunction(message) {
    const messageDiv = document.getElementById('formMessage');
    if (message.text === 'success') {
        messageDiv.innerHTML += `
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                <strong>${message.text}</strong>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
       `;
        formField.reset();
    } else {
        messageDiv.innerHTML += `
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
                <strong>An error occurred when sending your form. Please try again letter</strong>
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
       `
    }
}

console.log(window.location.href)