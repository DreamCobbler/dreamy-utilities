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

# Application.

from dreamy_utilities.Text import Stringify

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

def DownloadPage(URL: str) -> Optional[str]:

    ##
    #
    # Downloads a webpage and returns its code.
    #
    # @param URL The URL.
    #
    # @return The code of the downloaded page. **None**, if an error has occurred.
    #
    ##

    if not URL:
        return None

    response = requests.get(URL)
    if not response:
        return None

    return Stringify(response.content)

def DownloadSoup(URL: str, parser: str = "html.parser") -> Optional[BeautifulSoup]:

    ##
    #
    # Downloads a webpage and returns it as a soup of tags.
    #
    # @param URL The URL.
    #
    # @return The tag soup. **None**, if an error has occurred.
    #
    ##

    code = DownloadPage(URL)
    if not code:
        return None

    return BeautifulSoup(code, parser)