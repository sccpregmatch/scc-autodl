#!/usr/bin/env python

"""

    SCC Auto-downloader v1
    Copyright (C) 2014  pregmatch

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
""" 

class configuration():
    
    # Scc RSS feed URL
    SCC_RSS_URL = ""
    
    # Files
    # File to store shows / movies to download
    TV_SHOW_FILE = "shows"
    # Folder to save downloaded torrents (torrent client watch folder)
    TORRENT_DOWNLOAD_DIR = "/path/to/watch/folder"
    # File to save names of releases downloaded (so they aren't downloaded again)
    TORRENT_ARCHIVE_FILE = "/path/to/archive/file"
    
    # Pushover API credentials
    PUSHOVER_ENABLED = False
    PUSHOVER_TOKEN = ""
    PUSHOVER_CLIENT_ID = ""
