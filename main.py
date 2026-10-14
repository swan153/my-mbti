import streamlit as st

# -----------------------------------------------------------------------------
# 1. 페이지 기본 설정 및 디자인 (크림 & 노란색 톤, 큰 글씨)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="MBTI 단짝 포켓몬 찾기",
    page_icon="🐾",
    layout="centered"
)

# 파일 내 포함된 Custom CSS (따뜻한 크림/노란색 톤, 큰 폰트)
st.markdown("""
    <style>
    /* 전체 배경색: 따뜻한 크림톤 */
    .stApp {
        background-color: #FFFDF0;
        font-family: 'Malgun Gothic', 'Noto Sans KR', sans-serif;
    }
    
    /* 카드 컨테이너 */
    .pokemon-card {
        background-color: #FFFFFF;
        border: 3px solid #FFE066;
        border-radius: 20px;
        padding: 25px;
        box-shadow: 0 10px 20px rgba(255, 217, 102, 0.3);
        text-align: center;
        margin-top: 10px;
    }
    
    /* 제목 및 큰 글씨 */
    h1 {
        color: #D97706 !important;
        font-size: 2.3rem !important;
        font-weight: 800 !important;
        text-align: center;
    }
    
    .pokemon-name {
        color: #B45309;
        font-size: 2.2rem;
        font-weight: bold;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    .pokemon-type {
        background-color: #FEF3C7;
        color: #D97706;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    .pokemon-desc {
        color: #4B5563;
        font-size: 1.15rem;
        line-height: 1.6;
        background-color: #FFFBEB;
        padding: 15px;
        border-radius: 12px;
        text-align: left;
        margin-top: 10px;
    }
    
    /* 셀렉트박스 및 버튼 스타일 */
    .stSelectbox label {
        font-size: 1.3rem !important;
        font-weight: bold !important;
        color: #92400E !important;
    }
    
    /* 스트림릿 기본 하단/상단 여백 조정 */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. MBTI별 단짝 포켓몬 데이터 세트 (공식 렌더링 이미지 링크 사용)
# -----------------------------------------------------------------------------
POKEMON_DATA = {
    "INFP": {
        "ko_name": "이브이",
        "en_name": "Eevee",
        "type": "노멀",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "feature": "무한한 가능성을 가지고 있으며 주변 환경과 마음의 변화에 따라 다양한 모습으로 진화합니다.",
        "reason": "풍부한 감성과 무한한 가능성을 가진 INFP처럼, 이브이는 어떤 형태로든 진화할 수 있는
