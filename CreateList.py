import random
import json

Countries = ['Russia', 'England', 'France', 'Germany', 'Latvia', 'USA', 'Denmark', 'Croatia']
Names = ['Paul ', 'Serge ', 'Thomas ', 'Lutitia ', 'Gandalf ', 'Bilbo ', 'Saruman ']
Surnames = ['Black ', 'Ivanoff ', 'Maradonna ', 'Pele ', 'Ibragimovich ', 'Tretyak ']
Patronimics = ['Igorevich', 'Valerevich', 'Sergeevich', 'Israilevich', 'Petrovich']
Clubs = ['Akbars', 'Lokomotiv', 'Spartak', 'Alania']
Amplua = ['goalkeeper', 'defender', 'midfielder', 'striker']
random_players = [{'country': random.choice(Countries),
                   'NAME': random.choice(Names) + random.choice(Surnames) + random.choice(Patronimics),
                   'club': random.choice(Clubs),
                   'role': random.choice(Amplua),
                   'matches': random.randint(0, 10),
                   'goals': random.randint(-10, 10)} for _ in range(100000)]


with open('list_for_sort.txt', 'w') as fw:
    json.dump(random_players, fw)
