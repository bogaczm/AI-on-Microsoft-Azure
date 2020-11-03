# LAB 3. - **Process and Translate Speech**

## Translate speech input to text

### 1. Intro 

- The Speech-to-Text aspect of the Speech service transcribes audio streams into text. Your application can display this text to the user or act upon it as command input. You can use this service either with an SDK client library (for supported platforms and languages) or a representational state transfer (REST) API.

### 2. Use Cases

- Use cases presented in the tutorials:
  - Extend the reach of your applications across mobile, desktop, and web to provide speech-to-text transcription.
  - Easily translate to and from multiple, supported languages through the open REST interface of the Speech SDK. This API is a cloud-based automatic speech-translation service (also known as machine translation).
  - Perform Text-to-Speech operations that can accept text input and then output a spoken version of that text, using synthesized speech.
  - Perform entity recognition through integration with Language Understanding (LUIS)

- Other use cases, are very hard to think of, this process is usually just a smaller piece of the greater system.
  - Operating machines and programs with usage of voice commands.
  - Quick note making.

### 3. How to

- How to:

  - Create the resource group and choose pricing,
  - Use Python or C# to create the audio files management program,
  - The voice capturing happens in real time,
  - Send the request containing language definitions,
  - Receive a transcript.

- Price model:

  - The rules of pricing is quite complicated, so it is best to always check the web page before use.

    https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/

## Synthesize Text Input to Speech

### 1. Intro 

- Text-to-speech is sometimes known as voice synthesizing. Typically a collection of synthesized voices are available for users to choose from. The text that is used for input, is evaluated and then passed to the synthesizer to generate the spoken words. Synthesized speech has improved over time and now sound less like a computer-generated representation.
- The most interesting part of voice generation is the way that sound is created. Classic approach is to record actors and later their voice is enhanced by usage of deep neural networks.

### 2. Use Cases

- **Improving accessibility**: text-to-speech technology enables content owners and publishers to respond to the different ways people interact with their content. People with visual impairment or reading difficulties appreciate being able to consume content aurally. Voice output also makes it easier for people to enjoy textual content, such as newspapers or blogs, on mobile devices while commuting or exercising.
- **Responding in multitasking scenarios**: text-to-speech enables people to absorb important information quickly and comfortably while driving or otherwise outside a convenient reading environment. Navigation is a common application in this area.
- **Enhancing learning with multiple modes**: Different people learn best in different ways. Online learning experts have shown that providing voice and text together can help make information easier to learn and retain.
- **Delivering intuitive bots or assistants**: The ability to talk can be an integral part of an intelligent chat bot or a virtual assistant. More and more companies are developing chat bots to provide engaging customer service experiences for their customers. Voice adds another dimension by allowing the bot's responses to be received aurally (for example, by phone).

### 3. How to

- How to:

  - The process is identical to the one described before.
  - Difference is that the request contains text, and in response the audio file is sent back.

- Price model:

  - The rules of pricing is quite complicated, so it is best to always check the web page before use.

    https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/

## Translate speech with the speech service

### 1. Intro 

- Speech translation is the process by which conversational, spoken phrases are instantly translated (and spoken aloud) in a second language. Speech translation technology enables speakers of different languages to communicate easily across a broad range of services for both consumer and business scenarios, especially in the world science, cross-cultural exchange, and global business interaction.

  This services usually use many different systems embedded into work flow.

- Possibilities:

  - Translate Speech to Text from Microphone Input
  - Translate Speech to Speech in a Different Language
  - Translate Speech to Multiple Target Languages

### 2. Use Cases

- Live presentation translation
- In-person or remote translated communications
- Customer support
- Business intelligence
- Media subtitling
- Multilingual AI interactions

### 3. How to

- How to:

  - Create Azure Speech Resource,
  - Write the local code requesting the real time translation,
  - Speak,
  - Choose the language of translation.

- Price model:

  - The rules of pricing is quite complicated, so it is best to always check the web page before use.

    https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/