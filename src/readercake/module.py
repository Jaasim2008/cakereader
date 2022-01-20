import colorama
from colorama import Fore
import os


class ReaderCake:
    def __init__(self, filename, encoding, filedir):
        self.filename = filename
        self.encoding = encoding
        self.filedir = filedir

    def read_all(self):
        with open(self.filename) as file:
            file_data = file.read()
            return file_data

    def write_data(self, word):
        with open(self.filename, 'w') as file:
            file.write(word)
            print(f'{Fore.RED}Pass')

    def append_data(self, word):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(f' {word}')
            print(f'{Fore.RED}Pass')

    def read_line(self, line):
        with open(self.filename, 'r') as file:
            my_data = file.readline(line)
            return my_data

    def read_lines(self, line):
        try:
            with open(self.filename, 'r') as file:
                my_data = file.readlines(line)
                full_data_word = my_data[0]
                return full_data_word
        except Exception as e:
            print('')
            try:
                os.system('cls')
            finally:
                os.system('clear')
