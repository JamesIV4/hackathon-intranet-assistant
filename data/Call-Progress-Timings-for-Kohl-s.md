#### Purpose  
  
Determine call progress timing durations starting from Call Analysis until agent connect (2-way audio flowing when both agent and callee should be able to talk and hear).

#### Testing setup

  * UAT environment (non-production) on 2017 R2 P6
  * Dialer Power mode with AMD enabled
  * Single agent tester (Chuck Bailey in PS):
    * Remote number for client (Google voice phone) with persistent connection enabled
    * Whisper tone
  * 2 cell phones were dialed in the campaign (AT&T and Sprint)



#### Testing notes

Call IDs (2017-12-06):

1090600042 (AT&T) - ~2-3s delay

1090600052 (AT&T) - ~2-3s delay

1090600054 (AT&T) - ~2-3s delay

1090600056 (AT&T) - ~2-3s delay

1090600058 (AT&T) - ~2-3s delay

1090600065 (SPRINT) - ~2s delay

1090600067 (SPRINT) - ~2s delay

1090600069 (SPRINT) - ~2s delay

1090600074 (AT&T) - ~2-3s delay

 

Note methodology:

"I opened the clock on the pc and counted the seconds.

I counted from when I first said hello (as soon as I answered the call) to when the call connected to the agent.

There were 2 ways I confirmed that; Interaction Scripter will change when a call is connected and other examples I kept talking until I heard myself on the other phone."

#### Testing results

The below numbers are averages across all 9 calls.  The first metric is most important for US consideration under TCPA (from the end of the greeting to agent transfer).

  * 1.416 seconds from end of greeting to 2-way audio with agent



Further details:

  * Speaker delay: 1.176 seconds from line connect to start of greeting
  * 1.910 seconds from start of greeting to 2-way audio with agent
    * Segment breakdowns:
      * 0.493 seconds estimated greeting length
      * 0.700 seconds of silence required for detecting live speaker
      * 0.716 seconds from detected live speaker to connected 2-way audio (callee and agent)



#### Disparity between notes and analyzed results

Most calls were reported as experiencing 2-3 second delays, whereas the analysis shows on average it was 1.4 seconds.  The cell carrier and Google voice audio transmission delays were not factored in, however, in another dataset for another customer, it was found on an analyzed Verizon cell that the round trip delay was about 900ms (perhaps ~450ms each way), so if the carrier delays in this test were similar, then that would put the analysis on the lower to mid range of 2 seconds on average, which seems reasonably consistent with the reported experience.

#### Data and analysis files

HTML report contains an in-depth analysis of each call (audio, graphics, timings)

  * 


Storage location of data

  * \\\i3filesarchive\SpeechAnalyticsData\CallAnalysis\UnitedStates\Case944623_ParamountEquityMortgage\Kohls_UAT_comparison\2017_12_06



#### Total perceived delay

Using Kohl's data, we can see general timings with the [perceived delay](https://confluence.inin.com/display/MediaGroup/Total+perceived+delay).

 
