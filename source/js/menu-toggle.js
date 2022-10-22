const navMain = document.querySelector('.main-nav');
const navToggle = document.querySelector('.main-nav__toggle');

navMain.classList.remove('main-nav--nojs');

navToggle.onclick = () => {
    navMain.classList.toggle('main-nav--opened');
};
