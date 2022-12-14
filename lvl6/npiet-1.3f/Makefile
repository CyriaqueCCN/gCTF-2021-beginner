##
## Makefile for the npiet interpreter (and npietedit editor)
##

prefix =	/usr/local
exec_prefix =	${prefix}

BINDIR = $(exec_prefix)/bin
MANDIR = $(prefix)/man/man1

CC = gcc

##
## warn flags for gcc compiler:
##
# GWARN = -W -Wcomment -Wpointer-arith -Wcast-qual
GWAR2 = -Wall
WARN = $(GWARN) $(GWAR2)

##
## system dependent flags:
##
DEFS = -DHAVE_CONFIG_H
##

##
## Flags for debugging and production:
##
# FLAGS = -O
FLAGS = -g -O2
# LDFLAGS =
LDFLAGS = -g

## Uncomment for profiling:
# PROF = -pg

## win cygwin static flag:
# CYG = -mno-cygwin -static
# CYG_LIBS = -lgd -lpng -lgif -lz -lm

##
## libraries:
##
LIBS =  -lpng -lz -lm $(CYG_LIBS)

##
## installation commands:
##
INSTALL =		/usr/bin/install -c
INSTALL_PROGRAM =	${INSTALL}
INSTALL_DATA =		${INSTALL} -m 644

##
## commonly used binaries:
##
SHELL = /bin/sh
RM = rm
MKDIR = mkdir

##
## And more:
##
## Anything else below here should be independent.
##
CFLAGS = $(FLAGS) $(PROF) $(CYG) $(WARN) $(DEFS) $(LIBDIRPATH)

##
## How to build the target:
##
all:		npiet npiet-foogol html

npiet:		npiet.o
	$(CC) $(LDFLAGS) $(PROF) -o npiet npiet.o $(LIBS)

npiet.o:	npiet.c
	$(CC) $(CFLAGS) $(PROF) -c npiet.c

html:	npiet.1.html npietedit.1.html npiet-foogol.1.html

npiet.1.html:	npiet.1
	groff -man -T html npiet.1 > npiet.1.html

npietedit.1.html:	npietedit.1
	groff -man -T html npietedit.1 > npietedit.1.html

npiet-foogol.1.html:	npiet-foogol.1
	groff -man -T html npiet-foogol.1 > npiet-foogol.1.html

win:
	cp -p *.html win
	cp -p npietedit win/npietedit.tcl
	chmod -x win/*

al:	ftest

npiet-foogol:           npiet-foogol.o
	$(CC) $(LDFLAGS) $(PROF) -o npiet-foogol npiet-foogol.o $(LIBS)

npiet-foogol.o:		npiet-foogol.c
	$(CC) $(CFLAGS) $(PROF) -c npiet-foogol.c

npiet-foogol.c:         npiet-foogol.y
	bison -v -t -o npiet-foogol.c npiet-foogol.y

ftest:	npiet-foogol
	./npiet-foogol a.foo


test:	check
	@echo done

check:
	(cd examples ; make)
	(cd foo ; make)

##
## installation:
##
install:	$(PRG)
	${MKDIR} -p $(DESTDIR)$(BINDIR)
	$(INSTALL_PROGRAM) npiet $(DESTDIR)$(BINDIR)
	$(INSTALL_PROGRAM) npietedit $(DESTDIR)$(BINDIR)
	$(INSTALL_PROGRAM) npiet-foogol $(DESTDIR)$(BINDIR)
	${MKDIR} -p $(DESTDIR)$(MANDIR)
	$(INSTALL_DATA) npiet.1  $(DESTDIR)$(MANDIR)
	$(INSTALL_DATA) npietedit.1 $(DESTDIR)$(MANDIR)
	$(INSTALL_DATA) npiet-foogol.1 $(DESTDIR)$(MANDIR)

##
## some possible ``clean'' targets:
## 
clean:	
	$(RM) -f npiet npiet-foogol *.o gmon.out \
	      npiet-foogol.c npiet-foogol.output *~ core

mrproper realclean clobber:	clean
	$(RM) -f config.status config.log config.h config.cache

distclean:	realclean
	$(RM) -f Makefile configure
	autoconf
	echo 'all:' > Makefile
	echo '	./configure' >> Makefile
	echo '	@echo now run make again' >> Makefile

