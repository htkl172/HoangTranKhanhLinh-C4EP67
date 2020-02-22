quizzes = [
    {
        'Q': 'con nhen co may chan?',
        'Choices': [
            '3 chan',
            '6 chan',
            '4 chan',
            '8 chan',
        ],
        'right_answer': 3
    },
    {
        'Q': 'con cho co may chan?',
        'Choices': [
            '3 chan',
            '6 chan',
            '4 chan',
            '2 chan',
        ],
        'right_answer': 3
    },
]

for quiz in quizzes:
    print(quiz['Q'])
    choices = quiz['Choices']
    for i in range(len(choices)):
        print(f'{i+1}.{choices[i]}')
    user_choice = int(input('Moi ban chon cau tra loi dung: '))
    if user_choice == quiz['right_answer']:
        print('Ban gioi that!!')
    else:
        print('Ban sai roi :(')



# quiz = {
#     'Q': 'con nhen co may chan?',
#     'Choices': [
#         '3 chan',
#         '6 chan',
#         '4 chan',
#         '8 chan',
#     ],
#     'right_answer': 3,
# }
# print(quiz['Q'])
# choices = quiz['Choices']
# for i in range(len(choices)):
#     print(f'{i+1}.{choices[i]}') #string format
# user_choice = int(input('tra loi de: ')) - 1
# if user_choice == quiz['right_answer']:
#     print('ban gioi that!!')
# else:
#     print('ban sai mat roi :(')