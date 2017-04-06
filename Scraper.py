#!/usr/bin/python3

import requests, bs4

def get_soup(url):
    return bs4.BeautifulSoup(requests.get(url).text, 'html.parser')

def filter_elements(elements, _filter):
    return filter(_filter, elements)

def get_element_content(element, stripped=False):
    content = []
    if stripped:
        for string in element.stripped_strings:
            content.append(string)
    else:
        for string in element.strings:
            content.append(string)
    return content

def get_query(element, query, check_parents=True):
    #test type - attrs - siblings - parents
    type_match = test_type(element, query.type)
    attrs_match = test_attrs(element, query.attrs) if len(query.attrs) else True
    content_match = test_content(element, query.content) if len(query.content) else True
    #siblings_match = test_siblings(element, query.siblings) if len(query.siblings) else True
    #parents_match = test_parents(element, query.parents) if len(query.parents) and check_parents else True

    #print(type_match, attrs_match, content_match, siblings_match, parents_match)

    if type_match and attrs_match and content_match:
        return True
    else:
        return False

def test_type(element, _type):
    if element.name == _type:
        return True
    else:
        return False

def test_attrs(element, attrs):
    for key in attrs:
        if key in element.attrs:
            for item in element.attrs[key]:
                if item != attrs[key]:
                    return False
        else:
            return False
    return True

def test_content(element, content):
    for item in content:
        if item not in element.stripped_strings:
            return False
    return True

def test_siblings(element, siblings):
    all_siblings = element.previous_siblings + element.next_siblings
    for sibling in siblings:
        for sib in all_siblings:
            if not get_query(sib, sibling):
                return False
    return True

def test_parents(element, parents):
    for parent in parents:
        for element in element.parents:
            if not get_query(element, parent, check_parents=False):
                return False
    print('found parent')
    return True

#placeholder get queries working
def multibox_test(table):
    text = table.find_parent('table').find_previous_sibling('h3').get_text()
    print(text)
    if 'Used in' in text:
        return False
    else:
        return True

#list of all elements, filter using identifiers in single function
#query object
#return desired element
#an object? hasParent, hasAttribute {'att': value}, isType