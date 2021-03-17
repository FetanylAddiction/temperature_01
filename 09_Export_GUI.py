from tkinter import *
from functools import partial # to prevent unwanted windows

import random


class Converter:
    if __name__ == '__main__':
        def __init__(self):

                # Formatting Variables
                background_color = "#B3B3B3"

                # In actual program this is blank and is populated with user calculations
                self.all_calc_list = ['0 degrees C is 17.8 degrees F',
                                      '0 degrees C is 32 degrees F',
                                      '40 degrees C is 104 degrees F',
                                      '40 degrees C is 4.4 degrees F',
                                      '12 degrees C is 53.6 degrees F',
                                      '24 degrees C is 75.2 degrees F',
                                      '100 degrees C is 37.8 degrees F']
                # Converter Main Screen GUI..
                self.converter_frame = Frame(width=300, height=300, bg=background_color,
                                             pady=10)
                self.converter_frame.grid()
