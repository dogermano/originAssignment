document.querySelector("#submitForm").addEventListener("click", checkForm);

function checkForm() {
    if ((document.querySelector("#age").value == "") || (document.querySelector("#age").value < 0)) {
        event.preventDefault();
        window.alert("Your age must be equal or greater than 0.");
        return;
    }

    if ((document.querySelector("#vehicle").value == "yes") && ((document.querySelector("#year").value == "") || (document.querySelector("#year").value < 0))) {
        event.preventDefault();
        window.alert("Indicate when your vehicle was manufactured.");
        return;
    }
}
