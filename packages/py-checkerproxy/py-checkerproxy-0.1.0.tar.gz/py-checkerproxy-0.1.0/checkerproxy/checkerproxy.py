''' Requirements '''

import requests
import contextlib


class CheckerProxy():

    def __init__(self):
        pass

    def checker_proxy(self, filename:str):
        """This function will check list of proxies and store them in dictionary"""
        
        with open(filename, 'r') as file_:
            http_proxy = [str(line) for line in file_]


        working_proxy = {}
        counter = 0
        for line in http_proxy:
            proxy_dict = {"http": f"http://{line}"}
            with contextlib.suppress(requests.exceptions.RequestException):
                url = "http://httpbin.org/ip"
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) \
                    AppleWebKit/537.36 (KHTML, like Gecko) \
                    Chrome/41.0.2228.0 Safari/537.36'}
                response = requests.get(url, proxies= proxy_dict, headers=headers, timeout=1.9)
                proxy_dict = {}
                if response.status_code == 200:
                   counter += 1
                   proxy_dict["proxy"] = line.replace("\n", "")
                   proxy_dict["Timeout"] = int(response.elapsed.total_seconds() * 1000)
                   working_proxy[counter] = proxy_dict
        return working_proxy

