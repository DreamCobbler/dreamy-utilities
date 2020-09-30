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

# Add the package directory to the PATH variable.

import sys

sys.path.insert(0, "../")

# Application.

import dreamy_utilities.Interface

#
#
#
# The start-up routine.
#
#
#

interface = dreamy_utilities.Interface.Interface()

interface.Text("This is some text.")
interface.Comment("This is a comment.")
interface.Process("This is a process description.")
interface.Notice("This is a notice.")
interface.Error("This is an error.")
interface.LineBreak()
interface.EmptyLine()
interface.ProgressBar(55, 210, 40, "A progress bar", False)
interface.EmptyLine()
interface.Table(
    [
        ["A", "1"],
        ["B", "2"],
        ["C", "3"],
        ["D", "4"],
    ]
)