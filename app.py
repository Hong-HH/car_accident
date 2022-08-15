import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc

from area_app import run_area_app
from danger_app import run_danger_app
from year_app import run_year_app



def main() :
    # 한글 폰트 설정 
    font_path = "/usr/share/fonts/nanumfont/NanumGothic.ttf"
    font = font_manager.FontProperties(fname=font_path).get_name()
    print(font)

    # rc('font', family=font)




    st.title('교통사고 통계 (2015-2018)')
    menu = ['홈', '연도별 비교', '지역별 비교',  '사고가 가장 많은 OOO']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == '홈' :
        df = pd.read_csv('data/교통사고정보_2015_2018.csv')
        st.markdown('### 총 886435 개의 데이터와 28 개의 특징으로 이루어져 있습니다. 사이드바에서 분석하고 싶은 메뉴를 고르세요')

        eda_df = df[['발생년', '사망자수', '사상자수','중상자수' ,'경상자수', '부상신고자수' ]]

        # 글꼴 바꾸기 테스트
        eda_df.style.set_properties(**{'font-family': font})
     
        st.subheader('컬럼별 히스토그램')

        st.set_option('deprecation.showPyplotGlobalUse', False)
        eda_df.hist(figsize=(10,8))
        plt.show()
        st.pyplot()
        st.set_option('deprecation.showPyplotGlobalUse', True )

        # describe
        st.subheader('컬럼별 통계치')
        st.dataframe(eda_df.describe())
        st.subheader('가장 피해가 컸던 사고의 데이터')
        max_menu = ['사망자수', '사상자수','중상자수' ,'경상자수', '부상신고자수' ]
        select_max = st.selectbox('컬럼을 선택해주세요', max_menu)
        max_data = df.loc[df[select_max]==df[select_max].max() , ]
        st.dataframe(max_data)

        max_day = max_data['발생일'].values[0]
        max_day = str(max_day)
        print(max_day)
        print(max_day[0:4], max_day[4:6], max_day[6:], max_data['요일'].values[0])
        st.text('사고 발생일 : {}년 {}월 {}일 {}요일'.format(max_day[0:4], max_day[4:6], max_day[6:], max_data['요일'].values[0]))
        st.text('사망자수 : {}, 사상자수 : {}, 중상자수 : {}, 경상자수 : {} 의 피해가 있었습니다.'.format(max_data['사망자수'].values[0], max_data['사상자수'].values[0], max_data['중상자수'].values[0], max_data['경상자수'].values[0]))

        


    
    elif choice == '연도별 비교' :
        run_year_app()
    elif choice == '지역별 비교' :
        run_area_app()
    elif choice == '사고가 가장 많은 OOO' :
        run_danger_app()




if __name__ == '__main__' :
    main()