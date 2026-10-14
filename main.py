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
        padding: 20px;
        box-shadow: 0 8px 16px rgba(255, 217, 102, 0.3);
        text-align: center;
        margin-top: 10px;
        margin-bottom: 20px;
    }
    
    /* 제목 및 큰 글씨 */
    h1 {
        color: #D97706 !important;
        font-size: 2.2rem !important;
        font-weight: 800 !important;
        text-align: center;
    }
    
    .pokemon-name {
        color: #B45309;
        font-size: 2rem;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 5px;
    }
    
    .pokemon-type {
        background-color: #FEF3C7;
        color: #D97706;
        font-size: 1.1rem;
        font-weight: bold;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        margin-bottom: 15px;
    }
    
    .pokemon-desc {
        color: #4B5563;
        font-size: 1.1rem;
        line-height: 1.6;
        background-color: #FFFBEB;
        padding: 15px;
        border-radius: 12px;
        text-align: left;
        margin-top: 15px;
        border: 1px solid #FDE68A;
    }
    
    /* 셀렉트박스 라벨 크기 */
    .stSelectbox label {
        font-size: 1.2rem !important;
        font-weight: bold !important;
        color: #92400E !important;
    }
    
    /* 버튼 스타일 */
    .stButton > button {
        background-color: #F59E0B !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        padding: 10px 20px !important;
    }
    
    .stButton > button:hover {
        background-color: #D97706 !important;
    }

    /* 이미지 중앙 정렬 */
    .img-container {
        display: flex;
        justify-content: center;
        margin: 15px 0;
    }
    .img-container img {
        max-width: 260px;
        width: 100%;
        height: auto;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# 2. MBTI별 단짝 포켓몬 데이터 세트
# -----------------------------------------------------------------------------
POKEMON_DATA = {
    "INFP": {
        "ko_name": "이브이",
        "en_name": "Eevee",
        "type": "노멀",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/133.png",
        "feature": "무한한 가능성을 가지고 있으며 주변 환경과 마음의 변화에 따라 다양한 모습으로 진화합니다.",
        "reason": "풍부한 감성과 무한한 가능성을 가진 INFP처럼, 이브이는 어떤 형태로든 진화할 수 있는 따뜻하고 순수한 마음을 나누기 최고의 단짝입니다."
    },
    "INFJ": {
        "ko_name": "가디안",
        "en_name": "Gardevoir",
        "type": "에스퍼 / 페어리",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/282.png",
        "feature": "트레이너와의 깊은 유대감을 바탕으로 미래를 예지하고 목숨을 걸어 상대를 지켜냅니다.",
        "reason": "타인의 감정을 누구보다 잘 이해하고 깊은 신념을 가진 INFJ와 서로를 깊이 이해하며 끝까지 지켜주는 든든한 조력자가 되어줍니다."
    },
    "INTJ": {
        "ko_name": "뮤츠",
        "en_name": "Mewtwo",
        "type": "에스퍼",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/150.png",
        "feature": "압도적인 지능과 집중력을 지녔으며, 자신만의 가치와 세계관을 독립적으로 탐구합니다.",
        "reason": "독립적이고 전략적인 사고를 즐기는 INTJ처럼 깊은 통찰력을 지녔으며, 쓸데없는 잡음 없이 지적인 교감을 나누기 가장 적합합니다."
    },
    "INTP": {
        "ko_name": "고라파덕",
        "en_name": "Psyduck",
        "type": "물",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/54.png",
        "feature": "항상 생각이 너무 많아 두통을 겪지만, 결정적인 순간에 놀라운 숨겨진 잠재력을 발휘합니다.",
        "reason": "머릿속이 복잡한 호기심과 생각으로 가득 찬 INTP와 닮아있으며, 엉뚱하면서도 결정적일 때 기지를 발휘하는 묘한 매력을 공유합니다."
    },
    "ENFP": {
        "ko_name": "피카츄",
        "en_name": "Pikachu",
        "type": "전기",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png",
        "feature": "언제나 에너지와 호기심이 넘치며 붉은 볼에서 톡톡 튀는 전기를 발산합니다.",
        "reason": "모험을 좋아하고 긍정적인 에너지를 뿜어내는 ENFP와 만나면 매일매일이 신나고 예측할 수 없는 즐거운 스파크로 가득 차게 됩니다."
    },
    "ENFJ": {
        "ko_name": "토게피",
        "en_name": "Togepi",
        "type": "페어리",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/175.png",
        "feature": "주변 사람들의 행복한 마음을 에너지로 삼아 정화하고 행운을 나누어 줍니다.",
        "reason": "주변에 따뜻한 영향력을 넓히고 상대를 성장시키는 ENFJ의 선한 에너지를 누구보다 잘 받아들이고 배로 되돌려주는 귀여운 파트너입니다."
    },
    "ENTJ": {
        "ko_name": "리자몽",
        "en_name": "Charizard",
        "type": "불꽃 / 비행",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/6.png",
        "feature": "강한 상대를 만나면 열정적인 불꽃을 피우며 결코 도망치지 않는 카리스마를 가졌습니다.",
        "reason": "목표를 향해 강력하게 리드하는 ENTJ의 야망과 통찰력에 발맞추어 정상까지 함께 도달할 수 있는 열정적이고 강인한 단짝입니다."
    },
    "ENTP": {
        "ko_name": "팬텀",
        "en_name": "Gengar",
        "type": "고스트 / 독",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/94.png",
        "feature": "장난치기를 극도로 좋아하며 허를찌르는 예측불가한 능력으로 주변을 깜짝 놀라게 합니다.",
        "reason": "창의적인 장난과 센스 있는 재치, 유쾌한 논쟁을 즐기는 ENTP에게 매일 지루할 틈 없는 신선한 자극을 선물해 줍니다."
    },
    "ISTJ": {
        "ko_name": "꼬부기",
        "en_name": "Squirtle",
        "type": "물",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/7.png",
        "feature": "단단한 등껍질로 자신과 동료를 안전하게 보호하며 매우 기본에 충실하고 침착합니다.",
        "reason": "책임감이 강하고 규칙을 중시하는 ISTJ처럼 안정적이고 신뢰할 수 있는 단단함으로 묵묵히 곁을 지켜주는 믿음직한 친구입니다."
    },
    "ISFJ": {
        "ko_name": "이상해씨",
        "en_name": "Bulbasaur",
        "type": "풀 / 독",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/1.png",
        "feature": "등에 있는 씨앗에 양분을 모으며 온순하고 참을성이 깊어 주변을 따뜻하게 돌봅니다.",
        "reason": "배려심 깊고 진중한 ISFJ와 꼭 닮은 포켓몬으로, 서로를 묵묵히 케어해 주며 온화하고 조화로운 일상을 누릴 수 있습니다."
    },
    "ESTJ": {
        "ko_name": "윈디",
        "en_name": "Arcanine",
        "type": "불꽃",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/59.png",
        "feature": "위풍당당한 기품을 가졌으며 규칙을 준수하고 트레이너에게 절대적인 충성심을 보입니다.",
        "reason": "체계적이고 리더십이 뛰어난 ESTJ의 방침을 정확히 이행하며, 함께 거침없이 목표를 향해 달릴 수 있는 충직하고 늠름한 파트너입니다."
    },
    "ESFJ": {
        "ko_name": "푸린",
        "en_name": "Jigglypuff",
        "type": "노멀 / 페어리",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/39.png",
        "feature": "사람들의 관심을 받는 것을 좋아하며 부드러운 자장가로 주변을 편안하게 만들어 줍니다.",
        "reason": "모임의 분위기를 띄우고 타인의 기분을 잘 살피는 ESFJ에게 최고의 관심과 애정을 주고받을 수 있는 애교 만점 단짝입니다."
    },
    "ISTP": {
        "ko_name": "루카리오",
        "en_name": "Lucario",
        "type": "격투 / 강철",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/448.png",
        "feature": "상대의 파동을 감지하는 능력이 있으며, 말없이 실력과 결과로 자신을 증명합니다.",
        "reason": "불필요한 감정 소비 없이 문제 해결과 실전에 강한 ISTP와 깊은 이심전심의 미학을 공유할 수 있는 군더더기 없는 파트너입니다."
    },
    "ISFP": {
        "ko_name": "잠만보",
        "en_name": "Snorlax",
        "type": "노멀",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/143.png",
        "feature": "느긋하고 평화로운 성격으로 먹고 자는 유유자적한 삶을 최고의 행복으로 여깁니다.",
        "reason": "평화주의자이자 현재의 여유를 즐길 줄 아는 ISFP에게 아무런 스트레스 없이 따뜻하고 푹신한 휴식을 선사하는 완벽한 힐링 친구입니다."
    },
    "ESTP": {
        "ko_name": "번치코",
        "en_name": "Blaziken",
        "type": "불꽃 / 격투",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/257.png",
        "feature": "강인한 하체로 건물을 뛰어넘으며 역동적이고 신속한 액션에 최적화되어 있습니다.",
        "reason": "스릴과 도전을 두려워하지 않고 순발력이 뛰어난 ESTP와 함께 현장의 열기를 즐기며 액티브하게 움직일 수 있는 최강의 스포티 파트너입니다."
    },
    "ESFP": {
        "ko_name": "파모",
        "en_name": "Pawmi",
        "type": "전기",
        "img": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/921.png",
        "feature": "손바닥의 방전 기관으로 마음을 표현하며 친근하고 발랄한 애교가 넘칩니다.",
        "reason": "사랑스러움과 흥이 넘치는 ESFP의 에너지에 발맞추어 함께 분위기를 밝게 만들고 주변을 행복하게 만드는 인간 비타민 조합입니다."
    }
}

# -----------------------------------------------------------------------------
# 3. 화면 레이아웃 및 로직
# -----------------------------------------------------------------------------
st.title("✨ MBTI 단짝 포켓몬 찾기 ✨")
st.write("")

st.markdown("<p style='text-align: center; font-size: 1.25rem; color: #78350F; font-weight: bold;'>나의 MBTI를 선택하면 어울리는 포켓몬 친구를 소개해 드려요!</p>", unsafe_allow_html=True)

mbti_list = list(POKEMON_DATA.keys())
selected_mbti = st.selectbox("당신의 MBTI를 선택해 주세요:", mbti_list)

if st.button("💛 단짝 포켓몬 확인하기 💛", use_container_width=True):
    # 축하 폭죽 효과
    st.balloons()
    
    data = POKEMON_DATA[selected_mbti]
    
    # 결과 카드 출력
    st.markdown(f"""
        <div class="pokemon-card">
            <div class="pokemon-name">{data['ko_name']} <span style="font-size: 1.3rem; color: #6B7280;">({data['en_name']})</span></div>
            <div class="pokemon-type">타입: {data['type']}</div>
            <div class="img-container">
                <img src="{data['img']}" alt="{data['ko_name']}">
            </div>
            <div class="pokemon-desc">
                <b>📌 포켓몬 특징:</b><br>
                {data['feature']}<br><br>
                <b>🤝 {selected_mbti}와 어울리는 이유:</b><br>
                {data['reason']}
            </div>
        </div>
    """, unsafe_allow_html=True)

st.write("---")
st.caption("💛 배포 팁: GitHub에 올릴 때 `requirements.txt` 파일에 `streamlit` 하나만 적어서 함께 올려주시면 됩니다.")
