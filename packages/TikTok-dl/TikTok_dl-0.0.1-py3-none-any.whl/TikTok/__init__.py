import requests

class TikTok_dl:
    def __init__(self,link):
        
        headers = {
            'authority': 'lovetik.com',
            'accept': '*/*',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://lovetik.com',
            'referer': 'https://lovetik.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        data = {
            'query': link,
        }

        self.result = requests.post('https://lovetik.com/api/ajax/search', headers=headers, data=data).json()
        self._nowatermark = self.result['links'][0]['a']
        self._title = self.result['links'][0]['t']
        
        self._hashtag = self.result['desc']
        self._image = self.result['cover']
        self._watermark = self.result['links'][3]['a']
        self._audio = self.result['links'][4]['a']
    @property
    def nowatermark(self):
        return self._nowatermark
    @property
    def title(self):
        return self._title
    @property
    def hashtag(self):
        return self._hashtag
    @property
    def image(self):
        return self._image
    @property
    def watermark(self):
        return self._watermark
    @property
    def audio(self):
        return self._audio
    
    


