import os, sys
import telebot
import requests
import csv
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)
moviekey = os.getenv("OMDB_TOKEN")
botRunning = True

def csvExport(data):
    filename = "movie.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)

def getmovie(name):
    movieName=name.strip("/movie ")
    url = f"http://www.omdbapi.com/?apikey={moviekey}&t={movieName}"
    urlData = requests.get(url)
    print(f"Requested URL: {url}")

    if urlData.status_code == 200:
        try:
            fields = urlData.json()
            print(f"Response received: {fields}")
            if fields.get("Response") == "True":
                title, year, rating, photo = fields["Title"], fields["Year"], fields["imdbRating"], fields["Poster"]
                output = f'\n[Title]({photo}) : {title}\nYear : {year}\nimDbRating : {rating}'
                return output, fields
            else:
                print("Movie not found.")
                return "Movie not found. Please try again.", None
        except ValueError:
            print("Error parsing the movie data.")
            return "Error parsing the movie data.", None
    else:
        print(f"Failed to retrieve movie data. Status code: {urlData.status_code}")
        return "Failed to retrieve movie data. Please try again later.", None


@bot.message_handler(commands=['start', 'hello'])
def greet(message):
    global botRunning
    botRunning = True
    print("Bot started.")
    bot.reply_to(
        message, 'Hello there! I am a bot that will show movie information for you and export it in a CSV file.\n\n')
    
@bot.message_handler(commands=['stop', 'bye'])
def goodbye(message):
    global botRunning
    botRunning = False
    bot.reply_to(message, 'Bye!\nHave a good time')
    bot.stop_polling()
    sys.exit(0)

@bot.message_handler(func=lambda message: botRunning, commands=['help'])
def helpProvider(message):
    print("Help command received.")
    bot.reply_to(message, '1. You can use "/movie MOVIE_NAME" command to get the details of a particular movie. For example: "/movie The Shawshank Redemption"\n\n2. You can use "/export" command to export all the movie data in CSV format.\n\n3. You can use "/stop" or the command "/bye" to stop the bot.')

@bot.message_handler(func=lambda message: botRunning, commands=['movie'])
def getMovie(message):
    print(f"Movie command received: {message.text}")
    bot.reply_to(message, 'Getting movie info...')
    out, fields = getmovie(message.text)
    if fields:
        csvExport([fields["Title"], fields["Year"], fields["imdbRating"]])
        bot.reply_to(message, out, parse_mode="Markdown")
    else:
        bot.reply_to(message, out)

@bot.message_handler(func=lambda message: botRunning, commands=['export'])
def getList(message):
    filename = "movie.csv"
    if os.path.exists(filename):
        print("Export command received.")
        bot.reply_to(message, 'Generating file...')
        with open(filename, 'rb') as file:
            bot.send_document(message.chat.id, file)
    else:
        bot.reply_to(message, 'No movie data available to export.')
        print("No data available to export.")

@bot.message_handler(func=lambda message: botRunning)
def default(message):
    print(f"Unknown command received: {message.text}")
    bot.reply_to(message, 'I did not understand '+'\N{confused face}')

print("Bot is now polling for messages.")
bot.infinity_polling()
