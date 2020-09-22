define persistent.music_dokidoki = False
default seen_swim = False
default seen_catch = False
default seen_drink = False
default seen_read = False
default seen_dig = False
default seen_manga = False
default seen_picnic = False
default seen_grab = False
default pool = False
default beach_night = False
default persistent.music_firestorm = False
default persistent.music_mallattack = False
default persistent.music_confession = False
default persistent.music_poems = False
default persistent.music_custom1 = False
default persistent.music_custom2 = False
default persistent.music_custom3 = False
default persistent.currentpos = 0
default skippos = 0
default persistent.flower = False
default persistent.hair_color = "Pink"
default persistent.first_dlc = True
default persistent.using_space_dlc = False
default persistent.using_catears = False
default current_natsukifact = 0
default persistent.reloaded = False
default persistent.music1_name = ""
default persistent.music2_name = ""
default persistent.music3_name = ""
default persistent.seen_actionwarning = False
default persistent.current_music = "normal"

image blonde = "mod_assets/JustNatsuki/blonde.png"
image lime = "mod_assets/JustNatsuki/green.png"
image silver = "mod_assets/JustNatsuki/silver.png"
image red = "mod_assets/JustNatsuki/red.png"
image skyblue = "mod_assets/JustNatsuki/skyblue.png"
image ginger = "mod_assets/JustNatsuki/ginger.png"
image catears = "mod_assets/JustNatsuki/originalears.png"

label quitmenu:
    $ allow_dialogue = False
    $ HKBHideButtons()
    n "See you soon [player]!"
    $ renpy.quit()

label talkmenu:
    if persistent.date == "beach":
        jump beachtalkmenu
    elif persistent.date == "beach_night":
        jump beachnighttalkmenu
    elif persistent.date == "mall":
        jump malltalkmenu
    elif persistent.date == "park":
        jump parktalkmenu
    elif persistent.date == "club":
        jump clubtalkmenu
    elif persistent.date == "pool":
        jump pooltalkmenu
    elif persistent.date == "":
        jump normaltalkmenu_select
    else:
        "Congratulations! You broke the game!"
        $ renpy.quit()

label normaltalkmenu_select:
    $ time_alone -= 2
    $ allow_dialogue = False
    menu:
        "Ask a question":
            show screen talking_new
            jump normaltalkmenu
        "Type a question":
            jump normalchatmenu
        "{b}Anniversary Event{/b}":
            if persistent.seen_3yearevent:
                call screen confirm("Are you sure you want to replay the event?", yes_action=Return, no_action=Jump("ch30_loop"))
            call screen confirm("Initiating this event means you must watch it through before returning to normal gameplay.\nIf you quit at any point you will be returned to the start of the event.\nAre you sure you want to play it now?", yes_action=Jump("ch30_3yearevent"), no_action=Jump("ch30_loop"))
            jump ch30_loop
        "Compliments..." if persistent.natsuki_love:
            hide screen talking_new
            hide screen talking_new2
            jump ch30_loveyou
        "Can you change...":
            jump change
        "Goodbye":
            menu:
                "I have to go, Natsuki.":
                    n jsb "Aww, that's too bad [player]."
                    n "See you soon, though."
                    if persistent.natsuki_love:
                        n jha "I love you!"
                "I have to go to a class, Natsuki.":
                    if time_of_day = "Night":
                        n jnb "A night time class?"
                        n jha "Cool!"
                        n "Study hard, [player]!"
                    elif time_of_day = "Day":
                        n jsb "Aww, I'll miss you [player]."
                        n jnb "Study hard though, then you have time to spend with me!"
                "I'm going to sleep, Natsuki.":
                    if time_of_day == "Night":
                        n jha "Alright, rest well!"
                    elif time_of_day == "Day":
                        n jnb "In the day?"
                        n "Isn't that more of a nap?"
                        n "Well suit yourself, I guess."
                "Nevermind.":
                    n jnb "Oh, okay!"
                    jump ch30_loop
            if persistent.save_music_place:
                $ persistent.currentpos = get_pos()
            else:
                $ persistent.currentpos = 0
            $ renpy.quit()
        "Nevermind":
            jump ch30_loop

label funfact_start:
    $ current_natsukifact = renpy.random.randint(1, 5)
    call expression "funfact_" + str(current_natsukifact)
    jump ch30_loop

label funfact_1:
    n jnb "When the mod started development there were many iterations of the main Natsuki art."
    n "Originally it didn't exist, than the normal DDLC sprite was used. In Update 1.4 it was possible to choose if you wanted to use a temporary sprite or the game sprite."
    n "The temporary art, which was just a fanart of Natsuki, became the game's Natsuki art until it was replaced in 2.0. After not too long it was repalced with what you see now!"
    return

label funfact_2:
    n jnb "Older players may know of this one."
    n "In update 1.9 a story campaign was added to the mod."
    n "It was a two-part story that was concluded in a pre-release of 2.0"
    n "It has been since removed."
    return

label funfact_3:
    n jnb "ALL previous Just Natsuki updates can be played."
    n "I do NOT recommend this though as if your save file has data added in a newer update, you may experience a crash."
    return

label funfact_4:
    n jnb "Just Natsuki: Virus was a cancelled DLC that was supposed to have a simmilar campaign to the original Just Natsuki campaign."
    n "It was canceled as the Dev wanted all DLCs to be an expansion to the mod's core features and not a whole new story."
    return

label funfact_5:
    n "Just Natsuki has been translated into Spanish!"
    n "This version of the game is still stuck on Update 2.3, as the translator did not continue developing it."
    return

