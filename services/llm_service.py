from openai import OpenAI
import os

API_KEY = os.getenv("NVIDIA_API_KEY")

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=API_KEY
)


def generate_ai_summary(repo_data):

    prompt = f"""
    Analyze this GitHub repository and generate a short professional summary.

    Repository Name: {repo_data['name']}
    Stars: {repo_data['stars']}
    Forks: {repo_data['forks']}
    Open Issues: {repo_data['issues']}
    Language: {repo_data['language']}
    Give response in 2-3 professional lines.
    """

    try:

        stream = client.chat.completions.create(
            model="z-ai/glm4.7",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=200,
            stream=True
        )

        final_response = ""

        for chunk in stream:

            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            if delta.content:

                print(delta.content, end="")

                final_response += delta.content

        return final_response if final_response else "No AI summary generated"
            

        



    except Exception as e:

        print("ERROR:", e)

        return f"AI Summary Error: {str(e)}"