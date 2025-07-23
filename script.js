
function goBack() {
    document.body.classList.add('exit');
    setTimeout(() => {
        window.location.href = "index.html";
    }, 500);
}
