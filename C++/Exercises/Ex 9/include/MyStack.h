template <class T>
class MyStack{

 private:
    int size{};
    int head{};
    T* stack;

 public:

    explicit MyStack(int size) {
        this->size = size;
        this->head = 0;
        this->stack = new T[size];
    }

    MyStack(const MyStack& oldStack) {
        this->head = oldStack.head;
        this->size = oldStack.size;
        this->stack = new T[oldStack.size];

        for (int i = 0; i < oldStack.size; i++) {
            this->stack[i] = oldStack.stack[i];
        }
    }

    ~MyStack() {
        delete[] stack;
    }

    ////////////////////////////////////////////////

    [[nodiscard]] bool isFull() const {
        return (head == size);
    }

    [[nodiscard]] bool isEmpty() const {
        return (head == 0);
    }

    ////////////////////////////////////////////////

    T get() const {
        if (!isEmpty()) {
            return this->stack[this->head - 1];
        } else return -1;
    }

    T pop() {
        if (!isEmpty()) {
            this->head-=1;
            T value = this->stack[this->head];
            return value;
        } else return -1;
    }

    void push(T pushed) {
        if (!isFull()) {
            this->stack[this->head] = pushed;
            this->head++;
        }
    }
};
