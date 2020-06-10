# emotify-model

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/orzymandias/emotify-model/blob/master/emotify.ipynb)

## About the Emotify Model...

The emotify model is a non-binary classification model that uses neural networks to classify text into four different emotions (Happiness, Sadness, Anger, Worry). It is trained on tweets from the crowdflower dataset along with our tweets which we have web scraped ourselves. 
The model will be used to predict emotion from user input which are then used to search for music in the database.

### Dataset
There are limited textual datasets labelled with emotions and many which are found are either context specific (e.g. product reviews, dialogs) or labelled with emotion metrics (e.g. VAD) which were not aligned with our music labels.
We settled on using tweets dataset due to its accessibility and libraries such as tweepy which support easy web scraping. Furthermore, tweets capture an individual’s random thoughts which is plausible as input queries in our application. However, labels are subjective and the poor spelling and grammar of tweets may be disruptive to the model learning patterns.


### Model Development  (Experimental phase)
According to the Tensorflow documentation, sepCNN with GloVe embeddings layer performed best for text classification tasks. However, the ideal results could not be replicated with validation accuracy hovering around 30%. Issues could be due to ratio of text length to dataset size falling slightly below the recommended 1500. 
We have also experimented with transfer learning using a pre-trained embedding layer (Google News) and 2 MLP with slightly better results.


### Dependencies
Heroku deployment is running tf 2.0.1 due to space constaints
Local deployment uses tf latest version 2.2.0