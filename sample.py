# -*- coding: utf-8 -*-

import os
import sys
import argparse
import numpy as np
from keras.models import model_from_json

BASE_KEY = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'M': 4}


def check_input(input_seq):
    print(type(input_seq))
    if not type(input_seq) == str:
        print('The input must be a string.')
        sys.exit(1)
    if not len(input_seq) == 170:
        print('The sequence should be 170-mer.')
    if not input_seq.count('M') == 1:
        print('"M" should be appear only once in the sequence.')


def main(argv=sys.argv):
    parser = argparse.ArgumentParser(description='Receive a single 170-mer base sequence, and return the probabality of ESM')
    if len(argv) != 2:
        parser.parse_args(['-h'])
    parser.add_argument('sequence')
    args = parser.parse_args()
    input_seq = args.sequence
    check_input(input_seq)
    input_vec = np.zeros((1, 170, 5))
    for i in range(170):
        try:
            input_vec[0][i][BASE_KEY[input_seq[i]]] = 1
        except KeyError:
            print('Each base must be "A", "C", "G", "T", or "M"')
            sys.exit(1)
    model = model_from_json(open(os.path.join(os.path.dirname(__file__), 'seq_based_DNN.json')).read())
    model.load_weights(os.path.join(os.path.dirname(__file__), 'seq_based_DNN.hdf5'))
    predict = model.predict(input_vec, batch_size=1, verbose=0)
    print ('The probability of ESM: {}'.format(predict[0][0]))


if __name__ == '__main__':
    main()
