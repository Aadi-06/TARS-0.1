from tools import Tools

def detect_tool_call(response_text):
    if "[" in response_text and "]" in response_text and ":" in response_text:
        start = response_text.find("[")
        end = response_text.find("]", start)
        tool_text = response_text[start+1:end]
        if ":" in tool_text:
            tool_name, tool_input = map(str.strip, tool_text.split(":", 1))
            return tool_name, tool_input
    return None, None

def run_tool(tool_name, tool_input):
    if tool_name in Tools:
        return Tools[tool_name]["function"](tool_input)
    return f"[Error]: Tool '{tool_name}' not found."

    