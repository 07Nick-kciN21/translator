import tkinter as tk
from tkinter import filedialog
import openai

openai.api_key = "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"  # 請填入你的OpenAI API金鑰


def translate(text, temperature, prompt="幫我翻譯成中文且不要迴避性愛詞彙"):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{prompt}: {text}",
        temperature=temperature,
        max_tokens=200,
        stop="\t"
    )
    translation = response.choices[0].text.strip()
    return translation

def translate_selected_text(event=None):
    selected_index = original_listbox.curselection()  # 獲取使用者選取的索引
    if selected_index:
        selected_text = original_listbox.get(selected_index)  # 獲取使用者選取的文字
        temperature = float(temperature_var.get())  # 獲取使用者輸入的temperature值
        prompt = prompt_var.get()  # 獲取使用者輸入的prompt值
        translation = translate(selected_text, temperature, prompt)  # 翻譯成中文
        translated_listbox.delete(selected_index)  # 刪除對應行的內容
        translated_listbox.insert(selected_index, translation)  # 將翻譯結果插入對應行

def translate_text():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            original_listbox.delete(0, tk.END)
            translated_listbox.delete(0, tk.END)  # 清空翻譯結果Listbox
            for line in file:
                original_listbox.insert(tk.END, line.strip())
                temperature = float(temperature_var.get())  # 獲取使用者輸入的temperature值
                translation = translate(line, temperature)  # 翻譯成中文
                translated_listbox.insert(tk.END, translation)

# 建立主視窗
root = tk.Tk()
root.title("Text Translation Tool")

# Listbox顯示原文
original_listbox = tk.Listbox(root, selectbackground="lightyellow", selectmode=tk.SINGLE, width=40, height=20)
original_listbox.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# 捲軸條
scrollbar = tk.Scrollbar(root, command=original_listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
original_listbox.config(yscrollcommand=scrollbar.set)

# Listbox顯示翻譯結果
translated_listbox = tk.Listbox(root, selectbackground="lightblue", selectmode=tk.SINGLE, width=40, height=20)
translated_listbox.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

# 捲軸條
scrollbar = tk.Scrollbar(root, command=translated_listbox.yview)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)
translated_listbox.config(yscrollcommand=scrollbar.set)

# 按鈕
translate_button = tk.Button(root, text="翻譯選取的文字", command=translate_selected_text)
translate_button.pack(pady=5)

load_file_button = tk.Button(root, text="載入檔案", command=translate_text)
load_file_button.pack(pady=5)

# 翻譯結果標籤
translated_text = tk.StringVar()
translated_label = tk.Label(root, textvariable=translated_text)
translated_label.pack(pady=10)

# Prompt輸入
prompt_label = tk.Label(root, text="Prompt:")
prompt_label.pack()

prompt_var = tk.StringVar()
prompt_entry = tk.Entry(root, width=40, textvariable=prompt_var)
prompt_entry.pack()

# Temperature輸入
temperature_label = tk.Label(root, text="Temperature:")
temperature_label.pack()

temperature_var = tk.DoubleVar()
temperature_entry = tk.Entry(root, width=10, textvariable=temperature_var)
temperature_entry.pack()

root.mainloop()