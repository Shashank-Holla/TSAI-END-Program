# RNN Hands-On 3

The objective of this assignment is to train Seq2Seq machine translation models on conversational datasets.

With previous RNN based Encoder-Decoder models, the decoder crammed a lot of information into the hidden state. This required the hidden state to contain information about the whole of the source sequence, as well as all of the tokens that have been decoded so far during decoding. This resulted in information compression at context vector resulting in less efficient models. The following Seq2Seq model variants are considered-

1. Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation

2. Neural Machine Translation by Jointly Learning to Align and Translate

## Model Architecture

### Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation

![](images/seq2seq.png)

In this RNN Encoder-Decoder based approach, the decoder takes the context vector (generated from encoder) along with embedded input token and previous hidden state to predict the next hidden state. The context vector is fed to the linear layer along with hidden output to predict the next token.


### Neural Machine Translation by Jointly Learning to Align and Translate

![](images/seq2seq10.png)

The previous models for neural machine translation uses encoder-decoder architecture and consists of an encoder that encodes the source sentence into a fixed length context vector from which decoder generates the translation. This model puts forth that the use of a fixed length context vector is a bottleneck in improving the performance of this basic encoder-decoder architecture. It proposes to extend this by allowing a model to automatically (soft-)search for parts of a source sentence that are relevant to predicting a target word, without having to form these parts as a hard segment explicitly.

Encoder uses bidirectional GRU to encode the context vector. Bidirection GRUs create 2 context vector, one for each direction. Decoder block requires single context vector. This is created by concatenating the two context vectors together, passing them through a linear layer and applying the tanh activation function.

Attention vector is calculated from previous hidden state of the decoder, st−1 , and all of the stacked forward and backward hidden states from the encoder. Attention vector calculates how well each encoder hidden state matches the previous decoder hidden state.

Decoder uses the weighted attention vector along with previous decoder hidden state to calculate decoder hidden state. Attention vector is also used along with decoder hidden state to predict the next word.

## Datasets

### NarrativeQA

NarrativeQA is a data set constructed to encourage deeper understanding of language. This dataset involves reasoning about reading whole books or movie scripts. This dataset contains approximately 45,000 pairs of free text question-and-answer pairs

### OpenBookQA

OpenBookQA, inspired by open-book exams to assess human understanding of a subject. The open book that accompanies our questions is a set of 1329 elementary level scientific facts. Approximately 6,000 questions focus on understanding these facts and applying them to new situations.

### QASC

QASC is a question-and-answer data set that focuses on sentence composition. It consists of 9,980 8-channel multiple-choice questions on elementary school science (8,134 train, 926 dev, 920 test)


## Results

Following are results captured on test set (validation set in case test set was not available). 

| Dataset     | Test/Validation Loss | Test/Validation set perplexity score |
|-------------|----------------------|--------------------------------------|
| NarrativeQA |                      |                                      |
| openBookQA  |                      |                                      |
| QASC        |                      |                                      |
|             |                      |                                      |
