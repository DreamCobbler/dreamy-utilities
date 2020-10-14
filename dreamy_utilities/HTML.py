####
#
# Dreamy Utilities
# Copyright (C) (2020) Benedykt Synakiewicz <dreamcobbler@outlook.com>
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