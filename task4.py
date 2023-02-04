import os
import requests
from time import sleep
from bs4 import BeautifulSoup
import json

data = []


def scrape_block(blocknumber, page):
    # the URL of the web page that we want to get transaction data
    api_url = "https://etherscan.io/txs?block=" + str(
        blocknumber) + "&p=" + str(page)
    # HTTP headers used to send a HTTP request
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:72.0) Gecko/20100101 Firefox/72.0'
    }
    # Pauses for 0.5 seconds before sending the next request
    sleep(0.5)
    # send the request to get data in the webpage
    response = requests.get(api_url, headers=headers)

    # get the transaction table from the response data we get
    for row in BeautifulSoup(
            response.content,
            'html.parser').select('table.table-hover tbody tr'):
        # each row in the table is a transaction
        attributes = map(lambda x: x.text, row.findAll('td'))

        # extract transaction attributes
        _begin, hash, method, block, timestamp1, age, from1, _arr, to1, value1, txnfee, burnfee = attributes
        if len(method) > 0:
            print("Contract Method: ", method)
        # create a dictionary for each transaction
        dictionary = {
            'transaction_id': hash,
            'transaction_block': block,
            'from_address': from1,
            'to_address': to1,
            'transaction_fee': txnfee
        }

        data.append(dictionary)
        ######################## modify code below for each exercise #######################
        # print("transaction of ID:", hash, "block:", block, "from address",
        #       from1, "toaddress", to1, "transaction fee", txnfee, "age: ", age)


if __name__ == "__main__":  # entrance to the main function
    for i in range(3):
        scrape_block(15479087, i)
    json_object = json.dumps(data, indent=4)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(dir_path + "\\task5.json", "w") as outfile:
        outfile.write(json_object)
