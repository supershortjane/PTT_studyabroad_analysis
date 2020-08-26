# Analysis of Taiwanese international student's conversation toward pandemic by using PTT data.
What are Taiwanese student talking about pandemic? 



### Introduction

Studying abroad is a long journey filled with uncertainties. The outbreak of covid-19 makes the journey much more unpredictable and it greatly influences people's decision to study abroad. As an international student myself, I wonder how other Taiwanese international students react to the pandemic. 

### About Dataset

PTT is one of the largest online forums in Taiwan. The website contains various topics where people can share their ideas and thoughts . One of interesting topics for me is "studyabroad", where most Taiwanese international students would look up information or share their experience.

I web crawled the topic's data from 2020/01/01~2020/08/17, which contains 1077 posts. The data contains the following columns:

headline

date

author

push

boos

neutral

content

comment

web link

Snapshot of the DataFrame

### the volume of the discussion on "studyabroad"

Graph1 shows the trend volume from 2020/01/01 to 2020/08/17. The volume is defined as the number of comments of a post. In this analysis, a post which has a higher number than the average volume is considered as a popular post.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b2984a4f-36bd-49c9-8f7b-86ba0eba91ed/.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b2984a4f-36bd-49c9-8f7b-86ba0eba91ed/.png)

Graph2 shows the pandemic trend from 2020/01/01 to 2020/08/17, which defined the number of comments that mentioned words related with coronavirus. 

Within the 1077 posts, 11 percent mentioned the pandemic, compared to 25 percent within the 310 popular posts.

If we look at the trend over time, the trend is fluctuating, where it increases dramatically in the months of February, May and July.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c039ae4-4559-4431-9097-7f990cfbaa75/.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2c039ae4-4559-4431-9097-7f990cfbaa75/.png)

If we put graph1 and graph2 together, we can find that the volume is not always comes with a bigger size of conversation talking about pandemic.  For example, the most popular post has zero comment that mention virus. After reading through the post and its comment, the post is provided for people to report back their application status. Thus, there is up to 608 comments in this post.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6e1d6ac-0463-4834-8528-8a3399a90bee/vs.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a6e1d6ac-0463-4834-8528-8a3399a90bee/vs.png)

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52d73b82-ef63-46f8-a7d1-901e76338d5e/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/52d73b82-ef63-46f8-a7d1-901e76338d5e/Untitled.png)



Sorted by the number of comments mention pandemic, the following are the top 10 headlines discussing Covid-19. The subject could be mainly categorized in "the current epidemic situation in US",  "US visa issues", "defer decision".

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2df5b542-ca9b-47ff-aa7c-b2876dc6b505/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2df5b542-ca9b-47ff-aa7c-b2876dc6b505/Untitled.png)

1. [Q&A] Is it safe to go to US right away?
2. [Q&A] Won't people be afraid of being infected with the virus?
3. Re:[Q&A]Defer or not?
4. [NEWS]Harvard and MIT Sue to Overturn Order
5. [Thoughts]Wuhan pneumonia
6. [Thoughts]Rejection of AIT emergency appointment
7. [Q&A] Do we need to wear a mask?
8. [Q&A] Just asking... Do students are required to quarantine for 14 days as they enter US?
9. [Seeking people] (closed)cross school petition to restart AIT's regulations
10. Re:[Thoughts]Wuhan pneumonia

If we sort the ranking further by the number of comments, the top 3 popular posts are...

1. Re:[NEWS]Harvard and MIT Sue to Overturn Order
2. Re:[Q&A] Defer or not?
3. [Q&A] Won't people be afraid of being infected with the virus?

    ![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a8e18864-90df-4524-9d84-2cb09dfb554c/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a8e18864-90df-4524-9d84-2cb09dfb554c/Untitled.png)

### The change of international students' opinion towards epidemic

How do people's mind change to the virus at different times?

Taiwan's CDC announced that travel alerts are raised to level 3 for all the countries around the world. People should avoid any unnecessary travel, and those who travel back to Taiwan should have 14 days quarantine.

If 3/21 become a watershed moment, days before the watershed is classified as "Before a global outbreak", and days after the watershed is classified as "After a global outbreak".  

Before a global outbreak, people have few understanding of the covid-19 and underestimate its influence. After the outbreak, people around the world become anxious as new confirmed cases continuously grow at a fast pace. Meanwhile, governments propose epidemic prevention in succession and schools one after another reschedule the timeline of their programs and take measures in response to the virus. As a result, I wonder that "Before a global outbreak", how do Taiwanese students feel about covid-19? And How students react to the situation "After a global outbreak"?

### From face mask's shortage to an announcement of visa on foreign students

### Before a global outbreak

The chart shows a world cloud and top20 key words of the comments before a global epidemic outbreak.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5c56918-e6ae-4dd7-ae2a-4b1c50fcfa95/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f5c56918-e6ae-4dd7-ae2a-4b1c50fcfa95/Untitled.png)

From the graph, we could see those high frequency words are "Wuhan" "pneumonia" ''mask" "N95". It is observed that people mention these words often since the outbreak of epidemic make people to care about the current situation in local area and the issue that whether international students are able to buy masks in locals. Also, wearing a face mask or not is highly discussed during this time.

the source articles

1. [Q&A] Is it safe to go to US right away?
2. [Thoughts]Wuhan pneumonia
3. [NEWS] Suspension of US routine visa appointments
4. [Q&A] Do we need to wear a mask?
5. Re:[Thoughts]Wuhan pneumonia
6. [Q&A] Which items are highly needed in US? want to send packages to my family.

### After a global outbreak

The chart shows a world cloud and top20 key words of the comments after a global epidemic outbreak.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cabe8c1f-78ed-44a7-b705-2cccbdac41af/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cabe8c1f-78ed-44a7-b705-2cccbdac41af/Untitled.png)

In the later stage, "school", "student", "visa", "online class", "online" are highly appeared in comments. In contrast, "face mask" is not mentioned a lot as before. It is noted that  "visa", "online class", "online"  are the words that vastly related to the order baning foreign students from taking online courses in US. 

The timeline and information about the ban:

2020/07/06

The government declared that If all the courses turn into online courses for fall 2020 semester, international students should not stay in states. Also, bureau of immigration would not offer any visa to international students outside states. 

2020/07/14

After Harvard and MIT sued the government, Trump government dropped the announcement.

It is obvious that the action have stirred a backlash from universities and students. The action also prompt people's debate about the regulation on PTT website. From those popular post, beside the ban in July, the topics about that is it appropriate to study abroad currently? What is a possible impact if study abroad during epidemic? are greatly discussed among people as well.

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/717942ec-84fe-4ec6-91f4-2d9e3da80dd7/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/717942ec-84fe-4ec6-91f4-2d9e3da80dd7/Untitled.png)

### Conclusion

The trend chart helps us to track the volume  on "studyabroad" change overtime and wordcloud allowa us to take a look of what people actually talking about. Using all the data from people comments, instead of using our intuition, helps us to make more accurate decision in designing marketing campaigns.

This is my first analytics practice and web crawling. I enjoy the process a lot. This analysis is just a peek to the dataset. I know that there are much more things to find out from this data. I surely will explore this data further in the future.
