#! /bin/bash

THEANO_FLAGS='floatX=float32,device=gpu3,nvcc.fastmath=True' python train.py --proto=english-german-caencoder-nmt-bzhang --state german.py
