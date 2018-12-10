class Node {
    constructor(val)
    {
        this.val = val;
        this.next = null;
    }
}


class LinkedList {
    constructor()
    {
        this.head = null;
        this.length = 0;
    }
    insert(val) {
        var newNode = new Node(val);
        this.head = newNode;
        this.length += 1;
        return val;
    }
}
