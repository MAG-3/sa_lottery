import requests
import itertools
import pandas as pd

url = 'https://www.nationallottery.co.za/index.php?task=results.redirectPageURL&amp;Itemid=265&amp;option=com_weaver&amp;controller=lotto-history'

def lotto_scraper(start_draw, end_draw, save_filename):
    """Define first lotto draw number you want to scrape as well as the last lotto draw number. The filename is the name of the output CSV that will be saved to the machine."""
    
    new = []
    for i in range(start_draw, end_draw):
        params = {'gameName': 'Lotto', 'drawNumber': i, 'isAjax': True}

        r = requests.get(url, params=params)
        line = r.json()
        new_result = line['data']['drawDetails']

        if r.status_code == 200:
            print('API call successful')
        else:
            print(f'Error calling API. {r.status_code}')

        print(new_result['drawNumber'])
        print(new_result['drawDate'])

        new.append(dict(itertools.islice(new_result.items(), 10)))

        print(f'Draw number {i} is now complete.')
        #
        print('---------------------------------------------------------------------')

    final_lotto = pd.DataFrame(new)

    return final_lotto.to_csv(save_filename)
