import requests
import json

def main():
    req = requests.get()
    print("HTTP Status Code: " + str(req.status_code))
    print(req.headers)
    json_response = json.loads(req.content)
    print("Pokermon Name : " + json_response['name'])

if __name__ == '__main__':
    main()