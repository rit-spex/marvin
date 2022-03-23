'''Get astronomy photos each day.

Authors: Stevie Alvarez
'''

import requests
import json

def getAPOD() -> str:
    """Get the Astronomy Photo of the Day (APOD) from NASA.

    Returns:
        Formatted string containing APOD stuff
    """
    response = requests.get("https://api.nasa.gov/planetary/apod?api_key=W8xVWTgcI545bXUBPyfaf8BlbTG2EcWdH2gRwhwa");
    d = json.loads(response.text)
    # title in bold-italics, explination in a multi-line code block
    apod = "***" + d["title"] + "\n" + "***" + d["hdurl"] + "\n```" + d["explanation"] + "```"
    return apod

if '__main__'==__name__:
    getAPOD()