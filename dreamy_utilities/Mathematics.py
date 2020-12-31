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

from typing import Tuple

#
#
#
# Functions.
#
#
#

def GetDimensionsToFit(
    dimensions: Tuple[int, int],
    containerDimensions: Tuple[int, int]
) -> Tuple[int, int]:

    ##
    #
    # Proportionally scales a rectangle to fit inside another rectangle.
    #
    # @param dimensions          The dimensions of the rectangle.
    # @param containerDimensions The dimensions of the outside rectangle.
    #
    # @return A tuple containing new dimensions for the inside rectangle: (W, H).
    #
    ##

    width, height = dimensions

    if (not width) or (not height):
        return (0, 0)

    containerWidth, containerHeight = containerDimensions

    scale = min(
        containerWidth / width,
        containerHeight / height
    )

    return (
        int(scale * width),
        int(scale * height)
    )