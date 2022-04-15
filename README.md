# Snack Generator

The idea of this is that you run `main.py` and are asked to rate several different snacks.
The algorithm then uses this to try and identify what new snacks you may like.

# Dependencies
You need to have python3 installed.
You need to have gensim, nltk and numpy.

# Use
To train the Word2Vec model, run `make_model.py`
To train the K Means model, run `train_k_means.py`
To use the models and get suggested new snacks, run `main.py`

For training of Word2Vec and K Means you will need gensim and nltk,
but for `main.py` where snacks are generated, you only need numpy, random and json.


# See Dev and Demonstraions on Youtube
https://www.youtube.com/playlist?list=PLlExR4hS66N5CtcDzcRbHBPSQiiA1Vs3q
