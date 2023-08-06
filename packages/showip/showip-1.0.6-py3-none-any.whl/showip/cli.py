def main():
    from showip.showip import getdata
    import argparse

    parser = argparse.ArgumentParser(description='Get information about your IP or any other IP')
    parser.add_argument('-ip', type=str, help='Enter IP to get information')
    args = parser.parse_args()

    data = getdata(args.ip)
    print(f'IP: {data["query"]}\nCountry: {data["country"]}, {data["countryCode"]}\nRegion: {data["regionName"]}, {data["region"]}\nCity: {data["city"]}\nISP: {data["isp"]}\nReverse: {data["reverse"]}')