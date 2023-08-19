import os


def get_search_results(query):
    # Replace 'YOUR_API_KEY' and 'YOUR_CSE_ID' with your actual API key and CSE ID
    api_key = os.getenv("API_KEY")
    cse_id = os.getenv("cse_id")


    url = f'https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cse_id}'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if 'items' in data:
            search_results = []
            for item in data['items']:
                result = {
                    'title': item.get('title', ''),
                    'link': item.get('link', ''),
                    'snippet': item.get('snippet', '')
                }
                search_results.append(result)
            return search_results
        else:
            return []  # No search results found
    else:
        return None  # Error occurred during the API request



import requests


