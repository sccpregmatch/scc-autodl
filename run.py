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

from configuration import configuration
from base import scc

# Create SCC object
scc = scc()

feed = scc.parse(configuration.SCC_RSS_URL)

# Loop through feed entries
for f in feed.entries:
    # Check Feed Title against TV show Title list
    title = scc.replace(f.title)
    # If title in feed download
    if scc.search(title):
        url = f.links[0]['href']
        # Download
        scc.download(url, f.title)