
with open('file_a.txt', 'r', encoding='utf-8') as file_a:
    data_of_a = file_a.read()

# remove (,.-; etc), make a lowercase
data_of_a = data_of_a.replace('.', ' ').replace(',', ' ').replace(':', ' ').casefold()

# creating a list and sort it
data_of_a = data_of_a.split()
data_of_a.sort()

# creating a list and count how many times word is in the file_a.
times_word = []
for word in data_of_a:
    number = data_of_a.count(word)
    times_word.append(number)

# using dictionary comprehension
dict = {data_of_a[i]: times_word[i] for i in range(len(data_of_a))}

#write result in file_b
with open('file_b.txt', 'w', encoding='utf-8') as file_b:
    for key in dict:
        print(f'{key} = {dict[key]}', file=file_b)