label normalchatmenu:
    $ chatinput = renpy.input('Say something! (Type what you want to talk about lowercase. Dont make a proper sentence!)',length=30).strip(' \t\n\r')
    $ chat = chatinput.strip()
    if chatinput.strip() == "undertale":
        n jha "I've heard of that!"
        n "It's compared to this game a lot!"
        n "Maybe too much..."
        n "My favorite character is either Undyne or Alphys!"
        n "Obvious I know..."
    elif chatinput.strip() == "love":
        if persistent.natsuki_love:
            n jha "I love you too!"
        else:
            n jac "W-what!"
            n "D-don't tease me like that!!"
            jump ch30_loop
    elif chatinput.strip() == "school":
        n jaa "School sucks!"
        n "You just sit there for like 6 or so hours basically doing nothing!"
        n jnb "I've heard that schools in Finland are way better."
        n "Too bad I can't go to one..."
        jump ch30_loop
    elif chatinput.strip() == persistent.playername:
        n jnb "You want to talk about yourself?"
        n "Um..."
        n "Do you want to change your name?"
        menu:
            "Yes":
                n "Alright."
                $ newname = renpy.input('Please enter your new name! (Type nevermind to cancel)',length=30).strip(' \t\n\r')
                $ player = newname.strip()
                if newname.strip() == "Natsuki":
                    n "Really?"
                    n "Okay."
                elif newname.strip() == "nevermind":
                    n "Okay then..."
                    jump ch30_loop
                else:
                    n "Alright!"
                    n "From now I'll call you [player]!"
                $ persistent.playername = newname.strip()
            "No":
                n "Alright..."
    elif chatinput.strip() == "cupcake" or chatinput.strip() == "cupcakes":
        n jha "I love cupcakes man!"
        n "I really like my own though."
        n "I was going to bring this up at some point but have you ever noticed your own cooking tastes way better?"
        n "Maybe it's the attention and care you put it?"
        n "Almost like it your own child?"
        n "For instance..."
        n "I love my own cupcakes!"
        n "And so did the club!"
        n "And I hope if I ever actually could somehow enter your world I could bake some for you and your friends!"
        n "Ehehe!"
    elif chatinput.strip() == "natsuki":
        n jnb "You want to talk about me?"
        n "What's there to say?"
        n jha "I'm Natsuki!"
        n "Did that suffice?"
        n "Actually..."
        n "Don't answer that..."
    elif chatinput.strip() == "yuri":
        n jnb "You want to talk about Yuri eh?"
        n "What's there to say?"
        n jsb "Other then I miss her."
    elif chatinput.strip() == "club":
        n jnb "You want to talk about the club?"
        n "Well it WAS the only place I feel safe!"
        n "No big deal right?"
    elif chatinput.strip() == "baking":
        n jnb "If I ever did enter your world It would probably never be in a real human body."
        n "Just a robot."
        n "What if I became a cooking robot?"
        n jha "I could bake cupcakes in reality!"
        n "That would be awesome!"
    elif chatinput.strip() == "weather":
        n jnb "You wanna talk about weather?"
        n "Well I don't really get any anymore."
        n "But I guess being stuck in space does that..."
    elif chatinput.strip() == "sayori":
        n jsb "I miss her..."
    elif chatinput.strip() == "monika":
        n jaa "Fuck Monika..."
    elif chatinput.strip() == "halloween":
        n jha "You're excited too huh?"
    else:
        n jnb "What?"
    jump ch30_loop

label normaltalkmenu:
    $ allow_dialogue = False
    $ allow_boop = False
    menu:
        n "What's up?"
        "What's your favorite anime or manga?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_favanime
        "How are you today?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_mood
        "Whats your favorite kind of weather?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_weather
        "Do you like memes?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_memes
        "Do you miss Sayori?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_sayori
        "Next Page...":
            jump normaltalkmenu2
        "Nevermind.":
            hide screen talking_new
            hide screen talking_new2
            n "Okay..."
            jump ch30_loop

label normaltalkmenu2:
    $ allow_dialogue = False
    $ allow_boop = False
    menu:
        n "You sure have a lot to say..."
        "What do you think about Monika?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_monika
        "Why did you delete Yuri?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_yurikill
        "Why do you like to cook?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_cooking
        "How did you become self aware?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_aware
        "Next Page...":
            jump normaltalkmenu3
        "Last Page...":
            jump normaltalkmenu
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            n "Okay..."
            jump ch30_loop

label normaltalkmenu3:
    $ allow_dialogue = False
    $ allow_boop = False
    menu:
        "These romance games are so unrealistic!":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_smoshparody
        "Did you ever get bullied?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_bully
        "I bet you can't guess what day it is in my reality!":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_dateguess
        "Next Page...":
            jump normaltalkmenu4
        "Last Page...":
            jump normaltalkmenu2
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            n "Okay..."
            jump ch30_loop
label normaltalkmenu4:
    $ allow_boop = False
    menu:
        "What do you think about [player]?" if not persistent.natsuki_love:
            hide screen talking_new
            hide screen talking_new2
            jump ch30_mc
        "What is the coolest thing you can do?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_shutdown
        "How are you talking to me?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_talk
        "I am a carpet.":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_carpet
        "Next Page...":
            jump normaltalkmenu5
        "Last Page...":
            jump normaltalkmenu3
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_loop

label normaltalkmenu5:
    $ allow_boop = False
    menu:
        "What do you remember from before Monika messed with you?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_remember
        "How powerful are you?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_power
        "What is the Third Eye?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_3eye
        "How does the poem minigame work?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_poemgame
        "Next Page...":
            jump normaltalkmenu6
        "Last Page...":
            jump normaltalkmenu4
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_loop

label normaltalkmenu6:
    menu:
        "The purple fire?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_fire
        "How do you access the internet?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_internet
        "Can I feed you?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_feed
        "What is your political stance?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_politics
        "Next Page...":
            jump normaltalkmenu7
        "Last Page...":
            jump normaltalkmenu4
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_loop

label normaltalkmenu7:
    if persistent.anniversary:
        menu:
            "I'm going to wrap the presents!" if persistent.christmas_time == "Eve":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_christmasevent1
            "Ready to open gifts?" if persistent.christmas_time == "Day":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_christmasevent2
            "Were you and Yuri really friends?":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_yuri
            "What even is that fire?":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_fire2
            "Can I tell you my birthday?":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_bdayset
            "Next Page...":
                jump normaltalkmenu8
            "Last Page...":
                jump normaltalkmenu6
            "Nevermind":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_loop
    else:
        menu:
            "What is your political stance?":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_politics
            "Are you excited for 2019?" if persistent.seen_newyear:
                hide screen talking_new
                hide screen talking_new2
                jump ch30_2019
            "Were you and Yuri really friends?":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_yuri
            "What even is that fire?":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_fire2
            "Can I tell you my birthday?":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_bdayset
            "Next Page...":
                jump normaltalkmenu8
            "Last Page...":
                jump normaltalkmenu6
            "Nevermind":
                hide screen talking_new
                hide screen talking_new2
                jump ch30_loop

label normaltalkmenu8:
    menu:
        "What do you know about Monika's plan?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_plan
        "Ready to blow out the candles?" if persistent.two_years:
            hide screen talking_new
            hide screen talking_new2
            jump ch30_candle
        "What do you make of the \"trap\" meme?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_trap
        "Are you attracted to men or women?":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_attraction
        "Next Page...":
            jump normaltalkmenu8
        "Last Page...":
            jump normaltalkmenu7
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_loop

