import requests

response = requests.get("http://127.0.0.1:8080/api/jobs")
if response.status_code == 200:
    print(response.json())
else:
    print(f"{response.status_code} {response.reason}")

response1 = requests.get("http://127.0.0.1:8080/api/jobs/1")
if response1.status_code == 200:
    print(response1.json())
else:
    print(f"{response1.status_code} {response1.reason}")

response2 = requests.get("http://127.0.0.1:8080/api/jobs/59321")
if response2.status_code == 200:
    print(response2.json())
else:
    print(f"{response2.status_code} {response2.reason}")

response3 = requests.get("http://127.0.0.1:8080/api/jobs/sanabi")
if response3.status_code == 200:
    print(response3.json())
else:
    print(f"{response3.status_code} {response3.reason}")
