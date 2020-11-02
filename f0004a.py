név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') 

kor = int(kor) 

mostani_év = 2020 - kor
print(név, ', kend ', mostani_év, '-ban született.', sep='')
