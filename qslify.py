"""
qslify is a utility designed to dyanmically generate QSL cards from the command line, by API, or as
an AWS lambda.
By ThreeSixes <https://github.com/ThreeSixes> 27 Oct, 2020
"""

from lib import QslPdf

# If we're called from the CLI
if __name__ == "__main__":
    import argparse
    
    fields = {
        'address': '12345 NE Street St\nPlaceville, ST 55555',
        'callsign': 'AA1AAA',
        'tagline': 'QSL de Person Personly',
        'name': 'Person Personly',
        'qth': 'AA11bb',
        'qso_callsign': 'AB1BBB'
    }
    qslpdf = QslPdf({})
    qslpdf.create_file(fields)
