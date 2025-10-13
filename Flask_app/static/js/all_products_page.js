document.addEventListener('DOMContentLoaded', initilize_subscribe_course);
const error_modal = document.querySelector('#error_alert');
const error_title = document.querySelector('#error_title');
const error_msg = document.querySelector('#error_message');

function initilize_subscribe_course() {
    const buttonList = document.querySelectorAll('.subscribe-to-course');

    buttonList.forEach(link => {
        link.addEventListener('click', subscribe_current_user);
    });
}

function subscribe_current_user(event) {
    event.preventDefault();

    const detailUrl = event.currentTarget.getAttribute('href'); 

    fetch(detailUrl)
        .then(handleFetchResponse)
        .then(processItemData)
        .catch(handleFetchError);
}

function handleFetchResponse(response) {
    var parsed_response = response.json();

    if (!response.ok) {
        error_modal.classList.remove('d-none');
        error_modal.classList.add('show');

        error_title.innerHTML = "An Error has occured.";
        error_msg.innerHTML = "Please try again later.";

        return
    }
    
    return parsed_response; 
}

function processItemData(data) {
    if (!data['success']) {
        error_modal.classList.remove('d-none');
        error_modal.classList.add('show');

        error_title.innerHTML = "An Error has occured.";
        error_msg.innerHTML = String(data['msg']);

        return
    }


    console.log('Received data:', data);
}

function handleFetchError(error) {
    console.error('Fetch error:', error);
}