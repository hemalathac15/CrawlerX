#Step 3 Downloads webpage HTML
import requests

def download_page(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return response.text

    except Exception as e:
        print("Download Error:", e)

    return ""