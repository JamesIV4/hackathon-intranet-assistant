# 

# Merlin installation

* * *

## Prerequisites

Merlin is coded in python and need third-party python libraries such as:

  * **numpy, scipy, matplotlib, lxml:** Usually shipped with your python packages Available in Ubuntu packages 


  * **theano:**  Can be found on pip 


  *     * Need version 0.6 and above


  *     * <http://deeplearning.net/software/theano/>


  * **bandmat:**  Can be found on pip


  *     * <https://pypi.python.org/pypi/bandmat>


  * For running on NVIDIA GPU, you will need also CUDA


  *     * <https://developer.nvidia.com/cuda-zone>


  * and you might want also CUDNN [optionnal]


  *     * <https://developer.nvidia.com/cudnn>



## Package installation

  * Download: \\\hydfiles01\Public\Veera.Raghavendra\TTS\DNN\merlin-package.tar.gz
  * Installation
    * tar -xzf merlin-package.tar.gz
    * cd merlin/tools
    * ./compile_tools.sh
    * export sptk_dir=<tools-dir>/bin/SPTK-3.9/

    * export world_dir=<tools-dir>/bin/WORLD/

    * cd ..
    * export merlin_dir=`pwd`
    * add merlin_dir, sptk_dir and world_dir to ~/.bashrc
    * source ~/.bashrc



# Data preparation

* * *

## Initial training data

  * Training data is provided for initial training. Download the package from \\\hydfiles01\Public\Veera.Raghavendra\TTS\DNN\en-US_jill_non_preemp_60_coeffs.tar.gz



## Directory structure and other files of the initial training data

  * labels
    * label-phone-align: For phoneme level training  
    * label-state-align: For state level training
    * regression-phone-align: Test labels at phoneme level
    * regression-state-align: Test labels at state level
  * feats
    * bap
    * lf0
    * mgc
  * questions-radio_dnn_416.hed: en-US question file
  * file_id_list_full.scp: Training files list of id's
  * test_id_list.scp: Testing files list of id's
  * normalize_lab_for_merlin.py: Normalizing the full context labels to Merlin structure for both phoneme and state level.
    * Usage: python normalize_lab_for_merlin.py  <input_lab_dir> <output_lab_dir> <label_style> <file_id_list_scp> <optional: write_time_stamps (1/0)>
    * label_style: phone_align / state_align
  * prepare_training_data.sh: Script for packaging all the data into Merlin format
    * Usage: sh prepare_training_data.sh <output directory name>



## Create Merlin package for training

  * sh sh prepare_training_data.sh en-US_jill_non_preemp_60_coeffs
  * Note: Above script will create "en-US_jill_non_preemp_60_coeffs" directory "en-US_jill_non_preemp_60_coeffs.zip" file. 



# Training DNN models

* * *

## Create a working directory

  * cd $merlin_dir/egs
  * mkdir en-US
  * cd en-US
  * download  \\\hydfiles01\Public\Veera.Raghavendra\TTS\DNN\setup_16khz.tar.gz
  * tar -xzf setup_16khz.tar.gz
  * mv setup_16khz en-US_full_non_preemp_60_coeffs
  * cd ~~setup_16khz~~ en-US_full_non_preemp_60_coeffs



## Move Merling package prepare earlier

  * mv en-US_jill_non_preemp_60_coeffs.zip .



## Handling question files

  * We need to provide the question file during the training. That has been configured in **scripts/setup.sh**
    * echo "QuestionFile=questions-radio_dnn_416.hed" >> $global_config_file **at line no: 49  
**
  * questions files for en-US, de-DE and en-AU are available in ../../../questions directory



## Handling type of labels

  * We need to mention label type as "state_align" or "phone_align" in **scripts/setup.sh**
    * echo "Labels=state_align" >> $global_config_file**at line no: 48**



## Network architecture changes

  * For duration modelling: ../../../misc/recipes/duration_demo.conf
  * For acoustic modelling: ../../../misc/recipes/acoustic_demo.conf
  * Go to [Architecture] section and do changes



## Full training and synthesis

  * ./run_full_voice.sh <voice name>
  * ./run_full_voice.sh en-US_jill_non_preemp_60_coeffs > log 2>&1 &
  * This step first creates the configuration files and starts duration, acoustic model training followed by duration prediction, acoustic prediction and synthesis



## Duration training

  * ./scripts/submit.sh ${merlin_dir}/src/run_merlin.py conf/duration_<voice name>.conf



## Acoustic training

  * ./scripts/submit.sh ${merlin_dir}/src/run_merlin.py conf/acoustic_<voice name>.conf



# Synthesis using Merlin

* * *

