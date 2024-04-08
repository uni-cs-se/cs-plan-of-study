#!/bin/bash

trap "kill 0" SIGINT

for d in ./con/*/ ; do 
	cd $d
	uvicorn index:app --reload --port `basename $d` &
	cd ../../
done

wait
