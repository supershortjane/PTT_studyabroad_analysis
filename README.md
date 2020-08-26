# Analysis of PTT(online forum in Taiwan)Comments Related With Pandemic
What are Taiwanese student talking about pandemic? 



## Introduction
Studying abroad is a long journey filled with uncertainties. The outbreak of Covid-19 makes the journey much more unpredictable and it greatly influences people’s decision to study abroad. As an international student myself, I wonder how other Taiwanese international students react to the pandemic.

## Dataset
PTT is one of the largest online forums in Taiwan. The website contains various topics where people can share their ideas and thoughts . One of interesting topics for me is “studyabroad”, where most Taiwanese international students would look up information or share their experience.
I web crawled the topic’s data from 2020/01/01~2020/08/17, which contains 1077 posts. The data contains the following columns:
**headline, date, author, push, boos, neutral, content, comment, web link**
![image](https://user-images.githubusercontent.com/32606310/91281419-a49e6a00-e7ba-11ea-94c9-c075f6c379de.png)
![image](https://user-images.githubusercontent.com/32606310/91282353-d106b600-e7bb-11ea-9523-f197dc349b72.png)

## Packages
NLP:jieba<br/>
Visualization: matplotlib, wordcloud, plotly<br/>


## Visualization

**Volume on "studyaboard"**<br/>
![總留言數](https://user-images.githubusercontent.com/32606310/91273824-61d79480-e7b0-11ea-994d-ee7cea2135dd.png)<br/>

**Volume that mentions words related with epidemic on "studyaboard"**<br/>
![疫情留言數](https://user-images.githubusercontent.com/32606310/91274066-bc70f080-e7b0-11ea-8963-3129488c8582.png)<br/>

**Volume vs. Volume discussed epidemic** <br/>
![疫情vs總留言](https://user-images.githubusercontent.com/32606310/91279414-06a9a000-e7b8-11ea-91d9-cdc561ba75c5.png)<br/>

**"Before an global outbreak" wordcloud** <br/>
![Wordcloud_Before](https://user-images.githubusercontent.com/32606310/91279556-38bb0200-e7b8-11ea-885b-e0489f6541d6.png)<br/>

**"After an global outbreak" wordcloud** <br/>
![Wordcloud_After](https://user-images.githubusercontent.com/32606310/91279532-3193f400-e7b8-11ea-8a52-b9724dda3aa0.png)<br/>

## More details of my analysis
Go check my finding on [Medium](https://medium.com/@supershortjanechaseadream/analysis-of-taiwanese-international-students-conversation-toward-pandemic-by-using-ptt-data-d6d9d8589ad9)
