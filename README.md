# ml-0451-final-proj
Group members: Prateek, Xianzhi
# data source:
Factory Productivity and the Concession System of Incorporation in Late Imperial Russia, 1894 - 1908. Replication data set package by Amanda G. Gregg.
(here)[https://www.aeaweb.org/articles?id=10.1257/aer.20151656] is the url, hosted on American Economic Association.
### Source for some background reading on Logistic Regression 
(here)[https://statacumen.com/teach/SC1/SC1_11_LogisticRegression.pdf] is the url.
# Prompt: Predicting which factory was incorporated, i.e., owned by an incorporated firm in the historical setting of Late Imperial Russia during 1894 to 1908
# Our Project Proposal


# Abstract

We aim to study the history and effects of incorporation in Russia. Our project uses historical primary data from Russian factory censuses which were digitized, cleand and curated by Professor Amanda Gregg and are freely available on the American Economic Association's website. While economic historians frequently bicker about the origins and effectiveness of corporations- most agree that the 19th century witnessed the rise of the corporate business form in Europe and North America. Firms in Russia began incorporatinng relatively late- in the late 19th century. We aim to study the factors that may lead to a firm choosing to incorporate- and to study the effects of incorporation on the firm itself. We intend to use supervised learning and feature engineering to study the variables that are the most influenced incorporation, and the variables that make incorporation more likely. We need to note that this is an unbalanced data set, in the sense that most factories are not incorporated. 

We are interested in using supervised learning to look at how different features relate to the dependent variable, which is incorporated or not. 


# Motivation and Question
We are interested in identifying what are the factors a factory might considered before they make a decision to incorporate or not, in this historical setting.
We would like to use this replication data set to test our machine learning models (logistic regression, etc) and make predictions. We would also look out for bias in machine learning, since our data set is unbalanced. Also, it is a historical fact that there was only a low percentage of incorporation going on in Late Imperial Russia at that time. Our data comes from (here)[https://www.aeaweb.org/articles?id=10.1257/aer.20151656], and our question is how to predict whether a factory incorporate or not in that period. Our model should be about to give predictions that are more or less consistent with the arguments presented in the published paper, "Factory Productivity and the Concession System of Incorporation in Late Imperial Russia, 1894-1908."

# Planned Deliverables

We will have a Python package containing all code used for algorithms and analysis, including documentation.
We will have a Jupyter notebook illustrating the use of the package to analyze data.

We plan to include presentation slides to summarize our findings.

We describe what deliverable will be able to do and how we will evaluate its effectiveness. Let’s consider two scenarios:

“Full success:” 
We will have full success if we could implement a suitable machine learning model (for example, code up logistic regression using Newton's method) that is more sophisticated than simply applying the out-of-the-box sklearn functions, and make reasonable predictions about whether factories incorporate in Late Imperial Russia, 1894 - 1908.

“Partial success:” 
Maybe the ultra sophisticated model is actually not suitable for this question, so we have spent to much time on going down the wrong path. Then, we could demonstrate that this model would work in a different scenario, just not this one.

Alternatively, we could use a more naive approach to study the same time period in a more viable manner.

Written Deliverables
We will prepare a blog post summarizing our aims, methods and findings, and our findings easily accessible and publicly available.

# Resources Required
What resources do you need in order to complete your project? Data? Computing power? An account with a specific service?

We are currently unsure about the level of computing power our project will require. We think our laptop should have enough computing power for the job.
We are planning on using the replication data set in the link provided before. This data set is open to the public and could be accessed without any paywall.


# What We Will Learn

We hope to better understand how logistic regression works, and how we can use some of these techniques to study historical data. we also hope that this project will help improve our ability to work collaboratively, and take on creative risks. The risk of working on something somewhat independently can feel daunting and requires a good deal of grit to get through. We hope that this experience with this project will make us into more skilled managers, and effectively, better researchers.

# Risk Statement

We only have a beginner level understanding of the Newton method for logistic regression, ROC curve, and support vector machines, and we are concerned about the degree to which we may be able to implement it. If this approach does not appear to be viable for us anymore, we might need to use a more naive approach, akin to the standard implementation of logistic regression approach used in class as one of the blog posts.


# Ethics Statement

Our findings could be particularly beneficial to businesses that are debating about whether they should adopt the corporate form. They could also be beneficial to legal scholars and politicians aiming to regulate corporations for maximal societal well-being. This is particularly true for developing countries which are still in the process of determining the adequate and apppropriate legal powers and concessions for corporations. As our findings focus on Russia in the late 19th century and the early 20th century, they may not be externally valid to every legal system. 

We argue that the world could be a better place due to the nature of our research. Corporations are pivotal to the global economy in the 21st century. A better understanding of how corporations operate and has the potential to leave everyone in our highly interconnected economy better off. A greater understanding of why firms choose to incorporate and how much better off it leaves them helps inform us about the incentive structure within firms and how they can be taxed and regulated. It can also help firms decide whether they want to incorporate or not- which could result in them being better managed, treating their employees better and producing goods at lower prices benefiting consumers.
