import certifi
import requests

def is_secure_website(url):
    try:
        response = requests.get(url,verify=certifi.where())
        response.raise_for_status()
        return response.url.startswith('https://')
    except requests.exceptions.RequestException:
        return False
    
if __name__ == "__main__":
    website_url = input("Enter the website URL: ")

    if is_secure_website(website_url):
        print(f"{website_url} is secure website.")
    else:
        print(f"{website_url} is not a secure website.")