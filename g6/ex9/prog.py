import requests,json,sys

def main():

    serviceurl = "https://nominatim.openstreetmap.org/search.php?format=json&q=%s" % sys.argv[1]
    r = requests.get(serviceurl)
    print(json.dumps(r.json(),indent=2))

if __name__ == "__main__":
    main()