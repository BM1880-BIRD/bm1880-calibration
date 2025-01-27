#!/usr/bin/env python
##
## Copyright (C) Bitmain Technologies Inc.
## All Rights Reserved.
##

import argparse
import os, sys
import caffe

# Path to the Calibration.so, CNet.so, caffe_net_wrapper.so
sys.path.append('../../calibration_tool/lib')

os.environ['GLOG_minloglevel'] = '2'
from tune_utils import Tuner

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # params below used for auto tuning
    parser.add_argument('--model', metavar='input-model', help='Path to fp32 caffe model')
    parser.add_argument('--proto', metavar='input-proto', help='Path to fp32 prototxt')
    parser.add_argument('--calibration_proto', metavar='calibration-proto', help='Path to the original calibration pb2')
    parser.add_argument('--calibration_model', metavar='calibration-model', help='Path to the original calibration model')
    parser.add_argument('--output_path', metavar='output-path', help='Output directory')
    parser.add_argument('--data_list', metavar='data-list', help='Data list used in test feature diff')
    parser.add_argument('--data_limit', metavar='data-limit', help='The test data limit number')
    parser.add_argument('--image_params', metavar='image-params', help='The parameters for image preprocess')
    parser.add_argument('--tune_layer', metavar='tune-layer', help='Layer name that need to be tuned')
    parser.add_argument('--tune_diff', metavar='tune-layer-accuracy', help='Accuracy of the tune layer generated by the int8 caffemodel')
    arg = parser.parse_args()

    caffe.set_mode_gpu()
    caffe.set_device(0)
    # Call it when you are using yolo
    # caffe.yolo()

    if not os.path.isdir(arg.output_path):
	    os.mkdir(arg.output_path)

    tune = Tuner(arg)
    best_thres = tune.tune_layer(arg.tune_layer, arg.tune_diff)

    best_proto = os.path.join(arg.output_path, arg.tune_layer + '_thres_' + str(best_thres), "bmnet_tune_calibration_table.pb2")
    best_caffemodel = os.path.join(arg.output_path, arg.tune_layer + '_thres_' + str(best_thres), "bmnet_tune_int8.caffemodel")

    print('The best tune model: ' + best_caffemodel)
    print('The best tune proto: ' + best_proto)

    exit(0)
