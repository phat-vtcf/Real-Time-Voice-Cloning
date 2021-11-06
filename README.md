# Real-Time Voice Cloning
This repository is an implementation of [Transfer Learning from Speaker Verification to
Multispeaker Text-To-Speech Synthesis](https://arxiv.org/pdf/1806.04558.pdf) (SV2TTS) with a vocoder that works in real-time. Feel free to check [my thesis](https://matheo.uliege.be/handle/2268.2/6801) if you're curious or if you're looking for info I haven't documented. Mostly I would recommend giving a quick look to the figures beyond the introduction.

SV2TTS is a three-stage deep learning framework that allows to create a numerical representation of a voice from a few seconds of audio, and to use it to condition a text-to-speech model trained to generalize to new voices.

**Video demonstration** (click the picture):

[![Toolbox demo](https://i.imgur.com/8lFUlgz.png)](https://www.youtube.com/watch?v=-O_hYhToKoA)

(The assignment of Programming (CFMVT03A05) is added below at section 'Testing on variables (assignment Programming)'.)


### Papers implemented  
| URL | Designation | Title | Implementation source |
| --- | ----------- | ----- | --------------------- |
|[**1806.04558**](https://arxiv.org/pdf/1806.04558.pdf) | **SV2TTS** | **Transfer Learning from Speaker Verification to Multispeaker Text-To-Speech Synthesis** | This repo |
|[1802.08435](https://arxiv.org/pdf/1802.08435.pdf) | WaveRNN (vocoder) | Efficient Neural Audio Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN) |
|[1703.10135](https://arxiv.org/pdf/1703.10135.pdf) | Tacotron (synthesizer) | Tacotron: Towards End-to-End Speech Synthesis | [fatchord/WaveRNN](https://github.com/fatchord/WaveRNN)
|[1710.10467](https://arxiv.org/pdf/1710.10467.pdf) | GE2E (encoder)| Generalized End-To-End Loss for Speaker Verification | This repo |

## Testing on variables (assignment Programming)

For this assignment, we examined the work of this Text-To-Speech (cloning) program. We tested the program based on three variables: the difference in language that is used, the difference in input that is used, and the amount of input that is used. We used a survey (https://rug.eu.qualtrics.com/jfe/preview/SV_9MExPEGffVN2HGu?Q_CHL=preview&Q_SurveyVersionID=current) to obtain the performance of the model.

### Research question and hypothesis ###

The research question of this experiment is the following:

'Does the difference in language that is used, the difference in input that is used, or/and the amount of input that is used, have influence on the performance of the model?'

We expected that the language would make a difference in performance, as the model is trained on English data. Therefore, we expected that the Dutch sentences were harder to clone than the English sentences. Also, we expected that the input of the model also plays an important role, as we thought it is easier for the model to clone a voice to the same sentence as what is used as input. Finally, we expected that the more input the better the cloned voice will be.

### Methods

#### 1. Participants

All three participants that filled in the survey were native Dutch speakers, and second language English speakers. (How many? + more info?)

#### 2. Test the difference in language that is used
The original model of this repo is trained on the English language. To test whether this model works on different languages, we tried to test it on the Dutch language as well. We did this in four different ways.

##### English language to English language
One clone is created from an English input .wav file to an English sentence. The English input file contained the following text spoken by Suzanne de Vries:

'The North Wind and the Sun were disputing which was the stronger, when a traveller came along wrapped in a warm cloak. They agreed that the one who first succeeded in making the traveller take his cloak off should be considered stronger than the other. Then the North Wind blew as hard as he could, but the more he blew the more closely did the traveller fold his cloak around him; and at last the North Wind gave up the attempt. Then the Sun shined out warmly, and immediately the traveller took off his cloak. And so the North Wind was obliged to confess that the Sun was the stronger of the two.'

The input file can be found in the folder 'Recordings_VT/Input', 'northwind_EN_total.wav'. The output of the model was the clone of Suzanne's voice saying the sentence (once written down by Shakespeare):

'What's in a name? That which we call a rose by any other name would smell as sweet.'

The output can be found in the folder 'Recordings_VT/Output_Q1', 'ENinENout.wav'.


##### Dutch language to Dutch language
One clone is created from a Dutch input .wav file to a Dutch sentence. The Dutch input file contained the following text spoken by Suzanne de Vries and is the translation of the English text shown in the previous paragraph:

'De noordenwind en de zon waren erover aan het redetwisten wie de sterkste was van hun beiden. Juist op dat moment kwam er een reiziger aan, die gehuld was in een warme mantel. Ze kwamen overeen dat degene die het eerst erin zou slagen de reiziger zijn mantel te doen uittrekken de sterkste zou worden geacht. De noordenwind begon toen uit alle macht te blazen, maar hoe harder ie blies, deste dichter trok de reiziger zijn mantel om zich heen; en ten lange leste gaf de noordenwind het op. Daarna begon de zon krachtig te stralen, en hierop trok de reiziger onmiddellijk zijn mantel uit. De noordenwind moest dus wel bekennen dat de zon van hun beiden de sterkste was.'

The input file can be found in the folder 'Recordings_VT/Input', 'northwind_NL_total.wav'. The output of the model was the clone of Suzanne's voice saying the sentence (once written down by Shakespeare and translated to Dutch):

'Wat zegt een naam? Een roos zou toch niet minder lekker ruiken als je haar met een ander woord benoemde.'

The output can be found in the folder 'Recordings_VT/Output_Q1', 'NLinNLout.wav'.


##### English language to Dutch language
One clone is created from a English input .wav file to a Dutch sentence. The English input file is the same as for the English language to English language ('northwind_EN_total.wav'), but the output of the sentence contains the sentence:

'Wat zegt een naam? Een roos zou toch niet minder lekker ruiken als je haar met een ander woord benoemde.'

The output can be found in the folder 'Recordings_VT/Output_Q1', 'ENinNLout.wav'.

##### Dutch language to English language

One clone is created from a Dutch input .wav file to a English sentence. The Dutch input file is the same as for the Dutch language to Dutch language ('northwind_NL_total.wav'), but the output of the sentence contains the sentence:

'What's in a name? That which we call a rose by any other name would smell as sweet.'

The output can be found in the folder 'Recordings_VT/Output_Q1', 'NLinENout.wav'.

#### 3. Test the difference in input that is used

The second comparison we made is what different inputs will output. All different inputs has the output saying the following sentence:

'They agreed that the one who first succeeded in making the traveller take his cloak off, should be considered stronger than the other.'

The first input we used was the first sentence of the English text that was used at '2. Test the difference in language that is used' and can be found in the folder 'Recordings_VT/Input', 'northwind_EN_s1.wav'. The cloned version can be found in the folder 'Recordings_VT/Output_Q2', 's1_to_s2.wav'. So, for in this case the input sentence is differently from the output.

Then, the second file that we compared was the second sentence of the text without cloning it. This file can be found in the folder 'Recordings_VT/Output_Q2', 's2.wav'.

Finally, the input of the third file is the second language of the text that was used at '2. Test the difference in language that is used' and can be found in the folder 'Recordings_VT/Input', 'northwind_EN_s2.wav'. The cloned version can be found in the folder 'Recordings_VT/Output_Q2', 's2_to_s2.wav'. So, for in this case the input sentence is the same as the output.

#### 4. Test the amount of input that is used

The last comparison we made is what different amount of data is used to clone the input. The output for all the inputs was the same:

'What's in a name? That which we call a rose by any other name would smell as sweet.'

The input for the model was either a .wav file containing one sentence of the text uses in '2. Test the difference in language that is used' ('Recordings_VT/Input', 'northwind_EN_s1.wav'), two sentences of this text ('Recordings_VT/Input', 'northwind_EN_s1s2.wav'), or the whole text ('Recordings_VT/Input', 'northwind_EN_total.wav'). The outputs were respectively (from the folder 'Recordings_VT/Output_Q3'): 's1.wav', 's1s2.wav', and 'total.wav'.

#### 5. The survey

In the survey two sets of questions were asked. First, the participants had to order voices what they found the most human-like to the least human-like. For each of the three experiments one question was made. So, for example, for the comparison of using different languages, the four output files of '2. Test the difference in language that is used'.

Then, three questions (for each comparison separately) were asked what voices were the most similar to the demo file. The demo file was the input file with the first two sentences of the story described in the method part spoken by Suzanne de Vries. The participants had to order the files according to what was the most like the demo file and what the least.

The survey can be found here: https://rug.eu.qualtrics.com/jfe/preview/SV_9MExPEGffVN2HGu?Q_CHL=preview&Q_SurveyVersionID=current

### Results 

#### 1. Test the difference in language that is used

Four different cloned voices are examined for this question. The first file (1) was cloned English sentence using an English text as input. The second file (2) was a cloned English sentence using a Dutch text as input. The third (3) and fourth (4) file both had a cloned Dutch sentence as output, where the third file had English text as input and the fourth file had Dutch text as input. As we expected that the model would work the best for the English language and the worst for the Dutch language, we expected the following order of the file from the participants: 1, 2, 3, 4 (from best cloned voice to worst cloned voice).

The results show that there is indeed a division between the English output sentences (1 and 2) and the Dutch output sentences (3 and 4). File 1 and 2 are picked as best cloned voice and file 3 and 4 as worst cloned voice. However, the order between file 1 and 2 and between file 3 and 4 differed. 

Similar results were found when was asked which voice was the most similar to the demo voice. Two out of the three participants made again the division between the English output (file 1 and 2) and the Dutch output (file 3 and 4).

#### 2. Test the difference in input that is used

Three different files were used in this experiment. The first file (1) was a cloned voice with an input that was a different sentence. The second file (2) was the original voice, so without being cloned. The last file (3) was a cloned voice with an input that was the same sentence. We expected that the original voice would be picked as the most human-like, as this is a human voice. Then, we expected that the voice with the same input sentence as output sentence would be the best. So the order that we expected was: 2, 3, 1.

The results show that file 3 was actually the least like a human voice according to the three participants and either file 1 or file 2 were considered as most human-like. So the order that was given by the participants was either 1, 2, 3 or 2, 1, 3. When we asked what voice was the most similar to the demo voice the answers differ a lot. We cannot conclude anything from this.

#### 3. Test the amount of input that is used

For this experiment three different files were used. The first file (1) contained only the first sentence of a text, the second file (2) contained the first and the second sentence of a text and the third file (3) contained the whole text. We expected that the model would work better if more input was used than if less input was used. So we expected the following order: 3, 2, 1.

The results show that file 1 indeed created the least human-like voice according to the three participants. However, all participants said that file 2 had the most human-like voice, instead of file 3 as we suspected. When we asked what voice was the most similar to the demo voice the answers differ a lot again. We cannot conclude anything from this.

### Conclussion and Discussion

The results show that it seems to be the case that the model works better using the English language than the Dutch language. Especially, the English output seems to be better than the Dutch language. Also, the input of the model seems not to depend on if the sentence was already heard or not. Finally, the amount of input to the model seems to have a slightly difference. The cloned voice using the least amount of input was the least human-like according to the participants. However, the cloned voice using the most amount of input was not the most human-like according to the participants. 


Points of discussion are the following:

* The input files were really short. Especially for the experiment about the different amount of input data, this might have influence, as the differences of the files are very small.
* Every time, the neural network behind the model in the repo creates a new output, even if the input is the same. So, it might be the case that one output is very different from another output, while the same input file is used. In case there are very small differences between the file, then this also might be 'bad luck' that the model outputs a better or worse output than an other output where it is compared with.
* Because of limited time, we only found three participants to join our experiment. More participants are needed to find a significant result.

## Setup

While trying to run the code, we encountered some difficulties. This is why we updated the setup, so the repo is easier to use. Below are the steps that you need to follow.

Instructions when working with an Anaconda prompt:

Set your directory to where you cloned the repo.
You need Python 3.6 of 3.7 to run the program.
To create an environment with 3.6 or 3.7, use this command:

`conda create --name py37 python=3.7`
(always press y to proceed)

When it is done, use the next command:

`conda activate py37`

Now you are using your environment with Python 3.7


Next install ffmpeg and PyTorch with the following commands:

`conda install -c conda-forge ffmpeg`

`conda install -c pytorch pytorch` (this might take a while)

To install and check for the other packages, use the following command:

`pip install -r requirements.txt`


We encountered multiple errors after this. We had to install PySoundFile and webrtcvad manually.
Also, you have to use NumPy 1.20 for this repo to work. You can use the following commands:
(make sure pip is upgraded: `pip install --upgrade pip`)

`pip install webrtcvad-wheels`

`conda install -c conda-forge pysoundfile`

`conda install -c conda-forge numpy=1.20`

Then download the pretrained models using the link. When extracting the zip file, you will see three folders named 'encoder', 'synthesizer', and 'vocoder'.
Insert the content of these folders in the folders with the corresponding names in the repo.

To check if everything is working, now use the command:

`python demo_cli.py`

This will give you a message 'All test passed! You can now synthesize speech.', and a demo version which
can generate cloned speech from an input file already! When testing this, make sure to use the whole filepath and the extension of the input file. The output file
will be stored in the repo folder.

For the assignment we used the demo_cli.py to create the cloned voices. However, it is also possible to use the toolbox. Run the following command:

`python demo_toolbox.py`

This will show a nice interface to use to clone the files. How to use this interface is explained in the youtube video shown above.

## News
**05/11/21**: The repo is tested by Suzanne de Vries (@SKdeVries) and Tessa Zwart (@TessaZwart), using the following variables: the difference in language that is used, the difference in input that is used, and the amount of input that is used.

**14/02/21**: This repo now runs on PyTorch instead of Tensorflow, thanks to the help of @bluefish. If you wish to run the tensorflow version instead, checkout commit `5425557`.

**13/11/19**: I'm now working full time and I will not maintain this repo anymore. To anyone who reads this:
- **If you just want to clone your voice (and not someone else's):** I recommend our free plan on [Resemble.AI](https://www.resemble.ai/). You will get a better voice quality and less prosody errors.
- **If this is not your case:** proceed with this repository, but you might end up being disappointed by the results. If you're planning to work on a serious project, my strong advice: find another TTS repo. Go [here](https://github.com/CorentinJ/Real-Time-Voice-Cloning/issues/364) for more info.

**20/08/19:** I'm working on [resemblyzer](https://github.com/resemble-ai/Resemblyzer), an independent package for the voice encoder. You can use your trained encoder models from this repo with it.

**06/07/19:** Need to run within a docker container on a remote server? See [here](https://sean.lane.sh/posts/2019/07/Running-the-Real-Time-Voice-Cloning-project-in-Docker/).

**25/06/19:** Experimental support for low-memory GPUs (~2gb) added for the synthesizer. Pass `--low_mem` to `demo_cli.py` or `demo_toolbox.py` to enable it. It adds a big overhead, so it's not recommended if you have enough VRAM.

