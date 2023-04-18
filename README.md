# ml-0451-final-proj
Group members: Prateek, Xianzhi
# data source:
https://chroniclingamerica.loc.gov/
# Prompt: Predicting productivity on farms in Middlebury, Vermont in 1850 and 1860.
# Our Project Proposal


# Abstract

change 123

Our project uses historical primary data, which are scans of farm records, we have roughly 400 data entries. We are interested in what contributes to higher productivity on a farm.  
Alternatively, we could also use supervised learning to look at how different variables relate to the cash value of the farm. Cash value measured in 1850 and 1860 USD, and convert to the current dollar value.


# Motivation and Question
We 
for which we could test our models and make predictions. We would also look out for bias in machine learning, since our topic is controversial by definition. Our data comes from Chronicling America, and our questions is how to infer the likelihood of slavery being abolished from those newspaper articles in that period. Our model should be about to give predictions that are more or less consistent with what an educated middlebury student would guess.


# Planned Deliverables

We will have a Python package containing all code used for algorithms and analysis, including documentation.
We will have a Jupyter notebook illustrating the use of the package to analyze data.

We might include a short essay to summarize our findings.

We describe what deliverable will be able to do and how we will evaluate its effectiveness. Let’s consider two scenarios:

“Full success:” 
We will have full success if we could implement a suitable machine learning model that is quite more sophisticated than the naive bag of words approach, and make reasonable predictions about the likelihood regarding slavery being abolished that are consistent with human predictions.

“Partial success:” 
Maybe the ultra sophisticated model is actually not suitable for this question, so we have spent to much time on going down the wrong path. Then, we could demonstrate that this model would work in a different scenario, just not this one.

Alternatively, we could use a more naive approach to study the same time period in a more viable manner.

Written Deliverables
We will prepare a blog post summarizing our aims, methods and findings, and our findings easily accessible and publicly available.

# Resources Required
What resources do you need in order to complete your project? Data? Computing power? An account with a specific service?

We are currently unsure about the level of computing power our project will require.
We are planning on using the Library of Congress’s Chronicling America project- and are unsure about how we can bulk download the data. It looks as though there are some built in tools we could use (https://chroniclingamerica.loc.gov/about/api/), however, we’re not sure how we can filter by time period and region, and only download the text files. We might need some assistance here.

Please pay special attention to the question of data. If your project idea involves data, include at least one link to a data set you can use. If you can’t find data for your original idea, that’s ok! Think of something related to your group’s interests for which you can find data.

Most projects should involve data in some way, but certain projects may not require data. Ask me if you’re not sure.

# What You Will Learn

I hope to better understand how Natural Language Processing works, and how I can use some of these techniques to study historical textual data. I also hope that this project will help improve my ability to work collaboratively, and take on creative risks. The risk of working on something somewhat independently can feel daunting and requires a good deal of grit to get through. I hope that this experience with this project will make me a more skilled manager, and effectively, a better researcher.

# Risk Statement

We only have a surface level understanding of the Latent Dirichlet Algorithm and are concerned about the degree to which we may be able to implement it. If this approach does not appear to be viable for us anymore, we might need to use a more naive approach, akin to the bag of words- vectorization approach used in class to study the sentiment of covid 19 tweets.

The OCR used by Chronicling America is filled with errors. If the level of errors makes it impossible for us to parse the text through our program, we might need to pivot slightly and use a different, more modern dataset of newspapers.


# Ethics Statement

We are both deeply interested in the economic history of capitalism, how it impacts and how it impacts different groups of people. I (Prateek) am hoping to incorporate this model into a larger study that assess how plantations assessed the political risk of the abolition of slavery. I am currently using data on elections in the 1850s and 60s as a proxy for political risk- however- I also hope to use my results from this model for added robustness. In addition to being cruel and inhumane, slavery in the Antebellum South depressed wages and stunted the region’s economic development. However, the level of economic dependence on slavery, in addition to the predominantly white voting base’s racist tendencies, led to further entrenchment. Similar arguments of economic dependence are frequently made against other progressive political reforms. Studying how firms choose to hedge or leverage their position in the face of political risk can help inform how progressive policies can be implemented while minimizing economic disruption. We also hope to construct a dataset that future scholars of the history and economics of racism can use to better understand the roots of capitalism and racism in America.

I understand that, when studying a period history as cruel as this one, it is essential to be cognizant about the level of harm caused. Slavery, as an institution, resulted in the kidnapping and commodification of millions of black people for the profit of mostly white slave traders and plantation owners. The language used in newspapers in this period can be extremely disturbing. Nevertheless, the study of this period is essential for us to understand how the histories of racism and capitalism are deeply intertwined with one another. It is extremely important for us to work with this data in a manner that is sensitive and tasteful.
