from unittest import result
from convertor.encode_convertor import Encoder
import os
from pathlib import Path

import convertor
import unittest

ROOT_PATH = Path(__file__).parent
KEY_FILE = Path(os.path.dirname(convertor.__file__)) / 'key'
SOURCE_DIR = ROOT_PATH / 'source'
DECODED_DIR = ROOT_PATH / 'decoded_sources'
ENCODED_DIR = ROOT_PATH / 'encoded_sources'


strings = ["5|o3<!41 <4535 4|23|\|7 5|o3<!41 3|\|0|_|[# 70 8|234|< 7#3 |2|_|135", 
          "|234|)48!1!7¥ <0|_||\|75",
          "5|o4|253 !5 83773|2 7#4|\| |)3|\|53"]

sentence = ["special cases arent special enough to break the rules",
            "readability counts",
            "sparse is better than dense"]          

class TestEncoder(unittest.TestCase):
    def test_convert_text(self):
        """Length of strings and sentence must be equal. Pull into strings array already converted value for testing function. 
           Pull into sentence array value which contain only latin-letter."""
        with self.assertRaises(NotImplementedError):
            encoder=Encoder(KEY_FILE)
            for i in range(len(strings)):
                self.assertEquals(encoder.convert_text(input_text=strings[i]), sentence[i])



if __name__ == '__main__':
    unittest.main()
