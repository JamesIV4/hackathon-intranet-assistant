All, I need some help deciding what to do for instances where a whole context window cannot be taken.  I listed a couple examples below, but the main ?s are:   


**Can outer windows overlap into inner region?**

**Can inner windows overlap each other (left/right/center)?**

**Can inner windows overlap into outer region?**   


Examples:

We have a feature vector where keyword starts at index 2 and ends at index 18, and total length is 20.

What should the start/stop indices be for each context window?  Should we allow overlapping, enforce no overlapping, or a little of both(only inner windows can overlap, but outer cannot overlap into inner)?   


  |  feature vector start index  |  feature vector end index   
---|---|---  
Keyword  |  2  |  18   
Left-outer  |  0  |  2 or 12?   
Left-inner  |  2  |  14 or 10?   
Right-inner  |  6 or 10?  |  18?   
Right-outer  |  18 or 8?  |  20   
  
  


Also if we have a feature vector of length 14:

  |  feature vector start index  |  feature vector end index   
---|---|---  
Keyword  |  2  |  12   
Left-inner  |  2  |  14 or 12?   
Right-inner  |  2 or 0?  |  12 
