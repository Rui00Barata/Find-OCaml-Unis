import requests

def get_html(url):
    response = requests.get(url)
    return response.text 