label datemenu:
    $ allow_dialogue = False
    $ allow_boop = False
    menu:
        n "Where should we go?"
        "The Beach":
            #Code for loading the beach from the room.
            if persistent.date == "":
                n jha "Really!"
                n "Yay~!"
                if current_time >= 6 and current_time < 19:
                    if persistent.natsuki_romance >= 100 and persistent.wearing == "Bikini":
                        n jnb "Well, I won't have to change at least. So that's a plus."
                    elif persistent.natsuki_romance < 100 and persistent.wearing == "Beach":
                        n jnb "Well, I won't have to change at least. So that's a plus."
                    play sound closet_open
                    scene black with wipeleft_scene
                    pause 1.0
                    play sound closet_close
                    $ HKBHideButtons()
                    $ persistent.date = "beach"
                    hide dark onlayer front
                    jump chbeachdate_main
                else:
                    n jnb "At night?"
                    n "Alright."
                    n "We could go for a walk or just sit by the ocean."
                    n "I'm not changing though..."
                    $ HKBHideButtons()
                    $ persistent.date = "beach_night"
                    hide dark onlayer front
                    jump chbeachdate_night_main
            #Code for the leaving other places for the beach, since the room code causes a dialogue and image mismatch.
            elif persistent.date != "":
                if current_time >= 6 and current_time < 19:
                    n "Sure, beach sounds fun, I'll get changed!"
                    $ HKBHideButtons()
                    $ persistent.date = "beach"
                    hide dark onlayer front
                    jump chbeachdate_main
                else:
                    n "Sure, beach sounds fun, I'll get changed!"
                    $ HKBHideButtons()
                    $ persistent.date = "beach_night"
                    hide dark onlayer front
                    jump chbeachdate_night_main
            else:
                jump chbeach_loop
        "The Pool":
            if not pool:
                n jha "Oh! Yeah sure!"
                n "Let's go!"
                $ HKBHideButtons()
                $ persistent.date = "pool"
                hide dark onlayer front
                jump chpool_main
            else:
                jump chpool_loop
        "The Mall":
            if not mall:
                $ beach = False
                $ beach_night = False
                $ mall = True
                n "I love the mall!"
                $ HKBHideButtons()
                $ persistent.date = "mall"
                $ allow_dialogue
                hide dark onlayer front
                jump chmall_main
            else:
                jump chmall_loop
        "A Park":
            if not park:
                $ persistent.date = "park"
                n "Alright then..."
                $ HKBHideButtons()
                $ allow_dialogue
                hide dark onlayer front
                jump chpark_main
            else:
                return
        "The Literature Club":
            if not club:
                $ persistent.date = "club"
                n "..."
                n "Okay I guess."
                $ HKBHideButtons()
                $ allow_dialogue
                hide dark onlayer front
                jump chclub_main
            elif club:
                n "Were already here."
                jump chclub_loop
            else:
                return
        "Return to the room":
            if beach:
                $ persistent.date = ""
                n "Heading back then?"
                n "Alright!"
                if current_time >= 5 and current_time < 18:
                    play sound closet_open
                    scene black with wipeleft_scene
                    pause 1.0
                    play sound closet_close
                $ style.say_window = style.window
                $ style.namebox = style.namebox
                $ persistent.autoload = "ch30_autoload"
                hide nb1
                $ exiting_fight = True
                jump ch30_autoload
            if beach_night:
                $ persistent.date = ""
                n "Heading back then?"
                n "Alright!"
                $ style.say_window = style.window
                $ style.namebox = style.namebox
                $ persistent.autoload = "ch30_autoload"
                hide natsuki
                $ exiting_fight = True
                jump ch30_autoload
            elif mall:
                $ persistent.date = ""
                n "Heading back then?"
                n "Alright!"
                $ style.say_window = style.window
                $ style.namebox = style.namebox
                $ persistent.autoload = "ch30_autoload"
                $ exiting_fight = True
                jump ch30_autoload
            elif park:
                $ persistent.date = ""
                n "Heading back then?"
                n "Alright!"
                $ style.say_window = style.window
                $ style.namebox = style.namebox
                $ persistent.autoload = "ch30_autoload"
                $ exiting_fight = True
                hide natsuki
                jump ch30_autoload
            elif club:
                $ persistent.date = ""
                n "Heading back then?"
                n "Alright!"
                $ style.say_window = style.window
                $ style.namebox = style.namebox
                $ persistent.autoload = "ch30_autoload"
                $ exiting_fight = True
                hide natsuki
                jump ch30_autoload
            elif pool:
                $ persistent.date = ""
                n "Heading back then?"
                n "Alright!"
                $ style.say_window = style.window
                $ style.namebox = style.namebox
                $ persistent.autoload = "ch30_autoload"
                $ exiting_fight = True
                hide nb1
                jump ch30_autoload
            else:
                call screen dialog(message="You're already here, idiot.", ok_action=Return)
                jump ch30_loop
        "Nevermind":
            if persistent.date == "beach":
                jump chbeach_loop
            elif persistent.date == "beach_night":
                jump chbeach_night_loop
            elif persistent.date == "mall":
                jump chmall_loop
            elif persistent.date == "park":
                jump chpark_loop
            elif persistent.date == "club":
                jump chclub_loop
            elif persistent.date == "pool":
                jump chpool_loop
            else:
                jump ch30_loop

label malltalkmenu:
    $ allow_dialogue = False
    menu:
        n "What's up?"
        "Do you ever buy video games here?":
            jump chmall_videogames
        "Should we head over to the clothing store?":
            jump chmall_clothingstore
        "What bakeries do you recommend?":
            jump chmall_bakery
        "What would Sayori would have wanted to do if she was here?":
            jump chmall_sayori
        "Next Page...":
            jump malltalkmenu2
        "Nevermind.":
            jump chmall_loop

label malltalkmenu2:
    $ allow_dialogue = False
    menu:
        n "What's up?"
        "What's this mall called?":
            jump chmall_name
        "Wasn't this mall used in Rainclouds?":
            jump chmall_rainclouds
        "Last Page...":
            jump malltalkmenu
        "Nevermind.":
            jump chmall_loop

label beachtalkmenu:
    $ allow_dialogue = False
    menu:
        n "Hm?"
        "What should we do here?":
            jump chbeach_action
        "What's your favorite thing to do at the beach?":
            jump beachfavthings
        "Where did you get the swimsuit anyway?":
            jump swimsuit
        "Isn't the beach too hot?":
            jump sunburn
        "Next Page...":
            jump beachtalkmenu2
        "Nevermind.":
            n "Okay!"
            jump chbeach_loop

