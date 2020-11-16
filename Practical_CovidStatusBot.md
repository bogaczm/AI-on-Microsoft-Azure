# Covid Status Bot

### Youtube Video

https://youtu.be/g2CeKvuuOTE

### Use case

The bot will be enable user to easily access latest pandemics data i will also allow user to compare two countries side by side. The service will be based on 'COVID-19 API' (https://rapidapi.com/api-sports/api/covid-193/details).

Additional 'ester egg' function will use 'Random Useless Fact API'(https://uselessfacts.jsph.pl/).

### Used packages

- LUIS 
- Adaptive Cards
- Bot Framework Composer
- Bot Framework Emulator

### REST APIs

Both APIs are free, and both have very good examples, which can help in development. It is very important to create account on RapidAPI.com and generate the individual key, which allows to perform requests on particular API.

### Installation and bot creation process

1. Install Bot Framework Composer 
2. Create new bot
3. Create welcome action
4. Create triggers containing LUIS to jump to different dialogs
5. Generate example data for LUIS (best to do it outside of the composer in text editor)
6. Create dialog logic and HTTP requests
7. Create Adptive Cards

### Installation

From my experience it is best to use the desktop version, it is much easier for installation.

- Install Emulator (https://github.com/microsoft/BotFramework-Emulator/releases/tag/v4.11.0)
- Install .NET Core SDK 3.1 or above (https://dotnet.microsoft.com/download/dotnet-core/3.1)
- Install Composer (https://aka.ms/bf-composer-download-win)

### Create new bot 

It is best to create a new bot from scratch, but some functions are well shown in the examples section. It is valuable to look into them.



The welcome action is already created. Two most important pages are 'User Input' and 'Bot Responses', it is here where all definitions of actions are created.



It is a good practice to use these pages to create the placeholders for all actions, and later only use the names in the dialog trees.



Inside the trigger we can not only specify the example sentences and phrases, but also other conditions for score. 

``

Using the HTTP request is very similar to using request in postman or any other program (programming language). Be sure to check if the request was performed correctly - statusCode == 200. Additionally it is very important to save the requests response into internal variable otherwise it will be lost. The variable is structures in the same way as the response, so it is an object with properties.



### Creating Luis resource

LUIS doesn't work natively with Composer, it a service which needs to be activated and run in the background. Fortunately is free up to 5000 calls per month, so it is enough for this purpose. Even-though is quite useful to check the amount of used calls, to learn how much and when is used.



The Composer will ask for the generated key every time after program reset, when starting the bot.



### Create adaptive cards

Adaptive cars are very useful tool for data visualization, bot seems much more advanced and better prepared, when asked data is server inside well structured card. The cards are JSON structures, which can be read and interpreted by Emulator or any other Bot serving engine. On https://adaptivecards.io/ one can find many useful examples which can be reworked into any shape.



JSON files can be created from scratch or reworked inside the Cards designer. User data is delivered via JSON structures inside card declaration JSON the variables are written as `"${varaible}"` same variable must be later called in the user data file.

