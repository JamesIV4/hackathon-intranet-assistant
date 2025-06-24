false2flatpipe  
  
## Overview (taken from Media Server Interface doc)

All audio commands are sent from IC to the Media Server via Notifier messages. The Notifier messages are tunneled unmodified through an SBC or firewall, so no NATing or PATing is done on the addresses passed in these Notifier messages.

This is a problem when:

  * A Media Server and SIP device live in two different networks. The internal address of a Media Server can not be passed to a SIP device since that internal address is not reachable from that SIP device. The internal address was NOT NATed.
  * A Media Server and SIP device live in the same class network. A NAT exists between the IC server and the SIP device. The NATed address of a SIP device (as seen by the IC server) is passed from the IC server to the Media Server in a Notifier message, without being NATed. That address is not reachable from the Media Server since that address in unknown by the inside port of the SBC.



## Requirements

  * Support using SIP to negotiate media with the media server.
  * Support the new media server interface object model.
  * Support batching commands.
  * Minimize cases that need SIP.



## Design Docs

[Media Server Interface](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/mediaserver/docs/MediaServerInterface.doc)  
[Media Server API](http://perforce:8080/depot/systest/EIC/main/products/eic/resources/mediaserver/docs/MediaServerAPI.pdf)  
  


## Links

[Enabling VoIP with ASA 7.x](http://www.cisco.com/en/US/products/ps6120/products_configuration_example09186a008081042c.shtml)

## Testing

  


## Schedule

## Notes

### Meeting Notes

  *   *   *   *   * 


  *   *   *   *   * 


  *   * 


## Open Issues

Issue| Component| Description| Resolution| Open/Close  
---|---|---|---|---  
Batching across Media Servers| | How will a batch be handled if it spans Media Servers? Will TS or the Media Server API handle splitting the batch?| The Media Server API will handle splitting batches to multiple ones and sending it to the appropriate Media Server. The Media Server API will also collate the results from each batch into a single resultset before responding to TS.|    
Media Server Selection Rules| TS/| How will a Media Server be selected based on location?| Each Media Context will be associated with a location. TS will pass selection/exclusion list to the Media Server API with each create_media_context() call on the batch. TS can also pass a contextId as part of the selection rules that will indicate to the Media Server API that it wants that context to be created on the same server/location as the media context passed in.|    
Rollback| TS/| Are batches an all or nothing operation? If a failure occurs on one of the operations in the batch is the entire operation rolled back? Does TS or the Media Server API handle the rollback?| TS will handle any logic relating to failed operations on a batch. The Media Server API will simply report the results back to TS.|    
Error Reporting| | How will results for each command on the batch be returned to TS?| Media Server API will send an array of results back as a result of a commit() on the batch. Each result will correspond to a command issued on the batch and will contain an i3core:: it the operation failed. The results will maintain the same ordinal position in the array to the order in which its corresponding command was issued.|    
SIP to Media Server Configuration| TS/| How will the API know to use SIP for a particular Media Server?| The Media Server API will read the Media Server location and know whether SIP has to be used for commands on that Media Server.|    
Callbacks| TS/| How will TS be notified of events from the Media Server?| TS will register a callback with a create_media_context() call. The Media Server API will notify TS on any events for that media context via that callback. The callback will include the contextId, resourceId (if any), and the event/error detail.|    
Join| TS/| How do we handle joins that do not need to use SIP?| The Media Server API will keep track of the Media Context endpoints and know how to create the SDP for the joins if SIP is not needed. Another join() will be created that will take in contextIds and resourceIds which the Media Server API can optimize.|    
Batch Commands| | Should there only be one generic command object? Or an object hierarchy of commands (i.e. polymorph)?|  |  
