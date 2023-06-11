from octokit import Octokit
repos = Octokit().repos.list_for_user(username="MASHOD0")
languages = []
for repo in repos.json:
    lang = repo["language"]
    if lang not in languages:
        languages.append(lang)
print(languages)
# print(repos.json)