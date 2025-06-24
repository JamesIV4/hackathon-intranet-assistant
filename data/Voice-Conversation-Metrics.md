## Goal

Provide Voice Interaction analytics, data from analytics can be used to distinguish a normal and abnormal calls which allows quality management supervisor to cherry pick interactions that requires immediate evaluation of recording for agent assessment/scoring. 

## Proposed Voice Conversation Metrics

  * Agent/Customer Speech metrics (Time/Frequency).
  * Agent/Customer Silence (Time/Frequency).
  * Agent/Customer Talk Over (Time/Frequency).
  * Agent/Customer Speech volume (Decibel/Frequency).
  * Agent/Customer Speech rate (Unknown).
  * Conversation Metrics data confidence value (Decibel).
  * Timeline of segments (speech/silence/talkover) (Time).



## Conversation Metrics Data 

Sample speech metric of an agent channel. Data will be available for both channels (agent/customer).

{

 "e58da179-744b-404c-8c1c-1d621f8e32d5":

 {

  "speech":

  {

   "total":137.14,

   "min":0.16,

   "max":7.96,

   "avg":1.7359496,

   "std_deviation":1.5181614,

   "histogram":[

    {

     "bin_min":0,

     "bin_max":15,

     "bin_width":1

    },

    [36,18,12,7,3,1,1,1,0,0,0,0,0,0,0]

   ]

  }

 }

}

 

### Agent/Customer Speech Metrics Of Normal/Abnormal Call

Normal conversation         - 

Abnormal conversation     - 

Lognormal distribution graphs are generated using the conversation metrics created by i3cm from these two audio.

  * On first graph agent distribution is slightly bigger than customer and agent was in control, call progressed normally.
  * On second graph customer distribution is bigger than agent distribution and difference is pretty significantly shown.
  * Skewness and kurtosis of these distributions would help in finding abnormality between agent/customer conversation. Computing difference of area under curve with intersection of these distributions will show how apart were they in the conversation. Really higher ones like the second graph are indicative of abnormal call. 



### Agent/Customer Awkward Silences Of Normal/Abnormal Call

Using same conversation as above , histogram created with awkward silences from i3cm library.  

  * On first graph customer has more awkward silence, agent is in more control of the call.
  * On second graph, agent is not in control of the call, having too many awkward silences and trying to figure out the issue.



## Conversation Metrics Computation

I3cm library in media tier primarily provides data but it piggy backs on VAD signal processing component of our speech recognition and computes metrics frame by frame on a live audio within media server. [Great care should be taken even for considering extra metrics since it runs on HPAA thread]. 

## Available Conversation Metrics

  * Agent/Customer Speech metrics
  * Agent/Customer Silence



## Conversation Metrics Requiring Work

**I3cm/VAD**

Following list is the metrics that are essential and need working in i3cm library by priority.

  * Conversation Metrics data's  confidence value required for talkover metrics.[Currently we have signal to noise ratio but this not enough for deciding strength of speech/background speech, needing work on VAD side ]
  * Speech volume. VAD needs to provide speech energy of frame so i3cm can keep running average.[Its already available need to be exposed. I3cm may need to have different buckets for appropriate practical decibel]
  * Speech rate.[Should use same FFT values from VAD, can't afford to have extra computation on live audio].
  * Find intersection of two distributions and provide difference in area.
  * Timeline of various segments this should come from non-live audio component. This is depending on time availability with our team we need to provide rest service.



 

**Media Server**

I3cm has HPAA code but this component need to be integrated with live audio graph and adding stats returned to recording meta data.

**Pure Cloud**

Not sure. We would really like to collaborate with QM team. Ideally we would like to have log normal distribution graph displayed along with metrics, histogram of all the metrics. Also if possible have weighted scoring to provide priority number of each recording.

 

 

 
