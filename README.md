# NLP for Malayalam

This repository contains State of the Art Language models
 and Classifier for Malayalam, which is spoken by the Malayali people 
  in the Indian state of Kerala and the union territories of
   Lakshadweep and Puducherry.
   
The models trained here have been used in [Natural Language Toolkit for Indic Languages
 (iNLTK)](https://github.com/goru001/inltk)

## Dataset

#### Created as part of this project

1. [Malayalam Wikipedia Articles](https://www.kaggle.com/disisbig/malayalam-wikipedia-articles)

2. [Malayalam News Dataset](https://www.kaggle.com/disisbig/malyalam-news-dataset)

## Results

#### Language Model Perplexity

| Architecture/Dataset | Malayalam Wikipedia Articles |
|:--------:|:----:|
|   ULMFiT  |  26.39  |
|  TransformerXL |  25.79  |


#### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | Kappa Score |
|:--------:|:----:|:----:|
| Malayalam News Dataset |  94.36  |  91.54  |


#### Visualizations
 
##### Embedding Space

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-malyalam/master/language-model/embedding_projector_config.json) |
| TransformerXL | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-malyalam/master/language-model/embedding_projector_transformer_config.json)  |

## Pretrained Language Model

Download pretrained Language Model from [here](https://drive.google.com/open?id=1QHNR6xGN8JbvPEuDRXtb18J9WbGm9AwV)


## Classifier

Download classifier from [here](https://drive.google.com/open?id=1HVEIaNfmCzGjulAcTWJHzYJ7JHMa9OfS)


## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1jZ1QXVEhZnlQi2zyJG_O7l2r0pW38cbe)