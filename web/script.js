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