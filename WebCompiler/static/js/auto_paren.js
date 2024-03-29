document.addEventListener('keydown', function (event) {
    if (event.key === '{') {
        event.preventDefault();
        var editor = document.activeElement;
        var start = editor.selectionStart;
        var end = editor.selectionEnd;
        var text = editor.value;
        editor.value = text.substring(0, start) + '{\n\n};' + text.substring(end);
        editor.selectionStart = editor.selectionEnd = start + 2;
    }
});

document.addEventListener('keydown', function (event) {
    if (event.key === '(') {
        event.preventDefault();
        var editor = document.activeElement;
        var start = editor.selectionStart;
        var end = editor.selectionEnd;
        var text = editor.value;
        editor.value = text.substring(0, start) + '()' + text.substring(end);
        editor.selectionStart = editor.selectionEnd = start + 1;
    }
});
