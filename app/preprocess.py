def preprocess_data(posts):
    try:
        print("Starting data preprocessing...")

        posts_data = pd.DataFrame(posts.get('data', []))
        interactions = defaultdict(lambda: defaultdict(float))

        if not posts_data.empty:
            for _, post in posts_data.iterrows():
                user_id = post.get('username')
                post_id = post.get('id')
                if user_id and post_id:
                    view_weight = post.get('view_count', 0) * 1
                    upvote_weight = post.get('upvote_count', 0) * 3
                    rating_weight = post.get('average_rating', 0) * post.get('rating_count', 0) * 5

                    total_interaction = view_weight + upvote_weight + rating_weight
                    interactions[user_id][post_id] = total_interaction

        interaction_matrix = pd.DataFrame.from_dict(interactions, orient='index').fillna(0)

        features = []
        if not posts_data.empty:
            for _, post in posts_data.iterrows():
                features.append({
                    'id': post.get('id'),
                    'category_id': post['category'][0]['id'] if isinstance(post.get('category'), list) and post['category'] else 0,
                    'comment_count': post.get('comment_count', 0),
                    'upvote_count': post.get('upvote_count', 0),
                    'view_count': post.get('view_count', 0),
                    'rating_count': post.get('rating_count', 0),
                    'average_rating': post.get('average_rating', 0),
                    'share_count': post.get('share_count', 0),
                    'is_locked': 1 if post.get('is_locked') else 0,
                    'timestamp': post.get('created_at', 0)
                })

        content_features = pd.DataFrame(features).set_index('id') if features else pd.DataFrame()

        if not content_features.empty:
            numeric_columns = content_features.select_dtypes(include=[np.number]).columns
            content_features[numeric_columns] = (
                content_features[numeric_columns] - content_features[numeric_columns].mean()
            ) / content_features[numeric_columns].std()
            content_features = content_features.fillna(0)

        popularity_scores = calculate_popularity_scores(posts)
        return interaction_matrix, content_features, popularity_scores

    except Exception as e:
        print(f"Error preprocessing data: {str(e)}")
        traceback.print_exc()
        raise