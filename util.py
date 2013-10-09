# -*- coding: utf8 -*-
import urllib, os, sys, time

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
    # shit here, fix!
    name = name.encode('utf8')
    name = name.decode('utf8')[:255]
    name = ''.join([x in r'|\/:*?"<>・'+'\r\n' and ' ' or x for x in name])
    name = name.encode( sys.getfilesystemencoding() )   
    return name

def download_items(photo_list, album_folder):
    count = 0
    for url, name in photo_list:
        count += 1
        filename = to_filename(name)
        
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
            filename = filename.decode(sys.getfilesystemencoding())
            print '='.join([x for x in filename])
        
