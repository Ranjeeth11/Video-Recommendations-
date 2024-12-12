def fetch_paginated_data(endpoint, params=None):
    if params is None:
        params = {}
    
    params['resonance_algorithm'] = 'resonance_algorithm_cjsvervb7dbhss8bdrj89s44jfjdbsjd0xnjkbvuire8zcjwerui3njfbvsujc5if'

    all_data = []
    page = 1
    
    while True:
        try:
            current_params = {**params, 'page': page, 'page_size': 1000}
            url = f"{BASE_URL}{endpoint}"
            response = requests.get(url, headers=HEADERS, params=current_params)
            response.raise_for_status()
            data = response.json()

            if data.get('status') != 'success':
                break

            posts = data.get('posts', [])
            if not posts:
                break

            all_data.extend(posts)

            if len(posts) < current_params['page_size']:
                break

            page += 1

        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page} from {endpoint}: {str(e)}")
            break

    return {'data': all_data}

def fetch_data():
    try:
        posts = fetch_paginated_data('/posts/summary/get')
        views = fetch_paginated_data('/posts/view')
        likes = fetch_paginated_data('/posts/like')
        ratings = fetch_paginated_data('/posts/rating')
        users = fetch_paginated_data('/users/get_all')

        return posts, views, likes, ratings, users
    except Exception as e:
        print(f"Error fetching data: {str(e)}")
        raise