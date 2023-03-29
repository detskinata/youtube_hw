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
        return self.__channel_id

    def to_json(self, channel_json):
        with open(channel_json, 'w', encoding='UTF=8') as file:
            data = {
                'id': self.__channel_id, 'title': self.title, 'description': self.description, 'url': self.url,
                'subscriber_count': self.subscriber_count, 'video_count': self.video_count,
                'view_count': self.view_count
            }
            return json.dump(data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def get_service() -> object:
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


class Video:
    def __init__(self, video_id):
        load_dotenv()
        api_key: str = os.getenv('YOUTUBE_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.video_id = video_id
        self.channel = Channel.get_service()
        self.video = youtube.videos().list(id=self.video_id, part='snippet,statistics').execute()
        self.video_title = self.video['items'][0]['snippet']['title']
        self.view_count = self.video['items'][0]['statistics']['viewCount']
        self.like_count = self.video['items'][0]['statistics']['likeCount']

    def __str__(self) -> str:
        return self.video_title


class PLVideo(Video):

    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

        load_dotenv()
        api_key: str = os.getenv('YOUTUBE_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.playlists = youtube.playlists().list(id=self.playlist_id, part='snippet').execute()
        self.playlist_title = self.playlists['items'][0]['snippet']['title']

    def __str__(self) -> str:
        return f"{self.video_title} {self.playlist_title}"

# video1 = Video('9lO06Zxhu88')
# print(video1)
# video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
# print(video2)
#
# ch1 = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
# ch2 = Channel('UC1eFXmJNkjITxPFWTy6RsWg')
#
# vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
# # vdud.print_info()
# # print(vdud.title)
# # print(vdud.video_count)
# # print(vdud.url)
#
# # vdud.channel_id = 'Новое название'
# vdud.to_json('vdud.json')
# print(ch1)
# print(ch2)
