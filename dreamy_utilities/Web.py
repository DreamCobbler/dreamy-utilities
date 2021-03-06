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

# Application.

import dreamy_utilities.Configuration as Configuration
from dreamy_utilities.Text import Stringify

# Standard packages.

from requests import get, Session
from typing import Optional
from urllib.parse import urlparse

# Non-standard packages.

import cloudscraper
from bs4 import BeautifulSoup
import tldextract

#
#
#
# Constants.
#
#
#

DEFAULT_USER_AGENT = f"{Configuration.ApplicationName} {Configuration.ApplicationVersion}"
DEFAULT_TEXT_ENCODING = "utf-8"

#
#
#
# Functions.
#
#
#

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