document.addEventListener('DOMContentLoaded', function () {
  let $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0),
    $deleteIcons = Array.prototype.slice.call(document.querySelectorAll('.delete'), 0);

  if ($navbarBurgers.length > 0) {
    $navbarBurgers.forEach(function ($el) {
      $el.addEventListener('click', function () {
        let $target = document.getElementById($el.dataset.target);
        // Toggle the class on both the "navbar-burger" and the "navbar-menu"
        $el.classList.toggle('is-active');
        $target.classList.toggle('is-active');
      });
    });
  }

  if ($deleteIcons.length > 0) {
    $deleteIcons.forEach(function ($el) {
      $el.addEventListener('click', function () {
        let $target = document.getElementById($el.dataset.target);
        $target.remove();
      });
    });
  }

  // Initialize syntax highlighting
  hljs.initHighlightingOnLoad();
});
