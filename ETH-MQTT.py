def get_eth_price(label):
    api_key = '4NEoWwgPDVPHhiPktXvK7xIoEeTDB5PSHXZKsLEJKRzc9VrXg9nW5PY5eRhZTVaf'
    url = 'https://api.binance.com/api/v3/ticker/price'
    symbol = 'ETHUSDT'
    headers = {
        'X-MBX-APIKEY': api_key
    }

    # API request
    params = {'symbol': symbol}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        
        eth_price = float(data['price'])
        eth_price = "{:.2f}".format(eth_price)

        if 'prev_value' in get_eth_price.__dict__:
            prev_value = get_eth_price.prev_value
            if eth_price > prev_value: # New Price is Greater, Green
                label.config(fg='green')
            elif eth_price < prev_value:   # New Price is Less than, Red
                label.config(fg='red')
        
        # Update the label text with the price
        label.config(text=f'ETHUSDT Price: ${eth_price}')

        # Save the current value for the next comparison
        get_eth_price.prev_value = eth_price

        return eth_price

    else:
        label.config(text=f'Error: {response.status_code} - {response.text}')
