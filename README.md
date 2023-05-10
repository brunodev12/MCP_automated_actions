# MCP automated actions
Perform automated actions in the MegaCryptoPolis game

**Only available for testers at the moment**

## How does it work?

This bot obtains the hashes necessary to execute collection and repair transactions in the game.
These hashes are obtained through requests in the buildings detailed in the worksheet.

The private key is used to sign the hashes, in the ```get_sign_message.py``` script which imports the script:

```sign_message_evm.py```, ```sign_message_tron.js``` and ```sign_message_tron.py```

Feel free to review the scripts, you can also review the ```main.yml``` file where you can verify that the private key is only imported to sign the messages.

After obtaining the signed messages, a request is made to execute the transaction.

## Security

For your security, please enable two-step verification on your GitHub account and do not add collaborators to this repository.
This way, your secret variables will be more secure.

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

### - Step 4: Upload the .csv file to repository

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/81cf8db5-90da-4e48-8748-88170b96d2cf)

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/ea7b16dc-4e6f-4837-a2f4-a749d7902ab7)

Make sure you have only one .csv file on this repository, if there is another file it can cause the bot to run slower or fail. You can delete the files directly from GitHub

Once everything is set up your repository should look like this:

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/c1e31cb8-62e5-478e-8646-d38d846adec1)


### - Step 5: Run the bot

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/09b19959-c52b-452f-82b6-18890cc4b485)

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/d1b0ddd9-03d4-4160-9999-7d4633651297)

![image](https://github.com/brunodev12/MCP_automated_actions/assets/112636008/afa006a2-1984-491a-81fd-06a813e5dc04)

It's done. The bot will run every 6 hours.

Enjoy it :)

If you have any questions you can send me an email to: bruno.carter.dev@gmail.com

## Disclaimer

This repository is licensed under the GNU General Public License v3.0, which establishes that the author is not responsible for any kind of damage that this program may cause.

By using it you accept the terms and conditions.



