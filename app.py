import streamlit as st
import ollama

st.title("AI Chatbot")

# Store chat messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
# Get user input
user_input = st.chat_input("Type a message...")

if user_input:
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Get response from Ollama
    response = ollama.chat(
        model="llama3.2",
        messages=st.session_state.messages
    )

    bot_response = response["message"]["content"]

    # Add assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    # Display assistant response
    with st.chat_message("assistant"):
        st.write(bot_response)