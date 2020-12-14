# Automated Machine Learning

<hr>

<a href='https://www.youtube.com/watch?v=I8m4kZIeHJ4&ab_channel=MicrosoftDeveloper'>Nice YouTube Video</a>

<hr>

## 1. Intro


- The AutoML cloud service is used for creating, training and managing machine learning models. It combines many different types of models, and allows for easier training process. Deploying an effective ML model of any type is usually hard and requires time and resources that local machines usually lacks.

- In my understanding this service is supposed to provide all users, no matter of their education or field of expertise, the opportunity to enhance their everyday tasks with machine learning. Service allows to bypass the problematic part of the ML engineers work, one doesn't need to know how to write code or know any of the data-science or ML algorithms. 

  One can define a great variety of parameters, so the tool might be quite useful to normal data-scientists and programmers, but at the same time the entry threshold is low enough for almost everyone to use the service.

## 2. Use Cases

According to my knowledge, the main advantage of using the service is the speed and ease-of-use.

- Small companies, where data-analysis is not the main target of the product.
- Cases where the the time pressure is high.
- All custom classification, regression and clustering problems.

## 3. How to

- One can either use: the Azure platform, the SDK package or <a href='https://ml.azure.com/selectWorkspace?tid=common'>AutoML Webpage</a>, the last option is in my opinion easiest and most user friendly. It allows for step by step process which takes almost no time and effort. Inside created resource, user is allowed to manipulate data and methods - regression, classification and clustering, are all available to use. All algorithms are also implemented into the platform, as well as the pipeline data transformations or data augmentation algorithms.

  After training <a href='https://docs.microsoft.com/en-us/learn/modules/use-automated-machine-learning/use-auto-ml'>review</a> options are available.

  Deploying trained model is very similar to any other service in Azure. Finisher service is treated as endpoint, and one can connect to it as to ant Rest API service.

- Pricing - this time it is quite complicated, even at the basic level. There is no free version. <a href='https://azure.microsoft.com/pl-pl/pricing/details/machine-learning/'>Pricing Webpage</a> 

  The version best fitting the needs of the project I will be completing later is B2S version. 

  Virtual processors - 2

  RAM - 4GB

  Linux machine - $0.048/h

  Training machine - $0/h

  

  






