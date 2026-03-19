var foldBtns = document.getElementsByClassName("fold-button");

for (var i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function(event) {
        var btn = event.target;
        var postDiv = btn.closest('.one-post');
        if (btn.innerHTML === "Свернуть") {
            postDiv.classList.add('folded');
            btn.innerHTML = "развернуть";
        } else {
            postDiv.classList.remove('folded');
            btn.innerHTML = "Свернуть";
        }
    });
}