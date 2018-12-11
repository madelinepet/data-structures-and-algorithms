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
        if (this.head) {
            var current = this.head;
        }
        var newNode = new Node(val);
        this.head = newNode;
        if (current) {
            newNode.next = current;
        }
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
        this.length += 1;
        return val;
    }

    insertBefore(val, target) {
        if (this.head) {
            if (this.head.val === target) {
                var current = this.head;
                this.head = new Node(val, this.head);
                this.head.next = current;
                this.length += 1;
                return this.head;
            }
            else {
                current = this.head;
                while(current.next.val !== target) {
                    current = current.next;
                }
                current.next = new Node(val, current.next);
                this.length += 1;
                return current.next;
            }
        }
        else {
            this.insert(val);
        }
    }
    insertAfter(val, target) {
        if (this.head) {
            var current = this.head;
            while (current.val !== target) {
                current = current.next;
            }
            current.next = new Node(val, current.next)  ;
            this.length += 1;
            return current.next;
        }
        else {
            this.insert(val)
        }
    }

    removeVal(value) {
        if (this.head.val === value) {
            if (this.head.next) {
                this.head = this.head.next;
                this.length -= 1;
                return value;
            }
            else {
                this.head = null;
                this.length -= 1;
            }
        }
        if (this.includes(value)) {
            var current = this.head;
            var prev = this.head;
            while (current && current.val !== value) {
                prev = current;
                current = current.next;
            }
            prev.next = current.next;
            this.length -= 1;
            return value;

        }
        else {
            return -1;
        }
    }
}

LinkedList.prototype.kthFromEnd = function(ll, k) {
    if (ll.head) {
        var counter = 0;
        var currentNode = ll.head;
        while (currentNode && currentNode.next) {
            counter += 1;
            currentNode = currentNode.next;
        }
        if (k > counter) {
            return('exception')
        }
        var r = counter - (k - 1);
        currentNode = ll.head;
        while (counter < r) {
            currentNode = currentNode.next;
            counter += 1;
        }
        return currentNode.val;
    }
};
