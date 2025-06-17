def generate_user_description(user):
    """
    Generate a descriptive statement for a user profile based on their characteristics.
    """
    description = []
    
    # Basic user information
    name_info = f"{user['name']} (@{user['screen_name']})"
    description.append(name_info)
    
    # Activity level
    if user['statuses_count'] > 10000:
        activity = "very active"
    elif user['statuses_count'] > 1000:
        activity = "moderately active"
    else:
        activity = "less active"
    
    activity_info = f"is a {activity} user with {user['statuses_count']} tweets"
    description.append(activity_info)
    
    # Follower/Following dynamics
    social_info = f"has {user['followers_count']} followers and follows {user['friends_count']} accounts"
    description.append(social_info)
    
    # Engagement metrics
    if user['favourites_count'] > 0:
        engagement = f"has liked {user['favourites_count']} posts"
        description.append(engagement)
    
    # Location if available
    if user['location'] and user['location'] != 'unknown':
        location = f"is located in {user['location']}"
        description.append(location)
    
    # User's self description if available
    if user['description'] and len(user['description'].strip()) > 0:
        bio = f"describes themselves as: {user['description']}"
        description.append(bio)
    
    # Account verification status
    if user['verified']:
        description.append("is a verified account")
    
    # Join date
    created_at = pd.to_datetime(user['created_at'])
    join_info = f"joined Twitter on {created_at.strftime('%B %d, %Y')}"
    description.append(join_info)
    
    # Combine all parts into a coherent statement
    return " | ".join(description)

def create_profile_descriptions(df):
    """
    Create descriptive statements for all users in the dataframe.
    """
    descriptions = []
    for _, user in df.iterrows():
        desc = generate_user_description(user)
        descriptions.append(desc)
    return descriptions

# Example usage:
# descriptions = create_profile_descriptions(users_df)
# for desc in descriptions[:5]:  # Print first 5 descriptions
#     print(desc)
#     print("-" * 80) 