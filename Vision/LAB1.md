# Process and classify images with Azure cognitive vision services

<hr>

## Computer Vision Face and Emotion APIs

### Intro 

One of the most important and useful  features, the deep learning allowed us to accomplish is the ability to interpret the visual signals, that earlier were unrecognizable for the computers. APIs shown in this paragraph allow for the human face and face-emotion recognition.

- Face 
  - Detecting and feature analysis
  - Localization of basic features - hair, eyes, nose, mouth, etc.
  - Verification
  - Detection
  - Identification
  - Finding similarities
  - Grouping
- Emotions - adds functionalities to the Face Recognition API
  - distinguishes between: anger, disgust, fear, happiness, neutral, sadness, surprise.

### Use Cases

General use case is described in the name of the API - later only the imagination of the author is the limit ... sky is the limit :)

- Baby monitor with emotions recognition in hospitals, for easier management of multiple babies at the same time.
- Girlfriend monitor, one is never going to say something wrong anymore.
- Security cameras.
- ...

### How To

1. Create resource
2. Create API endpoint
3. Sending requests and receiving answers, like any other API.

### Pricing

There are several versions, but basic is free, it allows for 1000 connections/month wuthout paying.

<hr>

## Custom Vision

### Intro 

This module allows for quick and relatively easy creation and deployment of custom computer vision applications. Created and trained model is later deployed as an API, similarly to the face recognition.

### Use Cases

During my short carrier, I have created several models for computer recognition. It is always a long and painstaking process, choosing the correct framework, correct convolutional pretrained network, transfer-learning new data to existing model, calibrating the parameters, creating data pipeline. All this work can be hugely accelerated when using the Custom Vision module.

Again the possibilities are almost unending, from medical diagnostics to automating everyday work-flows. 

### How to

As always, one needs to create resource, than declare the project type. Later module requires to be fed with correctly prepared data, every image is supposed to be connected with label. After training the model, it can be published to corresponding URL.

### Pricing

There is a free version, comming with many constraints: 2 transactions/s, max 2 projects, only up to 1h of training time.

<hr>

## Video Indexer

### Intro 

One can call this module a leveled-up image recognizer, the video indexer is designed to extract insights from videos.

### Use Cases

- Finding matching videos
- Cutting out or censoring parts of videos
- Content matching

### How To

I works identical to all previous APIs.

### Pricing

- video analysis - priced per minute
- audio analysis - priced per minute
- basic audio analysis - much cheaper than normal - less features









