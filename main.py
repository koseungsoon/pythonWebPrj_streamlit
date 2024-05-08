from io import BytesIO

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
import openpyxl
#print("hi")



folder = 'c:/myPyCode/data/ch09/'
csv_file= folder + 'korea_rain1.csv'

df = pd.read_csv(csv_file, encoding='utf-8')
st.title("표")
st.dataframe(df)

import json
st.html("<hr>")
# 딕셔너리 데이터
dict_data = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "신체정보": {
        "키": 175.4,
        "몸무게": 71.2
    },
    "취미": [
        "등산",
        "자전거타기",
        "독서"
    ]
}

# 딕셔너리 데이터를 JSON 데이터로 변경
json_data = json.dumps(dict_data, indent=3, sort_keys=True, ensure_ascii=False)
st.json(json_data)
st.html("<hr>")
st.metric("온도", "25 °C", delta="1.5 °C")
st.html("<hr>")

#############################################
data1 = [ -2,   5,  -3,  -3,   9,  -4,  -7,  -9,   2,   3]
data2 = [  3,   4,  -4,  -2,  -3,  -2,   0,   7,  -6,   6]
data3 = [-10,   2,   8,   6,  -7,  -1,  -4,  -1,   4,   5]

dict_data = {"data1":data1, "data2":data2, "data3":data3}
df2 = pd.DataFrame(dict_data) # DataFrame

st.title("스트림릿에서 차트 그리기")

st.subheader("꺾은선형 차트: st.line_chart(df) 이용")
st.line_chart(df2, height=170) # 높이 지정

st.subheader("영역형 차트: st.area_chart(df) 이용")
st.area_chart(df2, height=170) # 높이 지정

st.subheader("세로 막대형 차트: st.bar_chart(df) 이용")
st.bar_chart(df2, height=170) # 높이 지정
st.html("<hr>")

import numpy as np

base_lat = 37.55  # 기준 위치 (위도)
base_lon = 126.95  # 기준 위치 (경도)

rand1 = [0.38731831, 0.88186355, 0.73767047, 0.48262488, 0.40470396,
         0.44718457, 0.62209526, 0.00927177, 0.45061387, 0.29512467,
         0.03209323, 0.21555133, 0.18564942, 0.21124898, 0.56080097,
         0.07353603, 0.96114633, 0.43632126, 0.61204948, 0.56378569]

rand2 = [0.33344199, 0.60650414, 0.30760968, 0.15650897, 0.61547323,
         0.4844213, 0.5180108, 0.52112468, 0.38900425, 0.71651658,
         0.75229359, 0.31247536, 0.53251045, 0.37826329, 0.17648217,
         0.57750034, 0.38393327, 0.34383632, 0.31099857, 0.26455346]

pos_lat = base_lat + np.array(rand1) * 0.02
pos_lon = base_lon + np.array(rand2) * 0.02

# 위도(latitude)와 경도(longitude)를 지정한 DataFrame 데이터 생성
pos_data = {"lat": pos_lat, "lon": pos_lon}  # 위도와 경도 데이터를 이용해 딕셔너리 데이터 생성
df_for_map = pd.DataFrame(pos_data)  # DataFrame 데이터의 열 이름은 lat와 lon으로 지정됨

st.title("스트림릿에서 차트 그리기")
st.subheader("지도 좌표(위도, 경도)에 점 그리기: st.map(df) 이용")
st.map(df_for_map, zoom=12)  # zoom에 초기의 지도 크기를 지정

st.html("<hr>")

# matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 꺾은선형 차트 데이터
folder3 = 'C:/myPyCode/data/ch09/'
file3 = folder3 + '공장별_생산현황.csv'
df3 = pd.read_csv(file3, index_col='year')

# 세로 막대형 차트 데이터
file3 = folder3 + '영업팀별_판매현황.xlsx'
df4 = pd.read_excel(file3, index_col='월')

st.title("스트림릿에서 차트 그리기")

