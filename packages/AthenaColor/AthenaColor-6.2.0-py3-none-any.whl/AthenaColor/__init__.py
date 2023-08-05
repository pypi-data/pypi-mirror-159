# ----------------------------------------------------------------------------------------------------------------------
# - All -
# ----------------------------------------------------------------------------------------------------------------------
# This "__all__" is in a permanent structure.
#   Things can be added (and probably will) in future releases
#   Nothing should ever be removed from this list, once something is added in a full version

__all__ = [
    "color_tuple_conversion","color_object_conversion",
    "RGB","RGBA","HEX","HEXA","HSV","HSL","CMYK",
    "Fore","Back","Underline","Style","Basic",
    "ForeNest","BackNest","UnderlineNest","StyleNest","BasicNest"
]
# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
import AthenaColor.data.colors_html as HtmlColorObjects
from AthenaColor.data.style import Style, StyleNest, Basic, BasicNest
from AthenaColor.data.bodies import Fore, ForeNest, Back, BackNest, Underline, UnderlineNest

from AthenaColor.models.color_system import RGB, RGBA, HEX, HEXA, HSV, HSL, CMYK

import AthenaColor.func.color_tuple_conversion as color_tuple_conversion
import AthenaColor.func.color_object_conversion as color_object_conversion

# apply the fix, so that in windows the colors are shown correctly
from AthenaColor.func.general import fix_console as _fix_console
_fix_console()