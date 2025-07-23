
document.addEventListener("DOMContentLoaded", () => {
  const sounds = {
    kimsuuk: new Audio("audio/kimsuuk.mp3"),
    ansaehyung: new Audio("audio/ansaehyung.mp3"),
    leejaehyun: new Audio("audio/leejaehyun.mp3"),
    jeonwoocheol: new Audio("audio/jeonwoocheol.mp3"),
    jungwooju: new Audio("audio/jungwooju.mp3")
  };

  document.querySelectorAll(".card").forEach(card => {
    const classes = card.classList;
    for (const name in sounds) {
      if (classes.contains(name)) {
        card.addEventListener("mouseenter", () => {
          sounds[name].currentTime = 0;
          sounds[name].play();
        });
      }
    }
  });
});
