# Catalog Notificator

This Python script monitors updates in the Roblox catalog and sends notifications to a specified Telegram channel when new items are listed It is designed to scrape specific item categories from Roblox, checking for any changes and informing users about new catalog items or limited-edition releases through Telegram alerts.

## Features

- Scrapes the Roblox catalog for specific item categories
- Sends Telegram notifications for newly added items
- Detects limited-edition items and sends an immediate alert
- Uses randomized time intervals between checks to avoid detection
- Sends alerts with item images and direct links to the Roblox catalog

## Prerequisites

- Python 3.x
- `requests` for making HTTP requests
- `beautifulsoup4` and `lxml` for parsing HTML content
- `telegram-send` for sending Telegram messages
- A valid Telegram bot token configured with `telegram-send`

## Installation

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Install required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure `telegram-send` by following the [telegram-send documentation](https://github.com/rahiel/telegram-send) to set up your bot and channel

## Usage

1. Modify the script as needed to customize the catalog URL or other parameters:
   - The `website` variable defines the URL for the Roblox catalog category to be monitored
   
2. Run the script:
    ```bash
    python catalog_notificator.py
    ```

3. The script will run in an infinite loop, periodically checking the catalog and sending notifications if updates are detected

## Customization

- **Item Categories**: You can change the `website` variable to monitor different categories by updating the URL parameters
- **Notification Frequency**: The `time.sleep()` and `random.randint()` functions control the timing between catalog checks Adjust these values to fit your needs

## Example Notification

When a new or limited item is detected, you'll receive a Telegram notification like the following:
```bash
❗ Лимитный предмет в каталоге обновлён ❗

[Item Name] [Link to the Roblox catalog item]
```
With an embedded image of the item

## Authors

This project is developed by Alexandr Kulakov
