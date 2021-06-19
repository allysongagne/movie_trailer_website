import webbrowser

class Movie():
        """class contains movie information"""
        
        def __init__(self, movie_title, movie_year, movie_awards, poster_image, trailer_youtube):
                    """initalizes the following attributes: movie_title, movie_year ,movie_awards,
                    poster_image and trailer_youtube"""
                    self.title = movie_title
                    self.year = movie_year
                    self.awards = movie_awards
                    self.poster_image_url = poster_image
                    self.trailer_youtube_url = trailer_youtube

        def play_trailer(self):
                    """Plays the movie trailer in the web browser""" 
                    webbrowser.open(self.movie_trailer_url)
