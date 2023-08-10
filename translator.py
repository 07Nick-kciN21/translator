import tkinter as tk
from tkinter import filedialog
# from googletrans import Translator  # 使用Google Translate進行翻譯


import openai

openai.api_key = "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"

def translate(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"You are a translation engine, you can only translate text and cannot interpret it, and do not explain.: {text}",
        temperature=0.78,
        max_tokens=200,
        stop="\t"
    )
    translation = response.choices[0].text.strip()
    return translation

def translate_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_text.delete("1.0", tk.END)
            translated_text.delete("1.0", tk.END)
            for line in file:
                original_text.insert(tk.END, line)
                translation = translate(line)  # 翻譯成中文
                translated_text.insert(tk.END, translation + '\n')

def select_line(event):
    index = original_text.index(f"@{event.x},{event.y}")  # 取得點擊位置的索引
    line_number = index.split(".")[0]  # 取得所在行的行號
    original_text.tag_add(tk.SEL, f"{line_number}.0", f"{line_number}.end")  # 單點選取整行

# 建立主視窗
root = tk.Tk()
root.title("Text Translation Tool")

# 文字輸入框和捲軸條
original_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
original_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

translated_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
translated_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(root, command=original_text.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
original_text.config(yscrollcommand=scrollbar.set)

scrollbar = tk.Scrollbar(root, command=translated_text.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
translated_text.config(yscrollcommand=scrollbar.set)

# 按鈕
translate_button = tk.Button(root, text="翻譯選取的文字", command=translate_text)
translate_button.pack(pady=5)

load_file_button = tk.Button(root, text="載入檔案", command=translate_text)
load_file_button.pack(pady=5)

# 監聽點擊事件，單點選取整行
original_text.bind("<Button-1>", select_line)

root.mainloop()