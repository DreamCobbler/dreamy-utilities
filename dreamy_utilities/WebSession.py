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
from typing import Optional, Union

# Non-standard packages.

from bs4 import BeautifulSoup
import cloudscraper

#
#
#
# Constants.
#
#
#

DEFAULT_TEXT_ENCODING = "utf-8"
DEFAULT_TAG_PARSER = "html.parser"

#
#
#
# Classes.
#
#
#

##
#
# Represents a web session.
#
##

class WebSession:

    def __init__(
        self,
        userAgent: str = "",
        useCloudscraper: bool = False
    ) -> None:

        ##
        #
        # The constructor.
        #
        # @param userAgent       The user-agent to be used.
        # @param useCloudscraper Should the cloudscraper be used instead of ordinary session?
        #
        ##

        self._userAgent = userAgent
        self._session = cloudscraper.CloudScraper() if cloudscraper else Session()

    def Get(
        self,
        URL: str,
        text: bool = True,
        textEncoding: str = DEFAULT_TEXT_ENCODING,
        stream: bool = False
    ) -> Optional[Union[bytes, str]]:


        ##
        #
        # Retrieves data using a GET request.
        #
        # @param URL          The URL.
        # @param text         Should the response be converted to text?
        # @param textEncoding The text encoding to be used during the conversion.
        # @param stream       Read data stream.
        #
        # @return Retrieved response (as *bytes* or *str*), or **None**.
        #
        ##

        # Prepare the headers.

        requestHeaders = {
            "User-Agent": self._userAgent
        }

        # Send the request.

        response = self._session.get(URL, headers = requestHeaders, stream = stream)
        if (not response) or (200 != response.status_code):
            return None

        # Process the response.

        data = Stringify(response.content, encoding = textEncoding) if text else response.content

        # Return.

        return data

    def Post(
        self,
        URL: str,
        payload,
        text: bool = True,
        textEncoding: str = DEFAULT_TEXT_ENCODING
    ) -> Optional[Union[bytes, str]]:


        ##
        #
        # Posts some data and receives the response.
        #
        # @param URL          The URL.
        # @param payload      The data to be posted.
        # @param text         Should the response be converted to text?
        # @param textEncoding The text encoding to be used during the conversion.
        #
        # @return Retrieved response (as *bytes* or *str*), or **None**.
        #
        ##

        # Prepare the headers.

        requestHeaders = {
            "User-Agent": self._userAgent
        }

        # Send the request.

        response = self._session.post(URL, headers = requestHeaders, data = payload)
        if (not response) or (200 != response.status_code):
            return None

        # Process the response.

        data = Stringify(response.content, encoding = textEncoding) if text else response.content

        # Return.

        return data

    def GetSoup(
        self,
        URL: str,
        parser: str = DEFAULT_TAG_PARSER
    ) -> Optional[BeautifulSoup]:


        ##
        #
        # Retrieves tag soup using a GET request.
        #
        # @param URL    The URL.
        # @param parser The tag parser to be used.
        #
        # @return Retrieved tag soup, or **None**.
        #
        ##

        # Get the data.

        data = self.Get(URL)
        if not data:
            return None

        # Create the tag soup.

        soup = BeautifulSoup(data, features = parser)

        # Return.

        return soup