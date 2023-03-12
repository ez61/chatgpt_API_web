import openai
import gradio as gr

openai.api_key = "Your API key here"

conversation=[{"role": "system", "content": "Here is our full conversation in case you need:"}]

def format_message(message):
    role = message["role"]
    content = message["content"]
    if role == "system":
        return f'<p><u>Here is our <strong>Full Chat History</strong> in case you need:</u></p>'
    elif role == "user":
        return f'<h5 class="user-message">{content}</h4>'
    elif role == "assistant":
        return f'<p class="assistant-message">{content}</p>'


def chatbot(query):
    conversation.append({"role": "user", "content": query})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
    )
    conversation.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
    return response['usage']['total_tokens'],response['choices'][0]['message']['content'], "\n\n".join([format_message(c) for c in conversation])



with gr.Blocks() as demo:
    
    gr.Markdown('<img src="https://em-content.zobj.net/source/microsoft-teams/337/merman_1f9dc-200d-2642-fe0f.png" width="60" height="60">')
    gr.Markdown("#### G'day")
    gr.Markdown("I'm your **Chat Assistant**, ask me any question")
    with gr.Row():
        with gr.Column():
            Query = gr.Text(placeholder="Ask me a question", label="Query")
            btn = gr.Button("Submit")
        with gr.Column():
            Tokens = gr.Text(label="Tokens Used")
            Response = gr.Text(label="Current Response")
            
    with gr.Row():
        History = gr.HTML(label="Full Chat")
        btn.click(chatbot, inputs=[Query], outputs=[Tokens, Response, History])

demo.launch()
