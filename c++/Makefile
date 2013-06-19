LIB=-L/usr/local/lib -Llib
INC=-I/usr/local/include -Iinclude

binary_search_test: binary_search.o
	g++ ${LIB} ${INC} test/algorithms/binary_search.cpp -lbinary_search.o -lgtest -lgtest_main -o bin/binary_search_test

binary_search.o:
	g++ -c ${INC} src/algorithms/binary_search.cpp -o lib/binary_search.o

clean:
	rm -rf bin/*
	rm -rf lib/*