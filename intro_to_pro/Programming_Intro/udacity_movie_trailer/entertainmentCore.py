# import media so that the Movie function could be used to display
# imformation about the movies.
import media
# import rotten_tomatoes to list the information of each movie in html format.
import rotten_tomatoes

# add the movie Sound of Music
sound_of_music = media.Movie(
    "Sound of Music",
    "a young woman named Maria is failing miserably in her attempts to become a nun",
    "https://upload.wikimedia.org/wikipedia/en/c/c6/Sound_of_music.jpg",
    "https://www.youtube.com/watch?v=UY6uw3WpPzY")
# add the movie Pride and Prejudice
pride_and_prejudice = media.Movie(
    "Pride and Prejudice",
    "Elizabeth Bennett, a witty, sarcastic, opinionated young lady who"
    " falls in love with Mr.Darcy, a shy, rich, man who defiantly"
    " believes in superior birth",
    "https://upload.wikimedia.org/wikipedia/en/0/03/Prideandprejudiceposter.jpg",
    "https://www.youtube.com/watch?v=1dYv5u6v55Y")
# add the movie Twilight
twilight = media.Movie(
    "Twilight",
    "A teenage girl risks everything when she falls in love with a vampire.",
    "https://upload.wikimedia.org/wikipedia/en/b/b6/Twilight_%282008_film%29_poster.jpg",
    "https://www.youtube.com/watch?v=edLB6YWZ-R4")
# add the movie My Fair Lady
my_fair_lady = media.Movie(
    "My Fair Lady",
    "A misogynistic and snobbish phonetics professor agrees to a wager"
    " that he can take a flower girl and make her presentable in high society.",
    "https://upload.wikimedia.org/wikipedia/en/d/d5/My_fair_lady_poster.jpg",
    "https://www.youtube.com/watch?v=WHrgSXPxr9w")
# add the movie Me Before You
me_before_you = media.Movie(
    "Me Before You",
    "A girl in a small town forms an unlikely bond with a"
    " recently-paralyzed man she's taking care of.",
    "https://upload.wikimedia.org/wikipedia/en/f/fd/Me_Before_You_%28film%29.jpg",
    "https://www.youtube.com/watch?v=Eh993__rOxA")
# add the movie Love, Rosie
love_rosie = media.Movie(
    "Love, Rosie",
    "Rosie and Alex have been best friends since they were 5, so they couldn't"
    "possibly be right for one another...or could they? When it comes to love,"
    "life and making the right choices, these two are their own worst enemies.",
    "https://upload.wikimedia.org/wikipedia/en/e/eb/Love%2C_Rosie_%28film%29_UK_poster.jpg",
    "https://www.youtube.com/watch?v=5zL3YJKygd4")
# add the movie Breakfast at Tiffanys
breakfast_at_Tiffanys = media.Movie(
    "Breakfast at Tiffany's",
    "A young New York socialite becomes interested in a young man who"
    "has moved into her apartment building.",
    "https://upload.wikimedia.org/wikipedia/en/a/a9/Breakfast_at_Tiffanys.jpg",
    "https://www.youtube.com/watch?v=uirBWk-qd9A")
# put the movies together in a list
movies = [
    sound_of_music,
    pride_and_prejudice,
    twilight,
    my_fair_lady,
    me_before_you,
    love_rosie,
    breakfast_at_Tiffanys, ]
# use rotten_tomatoes to display the list
rotten_tomatoes.open_movies_page(movies)
