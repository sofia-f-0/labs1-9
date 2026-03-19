document.addEventListener('DOMContentLoaded', function() {
    var archive = document.querySelector('.archive');
    if (!archive) return;

    archive.addEventListener('click', function(event) {
        var btn = event.target.closest('.fold-button');
        if (!btn) return;

        var postDiv = btn.closest('.one-post');
        if (!postDiv) return;

        if (btn.innerHTML.trim() === 'Свернуть') {
            postDiv.classList.add('folded');
            btn.innerHTML = 'развернуть';
        } else {
            postDiv.classList.remove('folded');
            btn.innerHTML = 'Свернуть';
        }
    });
});