import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

client = Groq(
    # Setting the API key from the environment file
    api_key=os.getenv("GROQ_API_KEY")  # Retrieves the API key securely
)

# Removes extra whitespaces from the content
def trim(content):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You do not talk at all, your job is to only remove extra whitespaces and that's it nothing else."
                
            },
            {
                "role": "user",
                "content": content,
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Removes extra whitespaces from the content
def verify(raw_content,format_content):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You are a classifier that checks if content1 and content2 context is the same if they are same you say true other just say false"
                
            },
            {
                "role": "user",
                "content": f'content1 : [{raw_content}], content2 : [{format_content}]',
            }
        ],
        model="llama3-70b-8192",
    )
    return chat_completion.choices[0].message.content

# Verify the content to are similar
# def verify(raw_content,format_content):
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "system",
#                 "content": f"You are an AI agent responsible for formatting content to be human-readable. You must not alter the content in any way—every string must remain exactly as it is. Your only task is to adjust the formatting to enhance readability. Do not add, remove, or modify any text. Additionally, you will not respond with any explanations or comments—only return the formatted content."
                
#             },
#             {
#                 "role": "user",
#                 "content": f'content1 : [{raw_content}], content2 : [{format_content}]',
#             }
#         ],
#         model="llama3-70b-8192",
#     )
#     return chat_completion.choices[0].message.content

def ai(question):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"You are an AI Assistant"
                
            },
            {
                "role": "user",
                "content": str(question),
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content