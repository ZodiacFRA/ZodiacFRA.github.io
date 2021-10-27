/* Get all slideshow containers */
var slideshowContainers = document.getElementsByClassName("slideshow_container");
/* For each container get starting variables */
for (let s = 0; s < slideshowContainers.length; s++) {
    showSlides(
        slideshowContainers[s].querySelectorAll("img"),
        0,
        slideshowContainers[s].dataset.cycle
    );
};

/* Function is alsmost same, but now it uses 3 new parameters */
function showSlides(slides, slideIndex, cycle) {
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    };
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1
    };
    slides[slideIndex - 1].style.display = "block";
    /* Calling same function, but with new parameters and cycle time */
    setTimeout(function() {
        showSlides(slides, slideIndex, cycle)
    }, cycle);
};
