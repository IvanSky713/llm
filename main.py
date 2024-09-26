import streamlit as st

from football import team_query,football_predict

def set_state(i):
    st.session_state.stage = i
    if(st.session_state.stage == 1):
        st.session_state.team_options = ['请选择'] + team_query(match_league)
if 'country_options' not in st.session_state:
    st.session_state.country_options = ["英超", "意甲", "西甲"]
if 'stage' not in st.session_state:
    st.session_state.stage = 0
if st.session_state.stage >= 0:
    # 页面开始
    st.header("AI⚽️预测🔥")
    with st.sidebar:
        add_country = st.text_input("添加联赛：")
        btn_country = st.button("添加联赛到下拉列表")
        if btn_country:
            st.session_state.country_options = [add_country] + st.session_state.country_options
        custom_prompt = st.text_area("自定义提示模板，不需要占位符：", on_change=set_state, args=[1])
    match_league = st.selectbox("请选择足球联赛:",
                                st.session_state.country_options)
    st.button('加载⚽️队伍', on_click=set_state, args=[1])
if st.session_state.stage >= 1:
    match_info = st.selectbox("请选择比赛：", st.session_state.team_options)
    submit = st.button("开始预测")
    if submit and custom_prompt:
        with st.spinner("AI按照自定义提示模板回答问题中，请稍后"):
            st.write(football_predict(match_info, custom_prompt))
    if submit and not match_info:
        st.info("请选择比赛")
        st.stop()
    if submit:
        with st.spinner("AI预测中，请稍后"):
            st.write(football_predict(match_info, custom_prompt))