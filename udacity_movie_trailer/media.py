# import webbrowser so that trailer can be shown using a pop up browser
import webbrowser
# create class Movie to initialize several inclusive parameters and define
# a function to show trailer.


class Movie():
    """Overview of Movie class"""
    # create and initialize necessary parameters(self, movie_title,
    # movie_storyline, etc...)

    def __init__(self, movie_title, movie_storyline, poster_image,
                 movie_trailer):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
