import requests
headers = {
    "Authorization": "Barear eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwiZXhwIjoxNzc1MTA4MDgwfQ.vQg4tJK0zkB1s_qfLG1SFfbCJnw80vjj5O9Q1cz6Y9w"
}
REQUISISAO = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)
print(REQUISISAO)
print(REQUISISAO.json)