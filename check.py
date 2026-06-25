
print('Введите название операции')
user_input_words_to_filter = input()
user_input_list = []

for word in user_input_words_to_filter.split(', '):
    user_input_list.append(word)

if len(user_input_list) > 1:
    print(type(user_input_list))
    print(user_input_list)
elif len(user_input_list) == 1:
    user_input_dict = ''.join(user_input_list)
    print(type(user_input_dict))
    print(user_input_dict)