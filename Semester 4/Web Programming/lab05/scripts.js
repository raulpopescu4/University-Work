
let dropdowns = document.getElementsByClassName("dropdown");
let menu = document.getElementsByClassName("menu");



for (let i = 0; i < dropdowns.length; i++) {
    let dropdown = dropdowns[i];
    let dropdownContent = dropdown.querySelector(".dropdown_content");

    menu.addEventListener("click", function() {
        this.classList.toggle("active");
        dropdown.classList.toggle("show");
    });


    dropdown.addEventListener("click", function() {
        this.classList.toggle("active");
        dropdownContent.classList.toggle("show");
    });



}
