# video_recommender/user_actions.py
from constants import LIKE, SHARE, WATCH, LOOP, STARTING_WEIGHT
from utils import debug_print


def observe_action_taken(
    interest_tag, liked=False, shared=False, watched=False, loop_count=0
):
    """
    Calculate the total points based on the user's actions.

    Parameters:
    interest_tag (str): The tag of the video.
    liked (bool): Whether the user liked the video.
    shared (bool): Whether the user shared the video.
    watched (bool): Whether the user watched the video.
    loop_count (int): The number of times the user looped the video.

    Returns:
    float: The total points calculated based on the user's actions.
    """
    Actions = {
        "LIKE": LIKE,
        "SHARE": SHARE,
        "WATCH": WATCH,
        "LOOP": LOOP,
    }

    total_action_points = 0

    if liked:
        total_action_points += Actions["LIKE"]
    if shared:
        total_action_points += Actions["SHARE"]
    if watched:
        total_action_points += Actions["WATCH"]
    total_action_points += loop_count * Actions["LOOP"]

    return total_action_points


def recalculate_percentages(user_dict_interest):
    """
    Recalculate the percentage of each interest relative to the total weight.

    Parameters:
    user_dict_interest (dict): Dictionary of user interests and their weights.

    Returns:
    dict: Dictionary of user interests and their percentages.
    """
    total_weight = sum(user_dict_interest.values())
    user_dict_percentage = {
        interest_tag: round((weight / total_weight) * 100, 2)
        for interest_tag, weight in user_dict_interest.items()
    }
    debug_print(user_dict_percentage, "recalculate_percentages (%)")
    return user_dict_percentage


def handle_interruptions(user_dict_percentage):
    """
    Handle intentional interruptions and suggest relevant interests (50% dominance) or recommend more of the same interest.

    Parameters:
    user_dict_percentage (dict): A dictionary where keys are interest tags and values are their percentages.
    """
    interest_tag, interest_percentage = max(
        user_dict_percentage.items(), key=lambda item: item[1]
    )
    if interest_percentage > 75:
        print(f"Have you been enjoying {interest_tag} so far?")
        response = input()  # Get user's response
        if response.lower() == "yes":
            print("Recommend less of the same interest.")
    elif interest_percentage > 50:
        print("Suggesting relevant interests...")
    debug_print(
        f"The highest tag is {interest_tag}. It dominates the interest weights by {interest_percentage}%.",
        "handle_interruptions",
    )


def note_actions_and_update_weights(
    user_dict_interest,
    interest_tag,
    liked=False,
    shared=False,
    watched=False,
    loop_count=0,
):
    """
    Update user interest weights based on their actions and handle interruptions.

    Parameters:
    user_dict_interest (dict): Dictionary of user interests and their weights.
    interest_tag (str): The tag of the video.
    liked (bool): Whether the user liked the video.
    shared (bool): Whether the user shared the video.
    watched (bool): Whether the user watched the video.
    loop_count (int): The number of times the user looped the video.

    Returns:
    dict: Updated dictionary of user interests and their weights.
    """
    total_action_points = observe_action_taken(
        interest_tag, liked, shared, watched, loop_count
    )
    if interest_tag in user_dict_interest:
        print(
            f"Updating weights for interest: {interest_tag}. Total points to add: {total_action_points}."
        )
        user_dict_interest[interest_tag] += total_action_points
        print(
            f"Updated weight for interest: {interest_tag}. New weight: {user_dict_interest[interest_tag]}."
        )
    else:
        print(
            f"Adding new interest: {interest_tag}. Total points to add: 10 (default)."
        )
        user_dict_interest[interest_tag] = STARTING_WEIGHT
        print(
            f"Added new interest: {interest_tag}. Weight: {user_dict_interest[interest_tag]}."
        )

    user_dict_percentage = recalculate_percentages(user_dict_interest)
    handle_interruptions(user_dict_percentage)
    user_dict_interest = dict(
        sorted(user_dict_interest.items(), key=lambda item: item[1], reverse=True)[:10]
    )

    return user_dict_interest
