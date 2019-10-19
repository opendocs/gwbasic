import glob


def fix_charset(path):
    with open(path, 'rb') as f:
        html = f.readlines()
    html[0] = (b'<!DOCTYPE html>\r\n<html>\r\n')
    html[4] = (b'<meta http-equiv="Content-Type" content="text/html; '
               b'charset=ISO-8859-1">\r\n</head>\r\n')
    html = b''.join(html)
    with open(path, 'wb') as f:
        f.write(html)


def main():
    for path in glob.glob('man/*.html'):
        if path.endswith('index.html'):
            print('Ignoring', path, '...')
            continue
        fix_charset(path)


if __name__ == '__main__':
    main()
