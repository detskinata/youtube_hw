import os
from googleapiclient.discovery import build
import json
from dotenv import load_dotenv


class Channel:
    def __init__(self, channel_id):
        '''получение данных о ютуб канале по его id'''
        self.channel_id = channel_id

        load_dotenv()
        api_key: str = os.getenv('YOUTUBE_KEY')
        youtube = build('youtube', 'v3', developerKey=api_key)
        self.channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self):
        '''вывод информации о канале'''
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


#vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
#vdud.print_info()
