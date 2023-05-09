# MCP automated actions
Perform automated actions in the MegaCryptoPolis game

**Only available for testers at the moment**

## How to install

### - Step 1 : Fork this repository

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/4f271e82-304e-4f5c-89de-fffb10b39ffd)

### - Step 2 : Set environment variables

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/8f19291c-3176-4533-83c0-caa732bef8a6)


![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/51bcaea9-7924-4c3e-9666-58b182f9ba5c)


![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/960ce0ab-4412-4412-ae49-b4dce5c0657d)

The names of the secret variables must be:

**ADDRESS_BSC**

**ADDRESS_ETH**

**ADDRESS_TRON**

**PRIVATE_KEY_BSC**

**PRIVATE_KEY_ETH**

**PRIVATE_KEY_TRON**

Example:

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/1b7a08e4-c834-42ca-971d-aa6d4bb9c8af)

These variables are private, once set the content is not visible so make sure you enter the values correctly.

Once the environment variables are set it should look something like this:

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/0b280652-b534-4e34-b7ab-0486adbd5795)

### - Step 3 : Set up the worksheet

You can copy this spreadsheet and edit the values with your buildings:

https://docs.google.com/spreadsheets/d/1Vw91UgvBMplBrSm-GXZUNilzuSdJyvyJtUE-Ah62qGM/copy#gid=1618421998

You should see something like this:

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/4e808ba1-183f-4b4a-bb60-c5fc2d016570)

If you don't want to collect set the values to 0 in **Collect every X days** for the corresponding buildings.
If you don't want to repair set the values to 0 in **Repair when conditions is X** for the corresponding buildings.

For residential, office or factories buildings, set the collection value to 0, since that function is not enabled at the moment.
In case you set a collection value other than 0, there will be no change but the bot execution will be a bit slower.

Repair works on any building.

Once the buildings are configured you must download the file as .csv:

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/d8a761bc-a75e-4e04-90d4-318d8c758c15)

### - Step 4: Upload the .csv file to GitHub

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/81cf8db5-90da-4e48-8748-88170b96d2cf)

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/ea7b16dc-4e6f-4837-a2f4-a749d7902ab7)

Make sure you have only one .csv file on GitHub, if there is another file it can cause the bot to run slower or fail. You can delete the files directly from GitHub

### - Step 5: Run the bot

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/09b19959-c52b-452f-82b6-18890cc4b485)

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/d1b0ddd9-03d4-4160-9999-7d4633651297)

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/afa006a2-1984-491a-81fd-06a813e5dc04)

It's done. The bot will run every 6 hours.

Enjoy it :)

Any questions you can send me an email to: bruno.carter.dev@gmail.com




