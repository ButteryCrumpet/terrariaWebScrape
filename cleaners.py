#!/usr/bin/python3
import utils

def list_filter(content_list, to_clean):
    filtered = [item for item in content_list if item not in to_clean]
    return list(filtered)

def clean_extra_vals(_list):
    cleaned = utils.take_after(_list, 'Ingredients')
    if len(cleaned):
        return cleaned
    else:
        return _list
