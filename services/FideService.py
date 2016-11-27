import logging

import requests


def getToken(link, serialKey):
    params = {'serial': serialKey}
    url = link + '/api/fidebox/login'
    response = requests.post(url, data=params)
    if response.status_code >= 300:
        logging.error(response.text)
        raise Exception('invalid serialKey')
    else:
        return response.text

# def saveToken(token):
#     print(token)


# getToken('http://admin.fidebox.com:9101', 'fidebox1', saveToken)
