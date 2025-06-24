# SCRs

Interactive Intelligencea6f784b9-ef5d-3d60-bca5-6d0a3771dd27IC-93888

# List of Dependencies to be Fixed

 

Component| Path| Status| Notes  
---|---|---|---  
ininmediaserver|  eic/bin/ininmediaserverU.exe|  In Progress - Builds with warnings|    
Component| Path| Status| Notes  
---|---|---|---  
com|  |  | Added to stream by mistake - remove.  
GetIdentifier| common/lib/getidentifierlibu.lib  
common/bin/getidentifierlibu.dll| Fixed| Just changed makefile and get_identifier_dll.h, no warnings  
i3baselib| common/lib/i3baseliba.lib| Fixed| Added hash256_sink::operator<<(unsigned long long value) to be able to pass in size_t (This was a problem in RecoGrammarLib)  
  
i3com| common/lib/i3comu.lib| Fixed|    
i3dbghelp| common/lib/i3dbghelpa.lib| Fixed - ininmediaserver| Deprecated; using i3core::ErrorInfo instead  
i3inet| common/lib/i3inetlibu.lib  
common/bin/i3inetLibU.dll| Fixed| Also fixed md5.h, which is an external source despite being in /products/common/inc  
tracehelperslib| common/lib/tracehelperslibu.lib|  | Removed false dependency from eventlogentry.  Remove from stream.  
utility| common/bin/utilityu.dll| Fixed| What is dependent on this? dispatcherlib  
  
DispatcherLib| eic/lib/dispatcherlibu.lib  
eic/bin/dispatcherlibu.dll| Fixed|    
eventlogentry| eic/lib/EventLogEntryUD.lib| Fixed| Fixed compiler directive in StreamingEventLogEntry.h. Otherwise the makefile and other compiler directives were already edited. No further warnings.Removed false dependency on tracehelperslib (header file included in StreamingEventLogEntry.cpp, but not used)  
i3webconfig| eic/lib/i3webconfigu.lib  
eic/bin/i3webconfigu.dll| Fixed| Just changed makefile and Common.h, no warnings  
ionmediaserverlib| eic/lib/ionmediaserverlibu.lib| Fixed| Just changed makefile and Common.h, no warnings  
mediaserverapi| eic/bin/mediaserverapiu.dll| Builds with warnings| time_t to long conversion, 32-bitDoes this need to be 64-bit?  
mediaserveraudiolib| eic/lib/mediaserveraudiolibu.lib| Fixed| Removed dependency on i3dbghelp. A few truncation warnings related to assignment to structs defined in icmediaserveraudio.h  
mediaserverlib| eic/lib/mediaserverlibu.lib| Fixed| Just changed makefile and Common.h, no warnings  
RecoApiBaseLib| eic/lib/recoapibaselibu.lib| Fixed| Just changed makefile and Common.h, no warnings  
RecoCommonLib| eic/lib/recocommonlibu.lib| Fixed| Just changed makefile and Common.h, no warnings  
RecoGrammarLib| eic/lib/recogrammarlibu.lib| Fixed  
Not used by ininmediaserver?| -ParseError now stores line and column as size_t  
-ParseLocation::Pos_t now defined as size_t not int** Should still convert to i3xml.  
RecoPropertyLib| eic/lib/recopropertylibu.lib| Fixed| Just changed makefile and Common.h, no warnings  
RecoWebConfigLib| eic/lib/recowebconfiglibu.lib| Fixed| Just changed makefile and Common.h, no warnings  
  
 

 

 

 
