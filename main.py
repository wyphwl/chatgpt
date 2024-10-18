import streamlit as st
from utils import generate_script

st.title("🎬视频脚本生成器")
with st.sidebar:
    openai_api_key=st.text_input("请输入OpenAI API密钥：",type="password")
    st.markdown("[获取OpenAI API密钥](https://platform.openai.com/account/api-key)")

subject=st.text_input("请输入视频的主题😊")

video_length=st.number_input("⏱请输入视频的大概时长（单位：分钟）",value=1.0,min_value=0.1,step=0.1)

creavity=st.slider("请输入视频脚本的创造力（数字小说明更严谨，数字大说明更多样）✨",min_value=0.1,max_value=1.5,value=0.5,step=0.1)

submit=st.button("生成脚本")

if submit and not openai_api_key:
    st.info("请输入密钥OpenAI API")
    st.stop()
if submit and not subject:
    st.info("请输入视频主题")
    st.stop()
if submit and not video_length>=0.1:
    st.info("视频长度需要大于等于0.1")
    st.stop()
if submit:
    with st.spinner(("生成中......")):
        search_result,title,script=generate_script(subject,video_length,creavity,openai_api_key)
    st.success("生成完毕！")
    st.subheader("🔥 标题：")
    st.write(title)
    st.subheader("📝 视频脚本：")
    st.write(script)
    with st.expander("维基百科搜索结果❤"):
        st.info(search_result)