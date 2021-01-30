import urllib.request
import requests

print("downloading with urllib")
url = "http://10.20.26.45:8080/program"
urllib.request.urlretrieve(url, "testdownload.txt")