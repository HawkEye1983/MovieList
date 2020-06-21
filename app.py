movieList = []

def getInput(item):
    if item == "firstName":
        firstName = input("What is your first name: ")
        return firstName
    elif item == "lastName":
        lastName = input("What is your last name: ")
        return lastName
    elif item == "age":
        age = int(input("How old are you? "))
        return age
    elif item == "gender":
        gender = input("Are (M)ale or (F)emale: ")[0].upper()
        while True:
            if gender == "M":
                return gender
                break
            elif gender == "F":
                return gender
                break
            else:
                print("Invalid input for age.")
                gender = input("Please enter either (M)ale or (F)emale: ")[0].upper()
                continue

def addMovie(movie):
    movieList.append(movie)
    print("Movie added successfully.")

def delMovie(movie):
    if movie > len(movieList):
        print("Sorry. That is not a valid selection.")
    else:
        movieCount = 0
        movieDictionary = {}
        for movies in movieList:
            movieCount += 1
            movieDictionary[movieCount] = movieList[movieCount - 1]
        movieList.remove(movieDictionary[movie])
        print("Movie successfully removed.")

def clearMovies():
    movieList.clear()
    print("Movie list cleared.")

def listMovies():
    movieCount = 0
    word1 = "are"
    word2 = "movies"
    if len(movieList) == 1:
        word1 = "is"
        word2 = "movie"
    print(f"There {word1} currently {len(movieList)} {word2} on the list.")
    for movies in movieList:
        movieCount += 1
        movie = movieList[movieCount - 1]
        print(f"{movieCount}: {movieList[movieCount - 1].title()}")

def save(fileName):
    with open(fileName, "w") as f:
        for movie in movieList:
            f.write(movie + "\n")
    print("File saved successfully.")

def load(fileName):
    try:
        with open(fileName, "r") as f:
            movie = f.readline().strip()
            while movie:
                movieList.append(movie)
                movie = f.readline().strip()
        print("File loaded successfully.")
    except IOError:
        print("There was an error opening the file.")
        return


def run():
    firstName = getInput("firstName")
    lastName = getInput("lastName")
    age = getInput("age")
    gender = getInput("gender")
    while True:
        command = input("> ").lower()
        if command == "quit":
            break
        elif command == "add":
            addMovie(input("Movie Name: ").lower())
        elif command == "del":
            listMovies()
            delMovie(int(input("Select a movie number to remove: ")))
        elif command == "clear":
            clearMovies()
        elif command == "list":
            listMovies()
        elif command == "info":
            if gender == "M":
                fullGender = "male"
            else:
                fullGender = "female"
            print(f"Your name is: {firstName} {lastName}\nYou are {age} years old.\nYou are a {fullGender}.")
        elif command == "save":
            save(input("Enter filename to save as: "))
        elif command == "load":
            load(input("Enter a filename to load: "))
        else:
            print("Try again.")
            continue

run()

movieList = []
with open("movies.txt", "r") as f:
    movie = f.readline().strip()
    while movie:
        movieList.append(movie)
        movie = f.readline().strip()
    print(movieList)