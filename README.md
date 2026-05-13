# GitHub Health Checker

A FastAPI-based GitHub repository health checker with NVIDIA LLM integration.

# Features

- GitHub repository analysis
- Health score generation
- AI-generated repository summary
- FastAPI REST API

# Tech Stack

- Python
- FastAPI
- GitHub API
- NVIDIA API
- OpenAI SDK
- Uvicorn

# Project Setup

## 1. Clone Repository
```bash 
git clone https://github.com/adilahmad9946-afk/Github-Health-Checker.git


cd Github-Health-Checker
```

## 2. Create Virtual Environment
```bash
python -m venv venv
```
## 3. Activate Virtual Environment
```bash
venv\Scripts\activate
```
## 4 Install Required Packages
```bash
pip install fastapi uvicorn requests openai python-dotenv
```
## 5.Add API Key
Create a .env file in the root folder.

Example:

``` id="s3" 
Github-Health-Checker/
│
├── main.py
├── README.md
├── .env
├── services/ 
```
Add your API Key inside .env file:
```env
OPENAI_API_KEY=your_api_key_here
```

Replace your_api_key_here with your actual API 


## 6. Run Project
```bash
uvicorn main:app --reload 
```

## 7. API Example
Open this in Browser
```bash
http://127.0.0.1:8000/health/fastapi/fastapi
```

# Demo Video
```bash
https://drive.google.com/file/d/18DAs0oNDbeS3_goe5wMlkfgI83BmHbV3/view?usp=drivesdk
```
