
# Fetch Danger Binaries Name from GTFO Bins

#Customization
# -> URL
# -> BinNameTags

import requests
from bs4 import BeautifulSoup
from urllib.parse import quote

url = "https://gtfobins.github.io/#+suid"
encoded_url = quote(url, safe=":/#") # Avoid Ingore #+suid !
response = requests.get(encoded_url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    binNameTags = soup.find_all("a", class_="bin-name")

    for binNameTag in binNameTags:
        print(binNameTag.get_text())

else:
    print("Failed to fetch the page.")