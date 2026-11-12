import requests

username = input("GitHub username kiriting: ")
url = f"https://api.github.com/users/{username}"

response = requests.get(url, timeout=10)


data = response.json()
print("===== GITHUB PROFIL =====")
print(f"Ismi: {data['name'] or 'Kiritilmagan'}")
print(f"Username: {data['login']}")
print(f"Profil: {data['html_url']}")
print(f"Public repository: {data['public_repos']}")
print(f"Followers: {data['followers']}")
print(f"Following: {data['following']}")
