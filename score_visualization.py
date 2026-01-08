
import requests
import matplotlib.pyplot as plt

API_URL = "https://jsonplaceholder.typicode.com/users"

response = requests.get(API_URL)
users = response.json()

scores = {user['username']: len(user['name']) * 5 for user in users}

average_score = sum(scores.values()) / len(scores)
print("Average Score:", average_score)

plt.bar(scores.keys(), scores.values())
plt.xticks(rotation=45, ha='right')
plt.title("Student Scores")
plt.tight_layout()
plt.show()
