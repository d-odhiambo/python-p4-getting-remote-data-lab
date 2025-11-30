import urllib.request
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """Send GET request and return raw body as bytes."""
        with urllib.request.urlopen(self.url) as response:
            return response.read()  # return bytes (test expects this)

    def load_json(self):
        """Return JSON-decoded Python object."""
        body = self.get_response_body()
        return json.loads(body)  # json.loads works on bytes
