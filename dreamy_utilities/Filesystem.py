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

import os
from os.path import expandvars, isfile
from pathlib import Path
import shutil
from string import ascii_letters, digits
import sys
from typing import List, Optional, Union
from uuid import uuid4

#
#
#
# Constants.
#
#
#

VALID_FILE_NAME_CHARACTERS = f"-',_.()[] {ascii_letters}{digits}"

#
#
#
# Functions.
#
#
#

def AddToPATH(path: Union[str, Path]) -> None:

    ##
    #
    # Adds a directory path to the PATH variable.
    #
    # @param path The directory path to be added.
    #
    ##

    if not path.is_dir():
        return

    sys.path.insert(0, str(path))

def CopyTree(sourceDirectoryPath: Path, destinationDirectoryPath: Path) -> None:

    ##
    #
    # Copies a directory, along with its contents.
    #
    # @param sourceDirectoryPath      The directory to be copied.
    # @param destinationDirectoryPath The directory in which the copy will be placed.
    #
    ##

    if not sourceDirectoryPath.is_dir():
        return

    destinationDirectoryPath.parent.mkdir(parents = True, exist_ok = True)

    shutil.copytree(sourceDirectoryPath, destinationDirectoryPath)

def FindExecutable(
    fileName: str,
    applicationName: Optional[str] = None,
    relativePath: Optional[str] = None
) -> Optional[Path]:

    ##
    #
    # Returns the absolute path to an executable.
    #
    # @param fileName        The name of the executable (without file name extension).
    #                        For example: "soffice".
    # @param applicationName The name of the application the executable belongs to.
    #                        For example: "LibreOffice".
    # @param relativePath    The relative path to the executable, inside the application's
    #                        directory. For example: "program".
    #
    # @return The absolute file path, or **None**.
    #
    ##

    path = shutil.which(fileName)
    if path:
        return Path(path)

    path = f"/usr/bin/{fileName}"
    if isfile(path):
        return Path(path)

    path = f"/bin/{fileName}"
    if isfile(path):
        return Path(path)

    localExecutablePath = f"{fileName}.exe"
    if relativePath:
        localExecutablePath = f"{relativePath}\\" + localExecutablePath
    if applicationName:
        localExecutablePath = f"{applicationName}\\" + localExecutablePath

    path = expandvars(f"%ProgramW6432%\\{localExecutablePath}")
    if isfile(path):
        return Path(path)

    path = expandvars(f"%ProgramFiles(x86)%\\{localExecutablePath}")
    if isfile(path):
        return Path(path)

    return None

def FindFiles(
    directoryPath: Optional[Union[str, Path]] = None,
    recursive: bool = True,
    suffixes: Optional[List[str]] = None
) -> List[Path]:

    ##
    #
    # Finds all the files in given directory.
    #
    # @param directoryPath The path to the directory. Optional.
    # @param recursive     Should we search the sub-directories as well?
    # @param suffixes      A list of accepted file name suffixes. Optional.
    #
    # @return A list of file paths.
    #
    ##

    # Process the directory path; set it to CWD if no path is provided.

    directoryPath = Path(directoryPath) if directoryPath else Path()

    # Find all files in the directory.

    searchExpression = "**/*" if recursive else "*"
    filePaths = [x for x in directoryPath.glob(searchExpression) if x.is_file()]

    # Process suffixes (make them all lowercase), then use them to filter the list of file paths.

    if suffixes:

        suffixes = [x.lower() for x in suffixes]
        filePaths = [x for x in filePaths if x.suffix.lower() in suffixes]

    # Return.

    return filePaths

def GetSanitizedFileName(string: str) -> str:

    ##
    #
    # Generates a valid file name from any string.
    #
    # @param string The input string.
    #
    # @return Sanitized input string.
    #
    ##

    return "".join(x for x in string if x in VALID_FILE_NAME_CHARACTERS)

def GetUniqueFileName() -> str:

    ##
    #
    # Generates a unique file name. Useful for creating temporary files.
    #
    # @return A unique file name.
    #
    ##

    return uuid4().hex

def ReadTextFile(
    filePath: Union[str, Path],
    lines: bool = False
) -> Union[Optional[str], Optional[List[str]]]:

    ##
    #
    # Reads the contents of a file to a string.
    #
    # @param filePath The file path.
    # @param lines    Should we return a list of lines?
    #
    # @return File contents - as either one long string, or a list of strings - or **None**.
    #
    ##

    try:

        # Process the file path.

        filePath = Path(filePath)

        if (not filePath) or not filePath.is_file():
            return None

        # Open and read the file.

        with open(filePath, "r", encoding = "utf-8") as file:
            return file.read() if (not lines) else file.readlines()

    except OSError:

        return None

def RemoveEmptyDirectories(directoryPath: Path) -> None:

    ##
    #
    # Removes all empty subdirectories within given directory.
    #
    # @param directoryPath The directory.
    #
    ##

    for path in [x for x in directoryPath.glob("*") if x.is_dir()]:

        if not len(os.listdir(path)):
            shutil.rmtree(path)

def WriteTextFile(filePath: Union[str, Path], content: str) -> bool:

    ##
    #
    # Writes a string to file, creating it or overwriting if necessary. The directory tree in which
    # the file is meant to reside will be created, if necessary.
    #
    # @param filePath The file path.
    # @param content  The file content.
    #
    # @return **True** if the file was written successfully, **False** otherwise.
    #
    ##

    try:

        # Process the file path.

        filePath = Path(filePath)

        if not filePath:
            return False

        # Create the directory tree.

        filePath.parent.mkdir(parents = True, exist_ok = True)

        # Write the file.

        with open(filePath, "w", encoding = "utf-8") as file:
            file.write(content)

        return True

    except OSError:

        return False