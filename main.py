from nextcord.ext import commands
from threading import Thread
import requests
import nextcord
from functools import partial
from flask import Flask,render_template
client = commands.Bot(intents=nextcord.Intents.all())
app = Flask(__name__,template_folder="")
@app.route("/")
def home():
  user = client.get_user(586369284272554032)
  img_data = requests.get(user.avatar.url).content
  with open('static/assets/img/obedient.png', 'wb') as handler:
    handler.write(img_data)
  return render_template("index.html",user=user)
partial_run = partial(app.run, host="0.0.0.0", port=80, debug=True, use_reloader=False)
t = Thread(target=partial_run)
t.start()
client.run('OTk2ODczOTg1MjM5Mjg5OTMy.GGpzvl.9lLpuSkthm1MxkwQnhXWr-Z7zJ3TFa61tU_eXc')