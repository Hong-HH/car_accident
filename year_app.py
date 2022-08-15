import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

def run_year_app(df) :
    
    # 선택 가능한 선택지 리스트
    col_name = ['발생지_시도', '발생시간', '주야', '요일', '사망자수', '사상자수', '중상자수', '경상자수',
       '부상신고자수', '도로종류', '노면상태_대분류', '노면상태', '기상상태', 
       '사고유형_대분류', '사고유형_중분류', '사고유형', '가해자_법규위반_대분류', '가해자_법규위반', '도로형태_대분류',
       '도로형태', '가채자_당사종별_대분류', '가해자_당사자종별', '피해자_당사자종별_대분류', '피해자_당사자종별']

    # 선택 가능한 년도
    year = ['2015', '2016', '2017', '2018']
    
    st.subheader('연도별 교통사고 통계 페이지 입니다.')

    # 여백을 위한 markdown
    st.markdown('')

    # 선택지 메뉴
    select_year = st.multiselect('원하시는 년도를 선택해 주세요', year)
    select_col = st.selectbox('원하시는 항목을 선택해 주세요',col_name)
    # 선택된 메뉴는 문자형태이기에 숫자로 변환
    for i in range(len(select_year)) :
        select_year[i] = int(select_year[i])

    # 선택한 사항을 묶어 dataframe 생성
    temp_df = df.groupby(['발생년', select_col])[select_col].count().unstack().loc[select_year,]
    # Nan데이터 0으로 채우기
    temp_df = temp_df.fillna(0)

    if len(select_year) > 0 :    
        # 그래프
        st.set_option('deprecation.showPyplotGlobalUse', False)
        temp_df.plot.bar()
        plt.legend(loc='center left', bbox_to_anchor=(1.04, 0.5))
        plt.show()
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', True)

        # 표        
        st.dataframe(temp_df)
