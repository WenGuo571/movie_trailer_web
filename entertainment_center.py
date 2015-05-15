import media
import fresh_tomatoes

# Create New Movie Object johnny_english_reborn
johnny_english_reborn = media.Movie("Johnny English Reborn",
                                    "Johnny English Reborn is a 2011 British sp"
                                    "y comedy film parodying the James Bond sec"
                                    "ret agent genre and film franchise reboots"
                                    ".",
                                    "http://image.tmdb.org/t/p/w500/vnS4Lb5rNx2"
                                    "ZucVdrW3TQd6n2AL.jpg",
                                    "https://youtu.be/MhU0C-dXAqs")
# Create New Movie Object lord_of_the_flies
lord_of_the_flies = media.Movie("Lord of the Flies",
                                "Stranded on an island, a group of schoolboys "
                                "degenerate into savagery.",
                                "http://image.tmdb.org/t/p/w500/nWg5YQEXIAgy0nf"
                                "RqwKAspqmu0S.jpg",
                                "https://youtu.be/QnCn2VTzY90")

# Create new Movie Object now_you_see_me
now_you_see_me = media.Movie("Now You See Me",
                             "An FBI agent and an Interpol detective track a te"
                             "am of illusionists who pull off bank heists durin"
                             "g their performances and reward their audiences w"
                             "ith the money.",
                             "http://image.tmdb.org/t/p/w500/d0pMBKFzLNOFMDlYDe"
                             "bz44iNoqR.jpg",
                             "https://youtu.be/B2mD9gwKej8")

# Create new Movie Object the_matrix
the_matrix = media.Movie("The Matrix",
                         "A man living two lives",
                         "http://image.tmdb.org/t/p/w500/gynBNzwyaHKtXqlEKKLioN"
                         "kjKgN.jpg",
                         "https://youtu.be/m8e-FF8MsqU")

# Create new Movie Object the_lion_king_II
the_lion_king_II = media.Movie("Simba's Pride",
                               "The circle of life continues for Simba, now ful"
                               "ly grown and in his rightful place as the king "
                               "of Pride Rock.",
                               "http://image.tmdb.org/t/p/w500/d1Wj5wfzu4CWvKOI"
                               "L1l42NBYnzE.jpg",
                               "https://youtu.be/DFtBjc1dz7w")

# Create new Movie Object two_states
two_states = media.Movie("2 States",
                         "A story about a romantic journey of a culturally oppo"
                         "site couple - Krish Malhotra and Ananya Swaminathan.",
                         "http://image.tmdb.org/t/p/w500/zAnS58Dkue1y9himro869q"
                         "qfKPt.jpg",
                         "https://youtu.be/REifdfJvCzw")

# Create new Movie Object bhaag_milkha_bhaag
bhaag_milkha_bhaag = media.Movie("Bhaag Milkha Bhaag",
                                 "The true story of the 'Flying Sikh'.",
                                 "http://image.tmdb.org/t/p/w500/aFh3FIQSJHv2O8"
                                 "5NtFfpKyx260o.jpg",
                                 "https://youtu.be/3uICXnnW86U")

# Create new Movie Object the_dark_knight_rises
the_dark_knight_rises = media.Movie("The Dark Knight Rises",
                                    "The final installment in Nolan's Batman fi"
                                    "lm trilogy.",
                                    "http://image.tmdb.org/t/p/w500/dEYnvnUfXrq"
                                    "vqeRSqvIEtmzhoA8.jpg",
                                    "https://youtu.be/yQ5U8suTUw0")

# Create new Movie Object x_men
x_men = media.Movie("X-Men",
                    "Two mutants, Rogue and Wolverine, come to a private academ"
                    "y for their kind whose resident superhero team, the X-Men,"
                    " must oppose a terrorist organization with similar powers.",
                    "http://image.tmdb.org/t/p/w500/4kYj7fUJzhEg7xz8J3oMPi7gDww"
                    ".jpg",
                    "https://youtu.be/6acRHWnfZAE")


# Movie array
movies = [johnny_english_reborn, lord_of_the_flies, now_you_see_me, the_matrix,
          the_lion_king_II, bhaag_milkha_bhaag, x_men]

# Create html file and open with browser
fresh_tomatoes.open_movies_page(movies)
