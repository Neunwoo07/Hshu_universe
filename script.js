
document.addEventListener("DOMContentLoaded", () => {
  const backBtn = document.querySelector(".back-button");
  if (backBtn) {
    backBtn.addEventListener("mouseenter", () => {
      backBtn.classList.add("wiggle");
    });
    backBtn.addEventListener("mouseleave", () => {
      backBtn.classList.remove("wiggle");
    });
  }
});
