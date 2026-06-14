import requests


def get_github_stats(username):

    repos_url = f"https://api.github.com/users/{username}/repos"

    repos = requests.get(repos_url).json()

    repo_count = len(repos)

    total_stars = sum(
        repo["stargazers_count"]
        for repo in repos
    )

    languages = {}

    for repo in repos:

        lang = repo["language"]

        if lang:

            languages[lang] = (
                languages.get(lang, 0) + 1
            )

    return {
        "repo_count": repo_count,
        "total_stars": total_stars,
        "languages": languages
    }