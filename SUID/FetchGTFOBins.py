
# Fetch SUID Binaries from GTFO Bins

#Customization
# -> URL
# -> BinNameTags

import requests
from bs4 import BeautifulSoup


url = "https://gtfobins.github.io/#+suid"

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    binNameTags = soup.find_all("a", class_="bin-name")

    for binNameTag in binNameTags:
        print(binNameTag.get_text())

else:
    print("Failed to fetch the page.")