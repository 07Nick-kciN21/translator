import openai
import time

openai.api_key = ""
def translate(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"完整翻譯成繁體中文.: {text}",
        temperature=0.0,
        max_tokens=200,
        stop="\t"
    )
    translation = response.choices[0].text.strip()
    return translation

# 讀取檔案
def translate_text():
    start_time = time.time()
    # 檔案路徑為: translator/translator.txt
    file_path = "jp.txt"
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                translation = translate(line)
                # translation寫入t1.txt
                with open('ch1.txt', 'a', encoding='utf-8') as f:
                    f.write(translation + '\n')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"總共耗時：{elapsed_time} 秒")
translate_text()  