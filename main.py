# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Saraksti - https://www.w3schools.com/python/python_lists.asp
# Vārdnīcas - https://www.w3schools.com/python/python_dictionaries.asp
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git

import json
films = []
films_file = open('films.json') # opening JSON file
films = json.load(films_file) # returns JSON object as a dictionary
films_file.close() # Closing file
print("1. Enter the name and the rating of the film")
print("2. Delete the film")
print("3. Print films")
print("4. Sort if the film was watched")
print("5. Sort if the film was not watched")
print("6. Sort by rating")
print("7. Clear the list")
print("8. Search the film by name")
print("9. Exit")
while True: 
    command = input("\nChoose command:")
    if command == "1": # we
        while True:#We check if the name is written correctly
            film_name = input("Enter the name of the film: ")
            if len(film_name) >= 2 and len(film_name) <= 120:#If everything is written correctly, we break the loop
                break
            else:  #If not, we repeat our question
                print("The name must be between 2 and 120 characters")
                pass
        while True: #We check if the rating is written correctly
            film_rat = int(input("Enter the rating of the film: "))
            if film_rat.isinstance() == True and film_rat >= 1 and film_rat <=10: #If everything is written correctly, we break the loop
                break 
            else:#If not, we repeat our question
                print("The rating must be a whole number and must be between 1 and 10")
        film_watched = input("Have you already watched that film? y/n: ")

        film = {"name":film_name, 
                    "rat": film_rat,
                    "watched": film_watched
                    }
        films.append(film)
        print(films)
        pass
    elif command == "2":
        film_delete = input("Enter the name of the film to delete it: ")
        for i in range(len(films)): #We are checking every element of the list 
            if films[i]['name'] == film_delete: #If we find it, we delete it
                del films[i]
                break
 
        print(films)
    elif command == "3":
        print(films)
        pass
    elif command == "4":
        watched_films = []
        for i in range(len(films)): #We are checking every element of the list for watched ones
            if films[i]['watched'] == 'y': #If we find it, we add it to the list
                watched_films.append(films[i])
        print(watched_films)
        pass
    elif command == "5":
        not_watched_films = []
        for i in range(len(films)):#We are checking every element of the list for unwatched ones
            if films[i]['watched'] == 'n': #If we find it, we add it to the list
                not_watched_films.append(films[i])
        print(not_watched_films)
        pass
    elif command == "6":
        def custom_sort(films): #Custom sort function
            return int(films['rat'])  

        sorted_films = sorted(films, key=custom_sort, reverse=True)
        for i in sorted_films[:10]:
            print(i) 
    elif command == "7":
        films.clear()
        print(films)
    elif command == "8":
        search_name = input("Enter the name: ")
        
        results = [x for x in films if search_name in x]
        print(results)
    elif command == "9":
        print("Exiting...")
        break

with open("films.json", "w") as outfile:
    json.dump(films, outfile)
