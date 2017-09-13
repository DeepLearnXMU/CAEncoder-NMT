#! /usr/bin/python

'''
    Evaluate the translation result from Neural Machine Translation
'''

import sys
import os
import re
import time
import string

run = os.system
path = os.path.dirname(os.path.realpath(__file__))

def eval_trans(src_sgm, ref_sgm, trs_plain):

    cmd = ("%s/multi-bleu.perl %s < %s > %s.eval.nmt" \
            %(path, ref_sgm, trs_plain, trs_plain))
    print cmd
    run(cmd)
    eval_nmt = ''.join(file('%s.eval.nmt' % trs_plain, 'rU').readlines())

    bleu = float(eval_nmt.strip().split(',')[0].split(' ')[-1])

    return bleu

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print '%s src_sgm(meaningless), ref_sgm(plain ref), trs_plain(plain trans)' % sys.argv[0]
        sys.exit(0)

    src_sgm = sys.argv[1]
    ref_sgm = sys.argv[2]
    trs_plain = sys.argv[3]

    eval_trans(src_sgm, ref_sgm, trs_plain)