# 꺾은선형 차트 그리기
ax = df3.plot(grid=True, figsize=(15,5))
ax.legend(['공장 A', '공장 B', '공장 C'], fontsize=10)
ax.set_title("공장별 생산 현황", fontsize=20) # 그래프 제목을 지정
ax.set_xlabel("연도", fontsize=15)            # x축 라벨을 지정
ax.set_ylabel("생산량", fontsize=15)          # y축 라벨을 지정
fig1 = ax.get_figure()                        # fig 객체 가져오기

st.subheader("꺾은선형 차트: Matplotlib과 st.pyplot(fig) 이용")
st.pyplot(fig1) # 스트림릿 웹 앱에 그래프 그리기

# 세로 막대형 차트 그리기
ax = df4.plot.bar(grid=True, rot=0,  figsize=(15,5))
ax.set_title("영업팀별 판매현황", fontsize=20) # 그래프 제목을 지정
ax.set_xlabel("월", fontsize=15)               # x축 라벨을 지정
ax.set_ylabel("판매현황", fontsize=15)         # y축 라벨을 지정
fig2 = ax.get_figure()                         # fig 객체 가져오기

st.subheader("세로 막대형 차트: Matplotlib과 st.pyplot(fig) 이용")
st.pyplot(fig2) # 스트림릿 웹 앱에 그래프 그리기


st.write("# 스트림릿의 st.write() 함수의 사용 예")

st.write("#### 텍스트 출력")
st.write("일반 텍스트로 출력할 수도 있고, **마크다운**으로 출력할 수도 있습니다. :thumbsup:")

st.write("#### 데이터 출력")
st.write("숫자 데이터 출력:", 1234)

df = pd.DataFrame({
        '1열': [10, 20, 30, 40],
        '2열': [50, 60, 70, 80,]})

st.write("DataFrame 데이터 출력", df)

# matplotlib을 이용한 그래프에 한글을 표시하기 위한 설정
matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False

# 그래프를 위한 데이터 생성
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
df = pd.DataFrame(y, index=x)

# 그래프 그리기
ax = df.plot(grid=True, figsize=(15,4), legend=False)
ax.set_title("sin(x) 그래프", fontsize=20) # 그래프 제목을 지정
ax.set_xlabel("x", fontsize=15)            # x축 라벨을 지정
ax.set_ylabel("y", fontsize=15)            # y축 라벨을 지정
fig = ax.get_figure()                      # fig 객체 가져오기

st.write("#### Matplotlib 차트 출력:", fig)

st.html("<hr>")

st.title("스트림릿의 버튼 입력 사용 예")

clicked = st.button('버튼 1')
st.write('버튼 1 클릭 상태:', clicked)

if clicked:
    st.write('버튼 1을 클릭했습니다.')
else:
    st.write('버튼 1을 클릭하지 않았습니다.')

clicked = st.button('버튼 2')
st.write('버튼 2 클릭 상태:', clicked)

if clicked:
    st.write('버튼 2를 클릭했습니다.')
else:
    st.write('버튼 2를 클릭하지 않았습니다.')

st.html("<hr>")


KTX_data = {'경부선 KTX': [43621, 41702, 41266, 32427],
            '호남선 KTX': [6626, 8675, 10622, 9228],
            '경전선 KTX': [4424, 4606, 4984, 5570],
            '전라선 KTX': [2244, 3146, 3945, 5766]}
col_list = ['경부선 KTX', '호남선 KTX', '경전선 KTX', '전라선 KTX']
index_list = ['2014', '2015', '2016', '2017']

df5 = pd.DataFrame(KTX_data, columns=col_list, index=index_list)

# DataFrame 데이터를 CSV 데이터(csv_data)로 변환
csv_data = df5.to_csv()

# DataFrame 데이터를 엑셀 데이터(excel_data)로 변환
excel_data = BytesIO()  # 메모리 버퍼에 바이너리 객체 생성
df5.to_excel(excel_data)  # DataFrame 데이터를 엑셀 형식으로 버퍼에 쓰기

