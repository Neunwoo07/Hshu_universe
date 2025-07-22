window.onload = function() {
  alert("⚠️ 전다은이 급식을 탐지했습니다. 급식판을 보호하세요!");

  // 배경색 깜빡임 효과
  let colors = ['hotpink', 'yellow', 'limegreen', 'cyan'];
  let i = 0;
  setInterval(() => {
    document.body.style.backgroundColor = colors[i % colors.length];
    i++;
  }, 300);

  // 효과음 재생
  const audio = new Audio('assets/enter_sound.mp3');
  audio.play();
};