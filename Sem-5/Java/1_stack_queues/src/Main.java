class Main{
    public static void main(String[] args) {
        Stack stack = new Stack(4);

        System.out.println("Popping from an empty stack");
        stack.pop();

        System.out.println("Inserting values into the stack");
        for (int i = 0; i < 4; i++) {
            stack.push(i);
        }

        System.out.println("Displaying elements of the stack");
        stack.display();
        
        System.out.println("Popping 2 elements from the stack");
        stack.pop();
        stack.pop();
        
        System.out.println("Displaying elements of the stack");
        stack.display();

        Queue q = new Queue(5);

        q.display();
        q.dequeue();

        for (int i = 0; i < 4; i++) {
            q.enqueue(i);
        }

        q.display();

        q.dequeue();
        q.dequeue();

        q.display();
    }
}