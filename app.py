import streamlit as st
import base64
from PIL import Image
import io

# 페이지 설정
st.set_page_config(
    page_title="NurseLink",
    page_icon="👩‍⚕️",
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
    
    /* 카드 컨테이너 스타일링 */
    .card-container {
        background-color: white;
        border-radius: 8px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        cursor: pointer;
        margin: 10px;
        height: 120px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    
    .card-container:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
    
    /* 아이콘 스타일 */
    .category-icon {
        font-size: 2.5rem;
        margin-bottom: 0.8rem;
    }
    
    /* 제목 스타일 */
    .category-title {
        font-size: 1.1rem;
        font-weight: bold;
        color: #333;
    }
    
    /* 컨테이너 스타일 */
    div.block-container {
        padding: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* 링크 스타일 제거 */
    a {
        text-decoration: none !important;
        color: inherit !important;
    }
    
    /* 헤더 스타일 */
    h1 {
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        font-size: 1.5rem;
        color: #666;
        margin-bottom: 2rem;
    }

    /* 뒤로가기 버튼 숨기기 */
    .css-fg4pbf, div.css-fg4pbf, button.css-fg4pbf,
    .css-1y4p8pa, div.css-1y4p8pa, button.css-1y4p8pa,
    [data-testid="baseButton-secondary"], 
    .main > div:first-child > div:first-child button,
    div[data-testid="stDecoration"] {
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

    /* 버튼 스타일 제거 */
    .stButton button {
        display: none;
    }
    </style>
""", unsafe_allow_html=True)

# 카테고리 정의
categories = [
    {"name": "진통제", "icon": "💊", "url": "진통제", "needs_detail": True},
    {"name": "호흡", "icon": "😮‍💨", "url": "호흡", "needs_detail": True},
    {"name": "자세 변경", "icon": "🔄", "url": "자세_변경", "needs_detail": False},
    {"name": "가습기치료", "icon": "💨", "url": "가습기치료", "needs_detail": False},
    {"name": "물", "icon": "💧", "url": "물", "needs_detail": False},
    {"name": "제증명 서류", "icon": "📄", "url": "제증명_서류", "needs_detail": False},
    {"name": "회진", "icon": "👨‍⚕️", "url": "회진", "needs_detail": False},
    {"name": "수액 교체", "icon": "💉", "url": "수액_교체", "needs_detail": False}
]

# 현재 페이지 상태 관리
if 'page' not in st.session_state:
    st.session_state.page = 'main'
    st.session_state.selected_category = None

def change_page(new_page, category=None):
    st.session_state.page = new_page
    if category:
        st.session_state.selected_category = category
    st.rerun()

# 메인 페이지 표시
def show_main_page():
    st.title("NurseLink")
    st.subheader("간호사에게 나의 요청을 보내요")

    # 설명 섹션
    with st.expander("📌 NurseLink 서비스 안내", expanded=False):
        st.write("---")
        
        col1, col2 = st.columns([1, 4])
        with col1:
            st.image("https://em-content.zobj.net/source/microsoft-teams/363/hospital_1f3e5.png", width=50)
        with col2:
            st.write("#### NurseLink는 환자와 간호사를 연결하는 스마트한 케어 서비스입니다.")
        
        st.write("---")
        st.write("#### 🔍 서비스 이용 방법")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.info("##### 1️⃣ 선택")
            st.write("원하시는 케어 카테고리를 선택해주세요")
        with col2:
            st.success("##### 2️⃣ 작성")
            st.write("요청하실 내용을 자세히 작성해주세요")
        with col3:
            st.warning("##### 3️⃣ 대기")
            st.write("담당 간호사가 최대한 빠르게 응답해드립니다")
            
        st.write("---")
        st.write("#### ⚠️ 주의사항")
        
        with st.container():
            st.error("##### 응급상황")
            st.write("응급상황의 경우 직접 간호사를 호출해주세요")
            
            st.info("##### 정확한 정보")
            st.write("현재 증상을 최대한 정확히 전달해주세요")
            
            st.success("##### 문의사항")
            st.write("문의사항은 언제든 자유롭게 요청해주세요")

    # 카드 컨테이너 생성
    container = st.container()
    with container:
        # 4x2 그리드 생성
        for i in range(0, len(categories), 4):
            cols = st.columns(4)
            for j in range(4):
                if i + j < len(categories):
                    category = categories[i + j]
                    with cols[j]:
                        if category['needs_detail']:
                            # 상세 페이지가 필요한 카테고리
                            st.markdown(f"""
                                <a href="/{category['url']}" target="_self">
                                    <div class="card-container">
                                        <div class="category-icon">{category['icon']}</div>
                                        <div class="category-title">{category['name']}</div>
                                    </div>
                                </a>
                            """, unsafe_allow_html=True)
                        else:
                            # 바로 완료 메시지를 보여줄 카테고리
                            st.markdown(f"""
                                <a href="/{category['url']}" target="_self">
                                    <div class="card-container">
                                        <div class="category-icon">{category['icon']}</div>
                                        <div class="category-title">{category['name']}</div>
                                    </div>
                                </a>
                            """, unsafe_allow_html=True)
                            if st.button("", key=f"{category['url']}_btn"):
                                change_page('completion', category)

# 완료 페이지 표시
def show_completion_page():
    st.markdown("""
        <div class="completion-message">
            <div class="completion-icon">✅</div>
            <h2>요청이 전달되었습니다</h2>
            <p>곧 간호사가 확인할 예정입니다</p>
        </div>
    """, unsafe_allow_html=True)
    
    if st.button("메인 화면으로 돌아가기"):
        change_page('main')

# 페이지 라우팅
if st.session_state.page == 'main':
    show_main_page()
elif st.session_state.page == 'completion':
    show_completion_page()

