document.addEventListener("DOMContentLoaded", ready);

function ready(){
    const form = document.getElementById('form');
    console.log(form);

form.addEventListener('submit', (e) => {
    e.preventDefault();

    check();
});
}

function check() {
    const email = document.getElementById("e-mail");
    console.log(email);
    const username = document.getElementById("username");
    console.log(username);
    const password = document.getElementById("password");
    console.log(password);
    const repeat_password = document.getElementById("repeat-password");
    console.log(repeat_password);
    if (!email.value || !email.value.includes("@") || email.value.length < 11) {
        setError(email, "Invalid E-mail");
        // alert("Поле e-mail заполнено некорректно.\n Требуемые параметры: длина не должна быть меньше 11 символов;" +
        //     " обязательно должен содержаться знак @!");
        // email.style.border = "2px solid red";
        // return false;
    }
    else{
        setSuccess(email);
    }

    if (!username.value || username.value.length < 5 || /[0-9]/.test(username.value)) {
        setError(username, "The username mustn't contain numbers and must be at least 5 characters long!");
        // alert("Имя пользователя заполнено некорректно. Минимально допустимая длина составляет 8 символов");
        // username.style.border = "2px solid red!";
        // return false;
    }
    else{
        setSuccess(username);
    }

    if (!password.value || password.value.length < 8 || !/[0-9]/.test(password.value)) {
        setError(password, "Password must contain numbers and be at least 8 characters long!");
        // alert("Пароль заполнен некорректно.\nТребуемые параметры: длина не должна быть меньше 8 символов;" +
        //     " обязательно должна содержаться хотя бы одна цифра!");
        // password.style.border = "2px solid red";
        // return false;
    }
    else{
        setSuccess(password);
    }

    if (!password.value || repeat_password.value !== password.value){
        setError(repeat_password, "Passwords do not match!")
        // alert("Пароли не совпадают!");
        // password.style.border = "2px solid red";
        // repeat_password.style.border = "2px solid red";
        // return false;
    }
    else{
        setSuccess(repeat_password);
    }

    // return true;
}
function setError(field, message){
    const formControl = field.parentElement;
    const small = formControl.querySelector('small');

    small.innerText = message;
    formControl.className = 'form-control error';
}

function setSuccess(field){
    const formControl = field.parentElement;
    formControl.className = 'form-control success';
}

