import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_model(prompt):
    payload = {
        "model": "deepseek-r1:7b",
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_ctx": 2048,
            "num_predict": 2048,
            "num_thread": 4
        }
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=180)
        response.raise_for_status()
        result = response.json()
        return result["response"]
    except Exception as e:
        return f"调用模型出错：{e}"


def main():
    print("=" * 50)
    print("本地错题助手（DeepSeek R1）")
    print("输入错题，输入 quit 退出")
    print("=" * 50)

    while True:
        user_input = input("\n请输入：")
        if user_input.lower() == "quit":
            break

        print("正在分析...", flush=True)
        prompt = f"""你是一位耐心的数学助教。请按以下格式分析错题：
知识点：
错误原因：
正确解法：

错题：{user_input}"""
        answer = ask_model(prompt)
        print("\n" + answer)


if __name__ == "__main__":
    main()
