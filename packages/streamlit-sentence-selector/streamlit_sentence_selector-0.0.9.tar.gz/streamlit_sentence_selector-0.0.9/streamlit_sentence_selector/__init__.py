import os
import streamlit.components.v1 as components

_RELEASE = True

if not _RELEASE:
    _component_func = components.declare_component(
        "streamlit_sentence_selector",
        url="http://localhost:3001",
    )
else:
    parent_dir = os.path.dirname (os.path.abspath (__file__))
    build_dir = os.path.join (parent_dir, "frontend/build")
    sentence_selector_ = components.declare_component ("streamlit_sentence_selector", path = build_dir)


def sentence_selector(sentences,key=None):

    component_value = sentence_selector_(sentences=sentences,key=key,default=False)

    return component_value


if not _RELEASE:
    import streamlit as st

    st.subheader("Component with variable args")

    name_input = st.text_input("Enter a name", value="Streamlit")
    greeting_input=st.text_input("greeting",value="greeting")
    for i in range(2):
        num_clicks = sentence_selector(sentences="你在干嘛 哈哈 我今天很好 今天是520 你吃饭喇嘛？？ sdfasdfasdfd asdfasdfasd 是的发斯蒂芬阿萨德分撒旦法是的发送到发 上的发送到发斯蒂芬深度辅导费上的发送到水电费水电费啥打法胜多负少的水电费是否是大法官的耳挂式打分是的发斯蒂芬啥打法胜多负少的水电费是否".split(),key=i)
        if num_clicks:
            st.text(num_clicks)
    st.markdown("返回结果是")
    st.markdown(num_clicks)
    # st.markdown("You've clicked %s times!" % int(num_clicks))
