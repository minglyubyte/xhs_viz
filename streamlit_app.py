import streamlit as st

st.set_page_config(
    layout = "wide",
    initial_sidebar_state = "expanded"
)

pg = st.navigation([st.Page("app_pages/map.py", title="小红书推荐可视化", icon=":material/map:", default=True), 
                    st.Page("app_pages/statistics.py", title = "小红书数据可视化", icon=":material/dashboard:")])
pg.run()