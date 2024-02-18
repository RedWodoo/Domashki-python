"""
program
"""
import os
import requests
os.makedirs('json_files',exist_ok=True)
get_jsons = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()
for i, get_json in enumerate(get_jsons):
    QWE1 = str(get_json) + ":" + str(get_jsons[get_json])
    with open(f'json_files/json_{i+1}.json','w',encoding= 'utf-8') as f:
        f.write(QWE1)
