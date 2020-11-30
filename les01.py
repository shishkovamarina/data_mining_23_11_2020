import requests
import time
import json
import random

headers = {
    'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)',
}
params = {'records_per_page': 100, 'page': 1}

api_url_category = 'https://5ka.ru/api/v2/categories/'
api_url = 'https://5ka.ru/api/v2/special_offers/'


# url = 'https://5ka.ru/special_offers/'


class CategoryObj:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


def get_data(url: str, params: dict) -> dict:
    while True:
        time.sleep(1)
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            break
    return response.json()


# Формируем список объектов Category_obj
resCategory = requests.get(api_url_category).json()
Category_obj = [CategoryObj(**cat) for cat in resCategory]
countCateg = len(Category_obj)

url = 'https://5ka.ru/api/v2/special_offers/'

results = []
while url:
    response = get_data(url, params)
    results.extend(response['results'])
    print('Загружено товаров', len(results))
    # if len(results) > 40:   # для отладки
    #  break
    url = response['next']
    params = {}


Cat_Dict = []
for Category in Category_obj:
    fname = Category.parent_group_name.replace('\n', '')
    fname = fname.replace('*', '')
    fname = fname.replace('"', '')
    d = {'category_id': Category.parent_group_code, 'category_name': fname, "items": []}
    Cat_Dict.append(d)

print(Cat_Dict)


goods_new = []
for good in results:
    good_cat = 'PUI' + str(random.randint(1, countCateg))
    good['cat_id'] = good_cat
    goods_new.append(good)

print(goods_new[0]['cat_id'])

for good in goods_new:
    items = []
    for cd in Cat_Dict:
        if good['cat_id'] == cd['category_id']:
            items.append(good['name'])
            break
    # print(cd['items'], items)
    cd['items'] = items

# Здесь сформируем требуемые заданием файлы
print(Cat_Dict)
for cd in Cat_Dict:
    with open(cd['category_name'] + '.json', 'w') as f:
        json.dump(cd, f)
    f.close()