#!/usr/bin/env python3

# Author: Hunter Steele
# Date: 12/12/25
# Version: 1.1

"""
Provides a small utility class for making HTTP GET requests and converting JSON responses into Python data structures.
"""

import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """sends a GET request and returns the raw response body as bytes"""
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        """loads the response body and converts it into a Python data structure"""
        response_body = self.get_response_body()
        return json.loads(response_body)