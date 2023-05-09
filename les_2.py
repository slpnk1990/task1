from random import randint

random = str(randint(100, 999))
digits = {random[0]: 1, random[1]:2, random[2]:3}

guess_flags = 0

for _ in range(10): # кол-во попыток
    digit_value = input('Введите число')
    position = int(input('Введите позицию'))
    
    if digit_value in digits:
        if position == digits[digit_value]:
            print('fermi')
            guess_flags |= 1<< (position - 1)
            if guess_flags == 0b111:
                print('WIN')
                exit()
        else:
            print('piko')
    else:
        print('bagels')
print('LOSE')
        
        
    