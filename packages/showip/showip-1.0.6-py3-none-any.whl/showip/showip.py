def getdata(ip=""):
    import requests, sys
    if ip == None or ip == "":
        ip = ""
    url = f"http://ip-api.com/json/{ip}?fields=66846719"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        if data["status"] == "success":
            isp = data["as"].split(" ")
            isp.pop(0)
            isp = " ".join(isp)
            data["isp"] = isp
            if data["reverse"] == "":
                data["reverse"] = data["query"]
        else:
            print(f"[FAIL] {data['message']}")
            sys.exit()
        return data
    else:
        print("[ERROR] Unknown error. Check your internet connection")
        sys.exit()

        