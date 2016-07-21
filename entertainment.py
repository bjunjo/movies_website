import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://www.impawards.com/1995/posters/toy_story_ver1_xxlg.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://vignette2.wikia.nocookie.net/jamescameronsavatar/images/5/59/Neytiri-and-Jake-avatar-10334770-1440-900.jpg/revision/latest/scale-to-width-down/1000?cb=20100815222617",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

#print(avatar.storyline)
#avatar.show_trailer()

wailing = media.Movie("The Wailing",
                      "The scariest movie in 2016",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcTlkMLP2ropKze0pUOF9ep9qpGLF7XB3Q_yAhS1YaE0JvUig1yu",
                      "https://www.youtube.com/watch?v=Ej25zrnaTXk")
#wailing.show_trailer()
school_of_rock = media.Movie("School of Rock",
                             "Jack Black!!",
                             "http://www.gstatic.com/tv/thumb/movieposters/33094/p33094_p_v8_aa.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

shrek = media.Movie("Shrek",
                    "Once upon a time, in a far away swamp, there lived an ogre named Shrek",
                    "http://originalvintagemovieposters.com/wp-content/uploads/2010/06/Shrek1.jpg",
                    "https://www.youtube.com/watch?v=W37DlG1i61s")
harry_potter = media.Movie("Harry Potter",
                           "Adaptation of the first of J.K. Rowling's popular children's novels about Harry Potter",
                           "http://harrypotterfanzone.com/wp-content/2009/06/harry-potter-deathly-hallows-part-2-final-poster-01.jpg",
                           "https://www.youtube.com/watch?v=K1KPcXRMMo4")

movies = [toy_story, avatar, wailing, school_of_rock, shrek, harry_potter]
fresh_tomatoes.open_movies_page(movies)
