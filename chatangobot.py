import ch_fixed
from math import sqrt
from random import randint

rooms = [""]
username = ""
password = ""

def commands():
    command_list = ["help","joke","alexa"]
    return command_list

def list_commands():
    command_list = commands()
    reply = "Commands: "+', '.join(str(command) for command in command_list)
    return reply

class bot(ch_fixed.RoomManager):
  def onInit(self):
    self.setNameColor("FFFFFF")
    self.setFontColor("FFFFFF")
    self.setFontFace("Arial")
    self.setFontSize(11)
    print('Bot Initialised...')
 
  def onPMMessage(self, pm, user, response):
    self.safePrint('PM: ' + user.name + ': ' + response)
    c = 0
    words = response.split(" ")
    flag = 0
    reply = ""
    for word in words:
        c += 1
        if word.lower() == "help" and c ==1:
            reply = list_commands()
            flag = 1
        elif word.lower() == "joke" and c == 1 and flag != 1:
            index_value = randint(0,9)
            jokes = ["Doctor: 'I’m sorry but you suffer from a terminal illness and have only 10 to live.'\nPatient: 'What do you mean, 10? 10 what? Months? Weeks?!'\nDoctor: 'Nine.'",
                     "A man asks a farmer near a field, 'Sorry sir, would you mind if I crossed your field instead of going around it? You see, I have to catch the 4:23 train.'\nThe farmer says, 'Sure, go right ahead. And if my bull sees you, you’ll even catch the 4:11 one.'",
                     "'Anton, do you think I’m a bad mother?'\n'My name is Paul.'",
                     "'My dog used to chase people on a bike a lot.\nIt got so bad, finally I had to take his bike away.'",
                     "What is the difference between a snowman and a snowwoman?\n\nSnowballs.",
                     "Mother: 'How was school today, Patrick?'\nPatrick: 'It was really great mum! Today we made explosives!'\nMother: 'Ooh, they do very fancy stuff with you these days. And what will you do at school tomorrow?'\nPatrick: 'What school?'",
                     "'Mom, where do tampons go?'\n'Where the babies come from, darling.'\n'In the stork?'",
                     "Man to his priest: 'Yesterday I sinned with an 18 year old girl.'\nThe priest: 'Squeeze 18 lemons and drink the juice all at once.'\nMan: 'And that frees me from my sin?'\nPriest: 'No, but it frees your face from that dirty grin.'",
                     "Doctor: 'I’ve found a great new drug that can help you with your sleeping problem.'\nPatient: 'Great, how often do I have to take it?'\nDoctor: 'Every two hours.'",
                     "My therapist told me 'write letters to people you hate and then burn them.' Did that, but now I don’t know what to do with the letter."]
            reply = jokes[index_value]
            flag = 1
        elif word.lower() == "joke" and flag != 1:
            reply = "Just send 'joke' for a joke :3 Type help for a list of commands"
            flag = 1
        elif word.lower() == "alexa" and c == 1 and flag != 1:
            reply = "ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Despacito\n\n─────⚪─────────────────────\n\n◄◄⠀▐▐ ⠀►►⠀⠀1:17 / 3:48 ⠀ ───○ ᴴᴰ ⚙ ❐ ⊏⊐"
            flag = 1
        elif word.lower() == "alexa" and flag != 1:
            reply = "I won't play despacito"
            flag = 1
        elif flag != 1:
            reply = "Type help for a list of commands"
    # output bot's message
    self.safePrint('Reply: ' + username + ': ' + reply)
    pm.message(user, reply) # response

bot.easy_start(rooms,username,password)
