import tkinter as tk
from tkinter import filedialog
from googletrans import Translator  # 使用Google Translate進行翻譯

def translate_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_text.delete("1.0", tk.END)
            translated_text.delete("1.0", tk.END)
            for line in file:
                original_text.insert(tk.END, line)
                translation = translator.translate(line, dest='en')  # 翻譯成英文，你可以更改'dest'來翻譯成其他語言
                translated_text.insert(tk.END, translation.text + '\n')

# 建立主視窗
root = tk.Tk()
root.title("Text Translation Tool")

# 創建翻譯器
translator = Translator()

# 文字輸入框和捲軸條
original_text = tk.Text(root, wrap=tk.WORD, height=20, width=40)
original_text.pack(side=tk.LEFT, padx=10, pady=10)

translated_text = tk.Text(root, wrap=tk.WORD, height=20, width=40)
translated_text.pack(side=tk.LEFT, padx=10, pady=10)

scrollbar = tk.Scrollbar(root, command=original_text.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
original_text.config(yscrollcommand=scrollbar.set)

scrollbar = tk.Scrollbar(root, command=translated_text.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
translated_text.config(yscrollcommand=scrollbar.set)

# 按鈕
translate_button = tk.Button(root, text="翻譯", command=translate_text)
translate_button.pack(pady=10)

root.mainloop()
