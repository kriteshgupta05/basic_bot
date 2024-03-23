import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a helpful healthcare assistant"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

interface = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "Your Healthcare Assistance")

interface.launch(share=True)
