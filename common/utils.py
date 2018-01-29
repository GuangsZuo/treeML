# coding=utf-8

# utils for treeml


def add(Dict, key, inc):
    if not Dict.get(key):
        Dict[key] = 0
    Dict[key] += inc
