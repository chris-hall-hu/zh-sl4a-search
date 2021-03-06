#zh-sl4a-search

##Introduction

**Note** this prototype was mainly developed on a Nexus 7 during bus journeys and there have been a couple of minor issues with git on the Nexus for example I cannot get commits to pick up my user.name. As this is a basic prototype of some of functionality and the limitations of working with git on a Nexus; the git repository is fairly simple.

A prototype to test the usefulness of a search tool (mostly via personal usage) to help learners of Mandarin Chinese. The purpose of the tool is to provide a search tool to allow searches fuzzy pinyin searches against a Chinese to English dictionary. Search results are returned ordered by frequency of usage ordered from high usage to low usage.

The dictionary database is derived from the [cc-cedict dictionary](http://www.mdbg.net/chindict/chindict.php?page=cedict), the frequerncy data is derived from Leeds university frequency lists (the one derived from the Internet Corpus) see [this page](http://corpus.leeds.ac.uk/list.html) for more details.

The tool provides a type of fuzzy search which allows a user to choose from alternative pinyin of sounds they may have miss-heard, or that may have been pronounced in a non-standard way. A unigue characteristic of the Chinese language is that every syllable has a meaning and that there are a limited number of sounds (compared to English), the sounds are complicated however by tone which also alters the meaning. In theory it should be realatively easy for even an early learner of Chinese to hear real words in context and look them up by their Chinese pinyin sounds, in practice getting the tone right and even the exact syllable (depending on the speakers accent and clarity) is very hard, more detail on [Mandarin as a stream of syllables] (http://friedelcraft.blogspot.co.uk/2013/07/mandarin-stream-of-syllables-with.html). 

Another difficulty is that many Chinese words sound the same even taking into account tone (but especially if you do a search that does not take tone into account) context is important but for a learner they are likely to be concerned with high frequency words rather than the huge numbers of archaic words or namees of Chinese provinces etc. that are contained in most dictionaries. For this reason, frequency information has been added to the dictionary so that the highest frequency (most likely) meanings are returned first.  
 
The final application will include more funtionality including further functionality to help users that are not fully familiar with pinyin.
 
The next prototype will be re-implemented as a seperate project and made available via a web-browser.

##Installing and running

In order to test this prototype on an Android device you will need to install SL4A (scripting language for android) and Python for Android, you should be able to do this on most phones and tablets and should not have to root the device. This is reasonably advanced though and not entirely user friendly and despite allowing me to try this out on a portable device I appreciate I am not likely to get much if any feedback until I have completed a web-based prototype. 

##Usage

##Technical

The application uses the Scripting languages for Android [SL4A](http://code.google.com/p/android-scripting/) and needs the [Python for Android](http://code.google.com/p/python-for-android/) installed to work with this. Install the code from this repository somewhere under the directory where SL4A scripts are and run the file ```chinese_lookup.py```. There is more of an [introduction to SL4A here](http://www.ibm.com/developerworks/library/mo-python-sl4a-1/).

##Searching

A variety of searches against the dictionary are offered for debug purposes the only one of any interest though is the fuzzy pinying option. 

Enter the pinyin syallables as you hear them for a word or phrase with a space between each one you can omit the space from the end. Tone numbers are optional, if you are sure of the tone for a syllable it may help to narrow down options. 
"gang cai" will return words that match the syllables gang and cai plus homonyms (eg. gan tai etc.) 
"gang1 cai2" will return word that match the syllable gang and cia plus homonyms in first and second tone.
"gang1 cai" as above but first tone for the first syllable and any tone for the second.

You can use a "?" if you have no idea about part of a word, this can result in a lot of hits but may still be useful as results are returned by frequency of use. If you enter "shen ? jia" for example result options will be returned for 'shen ? jie(11)' and 'sheng ? jie(10)'. The first result for 'sheng ? jie' is 'Sheng4 dan4 jie2' or "Christmas" the second is "sheng1 ping2 jian3 jie4" or "biographic sketch", at this point common sense and context are likely to take over.  

