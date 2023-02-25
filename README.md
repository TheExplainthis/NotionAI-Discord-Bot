# NotionAI Discord Bot

中文 | [English](README.en.md)

[![license](https://img.shields.io/pypi/l/ansicolortags.svg)](LICENSE) [![Release](https://img.shields.io/github/v/release/TheExplainthis/NotionAI-Discord-Bot)](https://github.com/TheExplainthis/NotionAI-Discord-Bot/releases/)


## 介紹
近幾個月筆記軟體 Notion 也開始推出了自己的 [NotionAI 服務](https://www.notion.so/product/ai)，功能有多強大呢？可以先看看下面的影片：

[![NotionAI Introduction](https://i.ytimg.com/vi/RDZ3mY10zY8/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAzPk5CktB6wPz8lgHguLi2UjfrOw)](https://youtu.be/RDZ3mY10zY8)


NotionAI 和 ChatGPT 相似，但提供多種不同的功能，例如翻譯、行程規劃、Email 撰寫、文案發想、頭腦風暴等。本文將教你如何在 Discord 上使用 NotionAI，增強團隊協作。

![NotionAI-Discord-Bot-Demo1](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/NotionAI-Discord-Bot-Demo1.png)
![NotionAI-Discord-Bot-Demo2](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/NotionAI-Discord-Bot-Demo2.png)



## 安裝步驟
### Token 取得
1. 取得 NotionAI Token：
    1. 登入網頁版 [Notion](https://www.notion.so/)
    2. 登入後按網頁 `右鍵` -> `檢查` -> `應用程式` -> Token 再 Cookies 裡，而 SpaceId 在 LocalStorage 裡，如下圖所示
    * ![Get-Notion-Token](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/Get-Notion-Token.png)
    * ![Get-Notion-SpaceId](https://github.com/TheExplainthis/NotionAI-Discord-Bot/blob/main/demo/Get-Notion-SpaceId.png)
2. 取得 Discord Token：
    1. 登入 [Discord Developer](https://discord.com/developers/applications)
    2. 創建機器人：
        1. 進入左方 `Applications`
        2. 點擊右上方 `New Application` 並輸入 Bot 的名稱 > 確認後進入新頁面。
        3. 點擊左方 `Bot`
        4. 點擊右方 `Add Bot`
        5. 下方 `MESSAGE CONTENT INTENT` 需打開 
        6. 按下 `Save Change`
        7. Token 在上方選擇 `View Token` 或已申請過則會是 `Reset Token` 的按鈕。
    3. 設定 OAuth2
        1. 點擊左欄 `OAuth2`
        2. 點擊左欄 `URL Generator`
        3. 右欄 `SCOPES` 選擇 `bot`、右欄下方 `BOT PERMISSIONS` 選擇 `Administrator`
        4. 複製最下方網址到瀏覽器中
        5. 選擇欲加入的伺服器
        6. 按下 `繼續` > `授權`

### 專案設置
1. Fork Github 專案：
    1. 註冊/登入 [GitHub](https://github.com/)
    2. 進入 [NotionAI-Discord-Bot](https://github.com/TheExplainthis/NotionAI-Discord-Bot)
    3. 點選 `Star` 支持開發者
    4. 點選 `Fork` 複製全部的程式碼到自己的倉庫
2. 部署（免費空間）：
    1. 進入 [replit](https://replit.com/)
    2. 點選 `Sign Up` 直接用 `Github` 帳號登入並授權 -> 按下 `Skip` 跳過初始化設定
    3. 進入後中間主頁的部分點選 `Create` -> 跳出框，點選右上角 `Import from Github`
    4. 若尚未加入 Github 倉庫，則點選連結 `Connect GitHub to import your private repos.` -> 勾選 `Only select repositories` -> 選擇 `NotionAI-Discord-Bot`
    5. 回到第四步，此時 `Github URL` 可以選擇 `NotionAI-Discord-Bot` 專案 -> 點擊 `Import from Github`。

### 專案執行
1. 環境變數設定
    1. 接續上一步 `Import` 完成後在 `Replit` 的專案管理頁面左下方 `Tools` 點擊 `Secrets`。
    2. 右方按下 `Got it` 後，即可新增環境變數，需新增：
        1. Discord Token:
            - key: `DISCORD_TOKEN`
            - value: `[由上方步驟一取得]`
        2. Notion Token:
            - key: `NOTION_TOKEN`
            - value: `[由上方步驟一取得]`
        3. Notion Space Id:
            - key: `NOTION_SPACE_ID`
            - value: `[由上方步驟一取得]`
2. 開始執行
    1. 點擊上方的 `Run`
    2. 成功後右邊畫面會顯示 `Hello World`，並將畫面中上方的**網址複製**下來，下一步驟會用到
    - 注意：若一小時內沒有任何請求，則程式會中斷，因此需要下步驟
3. CronJob 定時發送請求
    1. 註冊/登入 [cron-job.org](https://cron-job.org/en/)
    2. 進入後面板右上方選擇 `CREATE CRONJOB`
    3. `Title` 輸入 `NotionAI-Discord-Bot`，網址輸入上一步驟的網址
    4. 下方則每 `5 分鐘` 打一次
    5. 按下 `CREATE`


## 說明
| 指令 | 參數 + 說明 |
| --- | ---------- |
| `help_me_write` | prompt: 給 AI 的指令, context: 欲編輯的內文, page_title(Optional): 標題, rest_content(Optional): 其他部分的內文 |
| `continue_write` | context: 內文, page_title(Optional): 標題, rest_content(Optional): 其他部分的內文 |
| `help_me_edit` | prompt: 給 AI 的指令, context: 欲編輯的內文, page_title(Optional): 標題 |
| `translate` | language: 欲翻譯的語言, context: 欲翻譯的內文 |
| `change_tone` | context: 欲轉換風格的內文, tone: 內文風格 |
| `summarize` | context: 欲總結的內文, page_title(Optional): 標題 |
| `improve_writing` | context: 欲改善的內文, page_title(Optional): 標題 |
| `fix_spelling_grammar` | context: 欲修正的內文, page_title(Optional): 標題 |
| `explain_this` | context: 欲解釋的內文, page_title(Optional): 標題 |
| `make_longer` | context: 欲變長的內文, page_title(Optional): 標題 |
| `make_shorter` | context: 欲變短的內文, page_title(Optional): 標題 |
| `find_action_items` | context: 欲編輯的內文, page_title(Optional): 標題 |
| `simplify_language` | context: 欲編輯的內文, page_title(Optional): 標題 |
| `blog_post` | prompt: 給 AI 的指令 |
| `brainstorm_ideas` | prompt: 給 AI 的指令 |
| `outline` | prompt: 給 AI 的指令 |
| `social_media_post` | prompt: 給 AI 的指令 |
| `creative_story` | prompt: 給 AI 的指令 |
| `poem` | prompt: 給 AI 的指令 |
| `essay` | prompt: 給 AI 的指令 |
| `meeting_agenda` | prompt: 給 AI 的指令 |
| `press_release` | prompt: 給 AI 的指令 |
| `job_description` | prompt: 給 AI 的指令 |
| `sales_email` | prompt: 給 AI 的指令 |
| `recruiting_email` | prompt: 給 AI 的指令 |
| `pros_cons_list` | prompt: 給 AI 的指令 |

## 相關專案
[NotionAI](https://github.com/Vaayne/NotionAI)

## 授權
[MIT](LICENSE)