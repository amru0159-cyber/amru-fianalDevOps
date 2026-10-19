import requests

def ask_ai(question):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "qwen3:4b", "prompt": question, "stream": False},
        timeout=180
    )
    response.raise_for_status()
    return response.json()["response"]

if __name__ == "__main__":
    question = input("ถาม AI: ")
    print("กำลังประมวลผล...")
    print("AI:", ask_ai(question))
