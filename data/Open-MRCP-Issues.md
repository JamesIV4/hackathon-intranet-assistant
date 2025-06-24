This page describes open issues that were discovered while designing and implementing the MRCP ASR Server that affect components outside of Reco.

## Issue: After a RECOGNIZE request is started, the MRCP Server may never send a COMPLETE response

The MRCP spec states that sending a STOP request will cause the MRCP Server to never send a COMPLETE response for affected requests.  We implement no-input timeouts ourselves (because they can be more complicated than the MRCP spec easily allows for), and we use STOP to tell the server when the no-input timeout was reached.  The issue is that we tell i3inet to expect a response to the RECOGNIZE request, and when a no-input timeout occurs, we find out that we should not expect a response.  However, there is currently no mechanism to tell i3inet to ignore the response after asking for the next response.  As a result, an i3inet timeout expires, and i3inet closes the network connection.  This is bad because the recognition session often continues after a no-input timeout occurs.

The following components are affected, and need to be modified:

Component  |  Change  |  Details   
---|---|---  
i3mrcp  |  The i3mrcp Policy needs to detect when the response to a STOP request cancels a prior request.  |  When we receive responses, i3mrcp policy will check if the original request was a STOP request using the transaction table.  If so, we will check for an Active-Request-Id-List header in the response and invoke a new public method that tells i3inet to cancel the affected transactions.   
i3inet  |  i3inet needs to expose a public method that allows a transaction's response to become ignored after the response had been requested.  |  When i3mrcp receives a COMPLETE response to a STOP request there is no way of telling i3inet to cancel (or ignore) a prior request's timers. Beyond exposing a public method, the method should take an error pointer so that the transaction can signal a failure with policy-specified details.   
  
There was some concern that there could be a race condition between when the STOP response is received and when the i3inet timeout for the original RECOGNIZE request occurs.  However, the caller to RECOGNIZE will know the maximum time for the recognition, and we can set the timeout to be significantly longer than the maximum time for the STOP request to be sent (ex. 10 seconds longer).  The race condition would only occur if the MRCP Server takes a long time to respond to the STOP request.  However, the long delay would imply a problem with the MRCP Server or the networking, and so a connection timeout wouldn't be inappropriate.
