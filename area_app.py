import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc


def run_area_app(df) :

    df = pd.read_csv('data/교통사고정보_2015_2018.csv')
    
    # 항목 종류
    col_name = ['발생년', '발생시간', '주야', '요일', '사망자수', '사상자수', '중상자수', '경상자수',
       '부상신고자수', '도로종류', '노면상태_대분류', '노면상태', '기상상태', 
       '사고유형_대분류', '사고유형_중분류', '사고유형', '가해자_법규위반_대분류', '가해자_법규위반', '도로형태_대분류',
       '도로형태', '가채자_당사종별_대분류', '가해자_당사자종별', '피해자_당사자종별_대분류', '피해자_당사자종별']

    # 지역 종류
    area = ['서울', '부산' ,'경기', '강원', '충북', '충남' ,'전북', '전남' ,'제주', '대구', '인천', '광주' ,'대전', '경북' ,'경남', '울산', '세종']
    
    st.subheader('지역별 교통사고 통계 페이지 입니다.')

    # 여백을 위한 markdown
    st.markdown('')

    # 선택 메뉴
    select_area = st.multiselect('원하시는 지역을 선택해 주세요', area)
    select_col = st.selectbox('원하시는 항목을 선택해 주세요',col_name)

    # 선택한 사항만 묶어서 dataframe으로 만들기
    temp_df = df.groupby(['발생지_시도', select_col])[select_col].count().unstack().loc[select_area,]
    
    # 공백을 0으로 채우기
    temp_df = temp_df.fillna(0)

    if len(select_area) > 0 :    
        # 그래프
        st.set_option('deprecation.showPyplotGlobalUse', False)
        temp_df.plot.bar()
        plt.legend(loc='center left', bbox_to_anchor=(1.04, 0.5))
        plt.show()
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', True)

        # 표
        st.dataframe(temp_df)


    


    
