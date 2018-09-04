import ch_fixed
from math import sqrt
from random import randint

rooms = [""]
username = ""
password = ""
botname = "UWUBot"
owner = ""
developer = ""

def emotion(emotion=None,full_list=False):
    if full_list:
        full_emotion_list = ["OwO","QwQ","UwU","( ͡° ͜ʖ ͡°)","(´ω｀*)","ღゝ◡╹)ノ♡",":3","c:","╭( ･ㅂ･)و","(´・ω・｀)","(*≧∀≦*)","(◯Δ◯∥)","¯\_(ツ)_/¯","╮(╯∀╰)╭","乁ʕ •̀ ۝ •́ ʔㄏ","(´・ω・｀)","(╬ಠ益ಠ)","(ಠ ∩ಠ)","(#｀皿´)","(ಥ﹏ಥ)","(⋟﹏⋞)"]
        if emotion in full_emotion_list:
            return True
        else:
            return False
    if emotion == "happy":
        emotion_list_happy = ["( ͡° ͜ʖ ͡°)","(´ω｀*)","(*≧∀≦*)",":3","c:"]
        return " "+emotion_list_happy[randint(0,len(emotion_list_happy)-1)]
    elif emotion == "confused":
        emotion_list_confused = ["OwO","QwQ","UwU","(◯Δ◯∥)","¯\_(ツ)_/¯","╮(╯∀╰)╭","乁ʕ •̀ ۝ •́ ʔㄏ"]
        return " "+emotion_list_confused[randint(0,len(emotion_list_confused)-1)]
    elif emotion == "neutral":
        emotion_list_neutral = ["UwU","( ͡° ͜ʖ ͡°)","╭( ･ㅂ･)و","(´・ω・｀)"]
        return " "+emotion_list_neutral[randint(0,len(emotion_list_neutral)-1)]
    elif emotion == "sad":
        emotion_list_sad = ["QwQ","UwU","(；人；)","(◯Δ◯∥)","(ಥ﹏ಥ)","(⋟﹏⋞)"] #,"(つ﹏<。)" doesn't print due to the arrow
        return " "+emotion_list_sad[randint(0,len(emotion_list_sad)-1)]
    elif emotion == "angry":
        emotion_list_angry = ["(」ﾟДﾟ」","(◯Δ◯∥)","(╬ಠ益ಠ)","(ಠ ∩ಠ)","(#｀皿´)"]
        return " "+emotion_list_angry[randint(0,len(emotion_list_angry)-1)]
    else:
        emotion_list = ["OwO","QwQ","UwU","( ͡° ͜ʖ ͡°)","(´ω｀*)","ღゝ◡╹)ノ♡",":3","c:","╭( ･ㅂ･)و","(´・ω・｀)"]
        return " "+emotion_list[randint(0,len(emotion_list)-1)]

def commands():
    command_list = ["help","joke","alexa","hey","pm","featurerequest","hug","info"]
    return command_list

