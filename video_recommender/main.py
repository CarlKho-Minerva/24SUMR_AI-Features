# video_recommender/main.py

import pandas as pd
from chromadb_helper import (
    initialize_chromadb,
    add_or_update_chromadb_rows,
)
from recommender import (
    create_user_interest_dict,
    view_video,
    add_to_queue,
)
from constants import *

# Initialize queue and watched dict
user_interests = ["DevOps", "Tests (SAT)", "Machine Learning", "Dogs"]


def main():
    global queue, watched

    collection = initialize_chromadb()

    # Add or update ChromaDB rows
    add_or_update_chromadb_rows(df, collection)

    # Create user interest dictionary
    user_dict_interest = create_user_interest_dict(user_interests)

    # Add initial videos to the queue
    add_to_queue(user_interests[0], COUNT_QUEUED_VIDEOS, collection, df, queue, watched)

    # Simulate viewing videos
    for _ in range(
        6
    ):  # Replace 6 with the number of times you want to run the simulation
        queue = view_video(queue, user_dict_interest, watched, collection, df)


if __name__ == "__main__":
    main()
