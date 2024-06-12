# video_recommender/constants.py
# video_recommender/constants.py
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # take environment variables from .env.

NEW_VIDEO_WEIGHT = 10
STARTING_WEIGHT = 10
USER_MIN_INTEREST = 4
USER_MAX_INTEREST = 8
COUNT_QUEUED_VIDEOS = 5


# User Actions
LIKE = 1
SHARE = 2
WATCH = 1  # more than 50% of total duration
LOOP = 1

# AI-Related Constants
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_EmbeddingModel = "text-embedding-3-small"

# ChromaDB
chromadb_name = "Edgur_Video_DB_Vectorstore"

# DB
db_url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSAE2tBAnAdXsxk9a9YClFN7MSEVhzEmJD01ewwtooMLxL-Ilod26EbdD8sZeZk0ybiqD-jqT-9RZbn/pub?gid=497214901&single=true&output=csv"  # test spreadsheet
df = pd.read_csv(db_url)
