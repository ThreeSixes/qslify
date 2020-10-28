"""
This file is part of the qslify project.
By ThreeSixes <https://github.com/ThreeSixes> 27 Oct, 2020
"""

from pprint import pprint

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib import pagesizes


class QslPdf:
    def __init__(self, config):
        """
        """

        self.__canvas = None
        self.__config = config


    def __setup(self):
        """
        Take our incoming configuration and translate options to
        ones directly usable by our libraries.
        """

        pass


    def __create_canvas(self, canvas_config):
        """
        Create our PDF canvas given a configuration.
        """
        self.__canvas = Canvas(
            canvas_config['filename'], pagesize=pagesizes.LETTER)


    def __add_callsign(self, callsign, size=48, location=(1 * inch, 9.5 * inch),
                       color=colors.blue):
        """
        Add the source callsign to the canvas.
        """

        self.__draw_text(callsign, location, size, color=color, font="Helvetica-Bold")


    def __add_tagline(self, tagline, size=20, location=(1 * inch, 9.1 * inch),
                       color=colors.red):
        """
        Add the tagline to the canvas.
        """

        self.__draw_text(tagline, location, size, color=color, font="Helvetica-Bold")


    def __create_card(self, fields, filename):
        """
        Create our QSL card.
        """

        canvas_config={'filename': filename}
        location = (1 * inch, 9.5 * inch)

        self.__create_canvas(canvas_config)

        self.__add_callsign(fields['callsign'])
        self.__add_tagline(fields['tagline'])

        self.__canvas.save()


    def __draw_text(self, text, location, size_pt, color=None, font="Helvetica"):
        """
        Draw text on our canvas.
        """

        if color is not None:
            self.__canvas.setFillColor(color)
        
        self.__canvas.setFont(font, size_pt)
        self.__canvas.drawString(location[0], location[1], text)


    def create_file(self, fields, file_name=None):
        """
        Create the QSL card PDF given the card information.
        """

        self.__setup()

        self.__create_card(fields, "hello-world.pdf")


