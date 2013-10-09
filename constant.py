import re

USER = 'gyz' # change here for different user
ALBUM_DIR = '../..'
START_ITEM = 0
LIKEPAGE_URL = 'http://www.douban.com/people/%(USER)s/likes?start=' % locals()
MAX_ALBUM_NUMBER = 10 # need to change back when not testing
LIKEPAGE_ITEM = 15
ALBUMPAGE_ITEM = 18
START_TAG = '?start='
PHOTO_URL = 'http://img3.douban.com/view/photo/photo/public/p%s.jpg'

ALBUM_REG = re.compile(r'<a title="(.*)" href="(http://www.douban.com/photos/album/\d+/)" target="_self">')
LIKEITEM_REG = re.compile(r'<div class="fav-main">')
PHOTO_REG = re.compile(r'<a href="http://www.douban.com/photos/photo/(\d+)/" class="photolst_photo" title="(.*\n?.*)">')
# need to find good ways to deal with .*\n?.*