# CAEncoder-NMT
Source code for A Context-Aware Recurrent Encoder for Neural Machine Translation. Our model is much faster than the standard encoder-attention-decoder model, and obtains a BLEU point of 22.57 on English-German translation task, compared with that of 20.87 yielded by dl4mt.

If you use this code, please cite <a href="https://doi.org/10.1109/TASLP.2017.2751420">our paper</a>:
```
@article{Zhang:2017:CRE:3180104.3180106,
 author = {Zhang, Biao and Xiong, Deyi and Su, Jinsong and Duan, Hong},
 title = {A Context-Aware Recurrent Encoder for Neural Machine Translation},
 journal = {IEEE/ACM Trans. Audio, Speech and Lang. Proc.},
 issue_date = {December 2017},
 volume = {25},
 number = {12},
 month = dec,
 year = {2017},
 issn = {2329-9290},
 pages = {2424--2432},
 numpages = {9},
 url = {https://doi.org/10.1109/TASLP.2017.2751420},
 doi = {10.1109/TASLP.2017.2751420},
 acmid = {3180106},
 publisher = {IEEE Press},
 address = {Piscataway, NJ, USA},
}
```

## How to Run?

A demo case is provided in the `work` directory

### Training
You need process your training data and set up a configuration file, as the `german.py` does. The `train.py` script is used for training.

### Testing
All you need is the `sample.py` script. Of course, the directory for vocabularies and model files are required.


For any comments or questions, please email <a href="mailto:zb@stu.xmu.edu.cn">Biao Zhang</a>.
