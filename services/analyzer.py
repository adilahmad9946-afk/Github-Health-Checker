from datetime import datetime


def analyze_repo(repo_data):

    score = 0

    strengths = []
    weaknesses = []

    # Stars Analysis
    if repo_data["stars"] > 500:
        score += 3
        strengths.append("Popular repository")
    else:
        weaknesses.append("Low popularity")

    # Forks Analysis
    if repo_data["forks"] > 100:
        score += 2
        strengths.append("Strong community usage")
    else:
        weaknesses.append("Low fork activity")

    # Issues Analysis
    if repo_data["issues"] < 100:
        score += 2
        strengths.append("Issues under control")
    else:
        weaknesses.append("Too many open issues")

    # Contributors Analysis
    if repo_data["contributors"] > 5:
        score += 2
        strengths.append("Good contributor activity")
    else:
        weaknesses.append("Very few contributors")

    # Recent Activity Analysis
    updated_date = datetime.strptime(
        repo_data["updated_at"],
        "%Y-%m-%dT%H:%M:%SZ"
    )

    days_ago = (datetime.utcnow() - updated_date).days

    if days_ago < 30:
        score += 1
        strengths.append("Recently updated")
    else:
        weaknesses.append("Repository inactive recently")

    # Health Percentage
    percentage = (score / 10) * 100

    # Rating System
    if score >= 8:
        status = "Healthy"
        rating = "Excellent"

    elif score >= 5:
        status = "Moderate"
        rating = "Good"

    else:
        status = "Inactive"
        rating = "Poor"

    return {
        "health_score": f"{score}/10",
        "health_percentage": f"{percentage:.0f}%",
        "rating": rating,
        "status": status,
        "strengths": strengths,
        "weaknesses": weaknesses
    }