label beachnighttalkmenu:
    $ allow_dialogue = False
    menu:
        n "Hm?"
        "What should we do here?":
            jump chbeach_night_action
        "This reminds me of Anime beach episodes...":
            jump chbeach_night_episodes
        "You ever been to the beach at night?":
            jump chbeach_night_visit
        "Nevermind.":
            n "Okay!"
            jump chbeach_night_loop

label beachtalkmenu2:
    $ allow_dialogue = False
    menu:
        "Why did your hair change?":
            jump chbeach_hair
        "What if the others were here?":
            jump chbeach_others
        "This reminds me of Anime beach episodes...":
            jump chbeach_episodes
        "You look... nice...":
            jump chbeach_compliment
        "Next Page...":
            jump beachtalkmenu3
        "Last Page...":
            jump beachtalkmenu
        "Nevermind":
            jump chbeach_loop 

label beachtalkmenu3:
    $ allow_dialogue = False
    menu:
        "How come it's always day here even when it's nighttime?":
            jump chbeach_time
        "Last Page...":
            jump beachtalkmenu
        "Nevermind":
            jump chbeach_loop 

label parktalkmenu:
    $ allow_dialogue = False
    menu:
        n "Hm?"
        "What park is this?":
            jump chpark_location
        "What's that building in the back?":
            jump chpark_bg
        "What do you like to do here?":
            jump chpark_fun
        "Nevermind.":
            jump chpark_loop

label clubtalkmenu:
    $ allow_dialogue = False
    menu:
        "Is this giving you flash backs?":
            jump chclub_flashback
        "Did you like writing poems?":
            jump chclub_poem
        "Nevermind.":
            jump chclub_loop

label pooltalkmenu:
    $ allow_dialogue = False
    menu:
        "Put on some sunscreen!":
            jump chpool_sunscreen
        "You look cute Natsuki!":
            jump chpool_cute
        "Do your prefer the beach or the pool?":
            jump chpool_preferance
        "Nevermind...":
            jump chpool_loop

