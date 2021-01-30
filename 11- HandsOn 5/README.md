# Convolutional Sequence to Sequence learning

This assignment's objective is to build convolution based Sequence to Sequence machine translation model to translate sentences from German to English.

Compared to recurrent networks, convolutional models create fixed size context representations and this can be made larger by stacking convolutional layers on top of each other. This allows CNN control over the maximum length of of dependencies to be modeled. Similar to the idea of edges and gradients to textures to patterns to parts of objects being captured in multiple convolution blocks in image domain, Multi-layered CNN network creates hierarchical representation over the input sentence where nearby input elements interact at lower layers and distant elements interact at higher layers. Computations in convolutional network is applied over all elements in parallel in training and exploits the GPU hardware.

The inner working of the convolution model's encoder-decoder modules is explained [here.](https://dev.to/shashankholla_10/convolutional-sequence-to-sequence-learning-a-closer-look-bdn)

## Architecture

### Encoder

Encoder's role is to encode the input sentence which is in the source language into a context vector.
Encoder produces two context vectors per token. So if the input German sentence has 4 tokens, it would produce 8 context vectors. The two context vectors produced by the encoder are 'conved vector' and 'combined vector'. Conved vector is produced by passing each token through a few fully connected layers and the convolutional block. Combined vector is the sum of the convolved vector and the embedding of the token.

![](images/Encoder.png)

### Decoder

Decoder's role is to use the context vector to produce the output sentence in the target language. Decoder model, unlike recurrent models, predicts all the tokens in parallel in the target sentence.

![](images/Decoder.png)

## Results

### Train/Validation loss vs epoch

![](images/lossvsepoch.png)

### Test Loss and Bleu score

| Test Loss | Bleu Score |
|-----------|------------|
|  1.792    |   34.89    |


### Source sentence to attention mapping

X-axis : source sentence

Y-axis : predicted translation

Source sentence = 'ein', 'mann', 'in', 'einer', 'weste', 'sitzt', 'auf', 'einem', 'stuhl', 'und', 'hält', 'magazine', '.'

Target sentence = 'a', 'man', 'in', 'a', 'vest', 'is', 'sitting', 'in', 'a', 'chair', 'and', 'holding', 'magazines', '.'

Predicted sentence = 'a', 'man', 'in', 'a', 'vest', 'is', 'sitting', 'on', 'a', 'chair', 'holding', '<unk>', '.', '<EOS>'

The lighter the square at the intersection between two words, the more attention the model gave to that source word when translating that target word.

![](images/attention.png)


