import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

from area_app import run_area_app
from year_app import run_year_app



def main() :
    st.title('교통사고 통계 (2015-2018)')
    menu = ['홈', '연도별', '지역별']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == '홈' :
        df = pd.read_csv('data/교통사고정보_2015_2018.csv')
        st.dataframe(df.head(10))
        text = "{} 개의 데이터와 {}의 특징으로 이루어져 있습니다.".format(df.shape[0], df.shape[1])
        st.markdown('### 886435 개의 데이터와 28 개의 특징으로 이루어져 있습니다.')
        st.markdown('### 사이드바에서 분석하고 싶은 메뉴를 고르세요')
    
    elif choice == '연도별' :
        run_year_app()

    elif choice == '지역별' :
        run_area_app()




if __name__ == '__main__' :
    main()