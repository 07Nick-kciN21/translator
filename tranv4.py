# -*- coding: ISO-8859-1 -*-

import os
import openai


# openai.api_key = os.getenv("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")
openai.api_key = "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"
response = openai.ChatCompletion.create(
  model="gpt-4",
  messages=[
    {
      "role": "system",
      "content": "翻譯成繁體中文"
    },
    {
      "role": "assistant",
      "content": "アスナ先輩に一体何をしたんだ!"
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response["choices"][0]["message"]["content"])