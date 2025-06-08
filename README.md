# NurseLink

간호사와 환자를 연결하는 스마트한 케어 서비스입니다.

## 주요 기능

- 8가지 케어 카테고리 제공
  - 진통제 요청
  - 호흡 관리
  - 자세 변경
  - 가습기 치료
  - 물 요청
  - 제증명 서류
  - 회진
  - 수액 교체

- 직관적인 UI/UX
  - 4x2 그리드 레이아웃
  - 카드 디자인
  - 반응형 웹 디자인

## 설치 방법

1. 저장소 클론
```bash
git clone https://github.com/[사용자명]/nurselink.git
cd nurselink
```

2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 의존성 설치
```bash
pip install -r requirements.txt
```

4. 실행
```bash
streamlit run app.py
```

## 기술 스택

- Python
- Streamlit
- HTML/CSS 