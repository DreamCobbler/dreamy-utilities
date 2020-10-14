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

from requests import get, Session
from typing import Optional

# Non-standard packages.

from bs4 import BeautifulSoup

#
#
#
# Classes.
#
#
#

##
#
# A parsed URL (one that has been split into parts).
#
##

class ParsedURL:

    def __init__(self, URL: str) -> None:

        ##
        #
        # The constructor.
        #
        # @param URL The URL to be parsed.
        #
        ##

        self.Protocol = None
        self.Subdomain = None
        self.Domain = None
        self.Suffix = None

        self._Parse(URL)

    def _Parse(self, URL: str) -> None:

        ##
        #
        # Splits the given URL into components.
        #
        # @param URL The URL in question.
        #
        ##

        if not URL:
            return

        # Extract the protocol.

        separator = "://"
        position = URL.find(separator)

        if -1 != position:

            self.Protocol = URL[:position]
            URL = URL[position + len(separator):]

        else:

            self.Protocol = "http"

        # Remove the trailing part.

        separator = "/"
        position = URL.find(separator)

        if -1 != position:

            URL = URL[:position]

        # Extract the suffix.

        separator = "."
        position = URL.rfind(separator)

        if -1 != position:

            self.Suffix = URL[position + len(separator):]
            URL = URL[:position]

        # Extract the domain.

        separator = "."
        position = URL.rfind(separator)

        if -1 != position:

            self.Domain = URL[position + len(separator):]
            URL = URL[:position]

        else:

            self.Domain = URL
            URL = None

        # Extract the subdomain.

        if URL:

            self.Subdomain = URL

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

    response = session.get(URL) if session else get(URL)
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

    parts = ParsedURL(URL)

    return f"{parts.Domain}.{parts.Suffix}"

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

    parts = ParsedURL(URL)

    if parts.Subdomain:
        return f"{parts.Protocol}://{parts.Subdomain}.{parts.Domain}.{parts.Suffix}"
    else:
        return f"{parts.Protocol}://{parts.Domain}.{parts.Suffix}"