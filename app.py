# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model (1).pkl')

# 2. 모델 설명
st.title('불면증 발병 위험 판독 에이전트')
st.subheader('모델 설명')
st.write(' - 기계학습 알고리즘 : linear_regression ')
st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
st.write(' - 훈련    데이터 : 70,000건')
st.write(' - 테스트 데이터 : 30,000건')
st.write(' - 인공지능 모델 정확도 : 0.08')

# 3. 데이터시각화
col1, col2 = st.columns(2)  
with col1:
      st.subheader('데이터시각화1')
      st.image('시각화1.png' )   # 이미지 불러오기
with col2:
      st.subheader('데이터시각화2')
      st.image('시각화2.png' )   # 이미지 불러오기
# 4. 모델 활용
st.subheader('불면증 발병 위험 판독 에이전트')
st.write('**** 다음을 입력하세요.. 인공지능이 당신의 불면증 위험정도를 알려드립니다! ')

a = st.selectbox('성별을 입력하세요(남자:1, 여자:2', [1,2])
b = st.number_input(' 신장을 입력하세요.', value=0.0 )     # 초기값은 0.0
c = st.number_input(' 몸무게를 입력하세요.', value=0.0 )
                                                            # 사용자가  0,1 중에 선
d = st.selectbox('스트레스 정도를 입력하세요(적음:1, 보통:2,많음3', [1,3])
e = st.selectbox('병원 방문 정도를 입력하세요(적음:1, 보통:2,많음3', [1,3])
f = st.selectbox('외출 정도를 입력하세요(적음:0,많음:1', [0,1])

if st.button('불면증 위험도 예측'):            # 사용자가 '점수예측' 버튼을 누르면
        input_data = [[a,b,c,d,e,f]]     # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model.predict(input_data)         # model이 예측한 값을 p에 저장한다
        st.write('인공지능의 예측 점수는', p)

