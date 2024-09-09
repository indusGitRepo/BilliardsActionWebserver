CC = clang
CFLAGS = -Wall -std=c99 -pedantic -g

all: _phylib.so

clean:
	rm -i *.o *.so _phylib.so

libphylib.so: phylib.o
	$(CC) phylib.o -shared -o libphylib.so -lm

phylib.o: phylib.c phylib.h
	$(CC) $(CFLAGS) -c phylib.c -fPIC -o phylib.o

phylib_wrap.c: phylib.i
	swig -python phylib.i

phylib.py: phylib.i
	swig -python phylib.i

phylib_wrap.o: phylib_wrap.c
	$(CC) $(CFLAGS) -c phylib_wrap.c -I/usr/include/python3.11/ -fPIC -o phylib_wrap.o

_phylib.so: phylib_wrap.o libphylib.so
	$(CC) $(CFLAGS) -shared phylib_wrap.o -L. -L/usr/lib/python3.11 -lpython3.11 -lphylib -o _phylib.so