import streamlit as st
import pandas as pd
from datetime import datetime

# Streamlit 페이지 설정
st.set_page_config(page_title="마린이 - 2024 마라톤 대회 정보 및 기록 관리", layout="wide")

# 스타일 정의
st.markdown("""
    <style>
    body {
      font-family: 'Noto Sans KR', sans-serif;
      line-height: 1.6;
      color: #333;
      background-color: #f0f8ff;
    }
    .container {
      max-width: 1200px;
      margin: 0 auto;
      padding: 20px;
    }
    header {
      text-align: center;
      background-color: #4169e1;
      color: white;
      padding: 20px;
      border-radius: 10px;
      margin-bottom: 20px;
    }
    h1 {
      margin: 0;
      font-size: 2.5em;
    }
    .record-form {
      background-color: #fff;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      margin-bottom: 20px;
    }
    .row {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
    }
    .col-md-6 {
      flex: 1;
      min-width: 300px;
    }
    .mb-3 {
      margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# HTML 구조
st.markdown("""
<div class="container">
  <header>
    <h1>마린이</h1>
    <p>2024 마라톤 대회 정보 및 기록 관리</p>
  </header>

  <div class="row">
    <div class="col-md-6">
      <h2>2024년 마라톤 대회 일정</h2>
      <div id="marathonTable">
        <!-- DataFrame으로 채워질 예정 -->
      </div>
    </div>
    <div class="col-md-6">
      <h2>다음달 마라톤 일정</h2>
      <!-- 일정 생성 로직 -->
    </div>
  </div>

  <div class="row mt-4">
    <div class="col-md-6">
      <h2>참가 희망자 명단</h2>
      <div id="participantTable">
        <!-- DataFrame으로 채워질 예정 -->
      </div>
      <form id="participantForm">
        <div class="mb-3">
          <input type="text" class="form-control" id="name" placeholder="이름">
        </div>
        <div class="mb-3">
          <input type="text" class="form-control" id="event" placeholder="대회명">
        </div>
        <div class="mb-3">
          <input type="date" class="form-control" id="date">
        </div>
        <button type="submit" class="btn btn-primary">등록</button>
      </form>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# 데이터 예시
marathon_data = {
    '날짜': ['2024-01-01', '2024-02-01'],
    '대회명': ['New Year Marathon', 'Winter Run'],
    '장소': ['Seoul', 'Busan'],
    '거리': ['10km', '5km']
}
df_marathon = pd.DataFrame(marathon_data)

participant_data = {
    '이름': ['홍길동', '김철수'],
    '대회명': ['New Year Marathon', 'Winter Run'],
    '날짜': ['2024-01-01', '2024-02-01']
}
df_participant = pd.DataFrame(participant_data)

# DataFrame을 Streamlit 테이블로 표시
st.subheader("2024년 마라톤 대회 일정")
st.dataframe(df_marathon, use_container_width=True)

st.subheader("참가 희망자 명단")
st.dataframe(df_participant, use_container_width=True)

# 참가 희망자 등록 폼
with st.form(key='participant_form'):
    st.subheader("참가 희망자 등록")
    name = st.text_input("이름")
    event = st.text_input("대회명")
    date = st.date_input("날짜", value=datetime.today())
    submit_button = st.form_submit_button(label="등록")

    if submit_button:
        new_participant = pd.DataFrame({
            '이름': [name],
            '대회명': [event],
            '날짜': [date.strftime('%Y-%m-%d')]
        })
        df_participant = pd.concat([df_participant, new_participant], ignore_index=True)
        st.success(f"{name}님이 {event} 대회에 등록되었습니다.")
        st.dataframe(df_participant, use_container_width=True)