label actions:
    $ allow_dialogue = False
    if not persistent.seen_actionwarning:
        call screen dialog("Please note that a lot of this dialogue is outdated and needs work.", ok_action=Return)
        $ persistent.seen_actionwarning = True
    if persistent.date == "beach":
        menu:
            n "What do you wanna do?"
            "Look at the water!":
                if persistent.seen_waves:
                    n "Again?"
                else:
                    n "Alright! Let's go!"
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_waves = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 50:
                        n "I love doing romantic stuff like this with you!"
                    elif persistent.natsuki_romance >= 100:
                        n "I-I'd love to [player]!"
                        n "I love you!"
                    elif persistent.natsuki_romance >= 150:
                        n "Aww, you go to the trouble of getting me in my swimsuit and all you wanna do is stare at the water?"
                        n "Hehehe!"
                    elif persistent.natsuki_romance >= 200:
                        n "Hehehe aww, we're alone at the beach and you don't wanna don't wanna do anything together?"
                        n "Even though I dressed just for you."
                        menu:
                            "You're wearing the same swimsuit as always, Natsuki.":
                                pass
                        n "Urk!"
                        n "Uhh, let's go!"
                jump chbeach_oceanaction
            "Let's go swim!":
                if persistent.seen_swim:
                    n "Again?"
                else:
                    n "Yay!!"
                    $ persistent.natsuki_like += 10
                    $ persistent.seen_swim = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 200:
                        n "Hehe, maybe we could skinny dip?"
                        n "Would you like that?"
                        menu:
                            "...":
                                pass
                        n "Uhh, let's go!"
                    elif persistent.natsuki_romance >= 150:
                        n "Will you hold me and make sure it's not too cold?"
                    elif persistent.natsuki_romance >= 100:
                        n "Yay! You're the best [player]!"
                    elif persistent.natsuki_romance >= 50:
                        n "I love swimming!"
                        n "You know me so well!"
                jump chbeach_swimaction
            "Let's build a sand castle!":
                if persistent.seen_castle:
                    n "We already made one but okay..." 
                else:
                    n "Ooh sounds fun!"
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_castle = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 50:
                        n "Not the most romantic thing ever, but I mean we don't have a ton of options here."
                    elif persistent.natsuki_romance >= 100:
                        n "We should make a little couple sandhouse!"
                    elif persistent.natsuki_romance >= 150:
                        n "Ooh, sandcastles together! How romantic!"
                    elif persistent.natsuki_romance >= 200:
                        n "Or, I mean maybe we could, just lie on the beach..."
                        n "Or uhh, nevermind!"
                jump chbeach_sandcastleaction
            "Let's go grab a drink!":
                if persistent.seen_drink:
                    n "..."
                else:
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_drink = True
                jump chbeach_drinkaction
            "Let's dig for stuff!":
                if persistent.seen_dig:
                    n "..."
                else:
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_dig = True
                jump chbeach_digaction
            "Nevermind":
                n "Okay..."
                jump chbeach_loop
    if persistent.date == "beach_night":
        menu:
            n "What do you wanna do?"
            "Look at the water!":
                if persistent.seen_waves:
                    n "Again?"
                else:
                    n "Alright! Let's go!"
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_waves = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 200:
                        n 1bk "Y'know [player],{w=0.1} we're alone on the beach...{w=0.1} at night."
                        menu:
                            "So?":
                                pass
                        n 1bn "I mean...{w=0.1} anything can happen?"
                        menu:
                            "Like going for a walk?":
                                pass
                        n 3bi "Um, yeah sure..."
                    elif persistent.natsuki_romance >= 150:
                        n "Sounds so perfect too!"
                        n "A nice quiet romantic night with my boyfriend."
                        n "...{w=0.2}Or girlfriend, or whatever you choose to be."
                    elif persistent.natsuki_romance >= 100:
                        n "Sounds so romantic too!"
                    elif persistent.natsuki_romance >= 50:
                        n "Eh, do you think my outfit will be okay for the weather?"
                jump chbeach_night_oceanaction
            "Let's build a sand castle!":
                if persistent.seen_castle:
                    n "We already made one but okay..." 
                else:
                    n "Ooh sounds fun!"
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_castle = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 50:
                        n "Not the most romantic thing ever, but I mean we don't have a ton of options here."
                    elif persistent.natsuki_romance >= 100:
                        n "We should make a little couple sandhouse!"
                    elif persistent.natsuki_romance >= 150:
                        n "Ooh, sandcastles together! How romantic!"
                    elif persistent.natsuki_romance >= 200:
                        n "Or, I mean maybe we could, just lie on the beach and look at the stars."
                        n "Or uhh, nevermind!"
                jump chbeach_night_sandcastleaction
            "Let's dig for stuff!":
                if persistent.seen_dig:
                    n "..."
                else:
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_dig = True
                jump chbeach_night_digaction
            "Nevermind":
                n "Okay..."
                jump chbeach_night_loop
    if persistent.date == "mall":
        $ allow_dialogue = False
        menu:
            n "What should we do?"
            "Clothes shopping!":
                $ allow_dialogue = False
                n "Sound's great!"
                jump chmall_clothingstoreaction
            "Manga store?":
                if persistent.seen_manga:
                    n "..."
                else:
                    $ persistent.natsuki_like += 10
                    $ persistent.seen_manga = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 200:
                        n 1bl "Ohmigosh!"
                        n "Yey!!"
                        n "I love you so much [player]!"
                    elif persistent.natsuki_romance >= 150:
                        n 1bl "Aww, thank you [player]!"
                        n "You really do pay attention to what I like."
                        n "Let's go!"
                    elif persistent.natsuki_romance >= 100:
                        n 1bj "Yay! You're the best [player]!"
                    elif persistent.natsuki_romance >= 50:
                        n 1bj "Oh! Sounds fun."
                jump chmall_mangaaction
            "Why not go to a bakery?":
                if persistent.seen_bakery:
                    n "..."
                else:
                    $ persistent.natsuki_like += 10
                    $ persistent.seen_bakery = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 150:
                        n 1bz "That sounds so romantic!"
                        n "And I can get some good food."
                    elif persistent.natsuki_romance >= 100:
                        n 4bl "Oh! that sounds great!"
                        n 1bk "Do you want me to order something?"
                    elif persistent.natsuki_romance >= 50:
                        n 1bj "Hm, sounds like a plan!"
                jump chmall_bakeryaction
            "Nevermind.":
                jump chmall_loop
    if persistent.date == "park":
        $ allow_dialogue = False
        menu:
            n "What should we do?"
            "Go for a walk?":
                if persistent.seen_walk:
                    n "We already did that, but okay..." 
                else:
                    n "Ooh sounds fun!"
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_walk = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 150:
                        n 1bl "You're so sweet [player]!"
                        n "You always know what's fun or romantic to do!"
                    elif persistent.natsuki_romance >= 50:
                        n 4bl "Seems like a nice fun couple activity!"
                        n "I enjoy those."
                jump chpark_walkaction
            "Play catch?":
                if persistent.seen_catch:
                    $ persistent.reload_catch = False
                    n "We already did that, but okay..." 
                else:
                    n "A game of catch?"
                    n "Your on!"
                    $ persistent.reload_catch = False
                    $ persistent.natsuki_like += 5
                    $ persistent.seen_catch = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    n 2bq "Seems more like a thing you'd do with a friend,{w=0.3} or a child."
                    n 1bj "But it could be fun!"
                jump chpark_catchaction
            "Picnic?":
                if persistent.seen_picnic:
                    n "We already did that but okay..." 
                else:
                    n "Let's go!"
                    $ persistent.natsuki_like += 10
                    $ persistent.seen_picnic = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 150:
                        n 1bl "That's such a cute idea!"
                        n "I love it!"
                    elif persistent.natsuki_romance >= 50:
                        n 1bj "How sweet!"
                jump chpark_picnicactions
            "Nevermind.":
                jump chpark_loop
    if persistent.date == "club":
        $ allow_dialogue = False
        menu:
            n "What should we do?"
            "Read manga!":
                if persistent.seen_read:
                    n "We already did that but okay..." 
                else:
                    n "Finally!!!"
                    $ persistent.natsuki_like += 20
                    $ persistent.seen_read = True
                if persistent.natsuki_love:
                    $ persistent.natsuki_romance += 5
                    if persistent.natsuki_romance >= 200:
                        n 1k "How nostalgic, hehehe."
                        n 12e "I miss the old days when it was us in the club."
                        n "And...{w=0.3} Sayori...{w=0.3} and...{w=0.3}"
                        hide window
                        show natsuki 12f at s11
                        pause 4.0
                        n 12g "Uh!"
                        show natsuki 1n at t11
                        n "Sorry [player]!"
                        n "L-Let's go!"
                    elif persistent.natsuki_romance >= 100:
                        n "Parfait Girls was just getting good!"
                    elif persistent.natsuki_romance >= 50:
                        n 4s "Hm. I hope we know find something I like..."
                jump chclub_mangaaction
            "Grab some new manga!":
                if persistent.seen_grab:
                    n "We already did that but okay..." 
                else:
                    n "Finally!!!"
                    $ persistent.natsuki_like += 20
                    $ persistent.seen_grab = True
                    if persistent.natsuki_romance >= 200:
                        n "Just like old times..."
                    elif persistent.natsuki_romance >= 50:
                        n 4s "Heh, finally something new!"
                jump chclub_grabaction
            "Let's share poems!":
                n "Let's go then!"
                jump chclub_poemaction
            "Nevermind":
                jump chclub_loop
    if persistent.date == "pool":
        menu:
            "Swimming!":
                jump chpool_swimaction
            "Nevermind":
                jump chpool_loop
        jump chpool_loop
    if persistent.date == "":
        if not config.developer:
            menu:
                "None avalible..."
                "Nevermind.":
                    jump ch30_loop
        else:
            menu:
                "Welcome back programmer."
                "Check persistent.natsuki_like.":
                    "persistent.natsuki_like =[persistent.natsuki_like]"
                    jump ch30_loop

label musicmenu:
    $ allow_dialogue = False
    menu:
        n "Want a change of tune?"
        "Daijoubu!":
            play music t8
            $ persistent.current_music = "daijoubu"
            jump ch30_loop
        "Okay Everyone! (Natsuki)":
            play music tnatsuki
            $ persistent.current_music = "natsuki"
            jump ch30_loop
        "Doki Doki Pound!":
            play music tdokidoki
            $ persistent.current_music = "dokidoki"
            jump ch30_loop
        "Poems are Forever!":
            play music tpoems
            $ persistent.current_music = "poem"
            n jha "I know this isn't really a \"Natsuki\" song but I think it sounds nice, so it's here."
            jump ch30_loop
        "Confession" if persistent.natsuki_love:
            play music t10
            $ persistent.current_music = "confession"
            jump ch30_loop
            n "This reminds me of when we started dating."
        "Just Natsuki":
            play music m1
            $ persistent.current_music = "default"
            jump ch30_loop
        "No music, please.":
            stop music
            $ persistent.current_music = ""
            jump ch30_loop
        "Custom Music":
            jump custommusic
        "No I don't.":
            jump ch30_loop