class recipient_class:
    def __init__(self, name):
        self.name = name

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
        elif word.lower() == "pm" and c == 1 and flag != 1:
            try:
                recipient = recipient_class(words[1])
                message_to_send1 = ' '.join(str(w) for w in words[2:])
                message_to_send2 = "PM from '"+user.name+"': "+message_to_send1
                self.safePrint('Sent to '+recipient.name+' from '+user.name+': ' + message_to_send1)
                pm.message(recipient, message_to_send2) # response
                reply = "Sent!"+emotion("happy")
                flag = 1
            except:
                reply = "Empty user or empty message!" #empty values
        elif word.lower() == word.lower() == "pm" and flag != 1:
            reply = "Just send 'pm' followed by a 'username' and a 'message', eg. 'pm animelov3r69 hey dude'. Type help for a list of commands"+emotion("neutral")
            flag = 1
        elif word.lower() == "hug" and c == 1 and flag != 1:
            try:
                recipient = recipient_class(words[1])
                hug_to_send = "'"+user.name+"' hugged you &lt;3" #< character won't work for some reason without alt code
                self.safePrint('Hug sent to '+recipient.name+' from '+user.name)
                print(hug_to_send)
                pm.message(recipient, hug_to_send) # response
                reply = "Hug sent!"+emotion("happy")
                flag = 1
            except:
                reply = "*hugs you &lt;3*" #empty values
        elif (word.lower() == "featurereq" or word.lower() == "featurerequest" or word.lower() == "fr") and c == 1 and flag != 1:
            try:
                recipient = recipient_class(developer)
                message_to_send1 = ' '.join(str(w) for w in words[1:])
                message_to_send2 = "Feature Request from '"+user.name+"' for '"+botname+"': "+message_to_send1
                self.safePrint('Sent to DEV '+recipient.name+' from '+user.name+': ' + message_to_send1)
                pm.message(recipient, message_to_send2) # response
                reply = "Feature Request Sent!"+emotion("excited")
                flag = 1
            except:
                reply = "Error!" #empty values
        elif (word.lower() == "featurereq" or word.lower() == "featurerequest" or word.lower() == "fr") and flag != 1:
            reply = "Just send 'fr' followed by a 'feature request', eg. 'fr add this command'. Type help for a list of commands"+emotion("neutral")
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
            reply = "Just send 'joke' for a joke. Type help for a list of commands"+emotion("excited")
            flag = 1
        elif word.lower() == "alexa" and c == 1 and flag != 1:
            num1 = randint(0,3)
            if num1 == 3:
                num2 = randint(0,4)
                if num2 == 4:
                    num3 = randint(0,8)
                else:
                    num3 = randint(0,9)
            else:
                num2 = randint(0,5)
                num3 = randint(0,9)
            time_sec = (num1 * 60)+(num2 * 10)+(num3 * 1)
            progress_decimal = time_sec/228
            padding_left = round(27*progress_decimal)
            padding_right = 27 - padding_left
            string = "─"*padding_left+"⚪"+"─"*padding_right
            test = "─────⚪─────────────────────"
            reply = "ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Despacito\n\n"+string+"\n\n◄◄⠀▐▐ ⠀►►⠀⠀"+str(num1)+":"+str(num2)+str(num3)+" / 3:48 ⠀ ───○ ᴴᴰ ⚙ ❐ ⊏⊐"
            flag = 1
        elif word.lower() == "alexa" and flag != 1:
            reply = "I won't play despacito"+emotion("angry")
            flag = 1
        elif (word.lower() == "hey" or word.lower() == "hai" or word.lower() == "hi") and c == 1 and flag != 1:
            reply = "Hey there, "+user.name+"!"+emotion("happy")
            flag = 1
        elif (word.lower() == "hey" or word.lower() == "hai" or word.lower() == "hi") and flag != 1:
            reply = "Hey "+user.name+emotion()
            flag = 1
        elif (word.lower() == "info" or word.lower() == "uwu") and flag != 1:
            reply = "Hey "+user.name+". I am "+botname+"!\n\nI am owned and operated by "+owner+" and developed by "+developer+"!"+emotion("excited")
            flag = 1
        elif flag != 1:
            if response != "" and c == 1:
                boolean = emotion(response,True) #checks if the emoji is a registered one
                if boolean:
                    reply = response #if so, it responds with it
                else:
                    reply = "I don't understand '"+response+"'.\n\nTry again or type help for a list of commands."+emotion("sad")
            elif response != "":
                reply = "I don't understand '"+response+"'.\n\nTry again or type help for a list of commands."+emotion("sad")
            else:
                reply = "Stop trying to confuse me with empty messages"+emotion("angry")
    # output bot's message
    self.safePrint('Reply: ' + reply)
    pm.message(user, reply) # response

bot.easy_start(rooms,username,password)
