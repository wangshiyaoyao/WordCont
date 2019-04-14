# encoding=utf-8
"""
time: 2019-04-10
IDE :pycharm + python3.7
auther:
功能：对文本文件中的单词的词频进行统计
用法：Example：python WordCont.py **.txt
"""
# pylint: disable=invalid-name

import sys
import logging
import re


def get_argv():
    '''获取第2个参数'''

    argv = sys.argv
    if len(argv) == 2:
        return argv[1]
    return ''


def _word_check_in_line(line):
    """单词匹配"""
    pattern = r'(?<![a-zA-Z0-9])([a-zA-Z][0-9a-zA-Z]*)'
    result = re.findall(pattern, line)
    # logging.debug('word check in line result:%s', result)
    return result


def _file_check(filename):
    """判断参数是一个可读文件，否则报错"""
    try:
        file_obj = open(filename)
        file_obj.close()
    except IOError:
        logging.error("Invalid argument.\nNeed a readable file.")
        sys.exit(1)


class FileHandle:
    """文件处理"""

    def __init__(self, filename, encoding='utf-8'):
        self._chars = 0                                               # 统计ascii
        self._container = {}                                          # 统计词频
        self._lines = 0                                               # 统计行数
        self._words = 0                                               # 统计单词数
        self._sorted_container = []                                   # 输出词频
        _file_check(filename)
        self._analysis(filename, encoding)

    def _chars_analysis(self, line):
        """统计ascii字符个数"""
        self._chars += len(line)

    def _line_analysis(self, line):
        """统计有效行数"""
        if line.strip():
            self._lines += 1

    def _word_analysis(self, line):
        """统计词频"""
        for word_match in _word_check_in_line(line):
            word = word_match.lower()
            self._container[word] = self._container.get(word, 0) + 1

    def _word_sum(self, line):
        """统计单词数"""
        self._words += len(_word_check_in_line(line))

    def _analysis(self, filename, encoding):
        """文件分析统计"""
        with open(filename, encoding=encoding) as fobj:
            for line in fobj:
                # logging.debug('read line:%s', line)
                self._chars_analysis(line)
                self._line_analysis(line)
                self._word_analysis(line)
                self._word_sum(line)
        self._sort_container()              # 排序

    def _sort_container(self):
        """词频结果排序，获取前10结果"""
        self._sorted_container = sorted(self._container.items(), key=lambda x: (-x[1], x[0]))[:10]

    def chars(self):
        """get chars"""
        return self._chars

    def container(self):
        """get sorted container"""
        return self._sorted_container

    def lines(self):
        """get lines"""
        return self._lines

    def words(self):
        """get words"""
        return self._words


def out_result(chars, words, lines, container):
    """结果输出"""
    print('characters:', chars)
    print('words:', words)
    print('lines:', lines)
    for word, number in container:
        print(f'<{word}>:{number}')


def main(filename):
    """主函数"""

    handle = FileHandle(filename)
    result = (handle.chars(), handle.words(), handle.lines(), handle.container())
    out_result(*result)


if __name__ == '__main__':
    main(get_argv())
