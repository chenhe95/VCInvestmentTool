# LoopBox 
<img src="loopboxlogo.png" width="13%"/> is an intelligent form that startups would fill instead of bombarding VCs with unanswered emails.

### Problem
Two of us are entrepreneurs and we know that without a solid intro, our chances of getting a meeting with a top VC are very little. As we are versed in the topic, we learned that a lot of VCs are bombarded with email and they have very little time to be able to meet with all and spend time (Fred Wilson archived 1625 unread emails on new year's eve). As a young entrepreneur getting started, your chances of being introduced to a top tier VC are very little, and that means that VCs might miss out the next unicorn.

### Opportunity
The barriers to entry keep getting lower and lower. The ability for someone to create almost anything they want has become democratized. With the rise of funding demand, VCs have to develop a new way that allows them to filter and analyze companies. The opportunity lies in evaluating startups based on their responses and framework, giving a chance for the largest number of startups to be heard. From the VC side, the opportunity lies in cleaning out their email and in increasing the number of startups looked at which minimizes the risk of letting the next unicorn slip under their shoulder.

### Function
The form asks companies general questions. It can categorize startups and compare them in a clear way for the VC to look at and decide on who to respond. A query is available for the investor side where when a company name is typed, it automatically analyzes the list of currently registered companies using NLP similarities and analyzes potential competitors and differences between the two companies.

### Design
The backend component composes of a server that can take in and process the information that a company puts into the web app. Additionally, it uses information extraction and entity recognition to identify and deduct key aspects about the startup dynamically. We also used web scraped Bloomberg articles with a Quora question dataset to build a recent corporate and appropriate training set. In the backend, we use a deep neural network architecture composing of two LSTM units for word semantic embedding for the two documents linked to a series of dense layers terminated with a single unit softmax output for sentence similarity.

### Challenges
The very first challenge we ran into was finding the data about early-stage companies. We looked at some YC applicants alongside some financial information from Crunchbase in order to be able to create a few companies' portfolio. The second challenge was the competitive analysis. We could analyze quantitative data and make a use of it. Last but not least, doing the semantic questions analysis to be able to ask specific questions was a hard task. The architecture and data to train on were not very obvious.

