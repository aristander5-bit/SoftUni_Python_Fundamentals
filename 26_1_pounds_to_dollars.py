import requests, time

u = f"https://open.er-api.com/v6/latest/GBP"

while 1:
    try: print(requests.get(u, timeout=6).json()['rates']['USD'])
    except Exception as e:
        print("Error!, e")
        time.sleep(5)

