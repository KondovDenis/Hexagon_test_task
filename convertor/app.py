
import argparse
import re
import string
from convertor.encode_convertor import Encoder
import os
from pathlib import Path

import convertor
from convertor.decode_convertor import Decoder


ROOT_PATH = Path(__file__).parent
KEY_FILE = Path(os.path.dirname(convertor.__file__)) / 'key'
SOURCE_DIR = ROOT_PATH / 'source'
DECODED_DIR = ROOT_PATH / 'decoded_sources'
ENCODED_DIR = ROOT_PATH / 'encoded_sources'


def prepare_text_source(text: str):
    print(re.sub(string.punctuation, '', text.lower()))


def prepare_text_source(text: str):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for item in text:
        if item in punc:
            text = text.replace(item, "")
    return text


def decode():
    string = prepare_text_source(text=input())
    decoder = Decoder(KEY_FILE)
    print(decoder.convert_text(input_text=string))



def encode():
    text = input()
    encoder=Encoder(KEY_FILE)
    print(encoder.convert_text(input_text=text))
    

if __name__ == '__main__':
    encode()