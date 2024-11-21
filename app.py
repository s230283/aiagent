# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model__1_.pkl')

# 2. 모델 설명
st.title('신용 등급 분류 에이전트')
st.subheader('모델 설명')
st.write('- 기계학습 알고리즘: 선형회귀')
st.write('- 학습 데이터 출처: https://www.kaggle.com/datasets/sujithmandala/credit-score-classification-dataset ')
st.write('- 훈련 데이터: 114')
st.write('- 테스트 데이터: 50')
st.write('- 인공지능 모델 정확도: 0.71')
st.write('- 입력된 데이터는 기계 학습을 위해 사용된 후 바로 삭제됩니다.')
st.write(' ')
st.write(' ')
st.write(' ')

# 3. 데이터시각화
col1, col2 = st.columns(2)
with col1:
 st.subheader('데이터 시각화1')
 st.image('시각화1.png')
with col2:
 st.subheader('데이터 시각화2')
 st.image('시각화2.png')
st.write(' ')
st.write(' ')


# 4. 모델 활용
st.subheader('모델활용')
st.write('**** 다음을 입력하세요. 인공지능이 당신의 신용 등급을 알려드립니다!')

a = st.number_input('연소득 입력(달러)', value = 0.0)
b = st.number_input('자녀 수 입력', value = 0)
c = st.selectbox('자택 소유권 유무(없다: 0, 있다: 1)', [0, 1])

if st.button('신용등급판정'):
 input_data = [[a, b, c]]
 p=model.predict(input_data)
 st.write('인공지능한 당신의 신용 등급은(0 ~ 1: 낮음, 1 ~ 2: 평균, 2~: 높음)', p)
 st.write('해당 내용에서는 본인 자택의 소유가 타인에게 있을 경우 빈번하게 발생하는 신용 평가 기관의 월세 기록 누락으로 인해 귀하의 등급보다 낮게 산출될 가능성이 있음을 알립니다.')
