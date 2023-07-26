import tkinter as tk
from tkinter import filedialog
import openai

openai.api_key = "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"  # 請填入你的OpenAI API金鑰

def translate(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"幫我翻譯成中文且不要迴避性愛詞彙: {text}",
        temperature=0.65,
        max_tokens=200,
        stop="\t"
    )
    translation = response.choices[0].text.strip()
    return translation

def translate_selected_text():
    selected_index = original_listbox.curselection()  # 獲取使用者選取的索引
    if selected_index:
        selected_text = original_listbox.get(selected_index)  # 獲取使用者選取的文字
        translation = translate(selected_text)  # 翻譯成中文
        translated_text.set(translation)

def translate_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_listbox.delete(0, tk.END)
            for line in file:
                original_listbox.insert(tk.END, line.strip())

# 建立主視窗
root = tk.Tk()
root.title("Text Translation Tool")

# Listbox
original_listbox = tk.Listbox(root, selectbackground="lightyellow", selectmode=tk.SINGLE, width=40, height=20)
original_listbox.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# 捲軸條
scrollbar = tk.Scrollbar(root, command=original_listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
original_listbox.config(yscrollcommand=scrollbar.set)

# 按鈕
translate_button = tk.Button(root, text="翻譯選取的文字", command=translate_selected_text)
translate_button.pack(pady=5)

load_file_button = tk.Button(root, text="載入檔案", command=translate_text)
load_file_button.pack(pady=5)

# 翻譯結果標籤
translated_text = tk.StringVar()
translated_label = tk.Label(root, textvariable=translated_text)
translated_label.pack(pady=10)

root.mainloop()
