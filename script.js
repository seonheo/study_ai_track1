const nameInput = document.getElementById("nameInput");

const startButton = document.getElementById("startButton");



const messageArea = document.getElementById("resultArea");

function showMessage(text, type) {

  const messageBox = document.createElement("div");

  messageBox.className = `alert ${type}`;

  messageBox.textContent = text;

  messageArea.replaceChildren(messageBox);

}

function handleStartClick() {

  const name = nameInput.value.trim();

  if (name) {

    showMessage(`${name}님, 환영합니다! AI 협업 개발 실습을 시작합니다.`, "success");

  } else {

    showMessage("이름을 먼저 입력해주세요.", "warning");

  }

}



startButton.addEventListener("click", handleStartClick);


