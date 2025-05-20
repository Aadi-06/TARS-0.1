import requests

def query_ollama(prompt, model):
    try:
        response = requests.post(
            url = 'http://localhost:11434/api/generate',
            json = {
                'model' : model,
                'prompt' : prompt,
                'stream' : False
            }
        )
        response.raise_for_status()
        return response.json()['response']
    except Exception as e:
        return f"Error querying the model: {e}"