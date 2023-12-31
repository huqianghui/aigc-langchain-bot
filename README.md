<h1 align="center">AIGC By langchain + Bot Service
</h1>

This bot has been created using [Bot Framework](https://dev.botframework.com).

Services and tools used:

- Azure App Service (Web App) - Chatbot API Hosting
  <img width="1400" alt="Screenshot 2023-10-01 at 10 20 10" src="https://github.com/huqianghui/aigc-langchain-bot/assets/7360524/167796f5-270e-4410-89ff-dbd7ea4f1327">

- Azure Bot Service - A service for managing communication through various channels
  <img width="1400" alt="Screenshot 2023-10-01 at 10 21 21" src="https://github.com/huqianghui/aigc-langchain-bot/assets/7360524/fb6df525-eb24-4d8c-bfee-14da782b37c1">


## Deploy Bot To Azure Web App

Below are the steps to run the Bot API as an Azure Wep App, connected with the Azure Bot Service that will expose the bot to multiple channels including: Web Chat, MS Teams, Twilio, SMS, Email, Slack, etc..

1. In Azure Portal: In Azure Active Directory->App Registrations, Create an Multi-Tenant App Registration (Service Principal), create a Secret (and take note of the value)

2. Deploy the Bot Web App and the Bot Service by clicking the Button below and type the App Registration ID and Secret Value that you got in Step 1 along with all the other ENV variables you used in the Notebooks

3. Zip the code of the bot by executing the following command in the terminal:

4. Using the Azure CLI deploy the bot code to the Azure App Service created on Step 2
```bash
az login -i
az webapp deployment source config-zip --resource-group "<resource-group-name>" --name "<name-of-backend-app-service>" --src "aigc-langchain-bot.zip"
```
**Note**: If you get this error: `An error occured during deployment. Status Code: 401`. **Cause**: Some FDPO Azure Subscriptions disable Azure Web Apps Basic Authentication every minute (don't know why). **Solution**:  before running the above `az webapp deployment` command, make sure that your backend azure web app has Basic Authentication ON. In the Azure Portal, you can find this settting in: `Configuration->General Settings`.
Don't worry if after running the command it says retrying many times, the zip files already uploaded and is building.

5. In the Azure Portal: **Wait around 5 minutes** and test your bot by going to your Azure Bot Service created in Step 2 and clicking on: **Test in Web Chat**
<img width="1000" alt="Screenshot 2023-10-01 at 10 23 09" src="https://github.com/huqianghui/aigc-langchain-bot/assets/7360524/ae0b81cf-27fe-4f5b-912c-c5a44b906415">

**Note**: If you get this error: `An error occured during testing. Status Code: 404`. **Cause**: app:app cannot be found . **Solution**:   In the Azure Portal, you can find this settting in: `Configuration->Startup Command: gunicorn --bind 0.0.0.0 --worker-class aiohttp.worker.GunicornWebWorker --timeout 600 app:APP`.
Don't worry if after running the command it says retrying many times, the zip files already uploaded and is building. 

7. In the Azure Portal: In your Bot Service , add multiple channels (Including Teams) by clicking in **Channels**
<img width="1400" alt="Screenshot 2023-10-01 at 10 24 39" src="https://github.com/huqianghui/aigc-langchain-bot/assets/7360524/ffaa2909-4e71-4e45-b2a6-38e2778fad92">

8. Go to [apps/frontend](https://github.com/huqianghui/Azure-Cognitive-Search-Azure-OpenAI-Accelerator/tree/main/apps/frontend) folder and follow the steps in README.md to deploy a Frontend application that uses the bot.
<img width="1200" alt="Screenshot 2023-10-01 at 10 25 30" src="https://github.com/huqianghui/aigc-langchain-bot/assets/7360524/f7f05eba-81a9-43c2-9ea5-3f2b048bf3aa">



## Reference documentation

- [Bot Framework Documentation](https://docs.botframework.com)
- [Bot Samples code](https://github.com/microsoft/BotBuilder-Samples)
- [Bot Framework Python SDK](https://github.com/microsoft/botbuilder-python/tree/main)
- [Bot Basics](https://docs.microsoft.com/azure/bot-service/bot-builder-basics?view=azure-bot-service-4.0)
- [Azure Bot Service Introduction](https://docs.microsoft.com/azure/bot-service/bot-service-overview-introduction?view=azure-bot-service-4.0)
- [Azure Bot Service Documentation](https://docs.microsoft.com/azure/bot-service/?view=azure-bot-service-4.0)
- [Channels and Bot Connector Service](https://docs.microsoft.com/azure/bot-service/bot-concepts?view=azure-bot-service-4.0)
