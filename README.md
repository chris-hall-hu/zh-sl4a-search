#zh-sl4a-search

##Introduction

**Note** this prototype was mainly developed on a Nexus 7 during bus journeys and there have been a couple of minor issues with git on the Nexus for example I cannot get commits to pick up my user.name. As this is a basic prototype of some of functionality and the limitations of working with git on a Nexus; the git repository is fairly simple.

A prototype to test the usefulness of a search tool to help learners of Mandarin Chinese. The purpose of the tool is to initiall provide a search tool to allow searches against a Chinese to English dictionary. Search results are returned ordered by frequency of usage ordered from high usage to low usage.

The dictionary database is derived from the [cc-cedict dictionary](http://www.mdbg.net/chindict/chindict.php?page=cedict), the frequerncy data is derived from Leeds university frequency lists (the one derived from the Internet Corpus) see [this page](http://corpus.leeds.ac.uk/list.html) for more details.

The tool provides a type of fuzzy search which allows a user to choose from alternative pinyin of sounds they may have miss-heard, or that may have been pronounced in a non-standard way. A unigue characteristic of the Chinese language is that every syllable has a meaning and that there are a limited number of sounds (compared to English), the sounds are complicated however by tone which also alters the meaning. In theory it should be realatively easy for even an early learner of Chinese to hear real words in context and look them up by their Chinese pinyin sounds, in practice getting the tone right and even the exact syllable (depending on the speakers accent and clarity) is very hard. 

Another difficulty is that many Chinese words sound the same even taking into account tone (but especially if you do a search that does not take tone into account) context is important but for a learner they are likely to be concerned with high frequency words rather than the huge numbers of archaic words or namees of Chinese provinces etc. that are contained in most dictionaries. For this reason, frequency information has been added to the dictionary so that the highest frequency (most likely) meanings are returned first.  
 
The final application will include more funtionality including further functionality to help users that are not fully familiar with pinyin.
 
The next prototype will be re-implemented as a seperate project and made available via a web-browser.

##Installing and running

In order to test this prototype on an Android device you will need to install SL4A (scripting language for android) and Python for Android, you should be able to do this on most phones and tablets and should not have to root the device. 

This ia reasonably advanced though and despite allowing me to try this out on a portable device I appreciate I am not likely to get much if any feedback until I have completed a webbased prototype. 

##Usage

##Technical

The application uses the Scripting languages for Android [SL4A](http://code.google.com/p/android-scripting/) and needs the [Python for Android](http://code.google.com/p/python-for-android/) installed to work with this. Install the code from this repository somewhere under the directory where SL4A scripts are and run the file ```chinese_lookup.py```. There is more of an [introduction to SL4A here](http://www.ibm.com/developerworks/library/mo-python-sl4a-1/).
