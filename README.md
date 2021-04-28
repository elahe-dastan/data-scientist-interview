# data-scientist-interview
When I wanted to become a backend developer my gorgeous [boyfriend](https://github.com/1995parham) made some practical 
interview with me then created a [repository](https://github.com/4lie/stories) and put the questions and answers there.
Now I want to apply for a data scientist position in which unfortunately he has no experience, so I'm making this 
repository and want to put all my practices here.<br/>

## Logical
1. you have buckets one 5 liters the other 3 liters, measure 4 liters:<br/>
first I make the 3 liters bucket full and then pour it to 5 liters bucket then I make it full again and pour it to the 
   5 liters bucket till it gets full so the amount of water left in the 3 liters bucket is 1 liter then I make the 5 liters
   bucket empty and pour that 1 liter in it then make the 3 liters bucket full again and pour it to the 5 liters bucket 
   which had 1 liter inside, so the result is 4 liters of water in the 5 liters bucket.
   
## ML algorithms
1. Differences between supervised and unsupervised:<br/>
In supervised the data has label<br/><br/>
   
2. How is logistic regression done?<br/><br/>
3. Explain steps in decision tree<br/><br/>
4. How do you build a random forest?<br/><br/>
5. How can you avoid overfitting? lasso regression<br/><br/> 
6. **What are feature selection methods? Wrapper methods: forward selection, backward selection. Filter methods: 
   Chi-Square, ANOVA (learn f-distribution, t-test, p-value, null hypothesis and significance level)**<br/><br/>
7. How do you deal with more than 30% missing value?<br/><br/>
8. Explain dimensionality reduction and its benefits<br/><br/>
9. **How will you calculate eigen values and eigen vectors of a 3 by 3 matrix**<br/><br/>
10. **How to maintain deployed model?**<br/><br/>
11. **What are recommender systems?** collaborative, content-based<br/><br/>
12. It rains on saturday with 0.6 probability and rains on sunday with 0.2 probability what is the probability that it
    rains this weekend?<br/><br/>
13. How can you select k for k-means?<br/><br/>
14. **What is the significance of p-value?**<br/><br/>
15. How can outlier values be treated?<br/><br/>
16. **How can you say that a time series data is stationary?**<br/><br/>
17. How can you calculate accuracy using confusion matrix?<br/><br/>
18. Write the equation and calculate precision and recall rate<br/><br/>
19. If a drawer contains 12 red socks, 16 blue socks, and 20 white socks, how many must you pull out to be sure of 
    having a matching pair?<br/><br/>
20. People who bought this, also bought... recommendations seen on Amazon is a result of which algorithm?<br/><br/>
21. Write a SQL query to list orders with customer information?<br/><br/>
22. You are given a dataset on cancer detection. You've built a classification model and achieved an accuracy of 96%.Why 
    shouldn't you be happy with your model performance? What can you do about it?<br/><br/>
23. **Which of the following ML algorithms can be used for imputing missing values of both categorical and continuous 
    variables? K-means-clustering --> crash, linear regression --> crash, Decision tree --> crash, K-NN works**<br/><br/>
24. calculate entropy [0,0,0,1,1,1,1,1]<br/><br/>
25. **What is the standard of the mean?**

## CafeBazaar
I had to answer to a few questions in the first phase of interview for the data scientist position at cafebazaar and I
was rejected because the questions needed deep understanding of linear algebra which I had forgotten, I can't remember 
what they exactly asked for, but I can give you a sense and another important point is that I now write the answer I 
think is true, but I'm not sure so **don't rely on my answers**:<br/>

1. We generated 5 random numbers using uniform distribution from [0, d] and the numbers are 5, 11, 13, 17, 23 find the 
minimum d with more than 95% probability.<br/>
   #####################################
2. Given uniform distributions X and Y and the mean 0 and standard deviation 1 for both, what’s the probability of 2X > Y?
![](2x%3Ey.jpg)
as you see this question is supeeeeer easyyyyyy but I couldn't answer :)))) cause I didn't expect these kinds of questions
   so shout out to you, they ask something like this expect it.

3. What can you say about the rank of the matrix when the number of samples is many more than the number of features?
pay attention the first phase is a test so there is no one who you can talk to or there is no box in which you can explain
   what you know if I had the chance I could say that in order to find out a linear regression model I know gradient 
   descent and normal equation and in normal equation we should calculate the inverse of X multiplied by X transpose and
   this term is not invertible if the number of samples in many more than features or if features have high correlation
   with each other, but I just could check one answer about the rank I mean they ask for pure linear algebra.
   Well, I couldn't even remember what the rank of a matrix was. The **rank** of a matrix is the number of **linearly 
   independent** columns (or rows), you can find the rank of a matrix using **echelon**. To be honest I don't have an 
   intuition but there is a theorem which says the column rank is equal to the row rank, so the first thing we can say is
   that the rank of this matrix at most will be the min(number of rows, number of columns). In this question the rank will
   be at most the number of samples.<br/>
   Full rank means the rank of the matrix is the largest possible number so if your features have high correlation with 
   each other (and the number of features are less than the number of samples) your matrix won't be full rank.
   
    
## Digikala
My interview experience with digikala was much more reasonable than cafebazaar. I was asked any kind of question from 
easy to hard. I had to **code**, know **sql**, know **ml models**, know **statistics**, and the nice thing was that in 
each of them the understanding was much more important than answering completely and all the questions were example based
again I can't remember every detail but here's what I remember:<br/>

1. bias/variance tradeoff. not only the meaning, but I had to explain it in different situations for example: When you 
   are using a random forest instead of a decision tree, what are you doing about bias/variance? I'm reducing variance.
   
2. explain bagging and boosting and how each of them affect bias/variance: In bagging we train a few models of the same
   type with different datasets and then use voting among them. In boosting we train a model with whole dataset, and we 
   increase the weight of the samples which are wrongly predicted and then train the second model by this dataset and 
   so on. They both decrease the variance.
   
3. I tell you to measure the height of the people in your college, what is distribution? Normal. Now I tell you to measure 
   the height of girls and boys in your college separately, what is the distribution? More normal. Now I tell you to 
   measure their salary, what is the distribution? Normal. What is the difference between these two distribution? the 
   salary distribution has a heavier tail than the height distribution.
   
## ROC
This part is not a question asked in any of the interviews, but I had to write it here cause it made me thick of my whole
life decisions. This is the story happened to me which may happen to you too. Once I had to solve a coding challenge, it
was an imbalanced dataset, and I had to train a classifier. As you can guess precision is not a good metric in this 
problem, cause even always predicting false gives you a high prediction. Then I found out that recall is as important as
precision, and the first thing popped to my mind was F1-score but then in my searches I heard about another metric called
ROC_AUC which was claimed to work well for an imbalanced dataset. That's wrong, in ROC_AUC we are calculating the area 
under the receiver operating characteristic curve. In this curve the y-axis is the sensitivity or true positive rate:<br/>
True Positive Rate = True Positives / (True Positives + False Negatives)<br/>
It measures the proportion of the positive data that we classify correctly. The x-axis is the false positive rate:<br/>
False Positive Rate = False Positives / (False Positives + True Negatives)<br/>
it measures the proportion of the negative data that we classify as positive, so if your dataset is highly imbalanced, and 
most of the data is labeled negative then the number of True Negative samples can affect the whole curve, if the model
classifies all samples as negative then the number of True Negative will be so large and False Positive Rate will be so 
small, and it assumes the model is so good so this metric is not good at all for imbalanced dataset classification. To 
solve it, we should use precision instead of false positive rate:<br/>
Precision = True Positives / (True Positives + False Positives)<br/>
it measures the proportion of the data the model classifies as positive is really positive, and the areas under this curve 
can be used as a good metric.

