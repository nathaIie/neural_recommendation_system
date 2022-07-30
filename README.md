# Neural Recommendation System

Traditional approaches to building recommendation systems are divided into non-personalized and personalized recommendation methods. Each of these methods uses different machine learning algorithms and techniques. There are mainly two approaches in personalized
recommendation system: content-based and collaborative filtering. The first one is based on the users' items and profile features, and the second - seeks a similar users’ preferences. Furthermore, collaborative filtering methods can be sub-divided into model-based and memory-based (also commonly referred to as neighborhood-based) approaches.

For better results some recommendation systems combine both content-based and collaborative filtering. Using hybrid approaches we can avoid some limitations and problems of pure recommendation systems, like the cold-start or data sparsity problem.

Applying deep learning approaches to recommendation systems can increase their efficiency and operations in terms of speed and accuracy. This system uses the neural collaborative filtering framework for recommendations, which consists of:
- Generalized Matrix Factorization subnetwork,
- Multi-Layer Perception subnetwork.

The general idea behind the fusion is that the GMF better generates the linear dependencies and the MLP better models the non-linear dependencies of in the user-item interactions. The outputs of these two networks are concatenated in order to create a feature vector which can be passed to the further layers. Afterwards, we can calculate the final predictions:)

## Dataset

Neural recommendation system uses 
[Spotify Playlist](https://www.kaggle.com/datasets/andrewmvd/spotify-playlists) dataset from Kaggle, which is based on the subset of users in the #nowplaying dataset who publish their #nowplaying tweets via Spotify.
