def webscrap(search):
    # Get Input From User
    """
    import requests
    from bs4 import BeautifulSoup

    page=requests.get("http://spicier-raincoats.000webhostapp.com/product-category/clothing")
    if(page.status_code==200):
        html=page.content
        soup=BeautifulSoup(html,'html.parser')
        print(soup.prettify())
    """

    # Where results are stored
    search_results = []

    # Details
    shoe = [{'Product Name': 'Brown Sneaker', 'Price': '3500',
             'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1520096459084-096fcc53fa43-300x300.jpg'},
            {'Product Name': 'New Collections', 'Price': '2000',
             'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1543103582-ef9f6b5ed805-300x300.jpg'},
            {'Product Name': 'White Shoe', 'Price': '3000',
             'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1512374382149-233c42b6a83b-300x300.jpg'},
            {'Product Name': 'Yellow Shoe', 'Price': '2000',
             'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1514989940723-e8e51635b782-300x300.jpg'}
            ]

    clothes = [{'Product Name': "MEN's Fashion", 'Price': '1500',
                'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1484502249930-e1da807099a5-300x300.jpg'},
               {'Product Name': 'Tealer Tee', 'Price': '2000',
                'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1521498542256-5aeb47ba2b36-300x300.jpg'},
               {'Product Name': 'X Tee', 'Price': '1000',
                'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1485361767769-5ceffc9f2144-300x300.jpg'}
               ]

    electronics = [{'Product Name': 'Accessories', 'Price': '2000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1531297484001-80022131f5a1-300x300.jpg'},
                   {'Product Name': 'Audio Technica Headphones', 'Price': '6000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1481207727306-1a9f151fca7d-1-300x300.jpg'},
                   {'Product Name': 'Bluetooth Speaker', 'Price': '3000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1525004277915-9e455d05ca5d-300x300.jpg'},
                   {'Product Name': 'Canon DSLR', 'Price': '60000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1479909031872-133432b2d7c1-300x300.jpg'},
                   {'Product Name': 'Headphones and VR Box', 'Price': '3000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1478358161113-b0e11994a36b-300x300.jpg'},
                   {'Product Name': 'iPhone', 'Price': '80000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1511707171634-5f897ff02aa9-600x600.jpg'},
                   {'Product Name': 'MacBook Air Pro', 'Price': '175000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1468436139062-f60a71c5c892-300x300.jpg'},
                   {'Product Name': 'MacBook pro', 'Price': '175000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1484807352052-23338990c6c6-300x300.jpg'},
                   {'Product Name': 'Smart watch', 'Price': '10000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1434494878577-86c23bcb06b9-300x300.jpg'},
                   {'Product Name': 'Sony PS4', 'Price': '150000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1486401899868-0e435ed85128-300x300.jpg'},
                   {'Product Name': 'VR Glass Headset', 'Price': '8000',
                    'Image Link': 'https://spicier-raincoats.000webhostapp.com/wp-content/uploads/2018/12/photo-1459550532302-ba13832edcdf-300x300.jpg'}
                   ]
    # Items in store
    Items = ['shoes','shoe', 'tshirts','shoes','camera', 'fashion', 'accessories', 'PS4', 'DSLR', 'laptop', 'mobile', 'watch', 'VR Box']
    # Verifying item available or not
    search = search.lower()
    flag = False
    for i in Items:
        if search in i.lower():
            print("Item available")
            flag = True

    # Storing details in search result

    if "shoe" in search or "shoes" in search:
        search_results = shoe
    elif "tee" in search or "fashion" in search or "tshirt" in search or "shirts" in search:
        search_results = clothes
    else:
        search_results = electronics
    length=len(search_results)
    print(length)
    print(search_results)
    """for i in range(0, length):
        product_name=(search_results[i]['Product Name'])
        price=(search_results[i]['Price'])
        image_link(search_results[i]['Image Link'])
    """
    return search_results

    """"""
