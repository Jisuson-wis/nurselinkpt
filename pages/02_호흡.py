import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="호흡 관리 요청",
    page_icon="😮‍💨",
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
    
    /* 뒤로가기 버튼 숨기기 */
    .css-fg4pbf, div.css-fg4pbf, button.css-fg4pbf,
    .css-1y4p8pa, div.css-1y4p8pa, button.css-1y4p8pa,
    [data-testid="baseButton-secondary"], 
    .main > div:first-child > div:first-child button,
    div[data-testid="stDecoration"] {
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
    }

    div[data-testid="stButton"] button:hover {
        border-color: #aaa;
        color: #000;
    }
    </style>
""", unsafe_allow_html=True)

# 뒤로가기 버튼 처리
if 'back_button' not in st.session_state:
    st.session_state.back_button = False

col1, col2, col3 = st.columns([1, 3, 1])
with col1:
    if st.button("← 돌아가기"):
        st.switch_page('app.py')

st.title("호흡 관리 요청")

# 산소포화도 (폼 밖으로 이동)
has_oxygen_level = st.checkbox("산소포화도 측정값이 있나요?")

oxygen_value = None
if has_oxygen_level:
    oxygen_value = st.number_input(
        "산소포화도를 입력해주세요",
        min_value=0,
        max_value=100,
        value=95,
        help="모니터에 측정된 산소포화도를 입력해주세요"
    )
    
    # 산소포화도 수준에 따른 알림
    if oxygen_value < 90:
        st.warning("⚠️ 산소포화도가 90% 미만입니다. 의료진의 확인이 필요합니다.")
    elif oxygen_value < 95:
        st.info("ℹ️ 산소포화도가 다소 낮습니다. 호흡 상태를 관찰해주세요.")

# 폼 생성
with st.form("breathing_form"):
    st.write("### 호흡 관리 요청 정보를 입력해주세요")
    
    # 증상 선택
    symptoms = st.multiselect(
        "현재 겪고 계신 증상을 모두 선택해주세요",
        ["호흡 곤란", "기침", "가래", "흉통", "기타"],
        help="해당되는 증상을 모두 선택해주세요"
    )
    
    # 증상 지속 시간
    duration = st.selectbox(
        "증상이 지속된 시간을 선택해주세요",
        ["30분 이내", "1시간 이내", "2~3시간", "반나절 이상", "하루 이상"]
    )
    
    # 추가 설명
    additional_info = st.text_area(
        "추가로 전달할 내용이 있다면 입력해주세요",
        help="예: 평소 호흡기 질환, 현재 복용 중인 약 등"
    )
    
    # 제출 버튼
    submitted = st.form_submit_button("요청하기")
    
    if submitted:
        message = "호흡 관리 요청이 전달되었습니다."
        if has_oxygen_level:
            message += f"\n산소포화도: {oxygen_value}%"
        st.success(message)
        # TODO: 여기에 실제 데이터 처리 로직 추가 