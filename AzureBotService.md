# LAB 2. - **Azure Bot Service**

## Build a bot with QnA Maker and Azure Bot Service 

### 1. Intro 

- Due to growing user base of almost any kind of businesses, the companies and service providers had to ensure, all the customers are serviced and helped properly. One way of providing such amount of contact is to employ more help-desk workers. Another is to create bots and automated response machines, which after proper training can take over all or part of human worker responsibilities. The QnA Maker is supposed to speed up a process of creating such bots and services.
- Bots cognitive abilities and answers pool are based on two interconnected databases.
  - A *knowledge base* of question and answer pairs - usually with some built-in natural language processing model to enable questions that can be phrased in multiple ways to be understood with the same semantic meaning.
  - A *bot service* that provides an interface to the knowledge base through one or more channels.

### 2. Use Cases

- Cases presented in the lessons
  - Voice calls,
  - Messaging services,
  - Online chat applications,
  - Email,
  - Social media platforms,
  - Collaborative workplace tools.
- The upper-mentioned cases are describing the uses very widely, and again it is quite difficult to find more examples.
  - Employee management and problem resolving,
  - Medical pre-examination.

### 3. How to

- How to:

  - First one needs to create the a user support bot,
  - Next the service provides a dedicated *QnA Maker portal* web-based interface that you can use to create, train, publish, and manage knowledge bases.
  - Than one needs to create the resources - data bases, containing questions and answers. These questions and answers could be hand-made, generated from previous FAQs or imported from a pre-defined *chit-chat* data source.
  - Train and test the base.
  - Publish the base.
  - Create and publish the bot. This automated machine can be connected to service on any web page or other application.

- Pricing model, transactions are quite easy to understand. Documents are the data bases containing the questions and answers:

  - Free - 3 transactions/second - documents up to 1MB, up to 100 trans./minute and up to 50 000 trans./month. - up to 3 documents.

  - Standard - 3 transactions/second - 100 trans./minute - unlimited number of documents - 

    https://azure.microsoft.com/pl-pl/pricing/details/cognitive-services/qna-maker/