# chatgpt_API_web
Use ChatGPT API on the web

Build my own web version of ChatGPT using its API, together with the latest (as of 03 March 2023) **gpt-3.5-turbo** model, on a Mac.
Special thanks to **[OpsConfig](https://github.com/OpsConfig/OpenAI_Lab/tree/main/chatgpt)**, his demo code provides a foundation of this repository.

## Special?
Not special, but it can fulfill the basic function. It **remembers** the previous cponversation, it also shows the **full** conversation on the same page.

## Requirement
- Installation of **[openai](https://pypi.org/project/openai/)** and **[gradio](https://pypi.org/project/gradio/)**
- Mac (to use the **Script Editor** to build a **launcher** which actually opens the chat interface in a browser tab, here I used Safari)
- ChatGPT API key

## Note
- The file **ChatGPT_API.app** in this repository was created by **Script Editor** on mac, so you can use **Script Editor** to open and edit.
- **ui.py** contains the Python code you need to execute your chat commands.
- If the browser tab shows nothing, refresh the page.

## Steps
- Download the 2 files and edit them (*API key* and *Org ID* in the **.py** file, *path-to-python-code* and *URL* in the **.app** script)
- Double-click the **ChatGPT_API.app** to start your own UI.

## Demo ui
![demo ui](/demo_ui.png)

![demo ui 2](/demo_ui2.jpg)
