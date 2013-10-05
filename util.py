import urllib, os

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
    return ''.join([x in r'\/:*?"<>|' and '_' or x for x in name])