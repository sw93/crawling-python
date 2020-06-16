import requests

# image url
response = requests.get('https://thumbnail8.coupangcdn.com/thumbnails/remote/230x230ex/image/retail/images/2020/02/28/17/8/579b55ed-34c6-4ed0-9c41-a5e9cc0305a6.jpg')

# save file
with open('579b55ed-34c6-4ed0-9c41-a5e9cc0305a6.jpg', 'wb') as f:
    f.write(response.content)

print('save complete image file')