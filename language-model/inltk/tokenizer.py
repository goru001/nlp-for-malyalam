from fastai.text import *
import sentencepiece as spm

class MalyalamTokenizer(BaseTokenizer):
    def __init__(self, lang:str):
        self.lang = lang
        self.sp = spm.SentencePieceProcessor()
        self.sp.Load("/home/gaurav/PycharmProjects/nlp-for-malyalam/tokenizer/malyalam_lm.model")
        
    def tokenizer(self, t:str) -> List[str]:
        return self.sp.EncodeAsPieces(t)
