"""
This file was modified from udemy-dl
https://github.com/r0oth3x49/udemy-dl/

Copyright (c) 2018-2025 Nasir Khan (r0ot h3x49)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the
Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH 
THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


import time
import requests
from constants import HEADERS


class Session(object):
    def __init__(self):
        self._headers = HEADERS
        self._session = requests.sessions.Session()

    def _set_auth_headers(self, access_token="", cookies={}):
        self._headers["Authorization"] = "Bearer {}".format(access_token)
        self._headers["X-Udemy-Authorization"] = "Bearer {}".format(
            access_token)
        self._headers["Cookie"] = cookies

    def _get(self, url):
        for i in range(10):
            session = self._session.get(url, headers=self._headers)
            if session.ok or session.status_code in [502, 503]:
                return session
            if not session.ok:
                print('Failed request '+url)
                print(
                    f"{session.status_code} {session.reason}, retrying (attempt {i} )...")
                time.sleep(0.8)

    def _post(self, url, data, redirect=True):
        session = self._session.post(url,
                                     data,
                                     headers=self._headers,
                                     allow_redirects=redirect)
        if session.ok:
            return session
        if not session.ok:
            raise Exception(f"{session.status_code} {session.reason}")

    def terminate(self):
        self._set_auth_headers()
        return
