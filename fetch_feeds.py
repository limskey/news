import feedparser
import os

# List of RSS feed URLs
feed_urls = [
    'https://news.google.com/rss/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen',
    # Add more feed URLs as needed
]

# Directory to save the feeds
output_dir = 'daily'
os.makedirs(output_dir, exist_ok=True)

for i, url in enumerate(feed_urls, start=1):
    feed = feedparser.parse(url)
    if feed.bozo:
        print(f"Failed to parse {url}")
        continue
    
    file_path = os.path.join(output_dir, f'feed{i}.xml')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(feed.feed.get('title', 'No title'))
        f.write('\n')
        for entry in feed.entries:
            f.write(entry.title + '\n')
            f.write(entry.link + '\n\n')

print(f"Saved {len(feed_urls)} feeds to {output_dir}/")
