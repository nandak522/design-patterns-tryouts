import csv
import os
from zope.interface import Interface, Attribute, implements
from lxml.etree import iterparse

class IReader(Interface):
    '''
    This Reader should be programmed to have different implementations.
    Like Reading a CSV file, XML file etc...
    '''
    name = Attribute('''Name/Path of the file''')

    def open():
        '''
        This method opens the file for reading
        '''

    def close():
        '''
        This method closes the file after performing operations
        to the file.
        '''

    def reader():
        '''
        This method iterates on the lines of the file.
        It could be iterating on
        1. On individual records if its a csv file.
        2. On a specific node if its a xml file.
        3. etcetra....
        '''

class CSVFileReader(object):
    implements(IReader)

    def __init__(self, name):
        self.name = name

    def reader(self):
        for record in csv.reader(open(os.path.abspath(self.name), 'r'),
                                 delimiter=',',
                                 quotechar='"'):
            yield record

class XMLFileReader(object):
    implements(IReader)

    def __init__(self, name):
        self.name = name

    def reader(self):
        for _, node in iterparse(self.name,
                                 events=('end',),
                                 tag='emp'):
            yield node

if __name__ == '__main__':
    fl = CSVFileReader(name='sample.csv')
    #fl = XMLFileReader(name='sample.xml')
    for line in fl.reader():
        print line
