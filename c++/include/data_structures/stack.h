class StackNode
{
public:
    StackNode(int value);
    ~StackNode();
    int value_;
    StackNode* next_;
};

class Stack
{
public:
    Stack();
    ~Stack();
    bool empty();
    void push(int value);
    int pop();
    int peek();
    void clear();
private:
    StackNode* head_;
};