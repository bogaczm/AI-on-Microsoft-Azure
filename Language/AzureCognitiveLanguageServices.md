# LAB 1. - **Azure Cognitive Language Services**

## Classify and moderate text with Azure Content Moderator

### 1. Intro 

- This service is used to aid human moderator in running text based services. Azure assistant can block, approve and review text based content on web pages, forums or chats. The system is supposed to augment the ability of humans running the service to automate all the moderation systems. Additionally it allows to scan photos between 128 pixels to 4 MB, for pornography and inappropriate 
- Text moderation API can response with various information extracted from the text inputed to the API.
  - Potentially unwanted words or phrases, found in text.
  - The type of problem found in the unwanted text.
  - All personal information (PII) found in the text.

### 2. Use Cases

 - Shown during the course:
   	- Chat rooms,
    - Discussion boards,
    - Chatbots,
    - E-commerce catalogs,
    - Documents.
- Additional ideas, general ideas were shows in the course:
    - MES industrial systems - communication with clients,
    - In game chats - multi-player games,
    - Managing reviews,
    - Finding keywords, and later using it in NLP programs,
    - Key words and phrases can be connected with personal information to identify if text publisher is human or not.

### 3. How to

- How to use the service 
  - https://docs.microsoft.com/pl-pl/azure/cognitive-services/content-moderator/quick-start - best tutorial is the quick start written on the microsoft.com.
  - The set-up API takes in the text one wants to test, and in the response receive three JSON files:
    - Terms - words breaching policies and the location of the phrases,
    - Classification - three categories with scores between 0-1, how much entry matches the category,
    - PII - all available personal information.
- Pricing model:
  - Free, up to 1 transaction/second (5000 transactions per month),
  - Standard, up to 10 transactions/s (different thresholds, can be found on https://azure.microsoft.com/pl-pl/pricing/details/cognitive-services/content-moderator/).

## Language Understanding Intelligent Service (LUIS)

### 1. Intro 

- This service was created to enable easy and quick creation of interactive bots. LUIS is supposed to be embedded into other services to allow intelligent and sensible conversation with a human. LUIS uses key fragments of texts to interpret the immediate and indirect meaning of text. LUIS additionally extracts detail information from text, this activity could take a human worker long time.

- To interpret the meaning of the speaker (or writer) LUIS uses three basic aspects of language:

  - Utterances - the words used to convey information, just plain received text.
  - Intents - represents a task or action the user wants to perform. 
  - Entities - the key word or phrase LUIS is extracting from Utterance.

  Very good example is - "Please book two tickets to New York for New Years Eve", LUIS would extract the purpose '*book ticket*', the location *'New York'* and the time *'New Years Eve'* 

### 2. Use Cases

- Consumer friendly automated systems,
- Hospitals sign in systems,
- All types of booking systems,
- All types of automatic ordering systems - fast food restaurants.

### 3. How to

- How to use service

  One can test the LUIS on https://eu.luis.ai/. Again it works on basis of API requests, and in response the user receives information extracted from text or speech, categorized in the JSON files. File contains the grouped words and phrases with their interpretations and scorings between 0-1.

  To use the the functionality developer needs to use two services - LUIS resource and LUIS app.

  After creating LUIS resource, the model needs to be filled with appropriate data and trained on data.

- Pricing model:
  - Free, up to 5 transactions/second (up to 10000 transactions a month - one request is equal to two transactions),
  - Standard, up to 50 transactions/second (https://azure.microsoft.com/pl-pl/pricing/details/cognitive-services/language-understanding-intelligent-services/) - can transfer both text and speech requests.

## Discover sentiment in text with Text Analytics API

### 1. Intro 

- The service is supposed to help recognize the emotions and real opinions inside text or speech based opinions and feedbacks. The API is supposed to sort text based on what kind of emotions it conveys or if the feedback is positive or negative. 
- The main feature of this API is the compactness and it capabilities. The concept of rating the sentiment is not theoretically difficult problem, but it requires huge amount of labeled and good quality data, all of this is already in the service.

### 2. Use Cases

- Every customer based service, which needs to interpret feedback.
- It can be used to to aid **Content Moderator** in finding bad intent in text.

### 3. How to

- How to use service 
  - Use of API is very similar to previous services.
  - After setting up the Azure services, creating the resource and resource group it can be used in API console.
  - API returns JSON files with score between 0-1, where 0 is negative feedback and 1 is positive feedback.

- Pricing model - it is a part of Text Analytics Module:
  - Free - the most interesting one, inside the modules can be found: Sentiment Analytics, Key Phrase Extraction, Language Detection and Name entity Recognition (all together in free version get 5000 transactions per month)
  - Besides Standard version there are S0, S1, S2, S3 and S4 versions, all contain same features, but different prices at different thresholds. It is best to consult the https://azure.microsoft.com/en-us/pricing/details/cognitive-services/text-analytics/ web page before choosing the package.

