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

from typing import Any, List

#
#
#
# Functions.
#
#
#

def RemoveDuplicates(input: List[Any]) -> List[Any]:

    ##
    #
    # Removes duplicates from a list, preserving item order.
    #
    # @param input A list.
    #
    # @return The same list, with duplicates removed.
    #
    ##

    return list(dict.fromkeys(input))