label extrasmenu:
    $ allow_dialogue = False
    menu:
        "Games":
            menu:
                "Scribbles":
                    call screen dialog("This game is very broken and is being fixed!", ok_action=Jump("extrasmenu"))
                "Let's fight!":
                    jump startfight
                "Nevermind...":
                    jump ch30_loop
        "Background":
            if time_of_day == "Day":
                menu:
                    "The Beach":
                        if persistent.background_day == "beach":
                            n jha "We're already here, silly."
                            jump extrasmenu
                        else:
                            n jha "Okay, get ready!"
                            $ persistent.background_day = "beach"
                            stop music fadeout 2.0
                            scene white with dissolve_scene
                            $ renpy.movie_cutscene("nighttransition1.mpg")
                            call showroom
                            call playmusic
                            n jha "Here we are!"
                            jump ch30_loop
                    "The Park":
                        if persistent.background_day == "park":
                            n jha "We're already here, silly."
                            jump extrasmenu
                        else:
                            n jha "Okay, get ready!"
                            $ persistent.background_day = "park"
                            stop music fadeout 2.0
                            scene white with dissolve_scene
                            $ renpy.movie_cutscene("nighttransition1.mpg")
                            call showroom
                            call playmusic
                            n jha "Here we are!"
                            jump ch30_loop
                    "Nevermind.":
                        jump extrasmenu
            if time_of_day == "Night":
                n jnb "Sorry [player], there aren't any background options at night."
                jump extrasmenu
        "Flower" if persistent.has_flower:
            if not persistent.flower:
                n jnb "Sure, I'll put it on."
                show flower zorder 3
                $ persistent.flower = True
                jump ch30_loop
            else:
                n jnb "Alright, I'll take it off."
                hide flower
                $ persistent.flower = False
                jump ch30_loop
        "Hair Color" if persistent.natsuki_like >= 20:
            if persistent.natsuki_emotion == "Sad":
                n jsb "I don't want to change my hair [player]..."
                jump ch30_loop
            menu:
                "Blonde":
                    n jhb "Want blonde eh?"
                    n jha "Okay!"
                    hide blonde
                    hide red
                    hide skyblue
                    hide lime
                    hide silver
                    hide ginger
                    show blonde zorder 3
                    $ persistent.hair_color = "Blonde"
                    n "There!"
                    jump ch30_loop
                "Lime Green":
                    n jhb "Just like Bijuu Mike!"
                    n jha "Okay!"
                    hide blonde
                    hide red
                    hide skyblue
                    hide lime
                    hide silver
                    hide ginger
                    show lime zorder 3
                    $ persistent.hair_color = "Lime"
                    n "There!"
                    jump ch30_loop
                "Red":
                    n jhb "Just like my ribbons!!"
                    n jha "Okay!"
                    hide blonde
                    hide red
                    hide skyblue
                    hide lime
                    hide silver
                    hide ginger
                    show red zorder 3
                    $ persistent.hair_color = "Red"
                    n "There!"
                    jump ch30_loop
                "Sky Blue":
                    n jhb "Just like Sayori's eyes!"
                    n jha "Okay!"
                    hide blonde
                    hide red
                    hide skyblue
                    hide lime
                    hide silver
                    hide ginger
                    show skyblue zorder 3
                    $ persistent.hair_color = "Sky Blue"
                    n "There!"
                    jump ch30_loop
                "Ginger":
                    n jha "Hehe, I like ginger hair!"
                    n "Alright then!"
                    hide blonde
                    hide red
                    hide skyblue
                    hide lime
                    hide silver
                    hide ginger
                    show ginger zorder 3
                    $ persistent.hair_color = "Ginger"
                    n "There!"
                    jump ch30_loop
                "Silver" if persistent.has_silver:
                    n jhb "Hehe! I've never tried this one!"
                    n jha "I'm going to be old granny Natsuki."
                    hide blonde
                    hide red
                    hide skyblue
                    hide lime
                    hide skyblue
                    hide silver
                    hide ginger
                    show silver zorder 3
                    $ persistent.hair_color = "Silver"
                    n "There!"
                    jump ch30_loop
                "Pink":
                    n jhb "Back to normal eh?"
                    n jha "Alright!!"
                    hide blonde
                    hide red
                    hide skyblue
                    hide lime
                    hide silver
                    hide ginger
                    $ persistent.hair_color = "Pink"
                    n "There!"
                    jump ch30_loop
                "Nevermind...":
                    n jnb "Okay..."
                    jump ch30_loop
        "Clothing" if persistent.natsuki_like >= 10:
            n jnb "Sure, what to?"
            menu:
                "Megunin Costume":
                    if persistent.wearing == "Witch":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        n jha "Oh, alright then!"
                        n "Let me just..."
                        scene black
                        n "...turn of the lights."
                        pause 2.0
                        n "Arrright!"
                        $ persistent.wearing = "Witch"
                        call showroom
                        n jha "There we go!"
                        jump ch30_loop
                "Christmas \"Loli\" Outfit":
                    if persistent.wearing == "Christmas":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        n jha "Oh, alright then!"
                        n "Let me just..."
                        scene black
                        n "...turn of the lights."
                        pause 2.0
                        n "Arrright!"
                        $ persistent.wearing = "Christmas"
                        call showroom
                        n jha "There we go!"
                        jump ch30_loop
                "Maid Outfit":
                    if persistent.wearing == "Maid":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        if persistent.natsuki_like >= 60:
                            n jha "Oh, alright then!"
                            n jhd "Just for you ehehee."
                            scene black
                            pause 2.0
                            n "Arrright!"
                            $ persistent.wearing = "Maid"
                            call showroom
                            n jha "There we go!"
                            if persistent.natsuki_love:
                                n jhd "You like what you see [player]?"
                                n jhc "Ehehehe!"
                            jump ch30_loop
                        else:
                            n "Uh..."
                            n "That's a bit lewd..."
                            jump ch30_loop
                "Bikini" if persistent.natsuki_romance >= 200:
                    if persistent.wearing == "Bikini":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        if persistent.natsuki_romance >= 200:
                            n jnb "We're not at the beach..."
                            n jhd "But if you like it, then whatever!"
                            scene black
                            pause 2.0
                            n "Arrright!"
                            $ persistent.wearing = "Bikini"
                            call showroom
                            n jha "There we go!"
                            n jhd "You like what you see [player]?"
                            n jhc "Hehehe."
                            jump ch30_loop
                "Beach Clothes":
                    if persistent.wearing == "Beach":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        n jha "I love that outfit!"
                        n "It's great for the beach!"
                        scene black
                        pause 2.0
                        n "Arrright!"
                        $ persistent.wearing = "Beach"
                        call showroom
                        n jha "There we go!"
                        n "It's nice and airy!"
                        jump ch30_loop
                "Red Dress" if persistent.natsuki_romance >= 100:
                    if persistent.wearing == "Dress":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        if persistent.natsuki_romance >= 100:
                            n jnb "Something fancy?"
                            n jha "I like it!"
                            scene black
                            pause 2.0
                            n "Arrright!"
                            $ persistent.wearing = "Dress"
                            call showroom
                            n jha "There we go!"
                            n jhd "How do I look?"
                            jump ch30_loop
                "White Tank Top":
                    if persistent.wearing == "WhiteTank":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        n jnb "Good for warm weather!"
                        scene black
                        pause 2.0
                        n "Arrright!"
                        $ persistent.wearing = "WhiteTank"
                        call showroom
                        n jha "There we go!"
                        n jhd "This is nice and comfy!"
                        jump ch30_loop
                "School Uniform":
                    if persistent.wearing == "":
                        n "I'm already wearing it silly!"
                        jump ch30_loop
                    else:
                        n jha "Oh, alright then!"
                        n "Let me just..."
                        scene black
                        n "...turn of the lights."
                        pause 2.0
                        n "Arrright!"
                        $ persistent.wearing = ""
                        call showroom
                        n jha "There we go!"
                        jump ch30_loop
                "Nevermind":
                    n "Alright then."
                    jump ch30_loop
        "Room Decor":
            n jnb "Anything you have in mind?"
            menu:
                "Pride Flags":
                    n "Which pride flag would you like?"
                    menu:
                        "Gay":
                            $ persistent.flag = "Gay"
                            scene black
                            call showroom
                        "Lesbian":
                            $ persistent.flag = "Lesbian"
                            scene black
                            call showroom
                        "Transgender":
                            n jha "Huh, just like-...{w=0.5}{nw}"
                            n jnb "Uh, nevermind!"
                            $ persistent.flag = "Trans"
                            scene black
                            call showroom
                        "Non-Binary":
                            $ persistent.flag = "Enby"
                            scene black
                            call showroom
                        "Bisexual":
                            $ persistent.flag = "Bi"
                            scene black
                            call showroom
                        "Pansexual":
                            $ persistent.flag = "Pan"
                            scene black
                            call showroom
                        "Asexual":
                            $ persistent.flag = "Ace"
                            scene black
                            call showroom
                        "Nevermind":
                            jump extrasmenu
                    jump extrasmenu
                "Black Lives Matter Flag":
                    $ persistent.flag = "BLM"
                    scene black
                    call showroom
                "Can you take the [persistent.flag] flag down?" if persistent.flag != "":
                    $ persistent.flag = ""
                    n "Sure."
                    scene black
                    call showroom
                "Nevermind":
                    jump extrasmenu
            jump extrasmenu
        "Accessory":
            n jnb "Sure, what should I put on?"
            menu:
                "Glasses":
                    if persistent.head_accessory == "Glasses":
                        n "I'm already wearing them silly!"
                        jump ch30_loop
                    else:
                        n jnb "Glasses?"
                        n jha "Cool!"
                        $ persistent.head_accessory = "Glasses"
                        call showroom
                        n jha "There we go!"
                        jump ch30_loop
                "Face Mask":
                    if persistent.head_accessory == "Mask":
                        n "I'm already wearing them silly!"
                        jump ch30_loop
                    else:
                        n jnb "Well, gotta stay safe!"
                        $ persistent.head_accessory = "Mask"
                        call showroom
                        n jha "Now I know what you have to put up with."
                        jump ch30_loop
                "None" if persistent.head_accessory != "":
                    if persistent.head_accessory == "":
                        n "I'm already wearing them silly!"
                        jump ch30_loop
                    else:
                        n jnb "Okay."
                        $ persistent.head_accessory = ""
                        call showroom
                        n jha "There we go!"
                        jump ch30_loop
                "Nevermind":
                    n jnb "Okay."
                    jump extrasmenu
        "Lights" if time_of_day == "Night": 
            n jnb "You want to toggle the lights?"
            menu:
                "Turn On" if persistent.lights == False:
                    n "Alrgiht."
                    hide shade
                    $ persistent.lights = True
                    n "Aannnddd, they're on."
                    jump ch30_loop
                "Turn Off" if persistent.lights == True:
                    n "Alrgiht."
                    show shade zorder 5
                    $ persistent.lights = False
                    n "Aannnddd, they're off."
                    jump ch30_loop
                "Nevermind":
                    jump ch30_loop
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_loop

