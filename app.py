from flask import Flask
from CommentClassification import get_video_comment
import json
from keras.models import model_from_json
import tensorflow as tf
import numpy as np
from DataProcessing import preprocess_text
import tqdm
from transformers import BertTokenizer
from transformers import BertTokenizer,BertConfig, BertForSequenceClassification, AdamW
import pickle
import pandas as pd
import keras




app = Flask(__name__)

# @app.route('/')
# def hellp():
#     return get_video_comment()

@app.route('/')
def predict():
    comments_dic = get_video_comment()
    # model = load_model()
    # print(model.predict())
    # df = pd.DataFrame({'Video_ID':comments_dic['video_id'],'Comment':comments_dic['comment_text']})
    return comments_dic
    # test_df = np.array(comments_dic['comment_text']).apply(lambda x: preprocess_text(x))

    # X_unlabeled_input_ids = np.zeros((len(test_df), 256))
    # X_unlabeled_attn_masks = np.zeros((len(test_df), 256))

    # X_unlabeled_input_ids, X_unlabeled_attn_masks = generate_training_data(test_df, X_unlabeled_input_ids, X_unlabeled_attn_masks)

    # predicted_labels = model.predict({'input_ids': X_unlabeled_input_ids, 'attention_mask': X_unlabeled_attn_masks})
    # return predicted_labels

def generate_training_data(df_data, ids, masks):
    # Loop through each comment in the DataFrame using tqdm for progress tracking
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
    for i, comment in tqdm(enumerate(df_data['comment_text'])):
        # Tokenize the comment using the provided tokenizer
        tokenized_text = tokenizer.encode_plus(
            comment,
            max_length=256,               # Maximum sequence length
            truncation=True,              # Truncate if the comment exceeds max length
            padding='max_length',         # Pad the sequence to the max length
            add_special_tokens=True,      # Add [CLS] and [SEP] tokens
            return_tensors='tf'           # Return TensorFlow tensors
        )

        # Store the token IDs in the 'ids' array for the i-th sample
        ids[i, :] = tokenized_text.input_ids

        # Store the attention masks in the 'masks' array for the i-th sample
        masks[i, :] = tokenized_text.attention_mask

    # Return the populated 'ids' and 'masks' arrays
    return ids, masks

def load_model():
    # with open('YouTubeClassification_json.json', 'r') as json_file:
    #     model_json = json_file.read()
    # loaded_model = model_from_json(model_json)
    # loaded_model.load_weights('YouTubeClassification_weights.h5')
    model = pickle.load(open('Spam_Prediction.pkl','rb'))

    return model


if __name__ ==  '__main__':
    app.run(debug=False,host='0.0.0.0')