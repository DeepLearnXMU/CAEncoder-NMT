'''
Translates a source file using a translation model.
'''
import argparse

import numpy
import cPickle as pkl

from nmt import (build_sampler, gen_sample, load_params,
                 init_params, init_tparams)

def translate_model(model, options, k, normalize, n_best):

    from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams
    from theano import shared
    trng = RandomStreams(1234)
    use_noise = shared(numpy.float32(0.))

    # allocate model parameters
    params = init_params(options)

    # load model parameters and set theano shared variables
    params = load_params(model, params)
    tparams = init_tparams(params)

    # word index
    f_init, f_next = build_sampler(tparams, options, trng, use_noise)

    def _translate(seq):
        # sample given an input sequence and obtain scores
        sample, score = gen_sample(tparams, f_init, f_next,
                                   numpy.array(seq).reshape([len(seq), 1]),
                                   options, trng=trng, k=k, maxlen=200,
                                   stochastic=False, argmax=False)

        # normalize scores according to sequence lengths
        if normalize:
            lengths = numpy.array([len(s) for s in sample])
            score = score / lengths
        if n_best > 1:
            sidx = numpy.argsort(score)[:n_best]
        else:
            sidx = numpy.argmin(score)
        return numpy.array(sample)[sidx], numpy.array(score)[sidx]

    return _translate


def main(model, dictionary, dictionary_target, source_file, saveto, k=5,
         normalize=False, n_process=5, chr_level=False, n_best=1):

    # load model model_options
    with open('%s.pkl' % model, 'rb') as f:
        options = pkl.load(f)

    # load source dictionary and invert
    with open(dictionary, 'rb') as f:
        word_dict = pkl.load(f)
    word_idict = dict()
    for kk, vv in word_dict.iteritems():
        word_idict[vv] = kk
    word_idict[0] = '<eos>'
    word_idict[1] = 'UNK'

    # load target dictionary and invert
    with open(dictionary_target, 'rb') as f:
        word_dict_trg = pkl.load(f)
    word_idict_trg = dict()
    for kk, vv in word_dict_trg.iteritems():
        word_idict_trg[vv] = kk
    word_idict_trg[0] = '<eos>'
    word_idict_trg[1] = 'UNK'

    # create input and output queues for processes
    trser = translate_model(model, options, k, normalize, n_best)

    # utility function
    def _seqs2words(caps):
        capsw = []
        for cc in caps:
            ww = []
            for w in cc:
                if w == 0:
                    break
                ww.append(word_idict_trg[w])
            trs = ' '.join(ww)
            if trs.strip() == '':
                trs = 'UNK'
            capsw.append(trs)
        return capsw

    xs = []
    srcs = []
    with open(source_file, 'r') as f:
        for idx, line in enumerate(f):
            if chr_level:
                words = list(line.decode('utf-8').strip())
            else:
                words = line.strip().split()
            x = map(lambda w: word_dict[w] if w in word_dict else 1, words)
            x = map(lambda ii: ii if ii < options['n_words'] else 1, x)
            x += [0]
            xs.append((idx, x))
            srcs.append(line.strip())
    print 'Data loading over'

    print 'Translating ', source_file, '...'
    trans = []
    scores = []
    for req in xs:
        idx, x = req[0], req[1]
        tran, score = trser(x)
        trans.append(tran)
        scores.append(score)
        print 'the %d-th sentence' % idx
        print 'source side:\t%s' % srcs[idx]
        print 'target translation:\t%s' % ''.join(_seqs2words([trans[-1]]))

    if n_best == 1:
        trans = _seqs2words(trans)
    else:
        n_best_trans = []
        for idx, (n_best_tr, score_) in enumerate(zip(trans, scores)):
            sentences = _seqs2words(n_best_tr)
            for ids, trans_ in enumerate(sentences):
                n_best_trans.append(
                    '|||'.join(
                        ['{}'.format(idx), trans_,
                         '{}'.format(score_[ids])]))
        trans = n_best_trans

    with open(saveto, 'w') as f:
        print >>f, '\n'.join(trans)
    print 'Done'


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', type=int, default=5, help="Beam size")
    parser.add_argument('-n', action="store_true", default=False,
                        help="Normalize wrt sequence length")
    parser.add_argument('-c', action="store_true", default=False,
                        help="Character level")
    parser.add_argument('-b', type=int, default=1, help="Output n-best list")
    parser.add_argument('model', type=str)
    parser.add_argument('dictionary', type=str)
    parser.add_argument('dictionary_target', type=str)
    parser.add_argument('source', type=str)
    parser.add_argument('saveto', type=str)

    args = parser.parse_args()

    main(args.model, args.dictionary, args.dictionary_target, args.source,
         args.saveto, k=args.k, normalize=args.n,
         chr_level=args.c, n_best=args.b)
