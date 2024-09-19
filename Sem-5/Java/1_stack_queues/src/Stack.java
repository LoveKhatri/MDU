public class Stack {
    private int top;
    private final int size;
    private final int[] stack;

    public Stack(int size){
        this.size = size;
        this.stack = new int[size];
        this.top = -1;
    }

    public void push(int value){
        if(top == size-1){
            System.out.println("Stack is full");
            return;
        }
        stack[++top] = value;
    }

    public void pop(){
        if (top == -1){
            System.out.println("Stack is empty");
            return;
        }
        System.out.println("Popped Value: "+stack[top]);
        top-=1;
    }

    public void display(){
        int dtop = this.top;
        while (dtop > -1) { 
            System.out.printf("| %d |\n", stack[dtop]);   
            dtop--;
        }
        System.out.println("-----");
    }
}
