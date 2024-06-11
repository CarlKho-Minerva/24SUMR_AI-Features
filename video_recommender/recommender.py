# video_recommender/recommender.py
import random
from constants import *
from utils import debug_print
from user_actions import (
    recalculate_percentages,
    note_actions_and_update_weights,
)

queue = {}
watched = {}


def get_interest_tag_for_recommendation(user_dict_interest):
    """
    Select an interest tag for recommendation based on user interest percentages.

    Parameters:
    user_dict_interest (dict): Dictionary of user interests and their weights.

    Returns:
    str: Selected interest tag.
    """
    user_dict_percentage = recalculate_percentages(user_dict_interest)
    random_value = random.randint(0, 100)
    print("_" * 50)
    print(f"\nRandom value: {random_value}\n")
    cumulative_percentage = 0
    print("Based on User_Dictionary_Percentage (%)\n")
    for interest_tag, percentage in user_dict_percentage.items():
        previous_cumulative_percentage = cumulative_percentage
        cumulative_percentage += percentage
        print(
            f"Checking interest: {interest_tag}, cumulative range: {int(previous_cumulative_percentage)} - {int(cumulative_percentage)}"
        )
        if random_value <= cumulative_percentage:
            print(f"Selected interest: {interest_tag}")
            return interest_tag
    return None


def create_user_interest_dict(user_interests):
    """
    Create a dictionary with user interests and initial weights.

    Parameters:
    user_interests (list): List of user interests.

    Returns:
    dict: Dictionary of user interests and initial weights.
    """
    if not (4 <= len(user_interests) <= 8):
        print("Invalid number of user interests provided.")
        return {}

    user_dict_interest = {interest_tag: 10 for interest_tag in user_interests}
    debug_print(user_dict_interest, "create_user_interest_dict")
    return user_dict_interest


def mark_as_watched(video_id, title, watched_dict):
    """
    Mark a video as watched.

    Parameters:
    video_id (str): The ID of the video.
    title (str): The title of the video.
    watched_dict (dict): Dictionary of watched videos.

    Returns:
    dict: Updated dictionary of watched videos.
    """
    watched_dict[video_id] = title
    debug_print(
        f'Added "{title}" with ID {video_id} to watched videos.', "mark_as_watched"
    )
    return watched_dict


def show_video_again(video_id, title, watched_dict):
    """
    Remove a video from the watched list to show it again.

    Parameters:
    video_id (str): The ID of the video.
    title (str): The title of the video.
    watched_dict (dict): Dictionary of watched videos.

    Returns:
    dict: Updated dictionary of watched videos.
    """
    watched_dict.pop(video_id)
    debug_print(
        f'"{title}" with ID {video_id} has been removed from watched videos. It will be played again on algorithm match.',
        "show_video_again",
    )
    return watched_dict


def add_to_queue(interest_tag, n_results, collection, df, queue, watched):
    """
    Add videos to the queue based on the interest tag.

    Parameters:
    interest_tag (str): The tag of interest.
    n_results (int): Number of results to query.
    collection: ChromaDB collection.
    df (DataFrame): DataFrame containing video data.
    queue (dict): Queue of videos to be viewed.
    watched (dict): Dictionary of watched videos.

    Returns:
    dict: Updated video queue.
    """
    original_interest_tag = interest_tag

    results = collection.query(query_texts=[interest_tag], n_results=n_results)
    debug_print(
        f'Queried top {n_results} videos for tag "{interest_tag}"', "add_to_queue"
    )

    if len(results["ids"][0]) < n_results:
        print(
            f"Not enough results for interest tag '{interest_tag}'. Needed {n_results}, but got {len(results['ids'][0])}."
        )
        print("Algorithm set to Random mode.")
        interest_tag = "Random"
        watched.clear()
        results = collection.query(query_texts=[interest_tag], n_results=n_results)

    if len(results["ids"][0]) > n_results:
        print("More videos added. Removing Random mode.")
        interest_tag = original_interest_tag
        results = collection.query(query_texts=[interest_tag], n_results=n_results)

    for i in range(n_results):
        result_id = int(results["ids"][0][i])
        title = df.loc[df["video_id"] == result_id, "video_title"].values[0]
        tag = df.loc[df["video_id"] == result_id, "tags"].values[0].split(",")[0]

        if result_id not in watched:
            queue[result_id] = tag
            print(f'Added "{title}" with ID {result_id} and tag "{tag}" to the queue')

    return queue


def view_video(queue, user_dict_interest, watched_dict, collection, df):
    """
    View a video from the queue and update user interest weights.

    Parameters:
    queue (dict): Queue of videos to be viewed.
    user_dict_interest (dict): Dictionary of user interests and their weights.
    watched_dict (dict): Dictionary of watched videos.

    Returns:
    dict: Updated video queue.
    """
    if not queue:
        print("Queue is empty! Adding more videos...")
        new_interest_tag = get_interest_tag_for_recommendation(user_dict_interest)
        add_to_queue(
            new_interest_tag, COUNT_QUEUED_VIDEOS, collection, df, queue, watched
        )

    video_id, interest_tag = next(iter(queue.items()))
    del queue[video_id]
    title = df.loc[df["video_id"] == video_id, "video_title"].values[0]
    mark_as_watched(video_id, title, watched_dict)
    note_actions_and_update_weights(
        user_dict_interest, interest_tag, liked=True, watched=True
    )

    if len(queue) <= 2:
        print("\n2 cached videos left. \nAdding more videos to the queue...\n")
        new_interest_tag = get_interest_tag_for_recommendation(user_dict_interest)
        add_to_queue(
            new_interest_tag, COUNT_QUEUED_VIDEOS, collection, df, queue, watched
        )

    debug_print(
        f"Viewed video: {title}. Queue: {queue}. Watched: {watched_dict}", "view_video"
    )
    return queue
