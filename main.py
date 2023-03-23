import os
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv


class Channel:
    def __init__(self, channel_id):
        '''получение данных о ютуб канале по его id.'''

        self.__channel_id = channel_id

        load_dotenv()
        api_key: str = os.getenv('YOUTUBE_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=self.__channel_id, part='snippet,statistics').execute()

        self.title = self.channel['items'][0]['snippet']['title']
        self.description = self.channel['items'][0]['snippet']['description']
        self.url = 'https://www.youtube.com/' + self.__channel_id
        self.subscriber_count = int(self.channel['items'][0]['statistics']['subscriberCount'])
        self.video_count = self.channel['items'][0]['statistics']['videoCount']
        self.view_count = self.channel['items'][0]['statistics']['viewCount']

    def print_info(self):
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))

    @property
    def channel_id(self):
        self.__channel_id

    def to_json(self, channel_json):
        with open(channel_json, 'w', encoding='UTF=8') as file:
            data = {
                'id': self.__channel_id, 'title': self.title, 'description': self.description, 'url': self.url,
                'subscriber_count': self.subscriber_count, 'video_count': self.video_count,
                'view_count': self.view_count
            }
            return json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def get_service(self):
        load_dotenv()

        api_key: str = os.getenv('YOUTUBE_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube

    def __str__(self):
        return f"Youtube-канал: {self.title}"

    def __lt__(self, other):
        return self.subscriber_count > other.subscriber_count

    def __add__(self, other) -> int:
        return self.subscriber_count + other.subscriber_count


ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')

vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
# vdud.print_info()
# print(vdud.title)
# print(vdud.video_count)
# print(vdud.url)

# vdud.channel_id = 'Новое название'
vdud.to_json('vdud.json')
print(ch1)
print(ch2)
