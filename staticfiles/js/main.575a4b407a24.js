
window.onscroll = function () {
    scrollFunction()
    hideDropMenuWhenIsHamburgerMenu()
};


//modify nav when scrolling
function scrollFunction() {
    if (document.documentElement.scrollTop >= 80) {
        document.getElementsByTagName("nav")[0].style.height = "90px";
        document.getElementsByClassName("nav-bar")[0].style.display = "none";
        document.getElementById("hamburger-menu").style.display = "flex";
    } else if (document.documentElement.scrollTop <= 10
                && window.screen.width > 900){
        console.log(window.screen.width)
        document.getElementsByTagName("nav")[0].style.height = "134px";
        document.getElementsByClassName("nav-bar")[0].style.display = "flex";
        document.getElementById("hamburger-menu").style.display = "none";
    }
}

document.getElementById("hamburger-menu").onclick = function() {showDropdownMenu()};
document.getElementsByClassName("close-btn")[0].onclick = function() {showDropdownMenu()};

const dropdownMenu = document.querySelector('#dropdown-menu')
const hamburgerMenu = document.querySelector("#hamburger-menu")
const styleDropdownMenu = getComputedStyle(dropdownMenu)
const styleHamburgerMenu = getComputedStyle(hamburgerMenu)



function showDropdownMenu() {
    if (styleDropdownMenu.getPropertyValue('visibility') === 'visible') {
        document.getElementById("dropdown-menu").style.visibility = 'hidden';
    }
    else if (styleDropdownMenu.getPropertyValue('visibility') === 'hidden'){
        document.getElementById("dropdown-menu").style.visibility = 'visible';
    }
}

function hideDropMenuWhenIsHamburgerMenu(){
     if(styleHamburgerMenu.getPropertyValue('display') === 'none'){
        document.getElementById("dropdown-menu").style.visibility = 'hidden';
    }
}