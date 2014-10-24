'''
Created on Oct 23, 2014

@author: hemasudheer
'''


class SFConfig(object):

    def data(self, key, section=None):
        if section is None:
            section = self.parser.get('Nexus', 'infrastructure')
        return self.parser.get(section, key)

    def data_as_list(self, keys, section='TestData'):
        values = []
        for key in keys:
            values.append(self.parser.get(section, key))
        return values

    def data_as_dictionary(self, keys, section='TestData'):
        dictionary = {}
        for key in keys:
            dictionary[key] = self.parser.get(section, key)
        return dictionary
