# ml-0451-final-proj
Group members: Prateek, Xianzhi
# data source:
Factory Productivity and the Concession System of Incorporation in Late Imperial Russia, 1894 - 1908. Replication data set package by Amanda G. Gregg.
(here)[https://www.aeaweb.org/articles?id=10.1257/aer.20151656] is the url, hosted on American Economic Association review.
# Prompt: Predicting which factory was incorporated, i.e., owned by an incorporated firm in the historical setting of Late Imperial Russia during 1894 to 1908
# Our Project Proposal


# Abstract

Our project uses historical primary data, which are scans of Russian records, digitized, cleaned, and curated by Prof. Amanda G. Gregg, that is freely available on American Economic Association's website. We are interested in what are the features contributing to a factory being incorporated in this historical setting. We need to note that this is an unbalanced data set, in the sense that most factories are not incorporated. 

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
We will have full success if we could implement a suitable machine learning model that is more sophisticated than simply applying the out-of-the-box sklearn functions, and make reasonable predictions about whether factories incorporate in Late Imperial Russia, 1894 - 1908.

“Partial success:” 
Maybe the ultra sophisticated model is actually not suitable for this question, so we have spent to much time on going down the wrong path. Then, we could demonstrate that this model would work in a different scenario, just not this one.

Alternatively, we could use a more naive approach to study the same time period in a more viable manner.

Written Deliverables
We will prepare a blog post summarizing our aims, methods and findings, and our findings easily accessible and publicly available.

# Resources Required
What resources do you need in order to complete your project? Data? Computing power? An account with a specific service?

We are currently unsure about the level of computing power our project will require.
We are planning on using the replication data set in the link provided before. 

Please pay special attention to the question of data. If your project idea involves data, include at least one link to a data set you can use. If you can’t find data for your original idea, that’s ok! Think of something related to your group’s interests for which you can find data.

Most projects should involve data in some way, but certain projects may not require data. Ask me if you’re not sure.

# What You Will Learn

We hope to better understand how logistic regression works, and how we can use some of these techniques to study historical data. we also hope that this project will help improve our ability to work collaboratively, and take on creative risks. The risk of working on something somewhat independently can feel daunting and requires a good deal of grit to get through. We hope that this experience with this project will make us into more skilled managers, and effectively, better researchers.

# Risk Statement

We only have a beginner level understanding of the Newton method for logistic regression, ROC curve, and support vector machines, and we are concerned about the degree to which we may be able to implement it. If this approach does not appear to be viable for us anymore, we might need to use a more naive approach, akin to the standard implementation of logistic regression approach used in class as one of the blog posts.


# Ethics Statement

We are both deeply interested in the economic history of capitalism, how it impacts and how it impacts different groups of people. I (Prateek) am hoping to incorporate this model into a larger study that assess how plantations assessed the political risk of the abolition of slavery. I am currently using data on elections in the 1850s and 60s as a proxy for political risk- however- I also hope to use my results from this model for added robustness. In addition to being cruel and inhumane, slavery in the Antebellum South depressed wages and stunted the region’s economic development. However, the level of economic dependence on slavery, in addition to the predominantly white voting base’s racist tendencies, led to further entrenchment. Similar arguments of economic dependence are frequently made against other progressive political reforms. Studying how firms choose to hedge or leverage their position in the face of political risk can help inform how progressive policies can be implemented while minimizing economic disruption. We also hope to construct a dataset that future scholars of the history and economics of racism can use to better understand the roots of capitalism and racism in America.

I understand that, when studying a period history as cruel as this one, it is essential to be cognizant about the level of harm caused. Slavery, as an institution, resulted in the kidnapping and commodification of millions of black people for the profit of mostly white slave traders and plantation owners. The language used in newspapers in this period can be extremely disturbing. Nevertheless, the study of this period is essential for us to understand how the histories of racism and capitalism are deeply intertwined with one another. It is extremely important for us to work with this data in a manner that is sensitive and tasteful.
