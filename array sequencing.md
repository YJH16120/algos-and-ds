# Understanding what array sequencing is

assume you have a list of a = `[1, 2, 3, 4]`, every element in that list, is stored in memory (specifically in the RAM). When you want to grab a value by indexing it like so `a[0]` python will go to the memory location where the element '1' is located, and grab the value.

And each element takes a number of bytes, where 8 bits = 1 bytes. If for example each element in that list
takes up 1 byte, then python would need to allocate 4 bytes in memory to hold those values. But python doesn't
allocated exactly 4 bytes.

When you decide to add a new value to the list `a[4] = 5`. Python will first allocate memory for a new list, which 
double the size of the original. Then copy all of the values from list a, and add the value of '5' to the end of it.

Keep in mind that storing `[1, 2, 3, 4]` doesn't actually take 4 bytes. It actually takes 96, I only changed it to that
for simplicities sake.

It's worth nothing that when you make an empty list it has a default byte size of 64. This is to make sure it has 
memory so that you can insert values into it. Therefore, the memory needed to store values in a list will be slightly 
larger than it needs to be.

This same concepts applies to strings, lists, and tuples. As long as they can be refereced by index it applies.

