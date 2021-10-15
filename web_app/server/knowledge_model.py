import numpy as np
from tcn import TCN
from tensorflow.keras.layers import Input, Embedding, Dense, Dropout, SpatialDropout1D
from tensorflow.keras.layers import concatenate, GlobalAveragePooling1D, GlobalMaxPooling1D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

from pdf2line import *

trunc_type='post'
padding_type='post'
oov_tok = "<UNK>"
tokenizer = Tokenizer(oov_token=oov_tok)

def define_model(kernel_size=1, activation='tanh', input_dim=4321, output_dim=300, max_length=179):
    inp = Input(shape=(max_length,))
    x = Embedding(input_dim=input_dim, output_dim=output_dim, input_length=max_length)(inp)
    x = SpatialDropout1D(0.1)(x)

    x = TCN(128, dilations=[1, 2, 4], return_sequences=True, activation=activation, name='tcn1')(x)
    x = TCN(64, dilations=[1, 2, 4], return_sequences=True, activation=activation, name='tcn2')(x)

    avg_pool = GlobalAveragePooling1D()(x)
    max_pool = GlobalMaxPooling1D()(x)

    conc = concatenate([avg_pool, max_pool])
    conc = Dense(16, activation="relu")(conc)
    conc = Dropout(0.1)(conc)
    outp = Dense(2, activation="softmax")(conc)

    model = Model(inputs=inp, outputs=outp)

    return model

def predict_text(df, model):
    test_cv = list(df.Sentence)
    tokenizer.fit_on_texts(test_cv)

    # processing
    test_sequences = tokenizer.texts_to_sequences(test_cv)
    max_len = 179
    CVtest = pad_sequences(test_sequences, maxlen=max_len, padding=padding_type, truncating=trunc_type)

    # predict CV_test
    predict = model.predict(CVtest, verbose=0)
    yhat_probs = np.argmax(predict, axis=1)

    # Knowleadge predict
    knowledge = ''
    for i in range(len(test_cv)):
        if (yhat_probs[i] == 1):
            knowledge += ' ' + test_cv[i]

    return knowledge


def read_pdf_resumes(res, model_path):
    # Load model
    model = define_model()
    model.load_weights(model_path)

    df_path = res
    df = pdf2line(df_path)
    # print(df)

    knowleadge = predict_text(df, model)
    print('----------------------------')
    return knowleadge
