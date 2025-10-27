document.addEventListener('DOMContentLoaded', initilize_subscribe_course);
const error_modal = document.querySelector('#error_alert');
const error_title = document.querySelector('#error_title');
const error_msg = document.querySelector('#error_message');
const notif_modal = document.querySelector('#notification_alert');
const notif_title = document.querySelector('#notification_title');
const notif_msg = document.querySelector('#notification_message');
const def_timeout = 10000;


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
        .then(handleUserSubFecthResponse)
        .then(processUserSub)
        .catch(handleFetchError);
}

function handleUserSubFecthResponse(response) {
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

function processUserSub(data) {
    if (!data['success']) {
        error_modal.classList.remove('d-none');
        error_modal.classList.add('show');

        error_title.innerHTML = "An Error has occured.";
        error_msg.innerHTML = String(data['msg']);

        return
    }

    notif_modal.classList.remove('d-none');
    notif_modal.classList.add('show');

    notif_title.innerHTML = "Success.";
    notif_msg.innerHTML = "Subscribed to course.";

    
    setTimeout(function() {
      const alertInstance = new bootstrap.Alert(notif_modal);

      alertInstance.close(); 
      
    }, def_timeout);

    return
}

function handleFetchError(error) {
    console.error('Fetch error:', error);
}