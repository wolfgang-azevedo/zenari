#!/usr/bin/env python3.8
'''
It was a Honor to work with Zenari!

Regards,
Wolfgang
'''

import os
import sys

class MasterOfPuppet():

     def __init__(self, **kwargs):
         self.name = kwargs.get('name')


     def master(self):
        '''
        Master Method, for Master's only!
        '''

        if self.name is not None:

            if self.name == 'Zenari':
               return "He is working at Sandvine, yes he is a master!"

            else:
                return f'I do not recognizer {self.name} as a master!'
        else:
            return f'Enter a Master name!'

     def puppet(self):
        '''
        Puppet Method, for Master's of Puppet only!
        '''

        if self.name is not None:
            if self.name == 'Zenari':
                return "Yes, he is the Master of Swedish Puppets!"
            else:
                return f'I do not recognizer {self.name} as a Master of Puppets!'
        else:
            return f'Enter a Puppet Name'
