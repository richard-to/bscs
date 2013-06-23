class QueueNode
{
public:
    QueueNode(int value);
    ~QueueNode();
    int value_;
    QueueNode* prev_;
};

class Queue
{
public:
    Queue();
    ~Queue();
    void enqueue(int value);
    int dequeue();
    void clear();
    bool empty();
private:
    QueueNode* head_;
    QueueNode* tail_;
};