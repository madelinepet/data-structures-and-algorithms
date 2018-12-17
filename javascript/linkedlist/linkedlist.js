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
    if(ll.head) {
        var counter = (ll.length - k);
        var currentNode = ll.head;
        while(counter > 1) {
            currentNode = currentNode.next;
            counter -= 1;
        }
        return(currentNode.val);
    }
    else {
        return(-1);
    }
};

LinkedList.prototype.llMerge = function(ll, llTwo) {
    // start at the heads
    let currentOne = ll.head;
    let currentTwo = llTwo.head;

    while (currentOne && currentTwo) {
        var temp = currentOne.next;
        // assign next of ll to next of llTwo
        currentOne.next = currentTwo;
        var temp2 = currentTwo.next;
        // assign next of ll to former next of ll
        currentTwo.next = temp;
        currentOne = temp;
        currentTwo = temp2;


    }
    return ll.head;
};
