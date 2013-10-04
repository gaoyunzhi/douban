# -*- coding: utf8 -*-
from constant import ALBUM_DIR, START_ITEM, LIKEPAGE_URL, ALBUM_REG, \
    MAX_ALBUM_NUMBER, LIKEITEM_REG, LIKEPAGE_ITEM, START_TAG, ALBUMPAGE_ITEM, \
    PHOTO_REG, PHOTO_URL
from util import wget, create_folder, to_filename
import re, time, os, urllib

class Downloader(object):
    def __init__(self):
        self.albums_list = []
        self.filter = []
        
    def addfilter(self, filter_list):
        self.filter.extend(filter_list)
        
    def match_filter(self, url, album_name):
        if not self.filter: return True
        for filter_item in self.filter:
            if filter_item in url or filter_item in album_name:
                return True
        return False
    
    def auto(self):
        self.albums()
        for album_name, url in self.albums_list:           
            if not self.match_filter(url, album_name):
                continue
            album_name = create_folder(ALBUM_DIR, to_filename(album_name))
            self.download(url, album_name)
        
    def albums(self):
        self.albums_list = []
        current_item = START_ITEM
        while current_item < MAX_ALBUM_NUMBER:
            current_page = wget(LIKEPAGE_URL + str(current_item))
            self.albums_list.extend(re.findall(ALBUM_REG, current_page))
            current_item += LIKEPAGE_ITEM
            if not re.search(LIKEITEM_REG, current_page): 
                break # break if there is no likeitem anymore

    def download(self, url, album_name):
        current_item = 0
        photo_list = [] 
        while True:
            current_page = wget(url + START_TAG + str(current_item))
            current_list = re.findall(PHOTO_REG,current_page)
            if not current_list: break
            photo_list.extend(current_list)
            current_item += ALBUMPAGE_ITEM
        for photo_id, name in photo_list:
            try:
                url = PHOTO_URL % photo_id
                filename = os.path.join(album_name, to_filename(name) + '.jpg')
                urllib.urlretrieve(url, filename) 
            except Exception, e:
                print 'download failed for url = %(url)s, filename = %(filename)s, because of error %(e)s' % locals()
            
            
            
                   


D = Downloader()
D.addfilter([u'虎丘图册', u'再梦徽州'])
D.auto()
time.sleep(10)