let sections= document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header ul a');

window.onscroll = ()=>{
    sections.forEach(sec =>{
        let top = window.scrollY;
        let offset = sec.offsetTop -150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');
        if(top >= offset && top < offset + height){
            navLinks.forEach(links =>{
                links.classList.remove('active');
                document.querySelector('header ul a[href*='+ id +']').classList.add('active');
            });
        };
    });
};


ScrollReveal({
    // reset: true,
    distance:'80px',
    duration: 1750,
    delay:100
});

ScrollReveal().reveal('.home-content, .heading', {origin:'top'});
ScrollReveal().reveal('.home-img , .service-container, .project-box, .contact form', {origin:'bottom'});
ScrollReveal().reveal('.home-content h1, .about-img', {origin:'left'});
ScrollReveal().reveal('.home-content p, .about-content', {origin:'right'});

const typed = new Typed('.multiple-text',{
    strings : ['Bot', 'Doctor', 'Machine'],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop:true
});

const p1 = document.querySelector('#p-service1');
const words1 = p1.textContent;
const firstTenWords1 = words1.slice(0, 130)+"....";
p1.innerHTML=firstTenWords1;
const p2 = document.querySelector('#p-service2');
const words2 = p2.textContent;
const firstTenWords2 = words2.slice(0, 130)+"....";
p2.innerHTML=firstTenWords2;
const p3 = document.querySelector('#p-service3');
const words3 = p3.textContent;
const firstTenWords3 = words3.slice(0, 130)+"....";
p3.innerHTML=firstTenWords3;