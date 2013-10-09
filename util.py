# -*- coding: utf8 -*-
import urllib, os, sys

def wget(url):
    ''' get webpage '''
    # any better idea to close the socket automatically?
    sock = urllib.urlopen(url)
    ret = sock.read()
    sock.close()
    return ret

def create_folder(path, name):
    ''' create folder, and return folder's absolute path '''
    name = to_filename(name)
    folder = os.path.abspath(os.path.join(path, name))
    if not os.path.exists(folder):
        os.makedirs(folder)
    assert(os.path.exists(folder))
    return folder

def to_filename(name):
    ''' replace '\/:*?"<>|' in filename with '_' '''
    # seems the trans function doesn't work here 
    # because we have unicode name
    # '\n' part not tested
    name = name.encode( sys.getfilesystemencoding() )
    name = ''.join([x in r'|\/:*?"<>'+'\r\n' and '_' or x for x in name])
    return name

def download_items(photo_list, album_folder):
    count = 0
    for url, name in photo_list:
        count += 1
        filename = to_filename(name)[:255]
        filepath = os.path.join(album_folder, filename + '.jpg')
        if not filename or os.path.exists(filepath):
            filename += str(count)
        filepath = os.path.join(album_folder, filename + '.jpg')
        try:
            urllib.urlretrieve(url, filepath) 
        except Exception, e:
            try:
                errcode = str(e.code)
            except:
                errcode = 'None'
            print 'download failed for url = %(url)s, filename = %(filename)s' % locals()
            print 'with error code = %(errcode)s, because of error %(e)s' % locals()
            print '='.join([x for x in filename])
