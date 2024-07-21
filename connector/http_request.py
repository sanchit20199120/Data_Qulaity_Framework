import logging
import requests

logger = logging.getLogger('Data Quality')

def send_post_request(url, data=None, json_data= None, **kwargs):
    response = send_post_request(url=url, data=data, json_data =json_data, **kwargs)

    if response.status_code not in [200,201]:
        raise Exception(f"Error sending post request to url {url}: \n -Status Code: {response.status_code} "
                        f"\n- Reason: {response.reason} \n- text: {response.text}")
    else:
        data = response.json()
        print(response.status_code)
    return data

