# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

split_on = 'Summary\n\n'
must_contain = ['Project', 'Team Size']
with open('fgh.txt',encoding='latin-1') as f_input, open('d.txt', 'w',encoding='latin-1') as f_output:
    for part in f_input.read().split(split_on):
        if all(text in part for text in must_contain):
            f_output.write(split_on + part)