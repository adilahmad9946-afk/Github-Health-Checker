from fastapi import FastAPI

from services.github_service import get_repo_data
from services.analyzer import analyze_repo
from services.llm_service import generate_ai_summary

app = FastAPI()


@app.get("/")
def home():
    return {"message": "GitHub Health Checker Running"}


@app.get("/repo/{owner}/{repo}")
def repo_info(owner: str, repo: str):

    data = get_repo_data(owner, repo)

    return data


@app.get("/health/{owner}/{repo}")
def repo_health(owner: str, repo: str):

    repo_data = get_repo_data(owner, repo)

    analysis = analyze_repo(repo_data)

    summary = generate_ai_summary(repo_data)

    return {
    "repository": repo,
    "owner": owner,
    "analysis": analysis,
    "ai_summary": summary
}