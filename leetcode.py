licensePlate = "1s3 PSt"
words = ["step","steps","stripe","stepple"]

completing_letters = ''.join([char for char in licensePlate if char.isalpha()])
completing_letters = completing_letters.lower()

print(completing_letters)

charlist = list(completing_letters)

print(charlist)

dictionary = {}

for letter in charlist:
    if letter in dictionary:
        dictionary[letter] += 1
    else: 
        dictionary[letter] = 1

print(dictionary)

for word in words:
    copydictionary = dictionary.copy()
    listword = list(word)
    for char in listword:
        if char in copydictionary:
            copydictionary[char] -= 1
        total_sum = sum(copydictionary.values())
        if total_sum == 0:
            print(word)



    


print(dictionary)