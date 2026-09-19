# BeastX Save Restricted Bot

A customized and reorganized Telegram bot for saving/retrieving Telegram content through post links.

---

## BeastX

This distribution has been reorganized into a simpler structure and branded as **BeastX**.

### Official Links

- Update Channel: **@Beastx_Bots**
- Support: **@Beastx_Support**
- Developer / Maintainer of this customized build: **@Godmrunal**

## Credits & Attribution

This project is based on existing open-source work. Upstream attribution is retained here for the previous modification/source.

- **Previous modification/source attribution:** Tech VJ / VJBots
- **BeastX customization, reorganization and branding:** [@Godmrunal](https://github.com/Godmrunal)

The BeastX customization does not claim ownership of the upstream code.

---

## Project Structure

```text
BeastX/
├── main.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── Procfile
├── Dockerfile
├── runtime.txt
├── run cmd.txt
└── README.md
```

The previous `beastx/` and `database/` packages were consolidated into **`main.py`**.

**Telegram session files, virtual environments, `.env` files and other secrets are intentionally excluded from this repository.**

---

## Environment Variables

Copy `.env.example` as a reference and configure the variables in your hosting provider's environment-variable/settings panel.

| Variable | Required | Description |
|---|---|---|
| `BOT_TOKEN` | Yes | Bot token from BotFather |
| `API_ID` | Yes | Telegram API ID |
| `API_HASH` | Yes | Telegram API hash |
| `ADMINS` | Yes | Telegram user ID allowed to use `/broadcast` |
| `DB_URI` | Yes | MongoDB connection URI |
| `DB_NAME` | No | MongoDB database name; default: `beastxsavecontentbot` |
| `LOGIN_SYSTEM` | No | `True` enables `/login`; default: `True` |
| `STRING_SESSION` | Conditional | Required when `LOGIN_SYSTEM=False` |
| `CHANNEL_ID` | No | Optional channel ID used by the project configuration |
| `WAITING_TIME` | No | Delay between processed messages; default: `10` |
| `ERROR_MESSAGE` | No | Enable/disable error messages; default: `True` |

### Security

**Never commit real credentials to GitHub.** This includes:

- Bot tokens
- Telegram API ID/API hash when treated as private deployment configuration
- MongoDB usernames/passwords/URIs
- Telegram session files
- String sessions
- `.env` files

If a credential has previously been committed to a public repository, rotate/revoke it before publishing the repository.

---

## Installation

```bash
python -m venv venv
```

Windows CMD:

```bat
venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Linux/macOS:

```bash
source venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Configure the required environment variables, then run:

```bash
python main.py
```

---

## Commands

- `/start` — Start the bot
- `/help` — Show usage instructions
- `/login` — Create/store a Telegram session
- `/logout` — Remove the stored session
- `/cancel` — Cancel an ongoing task
- `/broadcast` — Broadcast a replied message (admin only)

---

## Usage

### Public chats

Send the Telegram post link.

### Private chats

Send the invite link first if the configured account is not already a member, then send the post link.

### Bot chats

Use the `/b/` format:

```text
https://t.me/b/botusername/4321
```

### Multiple posts

Use a range:

```text
https://t.me/xxxx/1001-1010
https://t.me/c/xxxx/101-120
```

---

## 🚀 Free Deployment on Koyeb

You can deploy BeastX for free on **Koyeb** using your GitHub repository and environment variables.

### YouTube Deployment Tutorial

📺 **Deploy BeastX on Koyeb for Free — Full Setup Tutorial**

> 🎥 YouTube tutorial link will be added here.

The tutorial will cover:

- Uploading the project to GitHub
- Connecting GitHub to Koyeb
- Creating the Koyeb service
- Adding environment variables
- Deploying the bot
- Checking the logs
- Testing the bot after deployment

---

## Deployment

### Procfile-based hosts

The included `Procfile` starts the bot with:

```bash
python3 main.py
```

### Web health endpoint

The included Flask app exposes `/` and returns a simple health message. To run it separately:

```bash
gunicorn app:app
```

### Docker

A Dockerfile is included for container-based deployment. Configure environment variables in the deployment platform rather than putting secrets in the image or repository.

---

## License / Upstream Notice

Check the upstream project's license and terms before redistributing or modifying this project. This repository keeps the previous source attribution listed above.

## Handler Notes

The command handlers are explicitly registered on the actual `Bot` instance because the project was consolidated into one file. The catch-all text handler excludes command messages so `/start`, `/help`, `/cancel`, `/login`, `/logout`, and `/broadcast` reach their dedicated handlers.
