# Remove caracteres especiais de vários arquivos com textos em português
# Inclui "ç" e letras acentuadas
# Pega todos os arquivos de "source", remove os caracteres especiais
# e coloca o resultado na pasta "dest"

from os import listdir
from os.path import isfile, join

source = "C:\\Users\\thiag\\Documents\\arquivos_velhos\\"
source_encoding = "ANSI"

dest = "C:\\Users\\thiag\\Documents\\novos_arquivos"
dest_encoding = "ANSI"

def remove_spec_char(line):
    ret = []
    for i in range(len(line)-1):
        ret.append(line[i])
        if ret[-1] == 'ã' or ret[-1] == 'á' or ret[-1] == 'à' or ret[-1] == 'â':
            ret[-1] = 'a'
        elif ret[-1] == 'é' or ret[-1] == 'è' or ret[-1] == 'ê':
            ret[-1] = 'e'
        elif ret[-1] == 'î' or ret[-1] == 'í' or ret[-1] == 'ì':
            ret[-1] = 'i'
        elif ret[-1] == 'õ' or ret[-1] == 'ô' or ret[-1] == 'ò' or ret[-1] == 'ó':
            ret[-1] = 'o'
        elif ret[-1] == 'û' or ret[-1] == 'ü' or ret[-1] == 'ù' or ret[-1] == 'ú':
            ret[-1] = 'u'
        elif ret[-1] == 'ç':
            ret[-1] = 'c'
        elif ret[-1] == 'Ã' or ret[-1] == 'Á' or ret[-1] == 'À' or ret[-1] == 'Â':
            ret[-1] = 'A'
        elif ret[-1] == 'É' or ret[-1] == 'È' or ret[-1] == 'Ê':
            ret[-1] = 'E'
        elif ret[-1] == 'Î' or ret[-1] == 'Í' or ret[-1] == 'Ì':
            ret[-1] = 'I'
        elif ret[-1] == 'Õ' or ret[-1] == 'Ô' or ret[-1] == 'Ò' or ret[-1] == 'Ó':
            ret[-1] = 'O'
        elif ret[-1] == 'Û' or ret[-1] == 'Ü' or ret[-1] == 'Ù' or ret[-1] == 'Ú':
            ret[-1] = 'U'
        elif ret[-1] == 'Ç':
            ret[-1] = 'C'
    return ''.join(ret)

files = [f for f in listdir(source) if isfile(join(source, f))]

for file in files:
    with open(join(source, file), "r", encoding=source_encoding) as file_r:
        with open(join(dest, file), "w", encoding=dest_encoding) as file_w:
            lines = file_r.readlines()
            for line in lines:
                file_w.write(remove_spec_char(line) + '\n')
