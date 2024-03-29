document.addEventListener('DOMContentLoaded', (event) => {
    const clearButton = document.getElementById('clearButton');
    const codeInput = document.getElementById('code');

    clearButton.addEventListener('click', function () {
        codeInput.value = '';
    });
});
