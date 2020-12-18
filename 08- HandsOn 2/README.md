# RNN hands On

The objective of these assignments are - 

a) Design and train Seq2Seq model with 3 LSTM layers to translate French sentences to German.

b) Write Python programs/functions snippets for dataset preparation.


## Seq2Seq model for French to German langauge translation

Based on encoder-decoder architecture. Encoder learns from French sentence training data to generate context vector. Inputs to the encoder are hidden state from previous cell and current timestep's embedded input.

Decoder takes in the hidden state of previous decoder timestep and also the predicted word from the previous timestep or ground truth (teacher forcing). Hidden state of the decoder are fed to a linear layer to predict the actual word.


## Collection of Python program/functions

Snippets of Python program/functions as part of training data preparation for language processing.
