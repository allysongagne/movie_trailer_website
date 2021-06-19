import media
import fresh_tomatoes

"""Defined six instances of the class Movie"""
all_about_eve = media.Movie(
    "All About Eve",
    "1950",
    "Winner of six Academy Awards including Best Picture",
    "https://upload.wikimedia.org/wikipedia/commons/a/a7/All_About_Eve_%281950_poster_-_retouch%29.jpg",
    "https://www.youtube.com/watch?v=LSntQerk8cQ")
singing_in_the_rain = media.Movie(
    "Singin' in the Rain",
    "1952",
    "Two Academy Award Nominations",
    "https://upload.wikimedia.org/wikipedia/commons/5/5d/Singin%27_in_the_Rain_%281952_poster%29.jpg",
    "https://www.youtube.com/watch?v=5_EVHeNEIJY")
how_to_marry_a_millionaire = media.Movie(
    "How to Marry a Millionaire",
    "1953",
    "Nominated for the Adademy Award in Best Costume Design",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/How_to_Marry_a_Millionaire.png",
    "https://www.youtube.com/watch?v=s8Q3j8nIeYo")
sabrina = media.Movie(
    "Sabrina",
    "1954",
    "Winner of one Academy Award and six nominations",
    "https://upload.wikimedia.org/wikipedia/commons/3/3b/Sabrina_%281954_film_poster%29.jpg",
    "https://www.youtube.com/watch?v=2izQFpAxGJk")
to_catch_a_theif = media.Movie(
    "To Catch a Thief",
    "1955",
    "Winner of one Academy Award and three nominations",
    "https://upload.wikimedia.org/wikipedia/commons/8/8b/To_Catch_a_Thief.jpg",
    "https://www.youtube.com/watch?v=YIc5SDKEC6g")
some_like_it_hot = media.Movie(
    "Some Like It Hot",
    "1959",
    "Winner of one Academy Award and six nominations",
    "https://upload.wikimedia.org/wikipedia/commons/b/b8/Some_Like_It_Hot_%281959_poster%29.png",
    "https://www.youtube.com/watch?v=rI_lUHOCcbc")

"""Array containing the above six movies"""
movies = [all_about_eve, singing_in_the_rain, how_to_marry_a_millionaire, sabrina,to_catch_a_theif, some_like_it_hot]

"""Takes the above array of movies and calls open_movies_page in order to view the webpage"""
fresh_tomatoes.open_movies_page(movies)
