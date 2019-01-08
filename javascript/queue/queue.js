class Node {
    constructor(val, next = null)
    {
        this.val = val;
        this.next = next;
    }
}

class Queue {
    constructor() {
        this.front = null;
        this.back = null;
        this.length = 0;
    }
    insert(val) {
        if (this.front) {
            var current = this.front;
        }
        var newNode = new Node(val);
        this.front = newNode;
        if (! this.back) {
            newNode = this.back;
        }
        if (current) {
            newNode.next = current;
        }
        this.length += 1;
        return val;
    }
    dequeue(val) {
        if (this.queue.length > 0) {
            this.length -= 1;
            var temp = this.front;
            this.front = this.queue[-1];
            return (temp);
        }
    }
}




