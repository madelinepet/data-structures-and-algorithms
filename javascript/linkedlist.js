class Node {
    constructor(val, next = null)
    {
        this.val = val;
        this.next = next;
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

    includes(val) {
        var currentNode = this.head;
        while (currentNode) {
            if(currentNode.val === val) {
                return true;
            }
            currentNode = currentNode.next;
        }
        return false;
    }

    append(val) {
        var current = this.head;
        while (current.next) {
            current = current.next;
        }
        var newNode = new Node(val);
        current.next = newNode;
    }

    insertBefore(val, target) {
        if (this.head.val === target) {
            var current = this.head;
            this.head = new Node(val, this.head);
            this.head.next = current;
            return this.head;
        }
        else {
            current = this.head;
            while(current.next.val !== target) {
                current = current.next;
            }
            current.next = new Node(val, current.next);
            return current.next;
        }
    }
    insertAfter(val, target) {
        var current = this.head;
        while (current.val !== target) {
            current = current.next;
        }
        current.next = new Node(val, current.next);
        return current.next;
    }
}
