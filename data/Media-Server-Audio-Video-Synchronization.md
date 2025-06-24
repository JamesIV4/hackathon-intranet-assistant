### Synchronization Requirements for Audio with Video Passthrough  
  
  1. Receive RTCP synchronization information for two or more streams from the same source endpoint.
  2. Transmit RTCP synchronization information for two or more streams with the same relative synchronization as received.



The RTP/RTCP specification allows for the synchronization of multiple RTP streams via RTCP Sender Report's NTP timestamp and RTP timestamp fields. These two fields provide a common point in time between the NTP time at the source and the stream's RTP timestamp. Given this pair, the NTP time of the source can be calculated from any given timestamp and vice versa the the RTP timestamp can be calculated for any given NTP time of the source.Two related streams may be synchronized using one pair each to calculate the equivalent RTP timestamp for a stream given the other stream's RTP timestamp.

The synchronization of the streams is important for rendering the streams at an endpoint, but Media Server will not render these streams so we only care about preserving the synchronization within Media Server and passing it on to destination endpoints. Preserving this information in Media Server requires:

  1. Information that tells Media Server which streams are related.
  2. Reception of RTCP sender reports for each stream.
  3. Generating RTCP sender reports with the same corresponding relative synchronization when data from these streams are re-transmitted.



### Synchronization Points

We've previously discussed the design of synchronization points. In our original concept, these would consist of an object in the graph independent of the audio (or video) streams that maintains a common point in time between one or more associated streams. Additionally, each audio buffer would contain a list of synchronization offsets, each consisting of a reference to their respective synchronization point and an offset representing that buffer's location in the stream relative to that synchronization point.

In recent discussions, we've revised this a little bit. Instead of a synchronization point for each set of related streams, we decided to either have a single point located in the graph or a single point for the entire engine. Audio buffers would require only one object representing the offset relative to the graph or engine synchronization point. The synchronization point itself could be simply a point in time in engine time (e.g. the start time of the engine).

A few implications of synchronization points:

  1. Elements that pass audio buffers (or normalized RTP buffers) will need to be modified to copy synchronization offset information from input buffers to output buffers.
  2. The elements that create the initial buffers containing synchronization points (RTP element, media reader elements) will need to maintain the state to set the proper offset when producing these buffers.



### Audio/Video Synchronization using Synchronization Points

On the reception side, we need a way of designating that two or more streams are synchronized and based off the same RTCP clock. We will need an object of some sort that stores the relationship between the sender's RTCP clock and our synchronization point's time (or engine time).

For the first stream added, we can pick an association between that stream and the system time that is based on the arrival times of some of that stream's packets. For subsequent related streams, we can apply them to the already created association. But, due to the chunkiness of video timestamps, it may be that we pick an association that doesn't match well with real time. This shouldn't be a problem unless we need to do something time-related inside media server. Since there are currently no synchronization points in Media Server, there is no problem. After we have synchronization points, we will have to take care that elements don't rely on audio matching closely with real time.

On the sender side, we will also need a way of designating that streams are related. Once we have this, the rest is straightforward. Each buffer in each stream will have a system time (or some common time object) that the RTCP senders can use to generate sender reports. Since all sender reports will be based off the same clock, the streams will be synchronized correctly.

 
