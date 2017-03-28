/**
 * Created by ajdoshi on 28/3/17.
 */
const handleFormSubmit = event => {
    event.preventDefault();

    const data = {};
    const dataContainer = document.getElementsByClassName('results__display')[0];

    dataContainer.textContent = JSON.stringify(data, null, "  ");
};

const form = document.getElementsByClassName('test')[0];
form.addEventListener('submit', handleFormSubmit);