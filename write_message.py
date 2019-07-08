#!/usr/bin/env python3
# -*- coding: utf-8 -*-

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I love programming.\n")