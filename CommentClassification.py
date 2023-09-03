
import requests
from urllib.parse import urlparse, parse_qs
import emoji
import csv



# Set your YouTube API key


# Replace 'CHANNEL_ID' with the actual Channel ID
# channel_id = "UCjWY5hREA6FFYrthD0rZNIw"

# # Get the list of video IDs from the channel
# channel_url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=10"
# response = requests.get(channel_url)
# videos_data = response.json()

# video_ids = [item["id"]["videoId"] for item in videos_data["items"]]

    # ['https://www.youtube.com/watch?v=MF_bkz3v3mE','https://www.youtube.com/watch?v=JMUxmLyrhSk&t=1s','https://www.youtube.com/watch?v=dTRBnHtHehQ','https://www.youtube.com/watch?v=HU7TMhkQHhA','https://www.youtube.com/watch?v=zi7qIMXNhA0','https://www.youtube.com/watch?v=AYXfaVD5o40','https://www.youtube.com/watch?v=VxMHHqSOSTk','https://www.youtube.com/watch?v=zd4ALKv8Das','https://www.youtube.com/watch?v=EW4dEzfBst0','https://www.youtube.com/watch?v=jGwO_UgTS7I&list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU','https://www.youtube.com/watch?v=Xn7KWR9EOGQ']


def get_video_id():
    video_ids = []
    youtube_urls = ['https://www.youtube.com/watch?v=YbJOTdZBX1g']
    for url in youtube_urls:
        url_parts = urlparse(url)
        query_params = parse_qs(url_parts.query)
        print(query_params)
        video_ids.append(query_params["v"][0])
    return video_ids
    


# Iterate through each video and fetch comments
def get_video_comment():
    API_KEY = "AIzaSyCXUkOuHoqdKUMozozDpOxywpOX8Wsq9zQ"
    comments_dic = {'video_id':[],'comment_text':[]}
    video_ids = get_video_id()
    for video_id in video_ids:
        # Fetch comments for the video
        comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?key={API_KEY}&videoId={video_id}&part=snippet&maxResults=100"
        comments_response = requests.get(comments_url)
        comments_data = comments_response.json()

        # Extract and print comments
        for comment_item in comments_data["items"]:
            # print(comment_item)
            comment = comment_item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            # print(comment)
            comments_dic["video_id"].append(video_id)
            comments_dic['comment_text'].append(comment)
    return comments_dic
# csv_file_path = "/Users/ankitakotadiya/Documents/normal_data_test.csv"

# with open(csv_file_path, "w", newline="") as csvfile:
#     csv_writer = csv.writer(csvfile)
#     csv_writer.writerows(comments)