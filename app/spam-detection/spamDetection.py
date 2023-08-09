import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import os
import pickle
import string

class SpamDetection():
    pipe = None
    model = None
    nltk.download('punkt')
    def __init__(self) -> None:
        pipe_path = os.path.join(os.getcwd(), 'C:/Users/inher/OneDrive/Desktop/kavach-files/nischal-backend-api/app/spam-detection/model exports/pipe.pkl')
        pipe_file = open(pipe_path,'rb')
        self.pipe = pickle.load(pipe_file)
        pipe_file.close()

        model_path = os.path.join('C:/Users/inher/OneDrive/Desktop/kavach-files/nischal-backend-api/app/spam-detection/model exports/model.pkl')
        model_file = open(model_path,'rb')
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
    
sd = SpamDetection()