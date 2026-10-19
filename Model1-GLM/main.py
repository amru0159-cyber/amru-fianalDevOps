import requests

def ask_ai(question):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "glm4:9b-chat-q2_K",
            "prompt": question,
            "stream": False
        },
        timeout=300
    )
    response.raise_for_status()
    return response.json()["response"]

if __name__ == "__main__":
    question = input("ถาม GLM: ")
    print("กำลังประมวลผล...")
    print("GLM:", ask_ai(question))
