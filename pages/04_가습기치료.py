import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="가습기 치료 요청",
    page_icon="💨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS 스타일
st.markdown("""
    <style>
    /* 사이드바 숨기기 */
    [data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* 완료 메시지 스타일 */
    .completion-message {
        text-align: center;
        padding: 50px;
        background-color: #f8f9fa;
        border-radius: 10px;
        margin: 50px auto;
        max-width: 600px;
    }

    .completion-icon {
        font-size: 4rem;
        margin-bottom: 20px;
        color: #28a745;
    }
    </style>
""", unsafe_allow_html=True)

# 뒤로가기 버튼
if st.button("← 돌아가기"):
    st.switch_page('app.py')

# 완료 메시지 표시
st.markdown("""
    <div class="completion-message">
        <div class="completion-icon">✅</div>
        <h2>가습기 치료 요청이<br>전달되었습니다</h2>
        <p>곧 간호사가 확인할 예정입니다</p>
    </div>
""", unsafe_allow_html=True) 