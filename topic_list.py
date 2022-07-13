import os

#Chatbot has a lot to learn, so for user not to get bored a progress bar is added. This class, after each conversation learned, stops and allows the progress bar to move.
class Progresor:

    def __init__(self) -> list:
        self.topics_folder_en = "venv\Lib\site-packages\chatterbot_corpus\data\english"
        self.topic_name_list = []

    def list_of_topic_names(self) -> list:
        for file in os.listdir(self.topics_folder_en):
            name_length = len(file) - 4
            self.topic_name_list.append(file[:name_length])
        return self.topic_name_list
