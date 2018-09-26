class HashTable:
    """A class for a hash table."""
    entries_count = 0
    alphabet_size = 52

    def __init__(self, size=8192):
        self.table_size = size
        self.hashtable = []

    def __repr__(self):
        return(f'Graph: {self.table_size}')

    def __str__(self):
        return f'{self.table_size}'

    def _hash_key(self, key):
        """Create a hash from a given key.
        args:
            key: a string to hash
        returns: an integer corresponding to hashtable index
        """
        hash_ = 0
        for i, c in enumerate(key):
            hash_ += pow(
                self.alphabet_size, len(key) - i - 1) * ord(c)
        return hash_ % self.table_size

    def set(self, key, value):
        """Add a key and value into the hash table.
        args:
            key: the key to store
            value: the value to store
        """
        return self.hashtable[self.hash_key(key)].insert({key: value})

    def get(self, key):
        """Retrieve a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        count = 0
        current = self.hashtable[self.hash_key(key)][count]

        while len(current):
            if key in current.value.keys():
                return current.value[key]
            count += 1
            current = self.hashtable[self.hash_key(key)][count]

    def remove(self, key):
        """Retrieve and remove a value from the hash table by key.
        args:
            key: a string to find the value in the hash table
        returns: the value stored with the key
        """
        item = self.hashtable[self.hash_key(key)]
        current = item[0]
        last = current
        count = 0
        while len(current):
            if key in current.val.keys():
                if last is not current:
                    count += 1
                    last[count] = current[count]
                else:
                    item[0] = current[count]
            try:
                return current.val[key]
            except KeyError:
                return []

            last = current
            count += 1
            current = current[count]
