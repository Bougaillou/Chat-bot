const logregBox = document.querySelector('.logreg-box');
const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');

registerLink.addEventListener('click',()=>{
    console.log('ibra');
    logregBox.classList.toggle('active');
})
loginLink.addEventListener('click',()=>{
    console.log('ibra');
    logregBox.classList.toggle('active');
})