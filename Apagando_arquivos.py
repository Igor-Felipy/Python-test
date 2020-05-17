import os # biblioteca para trabalhar com sistema operacional
import glob
import shutil # biblioteca para trabalhar com terminal

current_directory = os.path.dirname(os.path.abspath(__file__))

print(current_directory)

os.chdir('fakefolder') # entra na pasta
print(os.getcwd()) 

shutil.rmtree('local a ser apagado')

files = glob.glob('*.txt') # lista todos os arquivos com a extensão determinada
for file in files:
    print(file)
    os.unlink(file) # apaga arquivos

