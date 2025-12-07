import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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",
)

completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-OCR:novita",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Say name of car on photo"
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://wallpapers.com/images/hd/koenigsegg-jesko-silver-supercar-klen9sbz95pj1qkh.jpg"
                    }
                }
            ]
        }
    ],
)

