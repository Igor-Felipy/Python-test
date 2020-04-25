import os

def discover(initial_path):


    extensions = [
        # 'exe,', 'dll', 'so', 'rpm, 'deb', 'vmlinux', 'img' #ARQUIVOS DO SISTEMA
        'jpg', 'jpeg', 'gif', 'png', 'avg', 'psd', 'raw',  # IMAGENS
        'mp3', 'mp4', 'm4a', 'aac', 'ogg', 'flac', 'wav', 'wma', 'aiff', 'ape',  # AUDIO
        'avi', 'fiv', 'm4v', 'mkv', 'nov', 'mpg', 'mpeg', 'vmv', 'swf', '3gp',  # VIDEO
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',  # MICROSOFT OFFICE
        # OpeOffice, Adobe, Latex, Markdown, etc
        'odt', 'odp', 'ods', 'txt', 'rtf', 'text', 'pdf', 'epub', 'md', 'yml', 'yaml', 'json', 'xml', 'csv',
        # DADOS ESTRUTURADOS E CONFIG
        'db', 'sql', 'dbf', 'mdb', 'iso',  # BANCO DE DADOS E IMAGENS DE DISCO

        'html', 'htm', 'xhtml', 'php', 'asp', 'aspx', 'js', 'jsp', 'css',  # TECNOLOGIA WEB
        'c', 'cpp', 'cxx', 'h', 'hpp', 'hxx',  # CODIGO FONTE C E C++
        'java', 'class', 'jar',  # CODIGOS FONTE JAVA
        'ps', 'bat', 'vb',  # SCRIPTS DE SISTEMAS WINDOWS
        'awk', 'sh', 'cgi', 'pl', 'ada', 'swift',  # SCRIPTS DE SISTEMAS UNIX
        'go', 'py', 'pyc', 'bf', 'coffee',  # OUTROS CODIGOS FONTE

        'zip', 'tar', 'tgz', 'bz2', '7z', 'rar', 'bak',  # ARQUIVOS COMPACTOS E BACKUPS
    ]


    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolute_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolute_path.split('.')[-1]
            if ext in extensions:
                yield absolute_path

if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)
 