letter = str(input('Please type in your letter: '))
if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
    print(f'The letter {letter} is a vowel.')
elif letter in ['y', 'Y']:
    print(f'The letter {letter} is only sometimes a vowel and sometimes a consanant.')
    print('For more information, visit: https://english.stackexchange.com/questions/10458/when-is-y-a-vowel')
else:
    print(f'The letter {letter} is a consanant.')