import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="진통제 요청",
    page_icon="💊",
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
    
    /* 폼 스타일링 */
    .stForm {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    /* 컨테이너 스타일 */
    div.block-container {
        padding: 2rem;
        max-width: 1000px;
        margin: 0 auto;
    }

    /* 돌아가기 버튼 스타일 */
    div[data-testid="stButton"] button {
        background-color: #f0f2f6;
        border: 1px solid #ddd;
        padding: 10px 20px;
        font-size: 16px;
        width: 100%;
        margin: 0;
    }

    div[data-testid="stButton"] button:hover {
        border-color: #aaa;
        color: #000;
    }

    /* 버튼 컨테이너 여백 조정 */
    div.stButton {
        margin: 0 0 1rem 0;
        padding: 0;
    }
    </style>
""", unsafe_allow_html=True)

# 상단 여백 추가
st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)

# 뒤로가기 버튼 처리
if 'back_button' not in st.session_state:
    st.session_state.back_button = False

col1, col2, col3 = st.columns([2, 8, 2])
with col1:
    if st.button("← 돌아가기"):
        st.switch_page('app.py')

st.title("💊진통제 요청")

# 폼 생성
with st.form("pain_medication_form"):
    st.write("### 진통제 요청 정보를 입력해주세요")
    
    # 통증 부위
    pain_location = st.text_input("통증 부위를 입력해주세요", value="", 
                                placeholder="예: 머리, 허리, 다리 등")
    
    # 통증 강도
    pain_level = st.slider("통증 강도를 선택해주세요", 
                          min_value=1, 
                          max_value=10, 
                          value=1,
                          help="1(약한 통증) ~ 10(매우 심한 통증)")
    
    # 통증 느낌
    pain_feeling = st.selectbox("통증 느낌을 선택해주세요", 
                              options=["선택해주세요", "찌르듯이", "날카롭게", "둔하게", "타는듯이", "저린듯이", "누르는듯이", "타는듯한", "기타"],
                              index=0,
                              placeholder="통증 느낌을 선택해주세요")
    
    # 통증 시작 시간
    pain_start = st.time_input("통증이 언제 시작되었는지 선택해주세요")
    
    
    # 추가 설명
    additional_info = st.text_area("추가로 전달할 내용이 있다면 입력해주세요",
                                 value="",  # 빈 값으로 설정
                                 placeholder="예: 진통제 복용 이력, 알레르기 정보 등",
                                 help="예: 기존 복용 중인 약, 알레르기 정보 등")
    
    # 제출 버튼
    submitted = st.form_submit_button("요청하기")
    
    if submitted:
        st.success("진통제 요청이 전달되었습니다. 곧 간호사가 확인할 예정입니다.")
        # TODO: 여기에 실제 데이터 처리 로직 추가 