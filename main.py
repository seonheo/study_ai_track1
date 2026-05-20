import streamlit as st


st.title("First Streamlit App")
st.write("Hello, Streamlit!")
st.caption("간단한 입력과 버튼을 연습하는 Streamlit 예제입니다.")

# 사용자에게 이름을 입력받는 간단한 입력창입니다.
name = st.text_input("이름을 입력하세요")

# 사용자의 역할을 선택하는 기본 선택 상자입니다.
role = st.selectbox(
    "현재 역할을 선택하세요",
    ["학생", "개발자", "기획자"],
)

# 버튼을 누르면 입력한 이름과 선택한 역할을 화면에 보여줍니다.
if st.button("인사 받기"):
    if name:
        st.success(f"안녕하세요, {name}님! 현재 역할은 {role}입니다.")
    else:
        st.warning("이름을 먼저 입력해주세요.")
