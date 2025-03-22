data = ['Ayam bakar', 'ayam goreng','ayam KFC','teritip']
index = 3
for tanggal in range(1,100):
    if tanggal % 7 == 0:
        print(f'tranggal {tanggal} libur')
        print(len('libur'))
        continue
    elif tanggal == 32:
        break 

    print(f'tanggal {tanggal} makan {data[index]}')
    print(len(data[index]))
    index +=1 
    if index >3:
        index = 0