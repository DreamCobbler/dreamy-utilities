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

from getpass import getpass
import os
from typing import List, Optional, Tuple

# Non-standard packages.

import colorama
import termtables

#
#
#
# Classes.
#
#
#

##
#
# Represents textual user interface.
#
##

class Interface:

    def __init__(self) -> None:

        ##
        #
        # The constructor.
        #
        ##

        colorama.init()

    def GrabUserAttention(self) -> None:

        ##
        #
        # Attempts to grab the user's attention by making a "beep" sound. (On Windows it also makes
        # the taskbar button flash.)
        #
        ##

        print("\a")

        if "nt" == os.name:

            import ctypes

            ctypes.windll.user32.FlashWindow(
                ctypes.windll.kernel32.GetConsoleWindow(),
                True
            )

    def ReadString(
        self,
        description: str,
        options: Optional[List[str]] = None,
        default: Optional[str] = None
    ) -> str:

        ##
        #
        # Reads a string value from the uer.
        #
        # @param description The question asked.
        # @param options     The available answers.
        # @param default     The default value.
        #
        # @return Read value.
        #
        ##

        if options:

            optionsDescription = "/".join(options)
            readValue = input(f"@ {description} ({optionsDescription}) [{default}]: ")

            return readValue if (readValue in options) else default

        else:

            readValue = input(f"@ {description}: ")

            return readValue

    def ReadPassword(self, description: str) -> str:

        ##
        #
        # Reads a password from the uer.
        #
        # @param description The description.
        #
        # @return Read password.
        #
        ##

        return getpass(prompt = f"@ {description}: ")

    def Text(
        self,
        text: str,
        section: bool = False,
        clearLine: bool = False,
        end: str = "\n",
        color: Optional[str] = None,
        bold: bool = False
    ) -> None:

        ##
        #
        # Prints a line of text.
        #
        # @param text      The text to be printed.
        # @param section   Should we print an empty line before this text?
        # @param clearLine Should we clear the current line before printing?
        # @param end       The string printed immediately after the given text.
        # @param color     The color of the text.
        # @param bold      Should the printed text be bold?
        #
        ##

        if clearLine:
            self.ClearLine()

        if section:
            self.EmptyLine()

        print(
            self._GetFormattedText(text, color, bold),
            end = end
        )

    def Comment(
        self,
        text: str,
        section: bool = False,
        clearLine: bool = False,
        end: str = "\n"
    ) -> None:

        ##
        #
        # Prints a comment.
        #
        # @param text      The text to be printed.
        # @param section   Should we print an empty line before this text?
        # @param clearLine Should we clear the current line before printing?
        # @param end       The string printed immediately after the given text.
        #
        ##

        self.Text(f"# {text}", section, clearLine, end)

    def Process(
        self,
        text: str,
        section: bool = False,
        clearLine: bool = False,
        end: str = "\n"
    ) -> None:

        ##
        #
        # Prints a description of an ongoing process.
        #
        # @param text      The text to be printed.
        # @param section   Should we print an empty line before this text?
        # @param clearLine Should we clear the current line before printing?
        # @param end       The string printed immediately after the given text.
        #
        ##

        self.Text(f"> {text}", section, clearLine, end, color = "cyan", bold = True)

    def Error(
        self,
        text: str,
        section: bool = False,
        clearLine: bool = False,
        end: str = "\n"
    ) -> None:

        ##
        #
        # Prints an error of an ongoing process.
        #
        # @param text      The text to be printed.
        # @param section   Should we print an empty line before this text?
        # @param clearLine Should we clear the current line before printing?
        # @param end       The string printed immediately after the given text.
        #
        ##

        self.Text(f"! {text}", section, clearLine, end, color = "red")

    def Notice(
        self,
        text: str,
        section: bool = False,
        clearLine: bool = False,
        end: str = "\n"
    ) -> None:

        ##
        #
        # Prints some optional information.
        #
        # @param text      The text to be printed.
        # @param section   Should we print an empty line before this text?
        # @param clearLine Should we clear the current line before printing?
        # @param end       The string printed immediately after the given text.
        #
        ##

        self.Text(f"! Notice: {text}", section, clearLine, end, color = "green")

    def EmptyLine(self) -> None:

        ##
        #
        # Prints an empty line.
        #
        ##

        print()

    def ClearLine(self) -> None:

        ##
        #
        # Clears the current line.
        #
        ##

        print("\r", end = "")

    def LineBreak(self) -> None:

        ##
        #
        # Prints a line break.
        #
        ##

        self.Text(
            79 * "-",
            section = True,
            color = "cyan"
        )

    def ProgressBar(
        self,
        progress: int,
        total: int,
        length: int,
        description: str,
        clearLine: bool = True
    ) -> None:

        ##
        #
        # Prints a progress bar.
        #
        # @param progress    Current progress.
        # @param total       The maximum value of progress.
        # @param length      The length of the progress bar.
        # @param description The description.
        # @param clearLine   Should we clear the line before printing?
        #
        ##

        if clearLine:
            self.ClearLine()

        proportion = float(progress) / float(total)

        filledPart = int(proportion * length)
        remainingPart = length - filledPart

        bar = (filledPart * "█") + (remainingPart * "-")

        print(f"{description}: |{bar}|", end = "")

    def Table(
        self,
        data: List[List[str]],
        padding: Tuple[int, int] = (0, 1),
        alignment: str = "rl"
    ):

        termtables.print(
            data,
            style = termtables.styles.thin,
            padding = padding,
            alignment = alignment
        )

    @staticmethod
    def _GetColorMarker(
        color: str
    ) -> str:

        ##
        #
        # Returns a color marker for given color.
        #
        # @param color The name of the color.
        #
        # @return The color marker.
        #
        ##

        if color not in Interface._COLORS:
            return Interface._GetColorMarker("reset")

        return f"\u001b[{str(Interface._COLORS[color])}m"

    @staticmethod
    def _GetFormattedText(
        text: str,
        color: Optional[str] = None,
        bold: bool = False
    ) -> str:

        ##
        #
        # Formats text in a given way.
        #
        # @param text  The text to be formatted.
        # @param color The color of the text.
        # @param bold  The weight of the text.
        #
        # @return A formatted string, ready for printing.
        #
        ##

        if color:
            text = Interface._GetTextMarker(color) + text

        if bold:
            text = Interface._GetTextMarker("bold") + text

        text += Interface._GetTextMarker("reset")

        return text

    @staticmethod
    def _GetTextMarker(
        marker: str
    ) -> str:

        ##
        #
        # Returns an ANSI text formatting marker.
        #
        # @param marker The name of the marker.
        #
        # @return The marker.
        #
        ##

        if marker not in Interface._MARKERS:
            return Interface._GetTextMarker("reset")

        return f"\u001b[{str(Interface._MARKERS[marker])}m"

    _MARKERS = {
        "reset"  : 0 ,
        "bold"   : 1 ,
        "black"  : 30,
        "red"    : 31,
        "green"  : 32,
        "yellow" : 33,
        "blue"   : 34,
        "magenta": 35,
        "cyan"   : 36,
        "white"  : 37,
    }