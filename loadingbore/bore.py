'''
bore.py

Contains the base class for all the cool^H^H^H^H boring loading bars.
'''
from __future__ import print_function
from blessings import Terminal
import sys


class BoreBase(object):
    '''Loading bar base class'''
    bar_pre = '['
    bar_post = ']'
    bar_progress_full = '='
    bar_progress_half = '-'
    bar_progress_arrow = '>'
    bar_progress_spacer = ' '

    def __init__(self, max_value=100, value=0, width=Terminal().width):
        self.drawn = False
        self.value = value
        self.max_value = max_value
        self.width = width

    def _render(self):
        '''Render the progress bar'''
        # Get the final bar width
        width = self.width - (len(self.bar_pre) +
                              len(self.bar_post) +
                              len(self.bar_progress_arrow))

        bar_length = (float(self.value) / float(self.max_value)) * width

        half_amount = int(bar_length * 2) % 2
        full_amount = int(bar_length - half_amount)
        space_amount = int(width - (full_amount + half_amount))

        # Build up the bar
        return ''.join((self.bar_pre,
                        self.bar_progress_full * full_amount,
                        self.bar_progress_half * half_amount,
                        self.bar_progress_arrow if self.value != self.max_value
                        else self.bar_progress_full,
                        self.bar_progress_spacer * space_amount,
                        self.bar_post))

    def update(self, value):
        '''
        Update the bar with a new value.

        Extend this for extra cool functionality and stuff.
        '''
        self.value = value
        return self

    def draw(self):
        '''Print the loading bar'''
        sys.stdout.write('\r' + self._render())
        sys.stdout.flush()
