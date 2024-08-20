# Implementing Hash Tables as an ADT
"""
1. In this implementation the hash table is written as a class
2. The special functions like get item and set item are overridden
"""
class hashTable():
    def __init__(self, capacity):
        self.hashTable = [[] for i in range(capacity)]
    
    def hashFunc(self,key):
        sum = 0
        for char in key:
            sum = sum + ord(char)
        index = sum % 10
        return index

    def __setitem__(self, key, value):
        index = self.hashFunc(str(key))
        lis = self.hashTable[index]
        for i in range(len(lis)):
            if lis[i][0] == key:
                lis[i] = (key, value)
                return
        self.hashTable[index].append((key,value))
        return

    def __getitem__(self, key):
        index = self.hashFunc(str(key))
        if len(self.hashTable[index]) == 0:
            print("KEY ERROR")
            return
        
        for lis in self.hashTable[index]:
            if lis[0] == key:
                return lis[-1]
        
    def update(self, key, value):
        index = self.hashFunc(key)
        lis = self.hashTable[index]
        length = len(lis)
        for i in range(length):
            if lis[i][0] == key:
                lis[i] = (key,value)
    
    def delete(self, key):
        index = self.hashFunc(key)
        if len(self.hashTable) == 0:
            print("KEY ERROR")
            return
        
        lis = self.hashTable[index]
        length = len(self.hashTable[index])
        for i in range(length):
            if lis[i][0] == key:
                lis.pop(i)
        
    
    def __repr__(self):
        content = ""
        for lis in self.hashTable:
            if len(lis) == 0:
                continue
            elif len(lis) == 1:
                content += str(lis[0][0]) + " : " + str(lis[0][-1]) + " , "
            else:
               for chain in lis:
                   content +=str(chain[0]) + " : " + str(chain[-1]) + " , "
        return "{" + content.strip(" , ") + "}"
   
    def keys(self):
        result = []
        for lis in self.hashTable:
            if len(lis) == 0:
                continue
            
            elif len(lis) == 1:
                result.append(lis[0][0])
                
            else:
                for chain in lis:
                    result.append(chain[0])
        return result
    
    
    def values(self):
        result = []
        for lis in self.hashTable:
            if len(lis) == 0:
                continue
            
            elif len(lis) == 1:
                result.append(lis[0][-1])
                
            else:
                for chain in lis:
                    result.append(chain[-1])
        return result
    
    def items(self):
        result = []
        for lis in self.hashTable:
            if len(lis) == 0:
                continue
            
            elif len(lis) == 1:
                result.append(lis[0])
                
            else:
                for chain in lis:
                    result.append(chain)
        return result
    
    def __iter__(self):
        for key in self.keys():
            yield key
        return
    
# Driver Code
def main():
    h = hashTable(10)
    h["sneha"] = 131
    h["C"] = 345
    h["sreekar"] = 133
    h["singaram"] = 130
    print("The hashtable = ", h)
    
    h["sneha"] = "python"
    print("The updated dictionary: ",h)
    
    print("The list of keys:", h.keys())
    print("The list of values:", h.values())
    print("The list of items: ", h.items())
    
    h.delete("singaram")
    print("The dictionary after deleting: ", h)
    
    print("Iteration: ")
    for key in h:
        print(key)