label custommusic:
    if persistent.show_again:
        call screen custummusic(message="This is the custom music menu!\nIn the Just Natsuki directory is a folder named \"custom-music\"\nPut the song you want to use into it and name it either 01.ogg, 02.ogg etc...\nFile must be an OGG.", ok_action=Return)
    menu:
        n "Want to play something of your own?"
        "[persistent.music1_name]":
            $ persistent.current_music = "custom1"
            play music custom1
            jump ch30_loop
        "[persistent.music2_name]":
            $ persistent.current_music = "custom2"
            play music custom2
            jump ch30_loop
        "[persistent.music3_name]":
            $ persistent.current_music = "custom3"
            play music custom3
            jump ch30_loop
        "Skip to time" if config.developer: #This feature is mostly for me, if it proves to not be buggy, I may make it accessible for everyone.
            jump musicskip
        "I'd like to name my music.":
            jump namingmusic
        "Nevermind":
            hide screen talking_new
            hide screen talking_new2
            jump ch30_loop

label musicskip:
    $ skiptime = renpy.input('What time to skip to?',length=30).strip(' \t\n\r')
    $ skippos = skiptime.strip()
    if persistent.current_music == "custom1":
        play music "<from " + str(skippos) + " loop 0.0>custom-music/01.mp3"
    elif persistent.current_music == "custom2":
        play music "<from " + str(skippos) + " loop 0.0>custom-music/02.mp3"
    elif persistent.current_music == "custom3":
        play music "<from " + str(skippos) + " loop 0.0>custom-music/03.mp3"
    jump custommusic

