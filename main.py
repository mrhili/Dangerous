from modules.FaviconHasher import FaviconHasher

class Dangerous:
    def __init__(self, url_list):
        self.urls = url_list
        self.favicon_hasher = FaviconHasher()  # Instantiate FaviconHasher

    def start_bug_hunt(self):
        for url in self.urls:
            response = self.favicon_hasher.submit_url(url)
            print("---------------------------------")
            print(f"- {response['what']}")  # Access 'what' key in response
            print("---------------------------------")
            print(response['message'])  # Access 'message' key in response
            print("---------------------------------")

def main():
    # List of URLs to submit for bug hunting
    url_list = [
        'https://alwaysjudgeabookbyitscover.com/',
        'http://maze.toys'
    ]

    # Create an instance of Dangerous with the list of URLs
    dng = Dangerous(url_list)

    # Start the bug hunting process
    dng.start_bug_hunt()

if __name__ == "__main__":
    main()
