document.addEventListener('DOMContentLoaded', function () {
  const $navbarBurger = document.querySelector('.navbar-burger');
  $navbarBurger.addEventListener('click', function () {
    const $target = document.getElementById($navbarBurger.dataset.target);
    // Toggle the class on both the "navbar-burger" and the "navbar-menu"
    $navbarBurger.classList.toggle('is-active');
    $target.classList.toggle('is-active');
  });

  const $deleteIcons = document.querySelectorAll('.delete');
  if ($deleteIcons.length > 0) {
    $deleteIcons.forEach(function ($el) {
      $el.addEventListener('click', () => document.getElementById($el.dataset.target).remove());
    });
  }
});
