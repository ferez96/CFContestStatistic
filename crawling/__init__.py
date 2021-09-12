"""
package have crawling stuffs
"""
import logging
import typing
from http.client import responses

import requests

logger = logging.getLogger(__name__)


class CodeForcesHTTPClient(object):
    host: str
    port: int
    lang: str

    # generate API key at: https://codeforces.cc/settings/api
    # (public, secret)
    api_key: (str, str)

    def __init__(self, host="http://codeforces.cc", port=80, lang="en", api_key: (str, str) = None):
        self.host = host
        self.port = port
        self.lang = lang

        # TODO: verify key pair
        self.api_key = api_key

    def ping(self) -> bool:
        """Send an simple requests to verify CodeForces server is still up running"""
        try:
            self.send_request("recentActions", dict(maxCount=1))
            return True
        except requests.exceptions.RequestException:
            return False

    def send_request(self, method_name: str, params: dict) -> typing.Any:
        """generic request action"""
        url = "{host}:{port}/api/{method}".format(host=self.host, port=self.port, method=method_name)
        try:
            response = requests.get(url, params=params)
            logger.info(f"Send: {url} - {responses.get(response.status_code)}")
            if response.status_code == requests.codes.OK:
                return response.json().get("result")
            elif response.status_code == requests.codes.BAD_REQUEST:
                raise requests.exceptions.RequestException(response.json().get("comment"))
            else:
                logger.debug(f"{url} return: {response.status_code} - {response.text}")
                response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise e
