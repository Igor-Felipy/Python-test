def change_files(filename, crytoFn, block_size=16):

    with open(filename, 'r+b') as _file:
        raw_Value = _file.read(block_size)
        while raw_Value:
            cipher_value = crytoFn(raw_Value)
            #compara o tamanho do bloco cifrado  e plano (plain text)
            if len(raw_Value) != len(cipher_value):
                raise ValueError('o valor cifrado {} tem um valor diferente do valor plano {}'.format(len(cipher_value), len(raw_Value)))
            _file.seek(-len(raw_Value), 1)
            _file.write(cipher_value)
            raw_Value = _file.read(block_size)
