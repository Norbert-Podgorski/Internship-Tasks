#!/usr/bin/python
# -*- coding: utf-8 -*-

# Returns length of the longest substring without repeating characters in the given string `s`:
def longest_substring(s):
    if type(s) is not str:
        raise TypeError("Only strings are allowed")
    characters_list = []
    for character in s:
        if character not in characters_list:
            characters_list.append(character)
    return len(characters_list)