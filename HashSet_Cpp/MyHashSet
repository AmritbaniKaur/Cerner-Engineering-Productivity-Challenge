// cerner_2^5_2019
/**
 * The MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * bool param_3 = obj.contains(key);
 */ 
class MyHashSet 
{
private:
    set<int> hashSet;    
public:
    MyHashSet() {}
    void add(int key) // Creates the specified element
    {
        hashSet.insert(key);    
    }
    void remove(int key) // Removes the specified element
    {
        hashSet.erase(key);    
    }
    bool contains(int key) // Returns true if this set contains the specified element
    {
        bool result = false;
        set<int>::iterator it1; 
        for (it1 = hashSet.begin(); it1 != hashSet.end();  ++it1) 
        {
            if(*it1 == key)
            {
                result = true;
                return result;
            }
        }
        return result;
    }
};