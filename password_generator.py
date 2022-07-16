from random import sample


characters = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

letter_num = int(input('How many letters do you want?'))

generated_password = ''.join(sample(characters, letter_num))

print(generated_password)
