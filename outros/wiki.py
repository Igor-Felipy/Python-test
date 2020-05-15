import wikipedia as wp

while True:
    pesq = input('Faça sua busca: ')
    l = wp.search(pesq)
    for i in l:
        wp.summary(i, sentences=1)
        print('='*20)
        print(wp.summary(i, sentences=1))
        print('='*20)
        