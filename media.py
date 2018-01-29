class Movie():
    def __init__(self, blurb, title, img_url, trailer_url, average, pop, date):
        self.title = title
        self.stoyline = blurb
        self.poster_image_url = img_url
        self.trailer_youtube_url = trailer_url
        self.vote_average = average
        self.popularity = pop
        self.release_date = date
