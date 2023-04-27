import animedata 
import tree

genre_string = ""
for letter, genre in animedata.genres_choices.items():
    genre_string += f"{letter} - {genre}\n"


def show_genres():
    print(genre_string)


def greeting():
    print("Welcome to Bruce's Favorite Anime Suggester~!")
    print("This software is to recommend you some of the best anime from Bruce's favourite:\n" + genre_string)


def body(root):
    while True:
        input_genre = input("What kind of anime would you like to watch?\nType in the corresponding letter (a - j): ").lower()
        if input_genre in animedata.genres_choices:
            print(f"Got it! You would like to have recommendations for {animedata.genres_choices[input_genre]} Anime.\n")
            break
        else:
            print('Sorry. Invalid Input.\nPlease try again.\n')
    target_node = None
    for child in root.children:
        if child.value == animedata.genres_choices[input_genre]:
            target_node = child
            break
    if not target_node:
        print("Sorry, no recommendations found for this genre.")
    else:
        anime_data = [child.value for child in target_node.children]
        tree.display_anime(anime_data)
    
    while True:
        again = input("Would you like to see another genre? Enter y/n: ").lower()
        if again == 'y':
            show_genres()
            body(root)
        elif again == 'n':
            break
        else:
            print("Sorry. Invalid Input.\nPlease try again.")


def recommendation_search():
    greeting()
    root = tree.build_tree(animedata.anime_data)
    body(root)
    goodbye()


def goodbye():
  print("Thanks for using Bruce's Favorite Anime Suggester!")

recommendation_search()