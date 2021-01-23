import requests
from PIL import Image
from io import BytesIO

# Using Bing Search v7 resource on Azure
# Collecting images based on a range of ages
# Ranges used:
# New born - 1-4
# Toddler - 5-10
# Adolescent - 11-24
# Adult - 25-49
# Middle age - 50-64
# Old age - 65 and above
# In order to diversify the dataset ang extract new and varying features among people
# different ethic races and regions have also been included
# Different regions of people:
# Indian
# Chinese
# Korean
# Japanese
# American
# African
# British
# Dutch
# German
# Balkan
# Russian

subscription_key = "d89f21b980e2419389b23c09ae6c58e6"
search_url = "https://api.bing.microsoft.com/v7.0/images/search"
search_term = "Australian boy"

headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
params  = {"q": search_term, "license": "public", "imageType": "photo", "count":150}

# Count parameter as seen in documentation, can be set to a max of 150 

response = requests.get(search_url, headers=headers, params=params)
response.raise_for_status()

searchResults = response.json()

urls = [ img['thumbnailUrl'] for img in searchResults["value"][:50]]
# print(urls)

all_images = []
fname = 150
for url in urls:
  image = requests.get(url)
  image.raise_for_status()
  img = Image.open(BytesIO(image.content)).convert('RGBA')
  all_images.append(img)
  with open('toddler_' + str(fname) + '.png','wb') as f:
      xyz = bytearray(image.content)
      f.write(xyz)
      fname += 1