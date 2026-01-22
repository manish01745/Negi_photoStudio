document.addEventListener("DOMContentLoaded", function () {
  // this code for nav bar
  var menubar = document.querySelector(".infohamburger");
  var closebar = document.querySelector(".close-btn a");
  var menulist = document.querySelector(".head-mobile-menu-wrapper");
  menubar.addEventListener("click", () => {
    menulist.classList.add("activemenu");
  });
  closebar.addEventListener("click", (e) => {
    e.preventDefault();
    menulist.classList.remove("activemenu");
  });
  // this code for sticky nav bar
  window.addEventListener("scroll", () => {
    const header = document.querySelector(".inner_head");
    if (window.scrollY > header.offsetTop) {
      header.classList.add("sticky");
    } else {
      header.classList.remove("sticky");
    }
  });
  
});
