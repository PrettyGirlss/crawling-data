import streamlit as st
import time
from rag import get_response

# 페이지의 제목과 아이콘을 설정합니다.
st.set_page_config(page_title="Echo Bot", page_icon="🤖")

# 페이지 제목을 중앙에 표시합니다.
st.markdown("<h1 style='text-align: center;'>🤖 챗봇 데모</h1>", unsafe_allow_html=True)
st.markdown("---")

# st.session_state에 'messages'가 없으면 초기화합니다.
# 이 세션 상태는 페이지가 다시 실행되어도 대화 기록을 유지하는 데 사용됩니다.
if "messages" not in st.session_state:
    st.session_state.messages = []

# 이전 대화 내용을 모두 보여줍니다.
# for-loop를 통해 st.session_state.messages에 저장된 모든 메시지를 반복하여 출력합니다.
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# st.chat_input을 사용하여 사용자로부터 입력을 받습니다.
# 사용자가 메시지를 입력하고 엔터를 누르면, 해당 메시지가 'prompt' 변수에 저장됩니다.
if prompt := st.chat_input("무엇이든 물어보세요!"):
    # 사용자가 입력한 메시지를 대화 기록(st.session_state.messages)에 추가합니다.
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 사용자의 메시지를 화면에 즉시 표시합니다.
    with st.chat_message("user"):
        st.markdown(prompt)

    # 챗봇의 답변을 생성하는 부분입니다.
    # 실제 챗봇에서는 이 부분에 LLM(거대 언어 모델)을 호출하는 코드가 들어갑니다.
    # 여기서는 간단히 사용자의 입력을 그대로 따라하는 '에코' 기능을 구현했습니다.
    # time.sleep(3)
    with st.spinner("답변을 생각하고 있어요..."):
        # RAG 체인 함수를 호출해서 답변을 가져옴
        assistant_response = get_response(prompt)
        
        message_placeholder = st.empty()
        full_response = ""

        # 스트리밍 효과를 위해 한 글자씩 점진적으로 표시합니다.
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.1)
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
        
    # 챗봇의 최종 답변을 대화 기록에 추가합니다.
    st.session_state.messages.append({"role": "assistant", "content": full_response})