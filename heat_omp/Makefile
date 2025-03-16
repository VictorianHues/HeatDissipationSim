# Better to just add the pin binary to your $PATH
#PIN_ROOT=~/projects/pin/

.PHONY: run_with_tracing traces clean
MCPS_TRACER_ROOT=/home/spolstra/projects/mcps-tracer

# Take number of threads from environment var P, use 2 as default
P ?= 2

CURR_DIR=$(notdir $(basename $(shell pwd)))
PRJ=$(CURR_DIR)
SRC=$(wildcard *.c)
OBJ=$(patsubst %.c,%.o,$(SRC))
ANNOT_LIB=../lib/libannotation.a

CC=gcc
INCLUDES=-I../include
ifndef DEBUG
CFLAGS=-O2 -std=gnu99 -lm -fopenmp
LDFLAGS=-L../lib -lannotation -lm -fopenmp
else
CFLAGS=-O0 -g3 -std=gnu99 -fsanitize=address -fopenmp
LDFLAGS=-L../lib -lm -fsanitize=address -fopenmp
endif

all: $(PRJ)

$(ANNOT_LIB):
	make -C ../lib

$(PRJ): $(OBJ) $(ANNOT_LIB)
	$(CC) $(CFLAGS) $(INCLUDES) $(OBJ) -o $@ $(LDFLAGS)

%.o: %.c
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

run_with_tracing: all
	pin -t $(MCPS_TRACER_ROOT)/obj-intel64/tool/tracer.so -- ./$(PRJ) -i 1 -p $(P)

traces: run_with_tracing
	$(MCPS_TRACER_ROOT)/scripts/trace_converter.py address_log memory_trace.trf

clean:
	-rm -f $(OBJ) $(PRJ) address_log.* memory_trace.trf
	-make -C ../lib clean
