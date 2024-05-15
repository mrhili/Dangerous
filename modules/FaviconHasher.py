import requests

class FaviconHasher:
    def __init__(self):
        self.base_url = 'https://faviconhasher.codejavu.tech/'

    def submit_url(self, url_to_submit):
        response = requests.post(self.base_url, data={'url': url_to_submit})
        if response.status_code == 200:
            return {
                'what': url_to_submit,
                'message': f'Successfully submitted URL {url_to_submit} using FaviconHasher',
                'data': {}
            }
        else:
            return {
                'what': url_to_submit,
                'message': f'Failed to submit URL {url_to_submit} using FaviconHasher',
                'data': {}
            }
