import requests
import json

# Replace with your GitHub username
USERNAME = "YOUR_GITHUB_USERNAME"

url = f"https://api.github.com/users/{USERNAME}/repos"

response = requests.get(url)
repos = response.json()

projects = []

for repo in repos:
    projects.append({
        "name": repo["name"],
        "description": repo["description"] or "No description",
        "url": repo["html_url"]
    })

with open("projects.json", "w") as file:
    json.dump(projects, file, indent=4)

print("Projects updated successfully!")
