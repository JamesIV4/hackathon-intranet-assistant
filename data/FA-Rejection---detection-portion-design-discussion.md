**Ananth and I had a discussion on how to handle the detection portion of FA rejection.  Please provide thoughts/comments/etc to Discussion ?s below as I will begin to implement soon.**

The current behavior is that when the VAD goes down the top 10 keywords that have crossed the score threshold are sent out as notifications to Call Analysis.  Initially we thought we could just do the fa rejection check when the VAD goes down and then discard keywords that are marked as FA.  However this would require our feature buffer to span the entire length of the VAD, which could be quite long.  Our alternative is to check the keywords when they have crossed the score threshold and the max score has not changed for W frames( the frame length of the external right context window). 

FA Rejection buffering and context checkingL

## Discussion ?s

  1. We will need to feature buffer that has a frame history length of: NumBufferFrames = 2*(contextWindowLength)+(MaxKeywordLength) 
     1. Where is the appropriate place/class to instantiate this buffer?
     2. Any reason not to create a templatized buffer class in i3kws that is reusable, for example for LDA buffer or blackboard buffer?
  2.  In the figure above at time t1 a local max of the score is reached for keyword1, after the max score hasn't changed for W frames, where W is the context window width of the right external window, the fa rejection algorithm will be called to check if it is a true detection or false alarm (t1+W).  A isFA flag will be set in the keyword indicating whether it is a FA or DET.  Notice that at t2+W, the FA rejection algorithm will be called again to check because the max score increased, the isFA flag will be refreshed.   When the VAD goes down the top N keywords will be checked to see if they have crossed the score threshold and isFA is set to false.  These passing keywords will be sent out in a notification to CA.  Is there any problems with this?
  3. Notice at time t3 keyword2 is spotted, but the VAD ends shortly after (before W frames can accumulate and we can run the FA check).  When this happens and the VAD goes down, we will need to push the keyword into a buffer, wait until t3+W, check for a FA, and then send out a notification to CA if the keyword passed the FA check.  Is there any problems with this?
  4. In cases like t1+W (where the keyword crosses the threshold, the max hasn't changed for 12 frames, and it passes the FA check), do we need to wait for the VAD to go down or can we go ahead and send the keyword notification? 
     1. I believe I heard the notifications are sent out in a group of 3 to CA, if we send out only one to CA, will that affect performance?


