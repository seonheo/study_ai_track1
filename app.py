import streamlit as st


st.set_page_config(
    page_title="AI 협업 개발 실습",
    page_icon="🤝",
    layout="centered",
)

st.title("AI 협업 개발 실습용 첫 번째 Streamlit 앱")
st.caption("Python과 Streamlit으로 빠르게 웹앱을 만드는 기본 예제입니다.")

st.header("간단한 입력")
name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")
role = st.selectbox(
    "실습 역할을 선택하세요",
    ["기획자", "개발자", "디자이너", "테스터"],
)

if name:
    st.success(f"{name}님, {role} 역할로 실습을 시작합니다.")
else:
    st.info("이름을 입력하면 환영 메시지가 표시됩니다.")

st.header("오늘의 실습 체크리스트")
items = {
    "Streamlit 앱 실행하기": st.checkbox("Streamlit 앱 실행하기"),
    "UI 컴포넌트 사용해보기": st.checkbox("UI 컴포넌트 사용해보기"),
    "AI에게 기능 개선 요청하기": st.checkbox("AI에게 기능 개선 요청하기"),
}

completed = sum(items.values())
total = len(items)
st.progress(completed / total)
st.write(f"완료: {completed}/{total}")

st.divider()
st.write("실행 명령어:")
st.code("streamlit run app.py", language="bash")
