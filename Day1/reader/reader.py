import os
from reader.compress import bziptest, gziptest


extension_map = {
    'bz2':bziptest.opener,
    'gzip':gziptest.opener,
}


class Reader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.f = opener(filename, "rt")


    def close(self):
        self.f.close()

    def read(self):
        return(self.f.read())


def main():

    pass


if __name__ == '__main__':
    main()
    exit(0)