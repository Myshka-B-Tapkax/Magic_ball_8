import random
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай", "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет", "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет", "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
print('Я магический шар, и я знаю ответ на любой твой вопрос.')

def n_u(name):
    return name.isalpha()


def name_user():
    while True:
        name = input("Как вас зовут? ")
        print()
        if n_u(name):
            return name
        print("Вы забыли имя?")


print("Здравствуй,", name_user())


def que(question_1):
    return question_1.lower() and question_1 == "да" or question_1 == "нет")


def que_user():
    while True:
        print()
        question_1 = input("У вас есть ещё вопрос? Напишите да/нет ")
        if que(question_1):
            return question_1
        print()
        print("Напишите только да или нет в нижнем регистре.")



no = "нет"

while True:
    print()
    question = input("Какой у вас вопрос? ")
    print(random.choice(answers))
    if que_user() == no:
        break

print()
print("Спасибо за участие в игре!")
