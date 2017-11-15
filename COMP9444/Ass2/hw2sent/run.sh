#!/bin/bash

file_index=$1;

touch "$1_train_acc.txt"
touch "$1_test_acc.txt"
touch "$1_train_loss.txt"
touch "$1_test_loss.txt"

python "$1.py"
