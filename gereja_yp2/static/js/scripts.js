// === Toggle navbar ===
const navbar = document.querySelector(".navbar");
const navbarNav = document.querySelector(".navbar-nav");
const hamburger = document.querySelector("#hamburger-menu");
const closeMenu = document.querySelector("#close-menu");

hamburger.onclick = (e) => {
  e.preventDefault();
  navbarNav.classList.toggle("active");
  navbar.classList.toggle("active");
};

// === Tutup menu pakai tombol X ===
closeMenu.onclick = (e) => {
  e.preventDefault();
  navbarNav.classList.remove("active");
  navbar.classList.remove("active");
};

// === Tutup navbar jika klik di luar ===
document.addEventListener("click", function (e) {
  if (!navbar.contains(e.target)) {
    navbarNav.classList.remove("active");
    navbar.classList.remove("active");
  }
});

// === Dropdown toggle (mobile) ===
const dropdown = document.querySelector(".dropdown");
const dropdownBtn = document.querySelector(".dropbtn");

if (dropdown && dropdownBtn) {
  dropdownBtn.addEventListener("click", function (e) {
    e.preventDefault();
    if (window.innerWidth <= 768) {
      dropdown.classList.toggle("active");
    }
  });
}

// === Feather Icons refresh ===
feather.replace();
