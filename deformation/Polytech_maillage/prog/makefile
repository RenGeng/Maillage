#let's pass the compil in make argument, eg:clang
COMPIL=gcc

CC=$(COMPIL) -g
CFLAG = -lm -Wall
OBJS= \
	main.o \
	InOut.o \
	libmesh5.o \

all: main

main: $(OBJS)
	$(CC) -o main $(OBJS) $(CFLAG)

libmesh5: libmesh.c 
	$(CC) -c libmesh5.c -o libmesh.o

InOut: InOut.c
	$(CC) -c InOut.c -o InOut.o $(CFLAG)



clean:
	$(RM) -r $(OBJS) myprogram


