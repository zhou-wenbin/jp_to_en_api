#!/usr/bin/env python
# -*- coding: utf-8 -*-


from mtranslate import translate


def main():
    to_translate = 'how are you?'
    print(translate(to_translate, 'ja'))
 

if __name__ == '__main__':
    main()
