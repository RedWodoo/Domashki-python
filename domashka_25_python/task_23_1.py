"""
program
"""
import os
import random
import requests
for i in range(10):
    image_urls = [
        f"https://picsum.photos/id/{j}/500/300" for j in range(random.randint(1, 1000))
    ]
    response = requests.get(image_urls[i])
    os.makedirs(f'image_folder_{i+1}',exist_ok=True)
    with open(f'image_folder_{i+1}/img_{i+1}.jpg', "wb") as file:
        file.write(response.content)
