public class Queue {
    private final int[] queue;
    private final int size;
    private int front;
    private int rear;

    public Queue(int size) {
        this.size = size;
        this.queue = new int[size];
        this.front = 0;
        this.rear = -1;
    }

    public void enqueue(int value) {
        if (this.rear == this.size - 1) {
            System.out.println("Overflow");
        } else {
            queue[++rear] = value;
        }
    }

    public void dequeue() {
        if (front > rear) {
            System.out.println("Underflow");
        }else {
            System.out.println("Popped: "+queue[++front]);
        }
    }

    public void display(){
        
        int drear = rear;
        int dfront = front;

        System.out.printf("Queue: ");
        for (int i = dfront; i < drear; i++) {
            System.out.printf("%d ", queue[i]);
        }
        System.out.println();
    }
}
