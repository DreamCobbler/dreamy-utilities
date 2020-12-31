####
#
# Dreamy Utilities
# Copyright (C) (2020 - 2021) Benedykt Synakiewicz <dreamcobbler@outlook.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
####

#
#
#
# Imports.
#
#
#

# Standard packages.

import html
import re
from typing import Optional

# Non-standard packages.

from bs4 import BeautifulSoup

#
#
#
# Functions.
#
#
#

def EscapeHTMLEntities(code: str) -> str:

    ##
    #
    # Escapes HTML entities in code.
    #
    # @param code The input code.
    #
    # @return The input code with HTML entities escaped.
    #
    ##

    if not code:
        return code

    code = UnescapeHTMLEntities(code)

    return html.escape(code)

def ReadElementText(soup: BeautifulSoup, tagName: str) -> Optional[str]:

    ##
    #
    # Returns the content of the first found element of given name.
    #
    # @param soup    The input tag soup.
    # @param tagName The name of the tag.
    #
    # @return The content of the found element, or **None**.
    #
    ##

    if (not soup) or (not tagName):
        return None

    element = soup.select_one(tagName)
    if not element:
        return None

    return element.get_text().strip()

def UnescapeHTMLEntities(code: str) -> str:

    ##
    #
    # Unescapes HTML entities.
    #
    # @param code The input code.
    #
    # @return The processed code.
    #
    ##

    if not code:
        return codde

    for entity in re.findall("&[a-z]+?;", code):
        code = code.replace(entity, entity.lower())

    return html.unescape(code)