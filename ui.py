import os
import openai
import gradio as gr

openai.api_key = "Your API key here"
openai.organization = os.getenv("Org IDf") 

conversation=[{"role": "system", "content": "Here is our full conversation in case you need:"}]


def chatbot(query):
    conversation.append({"role": "user", "content": query})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=2,
        max_tokens=250,
        top_p=0.9
    )
    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return response['choices'][0]['message']['content'], "\n\n".join(c['content'] for c in conversation)

interface = gr.Interface(
    fn=chatbot,
    title="My Chat Assistant",
    inputs=gr.inputs.components.Textbox(label="Query", placeholder="Ask me a question"),
    outputs=[gr.outputs.components.Textbox(label="Response"), gr.outputs.components.Textbox(label="Full Conversation")],
)

interface.launch()
