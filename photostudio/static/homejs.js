document.addEventListener('DOMContentLoaded', () => {

  let slideIndex = 0;
  showSlides();
  
  // Next-previous control
  function nextSlide() {
    slideIndex++;
    showSlides();
    timer = _timer; // reset timer
  }
  
  function prevSlide() {
    slideIndex--;
    showSlides();
    timer = _timer;
  }
  
  // Thumbnail image controlls
  function currentSlide(n) {
    slideIndex = n - 1;
    showSlides();
    timer = _timer;
  }
  
  function showSlides() {
    let slides = document.querySelectorAll(".mySlides");
    let dots = document.querySelectorAll(".dots");
  
    if (slideIndex > slides.length - 1) slideIndex = 0;
    if (slideIndex < 0) slideIndex = slides.length - 1;
    
    // hide all slides
    slides.forEach((slide) => {
      slide.style.display = "none";
    });
    
    // show one slide base on index number
    slides[slideIndex].style.display = "block";
    
    dots.forEach((dot) => {
      dot.classList.remove("active");
    });
    
    dots[slideIndex].classList.add("active");
  }
  
  // autoplay slides --------
  let timer = 7; // sec
  const _timer = timer;
  
  // this function runs every 1 second
  setInterval(() => {
    timer--;
  
    if (timer < 1) {
      nextSlide();
      timer = _timer; // reset timer
    }
  }, 1000); // 1sec


  const testimonials = [
      {
          img: "https://firstsight.design/amie/onepage/wp-content/uploads/2021/05/Mask-Group-1-2.jpg",
          logo: "Coaching Client",
          text: "My family and my husband's family are not easy people to please, and they were floored by the beautiful images that were delivered to us so great to do. Alisa Hester is a magical creature. She is not only one of the nicest, most calm photographers I've ever worked with, but her work is, hands down, stunning."
      },
      {
          img: "https://firstsight.design/amie/onepage/wp-content/uploads/2021/05/Mask-Group-1-12.jpg",
          logo: "Andrew & Alina",
          text: "Alisa Hester is a magical creature. She is not only one of the nicest, most calm photographers I've ever worked with, but her work is, hands down, stunning. My family and my husband's family are not easy people to please, and they were floored by the beautiful images that were delivered to us so great to do."
      },
      {
          img: "https://firstsight.design/amie/onepage/wp-content/uploads/2021/06/Engagement-main.jpg",
          logo: "Manish",
          text: "My family and my husband's family are not easy people to please, and they were floored by the beautiful images that were delivered to us so great to do. Alisa Hester is a magical creature. She is not only one of the nicest, most calm photographers I've ever worked with, but her work is, hands down, stunning."
      }
  ];

  var button_previous = document.querySelector(".testi-icon-first");
  let button_next = document.querySelector(".testi-icon-second");
  let testimonialname = document.querySelector(".art-testimonial-name");
  let testimonialText = document.querySelector(".art-testimonial-data");
  let testimonialimg = document.querySelector(".swiper-slide img");
  let count = 0;

  // Initial display of testimonial
  testimonial_add();

  button_next.addEventListener("click", function () {
      count++;
      if (count > testimonials.length - 1) {
          count = 0; // Reset to the first testimonial
      }
      testimonial_add();
  });

  button_previous.addEventListener("click", function () {
      count--;
      if (count < 0) {
          count = testimonials.length - 1; // Set to the last testimonial
      }
      testimonial_add();
  });

  function testimonial_add() {
    testimonialname.innerHTML = testimonials[count].logo;
    console.log("Image source:", testimonials[count].logo);
    testimonialText.innerHTML = testimonials[count].text;
    console.log("Image source:", testimonials[count].text);
    testimonialimg.src = testimonials[count].img; // Set image source
    console.log("Image source:", testimonials[count].img);
  }
});
