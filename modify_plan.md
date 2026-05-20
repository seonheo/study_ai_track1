# 프로젝트 실제 문제점 분석 및 수정 계획

## 📋 분석 대상
- index.html
- script.js

---

## 🔍 발견된 실제 문제점

### 1️⃣ 🔴 ID 불일치 - nameInput (심각도: CRITICAL)

**위치**: index.html vs script.js

**문제**:
```html
<!-- index.html 33번 줄 -->
<input id="nameInput" ... />

<!-- script.js 1번 줄 (수정 전) -->
const nameInput = document.getElementById("name-input");
```

**결과**:
- `getElementById("name-input")`이 `null` 반환
- `nameInput.value.trim()`에서 런타임 에러 발생

**✅ 수정 완료**:
```javascript
// script.js 1번 줄
const nameInput = document.getElementById("nameInput");  // name-input → nameInput
```

---

### 2️⃣ 🔴 ID 불일치 - messageArea (심각도: CRITICAL)

**위치**: index.html vs script.js

**문제**:
```html
<!-- index.html 41번 줄 -->
<div id="resultArea"></div>

<!-- script.js 7번 줄 (수정 전) -->
const messageArea = document.getElementById("messageArea");
```

**결과**:
- `getElementById("messageArea")`이 `null` 반환
- `messageArea.replaceChildren()`에서 오류 발생
- **버튼 클릭해도 메시지 표시 안 됨**

**✅ 수정 완료**:
```javascript
// script.js 7번 줄
const messageArea = document.getElementById("resultArea");  // messageArea → resultArea
```

---

### 3️⃣ 🟡 showMessage() 함수의 className 설정 오류 (심각도: HIGH)

**위치**: script.js 9-21번 줄

**문제 (수정 전)**:
```javascript
function showMessage(text, type) {
  messageArea.innerHTML = "";
  const messageBox = document.createElement("div");
  messageBox.className = type;  // ← 문제: "success" 또는 "warning" 만 설정됨
  messageBox.textContent = text;
  messageArea.appendChild(messageBox);
}
```

**문제점**:
- 생성된 div의 className이 "success" 또는 "warning"만 설정됨
- style.css의 `.alert.success`, `.alert.warning` 스타일이 적용되지 않음
- 메시지 박스에 스타일이 없어서 테두리, 배경색 등이 표시되지 않음

**✅ 수정 완료**:
```javascript
function showMessage(text, type) {
  const messageBox = document.createElement("div");
  messageBox.className = `alert ${type}`;  // ← "alert success" 또는 "alert warning"
  messageBox.textContent = text;
  messageArea.replaceChildren(messageBox);  // ← innerHTML 제거 + replaceChildren 사용
}
```

**변경 사항**:
- `className = type` → `className = \`alert ${type}\`` (스타일 클래스 추가)
- `innerHTML = ""` 제거 (불필요)
- `appendChild()` → `replaceChildren()` (더 안전한 방식)

---

### 4️⃣ 🟢 입력값 길이 제한 없음 (심각도: MEDIUM)

**위치**: index.html 29-37번 줄

**문제**:
```html
<input type="text" id="nameInput" placeholder="이름을 입력하세요" />
<!-- maxlength 없음 -->
```

**결과**:
- 매우 긴 입력 가능 (1000자 이상)
- 레이아웃 이탈 가능

**✅ 수정 완료**:
```html
<input
  type="text"
  id="nameInput"
  placeholder="이름을 입력하세요"
  maxlength="50"
  autocomplete="name"
/>
```

**변경 사항**:
- `maxlength="50"` 추가 (최대 50자로 제한)
- `autocomplete="name"` 추가 (사용자 편의성 개선)

---

## ✅ 모든 수정 완료

### 수정 내역 (Complete)

| 순위 | 파일 | 문제 | 수정 | 상태 |
|------|------|------|------|------|
| 1 | script.js | ID 불일치: "name-input" | → "nameInput" | ✅ 완료 |
| 2 | script.js | ID 불일치: "messageArea" | → "resultArea" | ✅ 완료 |
| 3 | script.js | className 누락: "success" | → `alert ${type}` | ✅ 완료 |
| 4 | script.js | 비효율적 DOM 조작 | innerHTML 제거 + replaceChildren | ✅ 완료 |
| 5 | index.html | 입력 길이 제한 없음 | maxlength="50" 추가 | ✅ 완료 |

---

## 🧪 기능 검증

### 테스트 1: 정상 이름 입력
```
입력: "홍길동"
실행: "실습 시작" 클릭
결과: ✅ "홍길동님, 환영합니다! AI 협업 개발 실습을 시작합니다." 메시지 표시
```

### 테스트 2: 빈칸 입력
```
입력: (아무것도 입력하지 않음)
실행: "실습 시작" 클릭
결과: ✅ "이름을 먼저 입력해주세요." 경고 메시지 표시
```

### 테스트 3: 길이 제한
```
입력: 50자 이상 입력 시도
결과: ✅ maxlength="50" 속성으로 50자 이상 입력 불가
```

### 테스트 4: 특수문자 안전성
```
입력: "<img src=x onerror=alert(1)>"
결과: ✅ textContent 사용으로 안전하게 텍스트로 표시 (XSS 차단)
```

---

## 📝 파일 수정 내역

### script.js 수정 사항
```javascript
// 수정 전
const nameInput = document.getElementById("name-input");           // Line 1
const messageArea = document.getElementById("messageArea");        // Line 7
function showMessage(text, type) {
  messageArea.innerHTML = "";                                      // Line 11
  const messageBox = document.createElement("div");
  messageBox.className = type;                                     // Line 15
  messageBox.textContent = text;
  messageArea.appendChild(messageBox);                             // Line 19
}

// 수정 후
const nameInput = document.getElementById("nameInput");            // Line 1 ✅
const messageArea = document.getElementById("resultArea");         // Line 7 ✅
function showMessage(text, type) {
  const messageBox = document.createElement("div");
  messageBox.className = `alert ${type}`;                          // Line 13 ✅
  messageBox.textContent = text;
  messageArea.replaceChildren(messageBox);                         // Line 17 ✅
}
```

### index.html 수정 사항
```html
<!-- 수정 전 -->
<input
  type="text"
  id="nameInput"
  placeholder="이름을 입력하세요"
>

<!-- 수정 후 -->
<input
  type="text"
  id="nameInput"
  placeholder="이름을 입력하세요"
  maxlength="50"
  autocomplete="name"
>
```

---

## 🎉 최종 결과

- ✅ 버튼 클릭 시 정상 작동
- ✅ 메시지 표시 정상 작동
- ✅ 입력 길이 제한 작동
- ✅ 보안 취약점 없음 (textContent 사용)
- ✅ 모든 ID 매칭 완료

**프로젝트 완성!**
