setTimeout(scrollToContinue, 10);

function scrollToContinue() {
    let scrollDiv = document.querySelector("a.scrollToContinue");
    scrollDiv.style.opacity = 1;
    setTimeout(scrollToContinueBack, 2000);
  }
  
  function scrollToContinueBack() {
    let scrollDiv = document.querySelector("a.scrollToContinue");
    scrollDiv.style.opacity = 0.1;
    setTimeout(scrollToContinue, 2000);
  }

window.addEventListener('scroll', function(event) {
  const navigationBar = document.querySelector('.navbar');
  
  if (window.scrollY > 900) {
    navigationBar.style.backgroundColor = "rgba(0, 0, 0, 0.9)"
  } else {
    navigationBar.style.backgroundColor = "rgba(0, 0, 0, 0)"
    }
  });