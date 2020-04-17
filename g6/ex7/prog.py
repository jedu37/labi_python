import requests, time

start = time.time()

f = requests.get("https://twitter.com/")

end = time.time()

print(("Information gotten in %d seconds")%((end-start)))

print(f.__sizeof__())
print(f.status_code)
