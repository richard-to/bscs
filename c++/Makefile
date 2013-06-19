LIB=-L/usr/local/lib -Llib
INC=-I/usr/local/include -Iinclude

binary_search_test: binary_search.o
	g++ ${LIB} ${INC} test/algorithms/binary_search.cpp -lbinary_search.o -lgtest -lgtest_main -o bin/binary_search_test

binary_search.o:
	g++ -c ${INC} src/algorithms/binary_search.cpp -o lib/binary_search.o

stack_test: stack.o
	g++ ${LIB} ${INC} test/data_structures/stack.cpp -lstack.o -lgtest -lgtest_main -o bin/stack_test

stack.o:
	g++ -c ${INC} src/data_structures/stack.cpp -o lib/stack.o

clean:
	rm -rf bin/*
	rm -rf lib/*