dict(
        # network structure 
        dim_word=620,  # word vector dimensionality
        dim=1000,      # the number of LSTM units
        n_words_src=40000,  # source vocabulary size
        n_words=40000,  # target vocabulary size
        maxlen=80,  # maximum length of the description

        # process control
        max_epochs=10,
        finish_after=100000000,  # finish after this many updates
        dispFreq=1,
        saveto='search_model.npz',
        validFreq=5000,
        validFreqLeast=100000,
        validFreqFires=150000,
        validFreqRefine=3000,
        saveFreq=1000,   # save the parameters after every saveFreq updates
        sampleFreq=1000,   # generate some samples after every sampleFreq
        reload_=True,
        overwrite=True,
        is_eval_nist=False,

        # optimization
        decay_c=0.,  # L2 regularization penalty
        alpha_c=0.,  # alignment regularization
        clip_c=5.,   # gradient clipping threshold
        lrate=1.0,   # learning rate
        optimizer='adadelta',
        batch_size=80,
        valid_batch_size=80,
        use_dropout=False,
        shuffle_train=0.999,
        seed=1234,

        # development evaluation
        use_bleueval=True,
        save_devscore_to='search_bleu.log',
        save_devtrans_to='search_trans.txt',
        beam_size=10,
        proc_num=1,
        normalize=False,
        output_nbest=1,

        # datasets
        use_bpe=True,
        datasets=[
            '/Path-to-training-data/train.en.bpe',
            '/Path-to-training-data/train.de.bpe'],
        valid_datasets=['/Path-to-dev-data/dev.en.plain.bpe',
                        '/Path-to-dev-data/dev.de'],
        dictionaries=[
            '/Vocabulary/vocab.en.pkl',
            '/Vocabulary/vocab.de.pkl'],
)
