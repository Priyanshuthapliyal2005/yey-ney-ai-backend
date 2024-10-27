# models/reaction_model.py
def update_reaction(post_data, reaction):
    if reaction == "yey":
        post_data["yey"] += 1
    elif reaction == "ney":
        post_data["ney"] += 1
    return post_data
