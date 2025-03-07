# Weather Forecast Telegram Bot

A Telegram bot that provides weather forecasts based on city input. The bot integrates with the [OpenWeather API](https://openweathermap.org/api) to fetch current weather data and forecasts, delivering easy-to-understand weather information directly in your Telegram chats.

## Features

- **City-based Forecast:** Retrieve weather forecasts by simply entering a city name.
- **Real-Time Weather Data:** Fetch up-to-date weather information using the OpenWeather API.
- **User-Friendly:** Simple commands and interactions designed for ease of use.
- **Extensible:** Easily customizable and extendable to add more features.

## Requirements

- Python 3.8+
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library
- [requests](https://pypi.org/project/requests/) library (or any HTTP client for API calls)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/LeGiT300/CloudFather.git
   cd weather-forecast-telegram-bot
   ```

2. **Create a Virtual Environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   If you don't have a `requirements.txt`, you can install the needed packages manually:

   ```bash
   pip install python-telegram-bot requests
   ```

## Configuration

Before running the bot, you need to set up your API keys:

1. **Telegram Bot API Token:**

   - Create a new bot using [BotFather](https://core.telegram.org/bots#6-botfather) on Telegram.
   - Obtain your bot token and set it as an environment variable or insert it into your configuration file.

2. **OpenWeather API Key:**

   - Sign up for an account at [OpenWeather](https://openweathermap.org/api) and obtain your API key.
   - Set your API key as an environment variable or insert it into your configuration file.

You can configure your keys either via environment variables:

```bash
export TELEGRAM_TOKEN='your-telegram-token'
export OPENWEATHER_API_KEY='your-openweather-api-key'
```

Or by editing the configuration section in your main Python script.

## Running the Bot

Run the bot with the following command:

```bash
python bot.py
```

Make sure that your environment variables are set, or the configuration in your script is correctly filled out.

## Usage

- **Start the Bot:** Open your Telegram app, search for your bot by its username, and click "Start".
- **Get Forecast:** Send a message with the name of the city for which you want to see the weather forecast.
- **Help:** The bot will reply with current weather details and forecast information.

## Troubleshooting

- **Invalid API Key:** Ensure your Telegram and OpenWeather API keys are correctly configured.
- **Connection Issues:** Check your internet connection and API endpoint status.
- **Dependencies:** Make sure all dependencies are installed using the provided requirements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

## Acknowledgements

- Thanks to the developers of [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for providing an excellent library.
- Weather data provided by [OpenWeather](https://openweathermap.org).

---

Happy coding, and stay weather-aware!
