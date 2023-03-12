![New ui 13Mar2023](/img/ui_13Mar2023.jpg)

# chatgpt_API_web
Use ChatGPT API on the web

Built my own web version of ChatGPT using its API, together with the latest (as of 03 March 2023) **gpt-3.5-turbo** model, on a Mac.
Special thanks to **[OpsConfig](https://github.com/OpsConfig/OpenAI_Lab/tree/main/chatgpt)**, his demo code provides a foundation of this repository.

## Update history
#### 13 March 2023
- New & improved UI.
![New ui 13Mar2023](/img/ui_13Mar2023.jpg)

#### 10 March 2023: 
- Now supports **Google Chrome** and **Brave Browser** if you are not using **Safari** browser as I initially built. Please check [For_Chrome_browser.app](https://github.com/ez61/chatgpt_API_web/blob/main/For_Chrome_browser.app) for **Google Chrome** browser users, or if you're using **Brave Browser**, just get the same file for Chrome, and replace **Google Chrome** with **Brave Browser** in the .app file.
- Also when running the .app script, it will check if your preferred browser is active. If not, it will activate your chosen browser, go to the specified URL such as `http://127.0.0.1:7860`, and bring the UI to the front.

#### 5 March 2023
- Added a **Tokens Used** textbox on the right, to show the tokens consumed for this chat.
![demo of updated ui](/img/demo_ui_updated_5Mar2023.jpg)


## Ready to roll?

#### Requirement
- Installation of **[openai](https://pypi.org/project/openai/)** and **[gradio](https://pypi.org/project/gradio/)**
- Mac (to use the **Script Editor** to build a **launcher** which actually opens the chat UI in a browser tab)
- OpenAI **API key**


#### Steps

1. Download `ui.py` to your computer, and **Replace** the text `Your API key here` with your own API key.
2. Open **Script Editor** on your Mac, `copy` the code from either `ChatGPT_API.app` (for *Safari browser*) or `For_Chrome_browser.app` (for *Google Chrome*), and paste it into your **Script Editor**
3. Update the `PATH/TO/ui.py` to the actual file path on your computer, then *Save* and choose `application` under *File format*. Your saved file will have a `.app` suffix.
4. Double-click on the newly created `.app` file and your chat UI will start.

Sit back and enjoy!

## Buy me a coffee

I live in Melbourne and I LOVE coffee. If you find this useful and want to support me, you can [**buy me a coffee**](https://www.buymeacoffee.com/ez61). Thanks.


## FAQ

##### 1. Can I still use this if I'm using Windows?

The `ui.py` can still be used on Windows if you're using Jupyter Notebook. However, the `.app` files for either Safari or Chrome browsers are built for Mac OS users. Here, the `.app` file works as a **launcher** or **wrapper** to start your chat UI without the need to type code in the Terminal every time.

##### 2. What is URL used in the `.app` file?

The default URL is `http://127.0.0.1:7860`. The first time you start your **launcher** your chat UI will be on the default URL. If you have an active chat UI, and you start the second chat UI, the URL will be different, e.g. with port 7861 etc. If you want to find out, head to your Terminal and you will see the URL.

##### 3. What if I'm using Brave Browser?

Refer to **Update history** on 10 March 2023 listed above.

##### 4. My chat UI page cannot be reached?

Refresh the page and you will be okay to go. This is because in the `.app` file, we first execute the `ui.py` file to prepare the running environment before the chat UI page can be shown correctly. If you are seeing this error in Safari, don't panic, refresh the page will fix this. If you're using Google Chrome or Brave Browser, the page will be automatically refreshed.