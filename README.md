# CAEncoder-NMT
Source code for A Context-Aware Recurrent Encoder for Neural Machine Translation. Our model is much faster than the standard encoder-attention-decoder model, and obtains a BLEU point of 22.57 on English-German translation task, compared with that of 20.87 yielded by dl4mt.

If you use this code, please cite <a href="https://doi.org/10.1109/TASLP.2017.2751420">our paper</a>:
```
This paper is now accepted by IEEE/ACM Transactions on Audio, Speech, and Language Processing.
```

## How to Run?

A demo case is provided in the `work` directory

### Training
You need process your training data and set up a configuration file, as the `german.py` does. The `train.py` script is used for training.

### Testing
All you need is the `sample.py` script. Of course, the directory for vocabularies and model files are required.


For any comments or questions, please email <a href="mailto:zb@stu.xmu.edu.cn">Biao Zhang</a>.