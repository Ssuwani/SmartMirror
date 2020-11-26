import feedparser
headlines_url = "https://news.google.com/news?ned=kr&output=rss"

feed = feedparser.parse(headlines_url)

def get_posts():
    posts = [post['title'] for post in feed.entries[0:5]]
    return posts