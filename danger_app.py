import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc


def run_danger_app(df) :

    df = pd.read_csv('data/교통사고정보_2015_2018.csv')
    
    # 이용자가 이해하기 쉬운 단어로 rename
    df.rename(columns={'발생지_시도' : '지역', '발생시간': '시간', '가해자_법규위반_대분류' :'법규위반_대분류', '가해자_당사자종별' : '차종별'}, inplace=True)

    # 선택 가능한 컬럼 리스트
    col_name = ['지역', '시간', '요일',  
       '사고유형_대분류', '사고유형_중분류', '사고유형', '법규위반_대분류', '가해자_법규위반', 
       '도로형태',  '차종별', '피해자_당사자종별_대분류', '피해자_당사자종별']

    # 메뉴
    select_col = st.sidebar.radio('OOO을 선택해주세요', col_name)
    # 메뉴에 따른 제목 설정
    st.subheader('사고가 가장 많은 {}'.format(select_col))
    
    # 선택한 메뉴로 dataframe 만들고 데이터 정렬하기
    temp_df = df.groupby([select_col])[select_col].count()
    temp_df = temp_df.fillna(0)
    temp_df = temp_df.sort_values(ascending=False)
    
    
    # 그래프
    st.set_option('deprecation.showPyplotGlobalUse', False)
    temp_df.plot.bar()
    
    plt.show()
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', True)


    # 그래프 내용을 글로 보기 좋게 정리해 정렬
    for i in range(len(temp_df.index)) :
        st.write('{}위 : {} - {} 건'.format(i+1, temp_df.index[i], temp_df.values[i]))
