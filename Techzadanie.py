# ТехЗадание!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Все отделы программы будут в общем проекте game_cards
# Вывод через print()
# Нужно оставлять заметки и использовать гитхаб

# ВОЗВРАЩЕНИЕ - команда return!

# НАПИСАНИЕ КОДА: Стандартный класс это КАРТА в который входит масть и значение
# Suit: Diamomd<Spade<Heart<Club = 1<2<3<4/ Value: Ace - 1> King - 13 > Queen - 12 > Jack - 11

# 1. Card который отсылает на карты и включает в себя масть и значение
# __init__ - инициализация данных
# __gt__ - сравнивает 2 карты, если нынешняя карта БОЛЬШЕ следующей возвратит True иначе False
# __eq__ - сравнивает карты если они равны, возвращает булиановое значение

# 2. DeckOfCards - 13 карт по 4 масти - 52 карты всео
# cards_shuffle - перемешивает карты(функция shuffle)
# __init__ инициализация
# deal_one - дает 1 карту, возвращает карту которую выдала

# 3. Player - имя, личная колода, и кол-во карт у игрока. Во время запуска новой игры кол-во карт будет 26.
# __init__ - имя игрока и кол-во карт, если карт больше 26 или меньше 10 то карт будет 26, колода будет выглядеть как пустой список
# set_hand - получает личную колоду класса DeckOfCards и раздает оттуда карты для игрока по тому количеству которое игрок должен получить, deal_one в помощь
# get_card - Вытаскивает карту из личной колоды и удаляет карту из колоды. Возвращает карту которую забрали

# 4 CardGame - пакет с DeckOfCards и 2 Player
# __init__ -  имя игрока и кол-во карт, если карт больше 26 или меньше 10 то карт будет 26
# new_game - метод который размешает пакет и раздает карты. Вызов метода только из конструктора Если метод был вызван во время то будет выведена ошибка
# get_winner - вернет игрока у которого больше карт. Если карт одинаковое количество то вернет None

# 5 Главная программа запишет имена игроков и начнет игру с 26 картами у каждого игрока. С началом игры выведет имя игрока и карты которые он получил
# КАК ИДЕТ ИГРА:
# 1. Будет 10 раундов 2. Во время каждого раунда игрок кидает 1 карту из колоды
# 3. Игрок с более сильной картой забирает обе карты со стола 4. Выведи карты которые были брошены и кто выиграл в раунде
# В конце игры выведи данные победителя, при ничье - выведи ничью

# UNIT TEST:
# 1. Нужно протестировать все классы
# 2. Нужно протестировать "крайние случаи"
# 3. Нужно проверить верные и неверные случаи (Valid\Invalid)
# 4. Нужно проверить случаи когда параметры функции не существуют
# 5. Нужно протестировать в том числе инициализацию (__init__)
# 6. Не нужно тестировать __str__ __repr__
# 7. Нужно использовать Mock когда внутри фунцкии запускается дополнительная функция
# 8. Во всех случаях неудачи - проверить если сам тест исправен, если проблема в коде то исправить и протестировать до успешного результата

#CONSTANTS:
SUITS = ['Diamomd', 'Spade', 'Heart', 'Club']
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
