#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import codecs
import json
import re
import sys


def emoji_match_to_span(emoji_match):
    bytes = codecs.encode(emoji_match.group(), 'utf-8')
    bytes_as_json = json.dumps([ord(b) for b in bytes])
    return "<span class='emoji-bytes' data-emoji-bytes='%s'></span>" % bytes_as_json
    return emoji


def replace_emoji_characters(s):
    """
    Mechanical Turk will reject CSV input files containing Emoji
    characters with this error message:

      Your CSV file needs to be UTF-8 encoded and cannot contain
      characters with encodings larger than 3 bytes.
    """
    # The procedure for stripping Emoji characters is based on this StackOverflow post:
    #   http://stackoverflow.com/questions/12636489/python-convert-4-byte-char-to-avoid-mysql-error-incorrect-string-value

    if sys.maxunicode == 1114111:
        # Python was built with '--enable-unicode=ucs4'
        highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    elif sys.maxunicode == 65535:
        # Python was built with '--enable-unicode=ucs2'
        highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    else:
        raise UnicodeError("Unable to determine if Python was built using UCS-2 or UCS-4")

    return highpoints.sub(emoji_match_to_span, s)


def main():
    emoji = codecs.open('emoji.txt', encoding='utf-8').read().strip()
    print(replace_emoji_characters(emoji))


if __name__ == "__main__":
    main()
