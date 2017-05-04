#!/bin/sh
while [[ 1 ]]; do
	cur_dir=$(pwd)
	python $cur_dir"/get_tieba_email.py"
done