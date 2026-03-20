
# all th eimport necessary
import ollama
import json
from tools import tools
from function import tool_map

#the prompt to tell the machine how to act


system_prompt = """You are a calculator assistant.
For ANY math problem, use the calculator tools - do not calculate yourself.
If the query is not mathematical, respond conversationally."""

history = []

def chat(user_message):
    history.append({"role": "user", "content": user_message})
    messages = [{"role": "system", "content": system_prompt}] + history

    response = ollama.chat(model="qwen3:4b", messages=messages, tools=tools, options={"temperature": 0.1} )

    if response.message.tool_calls:
        for tool in response.message.tool_calls:
            name = tool.function.name
            args = tool.function.arguments
            try:
                result = tool_map[name](**args)
                print(f"[Tool called: {name}({args}) = {result}]")
                history.append({"role": "tool", "content": json.dumps({"result": result}), "name": name})
            except Exception as e:
                history.append({"role": "tool", "content": json.dumps({"error": str(e)}), "name": name})

        final = ollama.chat(model="qwen3:4b",
                            messages=messages + [response.message] + history[-len(response.message.tool_calls):] , options={"temperature": 0.1} )
        answer = final.message.content
    else:
        answer = response.message.content

    history.append({"role": "assistant", "content": answer})
    return answer