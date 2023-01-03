import pathlib
import zipfile

FILEPATH='file.txt'

def get_games(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        lista_local = file.readlines()
    return lista_local



def write_games(lista_local,filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(lista_local)

def make_archive(filepaths,dest_dir):
    dest_path=pathlib.Path(dest_dir,'compressed.zip')
    with zipfile.ZipFile(dest_path,'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath,arcname=filepath.name)

def parse(userinput):
    feet=float(userinput.split(' ')[0])
    inches=float(userinput.split(' ')[1])
    return feet,inches

def convertor(feet,inches):
    meters=feet*0.3048+inches*0.0254
    return meters
if __name__ == '__main__':
    parsed=parse('5 2')
    result=convertor(parsed[0],parsed[1])
    print(result)

def zip_archive(archivepath,destdir):
    with zipfile.ZipFile(archivepath,'r') as archive:
        archive.extractall(destdir)










