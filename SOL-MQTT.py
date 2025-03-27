    def get_sol_price(label):
    api_key = '4NEoWwgPDVPHhiPktXvK7xIoEeTDB5PSHXZKsLEJKRzc9VrXg9nW5PY5eRhZTVaf'

    url = 'https://api.binance.com/api/v3/ticker/price'

    symbol = 'SOLUSDT'


    headers = {
        'X-MBX-APIKEY': api_key
    }
    
    params = {'symbol': symbol}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        
        sol_price = float(data['price'])
        sol_price = "{:.2f}".format(sol_price)

        if 'prev_value' in get_sol_price.__dict__:
            prev_value = get_sol_price.prev_value
            if sol_price > prev_value: # New Price is Greater, Green
                label.config(fg='green')
            elif sol_price < prev_value:   # New Price is Less than, Red
                label.config(fg='red')
        
        # Update the label text with the price
        label.config(text=f'SOLUSDT Price: ${sol_price}')

        # Save the current value for the next comparison
        get_sol_price.prev_value = sol_price

        return sol_price

    else:
        label.config(text=f'Error: {response.status_code} - {response.text}')