# 스트림릿 화면 구성
st.title("스트림릿의 다운로드 버튼 사용 예")

st.subheader("DataFrame 데이터")
st.dataframe(df5)

st.subheader("CSV 파일로 다운로드")
st.download_button("CSV 파일 다운로드", csv_data, file_name='KTX_users.csv')

st.subheader("엑셀 파일로 다운로드")
st.download_button("엑셀 파일 다운로드", excel_data, file_name='KTX_users.xlsx')

st.html("<hr>")


st.title("스트림릿의 텍스트 입력 사용 예")

user_id = st.text_input('아이디(ID) 입력', value="streamlit", max_chars=15)
user_password = st.text_input('패스워드(Password) 입력', value="abcd", type="password")

if user_id == "streamlit":
    if user_password == "1234":
        st.write('로그인 됐습니다. 서비스를 이용할 수 있습니다.')
    else:
        st.write('잘못된 패스워드입니다. 다시 입력하세요.')
else:
    st.write('없는 ID 입니다. 회원 가입을 하거나 올바른 ID를 입력하세요.')

st.html("<hr>")

st.title("스트림릿의 숫자 입력 사용 예")

number1 = st.number_input('20 이상의 두 자리 숫자를 입력하세요', min_value=20, max_value=99)
st.write('**입력한 숫자**', number1)

height = st.number_input('키(cm)를 입력하세요', min_value=1.0, value=170.0, step=0.1)
weight = st.number_input('몸무게(kg)를 입력하세요', min_value=1.0, value=65.5)
BMI = weight/((height/100)**2)
st.write('**신체질량지수(BMI):**', BMI )

st.html("<hr>")

import datetime

st.title("스트림릿의 날짜 입력 사용 예")

# 날짜 지정
birthday = st.date_input("1. 당신의 생일은 언제입니까?",
                          value=datetime.date(2000, 1, 1))
st.write("당신의 생일: ", birthday)

# 날짜의 범위 지정
date_range = st.date_input("2. 시작과 끝 날짜를 선택해 주세요",
                           value=[datetime.date(2022, 1, 10), datetime.date(2022, 2, 1)],
                           min_value=datetime.date(2022, 1, 5),
                           max_value=datetime.date(2022, 2, 20))
st.write("당신이 선택한 날짜의 범위: ", date_range)

st.html("<hr>")

st.title("스트림릿의 셀렉트박스 사용 예")

selectbox1_options = ['하이든', '모짜르트', '베토벤', '슈만']
your_option1 = st.selectbox('1. 좋아하는 음악가는?', selectbox1_options)
st.write('**당신의 선택**:', your_option1)

selectbox2_options = ['보티첼리', '램브란트', '피카소', '뭉크']
your_option2 = st.selectbox('2. 좋아하는 화가는?', selectbox2_options)
st.write('**당신의 선택**:', your_option2)

st.html("<hr>")

st.title("스트림릿의 라디오 버튼 사용 예")

radio1_options = ['10', '20', '30', '40']
radio1_selected = st.radio('1. (5 x 5 + 5)은 얼마인가요?', radio1_options)
st.write('**선택한 답**:', radio1_selected)

radio2_options = ['마라톤', '축구', '수영', '승마']
radio2_selected = st.radio('2. 당신이 좋아하는 운동은?', radio2_options, index=2)
st.write('**당신의 선택**:', radio2_selected)

st.html("<hr>")

st.title("스트림릿의 체크박스 사용 예")

checked1 = st.checkbox('체크박스 1')
st.write('체크박스 1 상태:', checked1)

if checked1:
    st.write('체크박스 1을 체크했습니다.')
else:
    st.write('체크박스 1을 체크하지 않았습니다.')

checked2 = st.checkbox('체크 박스 2', value=True)
st.write('체크박스 2 상태:', checked2)

if checked2:
    st.write('체크박스 2를 체크했습니다.')
else:
    st.write('체크박스 2를 체크하지 않았습니다.')
st.html("<hr>")