from random import random


class DbConnector:
    def connect(self):
        assert random() > 0.5, 'connection error'
        return True

    def get_data(self):
        self.connect()
        return 'some data'
