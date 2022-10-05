import json
import requests
import os

if not os.path.exists('data'):
    os.mkdir('data')

def get_products(category_id):

    url = f'https://api.retailrocket.ru/api/2.0/recommendation/popular/54e2c43c1e99470d5c66f56a/?&features=%2FPropertyInterests&stockId=101&categoryIds={category_id}&isDebug=true&format=json'

    response = requests.get(url=url).json()

    if len(response) == 0:
        return f'Category {category_id} does not exists!'

    products = {}

    for key, product in enumerate(response):
        old_price = product.get('OldPrice')
        price = product.get('Price')
        item_id = product.get('ItemId')
        vendor = product.get('Vendor')
        description = product.get('Description')
        type_prefix = product.get('TypePrefix')
        model = product.get('Model')
        url = product.get('Url')
        name = product.get('Name')
        category_id = category_id
        params = product.get('Params')
        try:
            comments = params.get('comments')
        except:
            comments = 0

        products[key] =\
            {
                'OldPrice': old_price,
                'Price': price,
                'ItemId': item_id,
                'Vendor': vendor,
                'Description': description,
                'TypePrefix': type_prefix,
                'Model': model,
                'Url': url,
                'Name': name,
                'CategoryIds': category_id,
                'comments': comments,
            }
    
    try:
        with open(f'data/{type_prefix}_{category_id}.json', 'w', encoding='utf-8') as file:
            json.dump(products, file, indent=4, ensure_ascii=False)
    except:
        with open(f'data/{category_id}.json', 'w', encoding='utf-8') as file:
            json.dump(products, file, indent=4, ensure_ascii=False)

    
    return f'Category {category_id} is exists!'

def main():
    cat = 1
    while cat <= 1000:
        print(get_products(cat))
        cat += 1

if __name__ == "__main__":
    main()
