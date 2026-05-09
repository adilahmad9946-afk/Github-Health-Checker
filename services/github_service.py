import requests


def get_repo_data(owner, repo):

    repo_url = f"https://api.github.com/repos/{owner}/{repo}"
    contributors_url = f"https://api.github.com/repos/{owner}/{repo}/contributors"

    repo_response = requests.get(repo_url)
    contributors_response = requests.get(contributors_url)

    if repo_response.status_code == 200:

        data = repo_response.json()

        contributors = 0

        if contributors_response.status_code == 200:
            contributors = len(contributors_response.json())

        return {
            "name": data["name"],
            "owner": data["owner"]["login"],
            "stars": data["stargazers_count"],
            "forks": data["forks_count"],
            "issues": data["open_issues_count"],
            "language": data["language"],
            "updated_at": data["updated_at"],
            "watchers": data["watchers_count"],
            "contributors": contributors
        }

    else:
        return {"error": "Repository not found"}