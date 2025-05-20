from duckduckgo_search import DDGS

def search_web(query, max_result = 3):
    try:
        with DDGS() as ddgs:
            results = ddgs.text(query)
            return "\n".join([r["body"] for r in results][: max_result])
    except Exception as e:
        return f"[Tool Error] : {e}"

Tools = {
    "search_web" : {
        "function" : search_web,
        "description" : "Use this tool to answer current events, recent news, or trending info from the internet.",
    }
}