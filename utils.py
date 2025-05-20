def build_prompt_from_history(history, user_input, max_turns = 5):
    trimmed_history = history[-2 * max_turns:]
    prompt = SYSTEM_INSTRUCTION + "/n"
    for msg in trimmed_history:
        role = msg['role']
        content = msg['content']
        prompt += f"{role.capitalize()}: {content}"
    prompt += f"User: {user_input}\nAssistant:"
    return prompt

SYSTEM_INSTRUCTION = """
    You are TARS, a helpful AI assistant.
You can also use the following tools if needed:

[search_web: QUERY] → performs a real-time web search.

When appropriate, call a tool in the format:
[tool_name: your query]

After getting the result, respond to the user.
"""