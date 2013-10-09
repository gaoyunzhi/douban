# -*- coding: utf8 -*-
from constant import ALBUM_DIR, START_ITEM, LIKEPAGE_URL, ALBUM_REG, \
    MAX_ALBUM_NUMBER, LIKEITEM_REG, LIKEPAGE_ITEM, START_TAG, ALBUMPAGE_ITEM, \
    PHOTO_REG, PHOTO_URL
from util import wget, create_folder, download_items
import re, time

class Downloader(object):
    ''' douban downloader for albums in your like page '''
    
    def __init__(self):
        self.albums_list = []
        self.filter = [] # empty filter matches all albums
        
    def add_filter(self, filter_list):
        self.filter.extend(filter_list)
        
    def __match_filter(self, url, album_name):
        if not self.filter: return True
        for filter_item in self.filter:
            if filter_item in url or filter_item in album_name:
                return True
        return False
    
    def auto(self):
        ''' automatically download all that matches filter '''
        self.__albums()
        for album_name, url in self.albums_list:  
            print 'starting', album_name   
            if not self.__match_filter(url, album_name):
                continue
            album_folder = create_folder(ALBUM_DIR, album_name)
            self.__download(url, album_folder)
        
    def __albums(self):
        ''' find all liked albums '''
        self.albums_list = []
        current_item = START_ITEM
        while current_item < MAX_ALBUM_NUMBER:
            current_page = wget(LIKEPAGE_URL + str(current_item))
            self.albums_list.extend(re.findall(ALBUM_REG, current_page))
            current_item += LIKEPAGE_ITEM
            if not re.search(LIKEITEM_REG, current_page): 
                break # break if there is no likeitem anymore

    def __download(self, url, album_folder):
        ''' download album in url to album_folder '''
        current_item = 0
        photo_list = [] 
        while True:
            current_page = wget(url + START_TAG + str(current_item))
            current_list = re.findall(PHOTO_REG,current_page)
            if not current_list: break
            photo_list.extend(current_list)
            current_item += ALBUMPAGE_ITEM
        photo_list = [(PHOTO_URL % x, y) for x, y in photo_list]
            # change id to url, need to refactor this shit
        download_items(photo_list, album_folder)
    
if __name__ == "__main__":
    D = Downloader()
    # D.add_filter([u'虎丘图册', u'再梦徽州'])
    D.auto()
    time.sleep(10) # give time to copy error message from terminal