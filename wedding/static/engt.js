let menu = document.querySelector('#menu-bar');
        let navbar = document.querySelector('.navbar');
        menu.addEventListener('click', () => {
            menu.classList.toggle('fa-times');
            navbar.classList.toggle('nav-toggle');

        });
        window.onscroll = () =>{
            menu.classList.remove('fa-times');
            navbar.classList.remove('nav.toggle');
        }




const formOpenBtn = document.querySelector("#form-open"),
hom = document.querySelector(".hom"),
formContainer = document.querySelector(".form_container"),
formCloseBtn = document.querySelector(".form_close"),
signupBtn = document.querySelector("#signup"),
loginBtn = document.querySelector("#login"),
pwShowHide = document.querySelectorAll(".pw_hide");



formOpenBtn.addEventListener("click",() => hom.classList.add("show"))
formCloseBtn.addEventListener("click",() => hom.classList.remove("show"))
pwShowHide.forEach(icon =>{
    icon.addEventListener("click", () =>{
        let getpwInput = icon.parentElement.querySelector("input");
        if(getpwInput.type === "password"){
            getpwInput.type = "text";
            icon.classList.replace("uil uil-eye-slash" , "uil uil-eye");
        }
        else{
            getpwInput.type = "password";
            icon.classList.replace("uil uil-eye" , "uil uil-eye-slash");

        }
    
    })
});

signupBtn.addEventListener("click", (e) => {
e.preventDefault();
formContainer.classList.add("active");
});
loginBtn.addEventListener("click", (e) => {
    e.preventDefault();
    formContainer.classList.remove("active");
    });