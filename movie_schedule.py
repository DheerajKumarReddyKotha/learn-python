current_movies = {"Asuran": "11:00 AM",
                  "Bharateeyudu": "02:00 PM",
                  "Kabali": "06:00 PM",
                  "Nirnayam": "09:00 PM"}

print("We are showing following movies:")
for key in current_movies:
    print(key)

movie_name = input("Please enter a movie name\n")
show_time = current_movies.get(movie_name)
if show_time:
    print("Tickets available for show time:", show_time, sep=" ")
else:
    print("Movie is not in the List")
