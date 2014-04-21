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
import feedparser
import re
import requests
import pushover

class scc(object):
    def __init__(self):
            self.tvshows = self.tvlist(configuration.TV_SHOW_FILE)

    def parse(self, url):
        feed = feedparser.parse(url)
        
        return feed
    
    def tvlist(self, file):
        with open(file) as f:
            lines = f.read().splitlines()
            
        return lines    
    
    def replace(self, title):
        a = re.sub('[.-]', ' ', title)
        
        return a
        
    def search(self, title):
        for t in self.tvshows:
            m = re.search(t, title, re.IGNORECASE)
            if m:
                return True

    def allowdl(self, title):
        downloadedfile = open(configuration.TORRENT_ARCHIVE_FILE)
        downloadedlist = downloadedfile.readlines()
        downloadedfile.close()
        for line in downloadedlist:
            if title in line:
                return False
        
        return True        
    
    def writefile(self, file, type, content, title):
        write = open(file, type)
        write.write("{}\n".format(content))
        write.close()
    
    def download(self, url, title):
        r = requests.get(url)
        
        if self.allowdl(title):
            # Write Torrent to file
            self.writefile("{}{}.torrent".format(configuration.TORRENT_DOWNLOAD_DIR, title), "w", r.content, title)
            
            # Write Torrent name to archive
            self.writefile(configuration.TORRENT_ARCHIVE_FILE, "ab+", title, title)

            # Send Pushover notification
            if configuration.PUSHOVER_ENABLED:
                self.pushover(title)
                  
    def pushover(self, title):
        pushover.init(configuration.PUSHOVER_TOKEN)
        client = pushover.Client(configuration.PUSHOVER_CLIENT_ID)
        client.send_message(title, title=title, priority=1)