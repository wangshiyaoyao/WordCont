"""Test for WordCont"""
# pylint: disable=invalid-name

import os
import unittest

from xeger import Xeger
import WordCont

TEMP_FILE = '.test.txt'


def touch_test_file(line_num, word_num):
    """创建测试文件，随机生成字符，用于测试"""

    _x = Xeger()
    words = lambda: _x.xeger(r'[a-zA-Z][a-zA-Z0-9]*')       # 随机生成有效单词
    non_word = lambda: _x.xeger(r'\d[a-zA-Z0-9]*')          # 随机生成开头为数字的单词
    separator = lambda: _x.xeger(r'[^a-zA-Z0-9\n\r]')       # 随机生成非字母数字回车换行符的字符
    space = lambda: _x.xeger(r'\n[\s]*\n')                  # 随机生成回车空白字符回车

    # 统计生成的文件中字符、单词、有效行、词频
    result = {'chars': 0, 'words': word_num * line_num, 'lines': line_num, 'container': {}}

    # 创建文件，随机生成字符
    file_obj = open(TEMP_FILE, 'w')
    for _ in range(line_num):
        for _ in range(word_num):
            word = words()
            chars = word + separator() + non_word() + separator()
            result['chars'] += len(chars)
            result['container'][word.lower()] = result['container'].get(word.lower(), 0) + 1
            file_obj.write(chars)
        chars = space()
        result['chars'] += len(chars)
        file_obj.write(chars)
    file_obj.close()

    # 获取排序后的词频结果
    sort_result = sorted(result['container'].items(), key=lambda x: (-x[1], x[0]))[:10]
    result['container'] = sort_result
    return result


class TestWordCont(unittest.TestCase):
    """Test for WordCont"""

    def test_chars(self):
        """字符统计测试"""
        self.assertEqual(handle.chars(), result['chars'])

    def test_words(self):
        """单词测试"""
        self.assertEqual(handle.words(), result['words'])

    def test_lines(self):
        """有效行测试"""
        self.assertEqual(handle.lines(), result['lines'])

    def test_container(self):
        """词频测试"""
        self.assertEqual(handle.container(), result['container'])


result = touch_test_file(100, 40)
handle = WordCont.FileHandle(TEMP_FILE)
os.remove(TEMP_FILE)
if __name__ == '__main__':
    unittest.main()
