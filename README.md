# NLP for Malyalam

This repository contains State of the Art Tokenizer, Language model
 and Classifier for Malyalam, which is spoken by the Malayali people 
  in the Indian state of Kerala and the union territories of
   Lakshadweep and Puducherry.

## Dataset

* Download [Malyalam Wikipedia Articles Dataset](https://drive.google.com/open?id=1MRnh9Z7FNTVgehvlS2BfG_pSh_9ccs47) (12,388 articles) which I scraped, cleaned and
used to train the language model

* Download [Malyalam News classification Dataset](https://drive.google.com/open?id=14KpsL36GkEIhsW8injS4GiAexN-1Khrg) which I scraped and used to train 
the classifier

## Results

#### Language Model

`on 30% validation set`

* Perplexity of language model: ~26

#### Classifier

* Accuracy of classification model: ~94%
* Kappa score of classification model: ~91

## Pretrained Language Model

Download pretrained Language Model from [here](https://drive.google.com/open?id=1QHNR6xGN8JbvPEuDRXtb18J9WbGm9AwV)


## Classifier

Download classifier from [here](https://drive.google.com/open?id=1HVEIaNfmCzGjulAcTWJHzYJ7JHMa9OfS)


## Tokenizer

Trained tokenizer using Google's [sentencepiece](https://github.com/google/sentencepiece)

Download the trained model and vocabulary from [here](https://drive.google.com/open?id=1jZ1QXVEhZnlQi2zyJG_O7l2r0pW38cbe)