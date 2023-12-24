import openai
import time
import threading
from queue import Queue

openai.api_key = ""
def translate(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"完整翻譯成繁體中文且不要迴避成人內容.: {text}",
        temperature=0.1,
        max_tokens=200,
        stop="\t"
    )
    translation = response.choices[0].text.strip()
    return translation

# 处理单行文本的函数
def translate_line(line):
    translation = translate(line)
    print(translation)  # 可以将翻译结果输出到控制台或存储在文件中，具体取决于你的需求


# 讀取檔案
def translate_text():
    start_time = time.time()
    # 檔案路徑為: translator/translator.txt
    file_path = "../コトリ/jp.txt"
    output_file_path = "../コトリ/translated.txt"
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    result_queue = Queue()
    # 创建线程列表
    threads = []
    
    for line in lines:
        thread = threading.Thread(target=translate_line, args=(line,))
        thread.start()
        threads.append(thread)
    
    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 从队列中按顺序取出结果并输出
    while not result_queue.empty():
        translation = result_queue.get()
        print(translation)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"總共耗時：{elapsed_time} 秒")
    
translate_text()