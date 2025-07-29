
// 랭킹 저장 (로컬 스토리지 기반)
function saveRanking(name, score) {
    const now = new Date();
    const timestamp = now.getTime();
    const data = { name, score, timestamp };
    let rankings = JSON.parse(localStorage.getItem("rankings") || "[]");

    rankings.push(data);
    rankings.sort((a, b) => b.score - a.score);
    if (rankings.length > 10) rankings = rankings.slice(0, 10);
    localStorage.setItem("rankings", JSON.stringify(rankings));
}

// 최근 랭킹 불러오기
function displayRanking() {
    const rankings = JSON.parse(localStorage.getItem("rankings") || "[]");
    const container = document.getElementById("ranking");
    if (!container) return;

    container.innerHTML = "<h2>🌟 오늘의 랭킹 🌟</h2>";
    rankings.forEach((entry, index) => {
        const el = document.createElement("p");
        el.textContent = `${index + 1}등 - ${entry.name}: ${entry.score}점`;
        container.appendChild(el);
    });
}

// 퀴즈 재응시 제한 (2시간)
function checkCooldown() {
    const cooldown = 2 * 60 * 60 * 1000; // 2시간
    const lastAttempt = parseInt(localStorage.getItem("lastAttempt") || "0");
    const now = new Date().getTime();

    if (now - lastAttempt < cooldown) {
        const remaining = cooldown - (now - lastAttempt);
        const minutes = Math.floor(remaining / 60000);
        alert(`아직 ${minutes}분 남았습니다. 퀴즈는 2시간마다 한 번만 응시할 수 있습니다.`);
        return false;
    } else {
        localStorage.setItem("lastAttempt", now.toString());
        return true;
    }
}
