document.addEventListener('DOMContentLoaded', initilize_subscribe_course);

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
    if (!response.ok) {
        throw new Error('Request to server unsuccessful: ' + response.statusText);
    }
    return response.json(); 
}

function processItemData(data) {
    console.log('Received data:', data);
}

function handleFetchError(error) {
    console.error('Fetch error:', error);
}