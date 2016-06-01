from apiclient.discovery import build
from apiclient.errors import HttpError


DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=options,
    part="id",
    maxResults= 1
  ).execute()

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":

      return search_result["id"]["videoId"]

