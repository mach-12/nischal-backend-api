from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import nltk
import pickle
import string

class TextSpamService:
    @staticmethod
    async def evaluate_spam_message(message_content: str) -> str:
        sd = SpamDetection()
        return sd.predict(message_content)
    
    @staticmethod
    async def Calculate_score(text:str):
        score = "0.5"
        
        return str(score)
        

class SpamDetection():
    pipe = None
    model = None
    
    def __init__(self) -> None:
        nltk.download('stopwords')
        pipe_file = open("app/services/model exports/pipe.pkl",'rb')
        self.pipe = pickle.load(pipe_file)
        pipe_file.close()

        model_file = open("app/services/model exports/model.pkl",'rb')
        self.model = pickle.load(model_file)
        model_file.close()

    @staticmethod
    def basic_clean(x) :
        ps = PorterStemmer()

        words = word_tokenize(x.lower())
        final = []
        
        for word in words :     
            if word.isalnum():
                final.append(word)
        words = final[:]
        final= []
        stop_words = set(stopwords.words('english'))

        for i in words :
            if i not in stop_words and i not in string.punctuation:
                final.append(i)
        words = final[:]
        final= []
        
        for i in words :
            final.append(ps.stem(i))
        words = final[:]
        final = []
        return ' '.join(words)

    def predict(self, text):
        
        if self.model == None:
            return 0
        
        # preprocess
        transformed_text = self.basic_clean(text)
        print(transformed_text)

        # vectorize
        vector_input = self.pipe.transform([transformed_text])
        
        # predict
        result = self.model.predict_proba(vector_input)[0][1] 
        return {'riskScore':str(result), 'spam':result > 0.5}