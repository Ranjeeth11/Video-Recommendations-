def get_recommendations(user_id, interaction_matrix, content_features, popularity_scores, n_recommendations=10):
    try:
        if interaction_matrix.empty or user_id not in interaction_matrix.index:
            return get_popular_recommendations(popularity_scores, n_recommendations)
        else:
            return get_personalized_recommendations(user_id, interaction_matrix, content_features, popularity_scores, n_recommendations)
    except Exception as e:
        print(f"Error getting recommendations: {str(e)}")
        return get_popular_recommendations(popularity_scores, n_recommendations)
    
def get_popular_recommendations(popularity_scores, n_recommendations):
    return sorted(popularity_scores.items(), key=lambda x: x[1], reverse=True)[:n_recommendations]

def get_personalized_recommendations(user_id, interaction_matrix, content_features, popularity_scores, n_recommendations):
    user_interactions = interaction_matrix.loc[user_id]
    uninteracted_posts = [post_id for post_id in popularity_scores.keys() if post_id not in user_interactions or user_interactions[post_id] == 0]

    recommendations = []
    for post_id in uninteracted_posts:
        score = popularity_scores[post_id]
        if not content_features.empty and post_id in content_features.index:
            similar_posts = get_similar_posts(post_id, content_features)
            for similar_post_id, similarity in similar_posts:
                if similar_post_id in user_interactions:
                    score += similarity * user_interactions[similar_post_id]

        recommendations.append((post_id, score))

    return sorted(recommendations, key=lambda x: x[1], reverse=True)[:n_recommendations]

if __name__ == "__main__":
    try:
        posts, views, likes, ratings, users = fetch_data()
        interaction_matrix, content_features, popularity_scores = preprocess_data(posts)

        user_id = "kinha"
        recommendations = get_recommendations(user_id, interaction_matrix, content_features, popularity_scores)

        filepath = save_recommendations_to_csv(user_id, recommendations, posts)
        if filepath:
            print(pd.read_csv(filepath))

    except Exception as e:
        print(f"An error occurred: {str(e)}")


