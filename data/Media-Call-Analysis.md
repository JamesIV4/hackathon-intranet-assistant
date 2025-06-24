# Media Call Analysis  
  
This is the central repository related to call analysis through Edge premises (LDM) and AWS Edges (CDM) utilizing the media-service.

Note (2025/05/02): references to CIC/PureConnect will be removed in the near future as well as references to MSCA since that was a CIC/PureConnect name (it will simply be Call Analysis).

Note: a lot of this was originally written for the Interaction Media Server in PureConnect (known as CIC at that time), which was referred to as MSCA (referred to just as call analysis in Genesys Cloud).  The same i3ca call analysis code runs whether on an LDM Edge, media-service, or PureConnect Media Server (created and called from icmediaserveraudio in \\\media).  The client side accounts for the main difference in behavior between Genesys Cloud (edge control) and CIC (TsServer), however, there are also differences at the icmediaserveraudio level as well between platforms (PureConnect vs Genesys Cloud) but not between LDM vs CDM in Genesys Cloud.  For LDM Edges, icmediaserveraudio runs within the ininedgemedia process (//edge/main_systest/int/src/ininedgemedia/main.cpp) and for CDM, within the media-service application.cpp (//edge/media.service.latest_systest/int/src/mediaservice/application.cpp

  * MSCA Overview

  * MSCA Development

  * MSCA Testing

  * MSCA Support

  * MSCA Documentation and Presentations

  * MSCA Data

  * MSCA Research and New Features 

    * LHS

    * Correlation of rings to live speakers and machines

    * Call Progress Timing

    * ASE-405: Offline Diagnostic Autotagging

    * ASE-537: Improving Speech Endpointing using Neural Net

    * Adjustable Live Speaker Detection ([PURE-4000](https://inindca.atlassian.net/browse/PURE-4000))

    * [AMD Timeout and Silent Call Timeout](https://genesys-confluence.atlassian.net/wiki/display/MediaGroup/AMD+Timeout+and+Silent+Call+Timeout) ([PURE-5169](https://inindca.atlassian.net/browse/PURE-5169))

    * New Call Analysis Data Points (PURE-5812)

    * Answering Machine Tendency (AMT)

    * Learning Call Analysis (LCA)



