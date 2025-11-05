import threading, time, requests

def ping():
    url = "https://finalmm.choreoapps.dev"   # your Choreo public URL
    while True:
        try:
            requests.get(url, timeout=5)
        except Exception:
            pass
        time.sleep(7200)  # every 2 hours

def keep_alive():
    t = threading.Thread(target=ping, daemon=True)
    t.start()
