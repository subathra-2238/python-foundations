class URLShortener:
    def __init__(self):
        self.url_database = {}
        self.counter = 1

    def shorten(self, long_url):
        short_code = "url" + str(self.counter)

        self.url_database[short_code] = long_url
        self.counter += 1

        return short_code

    def retrieve(self, short_code):
        return self.url_database.get(short_code, "URL not found")


shortener = URLShortener()

long_url = "https://www.example.com/python"

short_url = shortener.shorten(long_url)

print("Short URL:", short_url)
print("Original URL:", shortener.retrieve(short_url))
