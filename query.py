#!/usr/bin/python3

class SoupQuery(object):

    attrs = {}
    parents = []
    content = []
    siblings = []

    def __init__(self, _type):
        self.type = _type

    def has_content(self, content):
        self.content.append(content)

    def has_attribute(self, attr, value):
        self.attrs[attr] = value

    def has_parent(self, query_object):
        self.parents.append(query_object)

    def has_sibling(self, query_object):
        self.siblings.append(query_object)
