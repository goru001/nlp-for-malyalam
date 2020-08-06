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

#### Open Source Datasets
1. [iNLTK Headlines Corpus - Malayalam](https://github.com/ai4bharat-indicnlp/indicnlp_corpus#publicly-available-classification-datasets) : Uses the Malayalam News Dataset prepared above

## Results

### Language Model Perplexity (on validation set)

| Architecture/Dataset | Malayalam Wikipedia Articles |
|:--------:|:----:|
|   ULMFiT  |  26.39  |
|  TransformerXL |  25.79  |


### Classification Metrics

##### ULMFiT

| Dataset | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Malayalam | 95.56 | 93.29 | [Link](https://github.com/goru001/nlp-for-malyalam/blob/master/classification/Malyalam_Classification_Model.ipynb) |

### Visualizations
 
##### Word Embeddings

| Architecture | Visualization |
|:--------:|:----:|
| ULMFiT | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-malyalam/master/language-model/embedding_projector_config.json) |
| TransformerXL | [Embeddings projection](https://projector.tensorflow.org/?config=https://raw.githubusercontent.com/goru001/nlp-for-malyalam/master/language-model/embedding_projector_transformer_config.json)  |


### Results of using Transfer Learning + Data Augmentation from iNLTK

##### On using complete training set (with Transfer learning)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Malayalam | (5036, 630, 630) | 95.56 | 93.29 | [Link](https://github.com/goru001/nlp-for-malyalam/blob/master/classification/Malyalam_Classification_Model.ipynb) |
 

##### On using 10% of training set (with Transfer learning)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Malayalam | (503, 630, 630) | 82.38 | 73.47 | [Link](https://github.com/goru001/nlp-for-malyalam/blob/master/classification/Malyalam_Classification_Model_without_aug.ipynb) |
 
##### On using 10% of training set (with Transfer learning + Data Augmentation)

| Dataset | Dataset size (train, valid, test) | Accuracy | MCC | Notebook to Reproduce results |
|:--------:|:----:|:----:|:----:|:----:|
| iNLTK Headlines Corpus - Malayalam | (503, 630, 630) | 84.29 | 76.36 | [Link](https://github.com/goru001/nlp-for-malyalam/blob/master/classification/Malyalam_Classification_Model_with_aug.ipynb) |


## Pretrained Models

#### Language Models 
Download pretrained Language Model from [here](https://drive.google.com/open?id=1QHNR6xGN8JbvPEuDRXtb18J9WbGm9AwV)


#### Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1jZ1QXVEhZnlQi2zyJG_O7l2r0pW38cbe)