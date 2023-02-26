# NotionAI Discord Bot

[中文](README.md) | English

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/NotionAI-Discord-Bot)](https://github.com/TheExplainthis/NotionAI-Discord-Bot/releases/)


## Introduction
Notion, a note-taking software, has launched its own NotionAI service in recent months. How powerful is it? You can check out the video below:

[![NotionAI Introduction](https://i.ytimg.com/vi/RDZ3mY10zY8/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAzPk5CktB6wPz8lgHguLi2UjfrOw)](https://youtu.be/RDZ3mY10zY8)

NotionAI is similar to ChatGPT, but it provides various functions, such as translation, itinerary planning, email writing, copywriting, brainstorming, etc. This article will teach you how to use NotionAI on Discord to enhance team collaboration.

![NotionAI-Discord-Bot-Demo1](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/NotionAI-Discord-Bot-En-Demo1.png)
![NotionAI-Discord-Bot-Demo2](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/NotionAI-Discord-Bot-En-Demo2.png)

## Installation Steps
### Token Retrieval
1. Obtain NotionAI Token:
    1. Login to the web version of [Notion](https://www.notion.so/)
    2. After logging in, right-click on the web page -> "Inspect" -> "Application" -> Token and then in Cookies, and SpaceId in LocalStorage, as shown below
    * ![Get-Notion-Token](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/Get-Notion-Token.png)
    * ![Get-Notion-SpaceId](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/Get-Notion-SpaceId.png)
2. Obtain Discord Token:：
    1. Login to [Discord Developer](https://discord.com/developers/applications)
    2. Create a bot:
        1. Enter `Applications` on the left
        2. Click `New Application` in the upper right corner and enter the name of the bot > after confirmation, enter the new page.
        3. Click `Bot` on the left
        4. Click `Add Bot` on the right
        5. The `MESSAGE CONTENT INTENT` below needs to be turned on
        6. Click `Save Change`
        7. The Token can be selected at the top by clicking `View Token` or if you have already applied, it will be the `Reset Token` button.
    3. Set up OAuth2
        1. Click `OAuth2` on the left
        2. Click `URL Generator` on the left
        3. On the right, select `bot` under `SCOPES` and `Administrator` under `BOT PERMISSIONS` at the bottom right
        4. Copy the bottom URL to the browser
        5. Select the server to join
        6. Click `Continue` > `Authorize`

### Project Setup
1. Fork Github project:
    1. Register/Login to [GitHub](https://github.com/)
    2. Access [NotionAI-Discord-Bot](https://github.com/TheExplainthis/NotionAI-Discord-Bot)
    3. Click `Star` to support the developer
    4. Click `Fork` to copy all the code to your own repository
2. Deployment (free space):
    1. Go to [replit](https://replit.com/)
    2. Click `Sign Up` to log in directly with your Github account and authorize it -> click `Skip` to skip the initialization settings
    3. After entering, click `Create` in the center of the main page -> a pop-up window will appear, click `Import from Github` in the upper right corner
    4. If the Github repository has not been added, click the link `Connect GitHub to import your private repos.` -> check `Only select repositories` -> select `NotionAI-Discord-Bot`
    5. Go back to step four, at this point the `Github URL` can choose the `NotionAI-Discord-Bot` project -> click `Import from Github`.

### Project Execution
1. Environment variable setting
    1. After completing the previous step of `Import` in the Replit project management page, click `Secrets` in the lower left corner of `Tools`.
    2. After clicking `Got it` on the right, you can add environment variables, and you need to add:
        1. Discord Token:
            - key: `DISCORD_TOKEN`
            - value: `[obtained from step one above]`
        2. Notion Token:
            - key: `NOTION_TOKEN`
            - value: `[obtained from step one above]`
        3. Notion Space Id:
            - key: `NOTION_SPACE_ID`
            - value: `[obtained from step one above]`
2. Start running
    1. Click `Run` above
    2. After success, the right side of the screen will display `Hello World`, and copy the URL in the upper left of the screen, which will be used in the next step
    - Note: If there are no requests within an hour, the program will be interrupted, so the next step is required.
3. CronJob timing request
    1. Register/Login to [cron-job.org](https://cron-job.org/en/)
    2. Select `CREATE CRONJOB` in the upper right of the panel
    3. Enter `NotionAI-Discord-Bot` in the `Title` and enter the URL from the previous step
    4. Click every `5 minutes` below
    5. Click `CREATE`

## Explanation
| Command | Parameters + Explanation |
| --- | ---------- |
| `help_me_write` | prompt: The command for AI, context: The text to be edited, page_title(Optional): Title, rest_content(Optional): Other parts of the text |
| `continue_write` | context: Text, page_title(Optional): Title, rest_content(Optional): Other parts of the text |
| `help_me_edit` | prompt: The command for AI, context: The text to be edited, page_title(Optional): Title |
| `translate` | language: The language to be translated, context: The text to be translated |
| `change_tone` | context: The text to be converted, tone: The style of the text |
| `summarize` | context: The text to be summarized, page_title(Optional): Title |
| `improve_writing` | context: The text to be improved, page_title(Optional): Title |
| `fix_spelling_grammar` | context: The text to be corrected, page_title(Optional): Title |
| `explain_this` | context: The text to be explained, page_title(Optional): Title |
| `make_longer` | context: The text to be lengthened, page_title(Optional): Title |
| `make_shorter` | context: The text to be shortened, page_title(Optional): Title |
| `find_action_items` | context: The text to be edited, page_title(Optional): Title |
| `simplify_language` | context: The text to be edited, page_title(Optional): Title |
| `blog_post` | prompt: The command for AI |
| `brainstorm_ideas` | prompt: The command for AI |
| `outline` | prompt: The command for AI |
| `social_media_post` | prompt: The command for AI |
| `creative_story` | prompt: The command for AI |
| `poem` | prompt: The command for AI |
| `essay` | prompt: The command for AI |
| `meeting_agenda` | prompt: The command for AI |
| `press_release` | prompt: The command for AI |
| `job_description` | prompt: The command for AI |
| `sales_email` | prompt: The command for AI |
| `recruiting_email` | prompt: The command for AI |
| `pros_cons_list` | prompt: The command for AI |

## Related Projects
[NotionAI](https://github.com/Vaayne/NotionAI)

## License
[MIT](LICENSE)
