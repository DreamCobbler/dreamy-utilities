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

from requests import Session
from typing import Optional
from urllib.parse import urlparse

# Non-standard packages.

from bs4 import BeautifulSoup
import tldextract

#
#
#
# Functions.
#
#
#

def DownloadPage(URL: str, session: Optional[Session] = None) -> Optional[str]:

    ##
    #
    # Downloads a webpage and returns its code.
    #
    # @param URL     The URL.
    # @param session The Session object to be used for the download.
    #
    # @return The code of the downloaded page. **None**, if an error has occurred.
    #
    ##

    if not URL:
        return None

    response = session.get(URL) if session else requests.get(URL)
    if not response:
        return None

    return Stringify(response.content)

def DownloadSoup(
    URL: str,
    session: Optional[Session] = None,
    parser: str = "html.parser"
) -> Optional[BeautifulSoup]:

    ##
    #
    # Downloads a webpage and returns it as a soup of tags.
    #
    # @param URL     The URL.
    # @param session The Session object to be used for the download.
    # @param parser  The HTML parser to be used.
    #
    # @return The tag soup. **None**, if an error has occurred.
    #
    ##

    code = DownloadPage(URL, session)
    if not code:
        return None

    return BeautifulSoup(code, parser)

def GetHostname(URL: str) -> str:

    ##
    #
    # Retrieves hostname from a URL ("protocol://a.b.com/1/2/3/" returns "b.com").
    #
    # @param URL The URL.
    #
    # @return The hostname extracted from the input URL.
    #
    ##

    if not URL:
        return URL

    parts = tldextract.extract(URL)

    return f"{parts.domain}.{parts.suffix}"

def GetSiteURL(URL: str) -> str:

    ##
    #
    # Returns the URL to the main site ("protocol://a.b.com/1/2/3/" returns "protocol://a.b.com").
    #
    # @param URL The URL.
    #
    # @return The URL to the main site.
    #
    ##

    if not URL:
        return URL

    URL = urlparse(URL)

    return f"{URL.scheme}://{URL.netloc}"