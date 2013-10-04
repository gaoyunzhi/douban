import urllib, os

def wget(url):
    sock = urllib.urlopen(url)
    ret = sock.read()
    sock.close()
    return ret

def create_folder(path, name):
    folder = os.path.abspath(os.path.join(path, name))
    if not os.path.exists(folder):
        os.makedirs(folder)
    assert(os.path.exists(folder))
    return folder

def to_filename(name):
    return ''.join([x in r'\/:*?"<>|' and '_' or x for x in name])