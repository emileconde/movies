class Movie:
    def __init__(self, id, title, overview, popularity, backdrop_path, poster_path, reslease_date, vote_average):
        self.id = id
        self.title = title
        self.overview = overview
        self.popularity = popularity
        self.backdrop_path = backdrop_path
        self.poster_path = poster_path
        self.reslease_date = reslease_date
        self.vote_average = vote_average
        
        
        def __str__ (self):
            return 'Movie(id=' + self.id + 'title=' + self.title + ')'
        
        
        
class tv_show:
    def __init__(self, id, name, overview, poster_path, backdrop_path, vote_average, first_air_date):
        self.id = id
        self.name = name
        self.overview = overview
        self.poster_path = poster_path
        self.backdrop_path = backdrop_path
        self.vote_average = vote_average
        self.first_air_date = first_air_date
        
        
class review:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        
    