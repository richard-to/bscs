LIB=-L/usr/local/lib -Llib
INC=-I/usr/local/include -Iinclude

all: binary_search_test insertion_sort_test stack_test queue_test gcd_test fib_test

binary_search_test: binary_search.o
	g++ ${LIB} ${INC} test/algorithms/binary_search.cpp -lbinary_search.o -lgtest -lgtest_main -o bin/binary_search_test

binary_search.o:
	g++ -c ${INC} src/algorithms/binary_search.cpp -o lib/binary_search.o

insertion_sort_test: insertion_sort.o
	g++ ${LIB} ${INC} test/algorithms/insertion_sort.cpp -linsertion_sort.o -lgtest -lgtest_main -o bin/insertion_sort_test

insertion_sort.o:
	g++ -c ${INC} src/algorithms/insertion_sort.cpp -o lib/insertion_sort.o

stack_test: stack.o
	g++ ${LIB} ${INC} test/data_structures/stack.cpp -lstack.o -lgtest -lgtest_main -o bin/stack_test

stack.o:
	g++ -c ${INC} src/data_structures/stack.cpp -o lib/stack.o

queue_test: queue.o
	g++ ${LIB} ${INC} test/data_structures/queue.cpp -lqueue.o -lgtest -lgtest_main -o bin/queue_test

queue.o:
	g++ -c ${INC} src/data_structures/queue.cpp -o lib/queue.o

gcd_test: gcd.o
	g++ ${LIB} ${INC} test/algorithms/gcd.cpp -lgcd.o -lgtest -lgtest_main -o bin/gcd_test

gcd.o:
	g++ -c ${INC} src/algorithms/gcd.cpp -o lib/gcd.o

fib_test: fib.o
	g++ ${LIB} ${INC} test/algorithms/fib.cpp -lfib.o -lgtest -lgtest_main -o bin/fib_test

fib.o:
	g++ -c ${INC} src/algorithms/fib.cpp -o lib/fib.o

clean:
	rm -rf bin/*
	rm -rf lib/*