label namingmusic:
    menu:
        "Which one?"
        "Track 1":
            $ track1 = renpy.input('Please enter the name of the track!',length=30).strip(' \t\n\r')
            $ persistent.music1_name = track1.strip()
        "Track 2":
            $ track2 = renpy.input('Please enter the name of the track!',length=30).strip(' \t\n\r')
            $ persistent.music2_name = track2.strip()
        "Track 3":
            $ track3 = renpy.input('Please enter the name of the track!',length=30).strip(' \t\n\r')
            $ persistent.music3_name = track3.strip()
    jump custommusic

label dlcmenu:
    $ config.overlay_screens = []
    hide screen hkb_overlay
    stop music fadeout 2.0
    scene club
    play music t4
    if persistent.first_dlc:
        "This menu is where you can find everything involving the coming DLC packs."
        "Clicking which one you want will activate it's features."
        "Keep in mind that you can only have one active at a time."
        $ persistent.first_dlc = False
    call screen dlc("Please choose which DLC you want activated.")
    $ exiting_fight = True
    scene black
    pause 1.0
    jump ch30_autoload

label space_dlc_check:
    show screen start_dlc_check("Checking for DLC\nPlease wait...")
    pause 5.0
    if os.path.isfile(basedir + "/dlc/tales_from_space.rpa"):
        hide screen start_dlc_check
        call screen dialog("DLC pack found!", Return)
        $ persistent.using_space_dlc = True
    else:
        hide screen start_dlc_check
        call screen dialog("Error: DLC pack not found!", Return)
    jump dlcmenu

label startup_dlc_check:
    if persistent.using_space_dlc:
        if not os.path.isfile(basedir + "/dlc/tales_from_space.rpa"):
            call screen dialog("Error: DLC pack not found!\nDLC is now disabled.", Return)
            $ persistent.using_space_dlc = False
    return

label tricks:
    menu:
        "Reload the game":
            n "Alright."
            n "Gimmie a sec, I need to turn off some anticheat measures."
            call updateconsole("persistent.anticheat = 0")
            $ persistent.anticheat = 0
            n "If I left that on the game would think your trying to cheat and shut off."
            n "Anyway, here we go!"
            $ persistent.autoload = "reloaded"
            call updateconsole("reload")
            $ renpy.utter_restart()

label reloaded:
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    show natsuki 1a at t11
    n "And we're back!"
    n "Sorry, I haven't set up the room yet."
    n "Usually I don't have to restart the game that way."
    n "Anyway, I'd better turn those anticheats back on and get everything ready!"
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_autoload"
    $ persistent.reloaded = True
    jump ch30_autoload

label change:
    menu:
        "...my name?":
            n jnb "You want me to change you name?"
            menu:
                "Yes":
                    n "Alright."
                    $ newname = renpy.input('Please enter your new name! (Type nevermind to cancel)',length=30).strip(' \t\n\r')
                    $ player = newname.strip()
                    if newname.strip() == "Natsuki":
                        n "Really?"
                        n "Okay."
                    elif newname.strip() == "nevermind":
                        n "Okay then..."
                        jump ch30_loop
                    elif newname.strip() == "Daisy":
                        n jnb "Wow, that's pretty!"
                        n jha "Like a pretty joyful flower."
                        n jnb "Daisies usually represent femininity and innocence. It's a very pretty name."
                        n "It's also the name of the mod creator, her name is Daisy."
                        n "She made a good choice."
                    elif newname.strip() == "Edgar":
                        n jnb "Oh! Really?"
                        n "Like Edgarmods, the creator of this mod."
                        n "Well, Edgar isn't her name. It's an online name."
                        n "So you want me to call you that? Cool."
                    elif newname.strip() == "Monika":
                        n jaa "Really?!"
                        n jad "Okay..."
                    else:
                        n "Alright!"
                        n "From now I'll call you [player]!"
                    $ persistent.playername = newname.strip()
                "No":
                    n "Alright..."
        "...my gender?":
            n jnb "Oh, why?{w=0.6}{nw}"
            n "Actually, I wont ask."
            menu:
                "What gender do you identify as?"
                "Male":
                    if persistent.player_gender == "Male":
                        n jnb "Uh [player], you're already a guy."
                        n "We're you just joking with me?"
                        jump normaltalkmenu_select
                    $ persistent.player_gender = "Male"
                "Female":
                    if persistent.player_gender == "Female":
                        n jnb "Uh [player], you're already a girl."
                        n "We're you just joking with me?"
                        jump normaltalkmenu_select
                    $ persistent.player_gender = "Female"
                "Non-Binary/Neither":
                    if persistent.player_gender == "Non-Binary":
                        n jnb "Uh [player], you're already Non-Binary/Neither..."
                        n "We're you just joking with me?"
                        jump normaltalkmenu_select
                    $ persistent.player_gender = "Non-Binary"
            n jha "Alright. from now on I'll refer to you as [persistent.player_gender]"
        "...my pronouns?":
            n jnb "Want me to use different pronouns?"
            n jha "Sure!"
            menu:
                "He/Him":
                    if persistent.player_pronouns == "he":
                        n jnb "Uh [player], I already use he/him for you..."
                        n jab "Are you pranking me?"
                        jump normaltalkmenu_select
                    $ persistent.player_pronouns = "he"
                "She/Her":
                    if persistent.player_pronouns == "she":
                        n jnb "Uh [player], I already use she/her for you..."
                        n jab "Are you pranking me?"
                        jump normaltalkmenu_select
                    $ persistent.player_pronouns = "she"
                "They/Them":
                    if persistent.player_pronouns == "they":
                        n jnb "Uh [player], I already use they/them for you..."
                        n jab "Are you pranking me?"
                        jump normaltalkmenu_select
                    $ persistent.player_pronouns = "they"
            n jha "Alright, feel free to ask me use different ones if you'd prefer that."
        "Nevermind":
            jump normaltalkmenu_select
    jump normaltalkmenu_select


#I didn't know I put this here...
label beachfavthings:
    n "I love the sand!"
    n "You can make so many things!"
    n "Like sandmen."
    n "That reminds me..."
    n "Me and my friends did that once!"
    n "Ehehe~!"
    jump chbeach_loop
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
