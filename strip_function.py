url = 'https://google.com'

# print(url.strip('https://'))

# Google

url = url.lstrip('https://')
url = url.rstrip('.com')
url = url.capitalize()

print(url)
