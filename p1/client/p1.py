from requests import get
from getpass import getpass

try:
    un = input("Enter username: ")
    pw = getpass("Enter password: ")
    url = "http://127.0.0.1:8000/dt"
    res = get(url, auth=(un, pw))
    
    if res.status_code == 200:
        data = res.json()
        msg = data.get("msg", "No message received.")
        print(msg)
    else:
        print("Check username/password")
except Exception as e:
    print("Issue:", e)