## Duration prediction

  * ./scripts/submit.sh ${merlin_dir}/src/run_merlin.py conf/test_dur_synth_<voice name>.conf



## Acoustic prediction and synthesis

  * ./scripts/submit.sh ${merlin_dir}/src/run_merlin.py conf/test_synth_<voice name>.conf
  * synthesis files are stored in experiments/<voice name>/test_synthesis/wav



## Synthesis using global variance

  * Download additional files from below location
    * \\\HYDFILES01\Public\Veera.Raghavendra\TTS\DNN\additional-source.7z
    * unzip the 7z file
      * 7z x additional-source.7z
      * cp parameter_generation.py $merlin_dir/src/frontend/
      * cp acoustic_base.py $merlin_dir/src/frontend
      * cp -r scripts $merlin_dir/
  * By default Merlin does not apply global variance. Instead. applies post processing on MGC's
  * We observed that global variance on F0 and MGC does help quality improvement
  * So, we are applying global variance and synthesize using world vocoder separately/
  * After synthesis **experiments/ <voice name>/test_synthesis/wav** contains spectral feature files (.lf0, .mgc, .bap, .vuv).
  * Above files are in binary format by default. So, we have to convert them into ascii and apply global variance.
    * python $merlin_dir/scripts/dnn_bin2ascii_with_gv.py **experiments/ <voice name>/acoustic_model/data/norm_info_mgc_lf0_vuv_bap_187_MVN.dat **experiments/ <voice name>/test_synthesis/wav **experiments/ <voice name>/test_synthesis/wav_i3tts******
  * ******"**experiments/ <voice name>/test_synthesis/wav_i3tts" ********contains global variance applied lF0, mgc, and original BAP in ascii format.
  * Now, we have to convert them back into binary and synthesize using world_vocoder
    * **cd********experiments/ <voice name>/test_synthesis/wav_i3tts******
    * ******cp $merlin_dir/scirpts/*.sh .******
    * ******sh temp.sh******
    * ******./world_synthesis.sh . wav_world******
  * wav_world contains the audio files.



# Additional steps

* * *

## Creating question files

  * Take HTS question file for the language and modify the question file as mentioned below.
    * Replace *; with ;
      * e.g: {p1=p;*,p1=b;*,p1=t;*,p1=d;*,p1=k;*,p1=g;*,p1=m;*,p1=n;*,p1=rr;*,p1=r;*,p1=f;*,p1=s;*,p1=hh;*,p1=w;*,p1=y;*,p1=l;*,p1=ch;*,p1=ny;*,p1=ll;*}  _**to  **_{p1=p;,p1=b;,p1=t;,p1=d;,p1=k;,p1=g;,p1=m;,p1=n;,p1=rr;,p1=r;,p1=f;,p1=s;,p1=hh;,p1=w;,p1=y;,p1=l;,p1=ch;,p1=ny;,p1=ll;}
    * Separate binary questions and continuous questions (Questions with numerical numbers are continuous questions and rest of them are binary)
      * Binary questions: {p1=p;,p1=b;,p1=t;,p1=d;,p1=k;,p1=g;,p1=m;,p1=n;,p1=rr;,p1=r;,p1=f;,p1=s;,p1=hh;,p1=w;,p1=y;,p1=l;,p1=ch;,p1=ny;,p1=ll;}
      * Continuous questions: 
        * QS "Num-Syl_from_prev-StressedSyl==X" {*b12=X;*}
        * QS "Num-Syl_from_prev-StressedSyl==0" {*b12=0;*}
        * QS "Num-Syl_from_prev-StressedSyl==1" {*b12=1;*}
        * QS "Num-Syl_from_prev-StressedSyl==2" {*b12=2;*}
        * QS "Num-Syl_from_prev-StressedSyl==3" {*b12=3;*}
        * QS "Num-Syl_from_prev-StressedSyl==4" {*b12=4;*}

        * QS "Num-Syl_from_prev-StressedSyl==5" {*b12=5;*}
        * QS "Num-Syl_from_prev-StressedSyl<=0" {*b12=0;*}
        * QS "Num-Syl_from_prev-StressedSyl<=1" {*b12=0;*,*b12=1;*}
        * QS "Num-Syl_from_prev-StressedSyl<=2" {*b12=0;*,*b12=1;*,*b12=2;*}
        * QS "Num-Syl_from_prev-StressedSyl<=3" {*b12=0;*,*b12=1;*,*b12=2;*,*b12=3;*}
        * QS "Num-Syl_from_prev-StressedSyl<=4" {*b12=0;*,*b12=1;*,*b12=2;*,*b12=3;*,*b12=4;*}
        * QS "Num-Syl_from_prev-StressedSyl<=5" {*b12=0;*,*b12=1;*,*b12=2;*,*b12=3;*,*b12=4;*,*b12=5;*}



 

  *     * Add continuous questions at the end
    * There are multiple questions for one continuous feature. In above example, b12 has 13 questions. We have to squeeze them to one with following regular expression in the question file.
      * **CQS** "Num-Syl_from_prev-StressedSyl==X" {b12=(\d+);}
      * Make sure that you change the "QS" to "CQS" at the beginning as highlighted 



## Download extra source

  * *****Ignore this step if you have downloaded extra source earlier*****
  * Download additional files from below location
    * \\\HYDFILES01\Public\Veera.Raghavendra\TTS\DNN\additional-source.7z
    * unzip the 7z file
      * 7z x additional-source.7z
      * cp parameter_generation.py $merlin_dir/src/frontend/
      * cp acoustic_base.py $merlin_dir/src/frontend
      * cp -r scripts $merlin_dir/



## Building a model with continuous F0

  * Generally, F0 features have zero and non-zero values. Model might be confusing with this behavior. So, we wanted to model F0 with continuous features. To accomplish, we follow below steps.
  * Once larger model (1024 * 3 MLP and 512 * 3 LSTM layer architecture) is trained, predict continuous F0 features for training data using training labels. This requires code change
    * Make **F0_continuous = True** in **../../../src/frontend/parameter_generation.py**
  * Copy training labels into "gen-lab" for synthesis
    * cp **experiments/ <voice name>/acoustic_model/data/label_state_align/*** **experiments/ <voice name>/test_synthesis/gen-lab/**
    * ls experiments/<voice name>/test_synthesis/gen-lab/* | sed -e 's/\\.lab$//g' > experiments/<voice name>/test_synthesistest_id_list.scp
  * Run synthesis script
    * ./scripts/submit.sh $merlin_dir/src/run_merlin.py conf/test_synth_<voice name>.conf
  * Predicted features are available in **experiments/ <voice name>/test_synthesis/wav**
  * Creating LF0 using transfer learning  

    * Convert Binary F0 into Ascii format
    * python $merlin_dir/scripts/dnn_bin2ascii_f0_train.py experiments/<voice name>/acoustic_model/data/norm_info_mgc_lf0_vuv_bap_187_MVN.dat **experiments/ <voice name>/test_synthesis/wav **experiments/ <voice name>/test_synthesis/wav_ascii_train****
    * Calculate maximum F0 value in the features
      * cat ****experiments/ <voice name>/test_synthesis/wav_ascii_train/f0/* | sort -k 1 -n -u | tail -1****
      * Use this value for normalization; "normalization_value" here after
    * Rename the directories in the "wav_ascii_train"****  
****
      * ****mv****experiments/ <voice name>/test_synthesis/wav_ascii_train/f0 ****experiments/ <voice name>/test_synthesis/wav_ascii_train/lf0_predicted************
      * ************cp  **experiments/ <voice name>/acoustic_model/data/lf0 ************experiments/ <voice name>/test_synthesis/wav_ascii_train/lf0_original**************************
    * Generate new set of features using lf0_predicted and lf0_original
      * When we have continuous F0, we will miss VUV data. To obtain VUV features during training, we embed that information in the feature.
      * Python script normalizes the Log F0 values that were predicted by Merlin.
      * Based on Original F0, it will add "1" for the non-f0 values.
      * During training, if the value is >1, we consider it as **" Voiced"** otherwise **" Unvoiced". **De-normalizes the F0 value using normalization value.
    * Editing lf0_mixing.py  

      * Open $merlin_dir/scripts/lf0_mixing.py and edit "baseDir" path on Line No: 5,
      * Set maxLf0 (normalization_value) at Line no: 24
      * python $merlin_dir/scripts/lf0_mixing.py
    * Convert **lF0** to**Binary**
      * **mkdir  **************************experiments/ <voice name>/test_synthesis/wav_ascii_train/lf0****************************
      * ****************************ls  **************************experiments/ <voice name>/test_synthesis/wav_ascii_train/lf0_mixed/*.lf0 | while read i; do fname=`basename $i`; x2x +af $i > experiments/<voice name>test_synthesis/******************************************************wav_ascii_train****************************************************** /lf0/$fname; done******************************************************
  * Replace "lf0" directory with this "lf0" in your data preparation directory and zip it back
  * Before running the training, following these changes  

    *  Open $merlin_dir/src/frontend/acoustic_base.py
    * Set **F0_continuous == True**  at Line no: 44
    * Set **maxLf0** based on "normalization_value"



 

 
