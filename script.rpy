﻿init python:

    import random
    # # VARIABLES ******************************************************************************************************

    money = 0

    current_day = 0

    stamina_max = 10

    stamina = 10

    reputation = 0

    corruption = 0

    happiness = 10

    lust = 0

    tipsMultiplier = 1

    staminaWork = 2

    cafeTutorial = False

    studioTutorial = False

    hotelTutorial = False

    barTutorial = False

    corruptionLives = 3

    happinessLives = 3

    sadnessLives = 3

    pornCareer = 0

    honesty = 0

    junkie = 0

    eviction = 3

    # # FUNCTIONS ******************************************************************************************************

    def jobPay(min, max):
        pay = random.randint(min, max)
        tips = (pay/2) * (tipsMultiplier + reputation)
        finalPay = pay + tips
        return finalPay

    furinaApronSprites = ['furinaapron1.png']

    furinaNakedApronSprites = ['furinanakedapron1.png','furinanakedapron2.png']

    furinaPhotoSprites = ['furinaphotoshoot1.png','furinaphotoshoot2.png','furinaphotoshoot3.png','furinaphotoshoot4.png']

    furinaBikiniSprites = ['furinabikini1.png','furinabikini2.png','furinabikini3.png','furinabikini4.png','furinabikini5.png','furinabikini6.png','furinabikini7.png']

    furinaNakedSprites = ['furinanaked.png','furinanaked2.png','furinanaked3.png','furinanaked4.png','furinanaked5.png','furinanaked6.png','furinanaked7.png']

    furinaPornSprites = ['furinaporn1.jpg','furinaporn2.jpg','furinaporn3.jpg','furinaporn4.jpg']

    furinaFetishSprites = ['furinafetish1.png','furinafetish2.png','furinafetish3.png','furinafetish4.png','furinafetish5.png','furinafetish6.png']

    furinaAdventureSprites = ['furinaadventure1.png', 'furinaadventure2.png','furinaadventure3.png','furinaadventure4.png','furinaadventure5.png','furinaadventure6.png','furinaadventure7.png']

    furinaEscortSprites = ['furinaescort1.png','furinaescort2.png']

    furinaBarSprites = ['furinabar1.png','furinabar2.png','furinabar3.png']

define f = Character("Furina")
define m = Character("Manager")
define c = Character("Charlotte")


# The game starts here.

label start:

    play music "Date.mp3" loop

label intro:

    scene crying:
        zoom 3

    "After her trial Furina fell in disgrace."
    "She lost her title as archon and all privileges that came with it."
    "Her so called friends also abandoned her, even the traveler."
    "Neuvillette also kept his distance, but in respect of her former position he gave her a home and payed for all her utilities and food."
    "Furina had more than enough to survive, but she wanted more."
    "She was used to a life of luxury! She was a goddess!"
    "Now forgotten and broke, she needs to make money on her own."

    scene street

    show furina

    f "I will show them I'm capable of supporting myself!"
    f "I was an archon, they should've show some more respect."
    f "*pouts*"
    f "Anyway, let's see what monsier Neuvillette arranged for me."

    hide furina
    scene livingroomday

    show furina

    f "This place isn't THAT bad, but I deserve better"
    f "I want my palace back!"
    "Furina helds back her tears."
    f "I need money, but for that..."
    f "I need a job..."
    f "Where do common folk get jobs?"

    scene black

    "You must tend to Furina needs."
    "Make sure she has money and it's still happy."
    "You must pay for her rent everyday! The rent costs: $[rentValue]"
    "Also looing out for her corruption and not letting it consume Furina!"

    jump map

label map:

    play music "Date.mp3" loop

    scene livingroomday

    show screen day_money_counter

    menu:

        f "where should I go?"

        "Café":
            if cafeTutorial == False:
                jump cafetutorial
            else:
                jump cafe
        "Studio":
            if studioTutorial == False:
                jump studiotutorial
            else:
                jump studio
        "Bar":
            jump bar
        "Hotel":
            jump hotel
        "Mall":
            jump mall
        "Pharmacy":
            jump pharmacy
        "Adventure":
            jump adventure

        "Rest":
            jump endday


label endday:

    play music "Date.mp3" loop


    f "It was a very long day, even a goddess like me needs to rest!"

    if money >= rentValue:
        f "I payed my rent, it costs $[rentValue]"
        $ eviction = 0
    elif money < rentValue:
        f "I didn't had enough money to pay my rent!"
        f "If I don't pay rent for 3 days straight I will be evicted! I still have [eviction] days before that!"
        $ eviction -= 1

    if eviction == 0:
        jump evictedEnding

    

    $ stamina = stamina_max
    $ current_day += 1

    if corruption >= 100:
        "Furina is too corrupted! Save her before it's too late!"
        $ corruptionLives -= 1
    elif corruption <= 100:
        $ corruptionLives = 3

    if corruptionLives <= 0:
        f "Yes! This is great! I'm going to sell my body and soul! That's who I am now!"
        f "A worthless slut! A worthless and useless goddess!"
        "Furina is too far gone with her corruption."
        jump corruptionending

    if junkie >= 50:
        "Furina begins to expirience some side effects from the drugs."
    elif junkie >= 70:
        "Furina barely sleeps feeling the effects of the drugs."
    elif junkie >= 100:
        "Furina can't handle her addiction anymore"
        jump junkieending

    if honesty >= 50:
        "Before sleeping, Furina thinks about how much she's enjoying having a normal job."
    elif honesty >= 70:
        "Furina is beginning to like the idea of become a regular person."
    elif honesty >= 100:
        "Furina decided to become a worker!"
        jump honestyending
        
    if happiness >= 100:
        "Furina feels very happy with her new life."
        $ happinessLives -= 1
    elif happiness <= 100:
        $ happinessLives = 3

    if happinessLives <= 0:
        f "I see now, I see that I can be happy."
        "Furina goes to bed with a genuine smile."
        jump happyending

    if happiness <= 0:
        "Furina is sad, she cried herself to sleep."
        $ sadnessLives -= 1
    elif happiness >= 50:
        $ sadnessLives = 3

    if sadnessLives <= 0:
        f "I'm... I can't get out of bed..."
        "Furina is too sad to do anything."
        jump sadending

    if pornCareer >= 50:
        "Before sleeping, Furina contemplates following the porn star career."
    elif pornCareer >= 70:
        "Furina is beginning to like the idea of become a porn star."
    elif pornCareer >= 100:
        "Furina decided to become a pornstar!"
        jump pornending


    if corruption >= 50:
        $ happiness -= 20
    elif corruption >= 70:
        $ happiness -= 30
    elif corruption >=100:
        $ happiness -= 50
    else:
        $ happiness -= 10

    $ honesty -= 2


    jump map

label cafetutorial:

    scene cafe

    show furina

    "Furina enters the café and approaches the manager."

    f "H-hi! Are you guys hiring?"

    m "Aren't you Furina the archon?"

    f "You're correct, mortal. That's me! I Focalors, bless this shop with my presence."

    m "Weren't you like a fraud or something?"

    f "No!"

    "Furina sighs frustated."

    f "This was a mistake, sorry."

    "Furina was ready to leave when the manager holds her arm."

    m "Wait, you want to work here?"

    f "Yes."

    m "Well, having someone as famous as you working here might be good for business."

    m "Even if you're in disgrace."

    f "I'm not in disgrace!"

    "The manager leads Furina to his office."

    m "Have you ever made a coffee before?"

    f "No. My only job in 500 years was being an archon."

    m "You'll have to show me something if you want to convice me."
    
    hide furina

    show furinaangry

    f "S-show you something?"

    m "Yes, show me how much you want to work here."

    jump cafechoice

label cafechoice:

    show furinaangry

    scene cafe

    m "So, what are you going to do?"

    menu:

        "Pull shirt up.":
            $ corruption += 1
            hide furina
            show furinatopless
            "Furina looks down realizing she had hit rock bottom."
            "She ends up agreeing to the manager's lewd proposition"
            "Furina pulls up her shirt"

    "The manager feels Furina's perky breasts while she moans."

    m "You're enjoying this."

    f "No!"

    "Furina pushes his hands away."

    f "I think I already proved that I want to work here."

    hide furinatopless
    show furinaangry

    m "You only proved how desperate you're."

    f "I have the job or not?"

    m "Okay, I'll give you the job. But I might require your assistance in situations like this."

    "The manager trains Furina and gives her the uniform."

    $ cafeTutorial = True
    jump cafe

label cafe:

    scene cafe

    f "I can do this!"

    menu:

        "Work costs [staminaWork] stamina."

        "Work properly":
            if stamina < staminaWork:
                f "I'm too tired for this!"
                jump cafe
            else:
                $ furinaApron = renpy.random.choice(furinaApronSprites)
                show expression furinaApron
                $ salary = jobPay(5, 20)
                $ money += salary
                $ stamina -= staminaWork
                $ happiness -= 2
                $ honesty += 5
                "Furina worked honestly and made $[salary]"
                hide furinaApron
                jump cafe
        
        "Wear only apron (more tips)" if corruption >= 20:
            if stamina < staminaWork:
                f "I'm too tired for this!"
                jump cafe
            else:
                $ furinaNakedApron = renpy.random.choice(furinaNakedApronSprites)
                show expression furinaNakedApron
                $ tipsMultiplier = 2
                $ salary = jobPay(20, 40)
                $ money += salary
                $ stamina -= staminaWork
                $ happiness -= 2
                $ corruption += 1
                "Furina wears nothing under the apron attracting more customers and attention. She made $[salary]"
                jump cafe

        "I'm done working for today.":
            jump map


label studiotutorial:

    play music "Sexy.mp3" loop


    scene studio

    "Furina walks by a photography studio with a advertisment asking for models."

    show furina

    f "I can be a model! I, Furina, will show to these people what real beauty looks like!"

    "Furina enters the studio interest in the job."

    f "Rejoice, photographer! The best looking model of Fontaine just arrived! Ready your camera!"

    show charlotte

    c "Lady Furina?"

    f "Charlotte? I thought you worked for the steambird."

    c "I do, this is like a side gig for me."

    f "I see, so where should I pose?"

    c "Calm down, Lady Furina! First we can begin with some ads for magazines and the steambird."

    f "Sure! Just capture my best angles!"

    "Charlotte takes some pictures of Lady Furina."

    "After the photoshoot, Charlotte leads Lady Furina to a corner."

    c "You know, if you're willing, we can make more lewd pictures. Those sell well."

    "Lady Furina gets flustered."

    f "I... I'm a goddess! I can't be seem by my subjects like that!"

    c "You aren't a goddess anymore, how about we begin with some bikimi photos?"

    "Lady Furina pouts and sighs but ultimately changes into the bikini."

    "Charlotte takes some normal pictures of Furina, but also some lewd ones in provocative poses."

    c "I think we have enough. How do you feel?"

    f "I don't know, a mix of feeling hot and feeling used."

    c "*laughs*"

    c "You'll get used to it."

    hide charlotte

    $ studioTutorial = True

    jump studio


label studio:

    play music "Sexy.mp3" loop

    scene studio

    f "Time to look good!"

    menu:

        "Work costs [staminaWork] stamina."

        "Advertsiment Photoshoot (-2 stamina)":
            if stamina < staminaWork:
                f "I'm too tired for this!"
                jump studio
            $ furinaPhoto = renpy.random.choice(furinaPhotoSprites)
            show expression furinaPhoto
            $ salary = jobPay(5, 10)
            $ money += salary
            $ stamina -= staminaWork
            "Furina worked honestly and made $[salary]"
            hide expression furinaPhoto
            jump studio
        
        "Bikini photoshoot (More tips, increases corruption, -2 stamina)":
            if stamina < staminaWork:
                f "I'm too tired for this!"
                jump studio
            $ furinaBikiniPhoto = renpy.random.choice(furinaBikiniSprites)
            show expression furinaBikiniPhoto
            $ tipsMultiplier = 2
            $ salary = jobPay(10, 25)
            $ money += salary
            $ stamina -= staminaWork
            $ corruption += 1
            $ happiness += 1
            "Furina takes some lewd bikini photos and made $[salary]"
            hide expression furinaBikiniPhoto
            jump studio

        "Naked photoshoot (Even more tips, increases corruption more, -3 stamina)" if corruption >= 20:
            if stamina < 3:
                f "I'm too tired for this!"
                jump studio
            $ furinaNakedPhoto = renpy.random.choice(furinaNakedSprites)
            show expression furinaNakedPhoto
            $ tipsMultiplier = 3
            $ salary = jobPay(30, 40)
            $ money += salary
            $ stamina -= 3
            $ corruption += 2
            $ happiness += 2
            $ pornCareer += 1
            "Furina takes naked pictures and made $[salary]"
            jump studio

        "Porn movie (great money, great corruption), -5 stamina" if corruption >= 50:
            if stamina < 5:
                f "I'm too tired for this!"
                jump studio
            $ furinaPornPhoto = renpy.random.choice(furinaPornSprites)
            show expression furinaPornPhoto
            $ tipsMultiplier = 6
            $ salary = jobPay(50, 70)
            $ money += salary
            $ stamina -= 5
            $ corruption += 5
            $ happiness -= 10
            $ pornCareer += 5
            $ honesty -= 10
            "Furina makes a porn movie and made $[salary]"
            jump studio

        "Fetish porn movie (Best money, worst corruption), -10 stamina" if corruption >= 70:
            if stamina < 10:
                f "I'm too tired for this!"
                jump studio
            $ furinaFetishPhoto = renpy.random.choice(furinaFetishSprites)
            show expression furinaFetishPhoto
            $ tipsMultiplier = 8
            $ salary = jobPay(150, 250)
            $ money += salary
            $ stamina -= 10
            $ corruption += 10
            $ happiness -= 15
            $ pornCareer += 20
            $ honesty -= 20
            "Furina makes a fetish porn movie and made $[salary]"
            jump studio

        "I'm done working for today.":
            jump map

label bar:

    play music "Relax.mp3" loop

    scene bar

    f "Let's have some fun!"

    menu:

        "Hookup (-5 stamina)":
            if stamina < 5:
                f "I'm too tired for this!"
                jump bar

            $ furinaEscortPhoto = renpy.random.choice(furinaEscortSprites)
            show expression furinaEscortPhoto
            $ stamina -= 5
            $ corruption += 10
            $ happiness += 15
            "Furina spends the night with an stranger."
            jump hotel

        "Have a few drinks. ($50, -5 stamina)":
            if stamina < 5:
                f "I'm too tired for this!"
                jump bar
            elif money < 50:
                f "I don't have money for it!"
                jump bar

            $ furinaBarPhoto = renpy.random.choice(furinaBarSprites)
            show expression furinaBarPhoto
            $ money -= 50
            $ stamina -= 5
            $ corruption += 10
            $ happiness += 15
            "Furina spends the night drinking."
            jump bar


        "Go home":
            jump map

    jump map

label hoteltutorial:

    scene hotel

    f "I used to come to this hotel and stay at the most expensive suite!"

    f "I loved to throw parties here."

    f "Neuvillette always warned me about the shady activities happening here. Like girls selling their bodies."

    f "I... I would never do that, would I?"

    $ hotelTutorial = True
    jump hotel

label hotel:

    scene hotel

    f "Let's see if anyone can use my company."

    menu:

        "Escort service (-5 stamina)":
            if corruption < 50:
                f "No! I'm not THAT corrupted yet!"
                jump hotel
            if stamina < 5:
                f "I'm too tired for this!"
                jump hotel
            $ randomEvent = random.randint(0, 10)
            if randomEvent == 2:
                "The customer liked Furina and tipped her extra money. ($50)"
                $ money += 50
            elif randomEvent == 4:
                "The customer was very nice and caring with Furina (+35 happiness)"
                $ happiness += 35
            elif randomEvent == 6:
                "The customer was extra rough on Furina! (+20 corruption)"
                $ corruption += 20
            elif randomEvent == 8:
                $ customerTheft = money / 10
                $ money -= customerTheft
                "The customer took part of Furina money while she was distracted! $[customerTheft]"
            elif randomEvent == 10:
                "There was no customers, Furina got too tired waiting and has to rest now."
                $ stamina = 0
                jump hotel

            $ furinaEscortPhoto = renpy.random.choice(furinaEscortSprites)
            show expression furinaEscortPhoto
            $ tipsMultiplier = 5
            $ salary = jobPay(100, 200)
            $ money += salary
            $ stamina -= 5
            $ corruption += 20
            $ happiness -= 35
            $ honesty -= 20
            "Furina spends some time with a customer and receives $[salary]."
            jump hotel

        "Go home":
            jump map


    jump map


label adventure:

    scene adventure

    f "It's time for some adventure."

    menu:

        "Adventure (-5 stamina)":
            if stamina < 5:
                f "I'm too tired for this!"
                jump adventure
            $ randomEvent = random.randint(0, 10)
            if randomEvent == 2:
                "Furina fould a treasure chest. ($50)"
                $ money += 50
            elif randomEvent == 4:
                "Furina met some friendly travelers along the way (+35 happiness)"
                $ happiness += 35
            elif randomEvent == 6:
                "Furina found a mysterious artifact that healed her (-20 corruption)"
                $ corruption += 20
            elif randomEvent == 8:
                $ customerTheft = money / 10
                $ money -= customerTheft
                "Furina was attacked by some Treasure Hoarders! She lost $[customerTheft]"
            elif randomEvent == 10:
                "Furina found some ruins and got lost inside, it took her all day to get out."
                $ stamina = 0
                jump adventure

            $ furinaAdventurePhoto = renpy.random.choice(furinaAdventureSprites)
            show expression furinaAdventurePhoto
            $ tipsMultiplier = 1
            $ salary = jobPay(100, 150)
            $ money += salary
            $ stamina -= 5
            $ corruption -= 20
            $ happiness += 30
            $ honesty += 20
            "Furina completes some quests and earns $[salary]."
            jump adventure

        "Go home":
            jump map


    jump map

label mall:

    scene mall

    f "I need some time for myself!"

    menu:

        "Go to the movies ($30)":
            if money < 30:
                f "I don't have enough money!"
                jump mall
            else:
                "Furina enjoyed the movie"
                $ happiness += 10
                $ money -= 30
                jump mall
        "Eat fast food ($50)":
            if money < 50:
                f "I don't have enough money!"
                jump mall
            else:
                "Furina enjoyed the food."
                $ happiness += 15
                $ money -= 50
                jump mall
        "Eat at her favorite coffee shop($100)":
            if money < 100:
                f "I don't have enough money!"
                jump mall
            else:
                "Furina enjoyed some coffee and her favorite cakes"
                $ happiness += 25
                $ money -= 100
                jump mall
        "Buy clothes ($500)":
            if money < 500:
                f "I don't have enough money!"
                jump mall
            else:
                "Furina buys some clothes for herself."
                $ happiness += 30
                $ money -= 500
                jump mall
        "Eat at expensive restaurant ($700)":
            if money < 30:
                f "I don't have enough money!"
                jump mall
            else:
                "Furina have a lavish and expensive meal."
                $ happiness += 40
                $ money -= 700
                jump mall
        "Buy expensive clothes ($1000)":
            if money < 1000:
                f "I don't have enough money!"
                jump mall
            else:
                "Furina buys clothes from the latest fashion trend."
                $ happiness += 50
                $ money -= 1000
                jump mall
        "Buy designer bags ($3000)":
            if money < 3000:
                f "What do you mean my card been declined? Try it again!"
                jump mall
            else:
                "Furina buys a bag from her favorite brand."
                $ happiness += 70
                $ money -= 3000
                jump mall
        "Go back home.":
            jump map


label pharmacy:

    scene pharmacy

    f "Here I can buy some meds."

    menu:

        "Stamina drug ($150)":
            if money < 100:
                f "I don't have enough money!"
                jump pharmacy
            else:
                $ money -= 100
                $ stamina = stamina_max
                $ junkie += 10
                f "I've never felt so productive!"
                jump pharmacy
                 
        "Happiness drug ($130)":
            if money < 130:
                f "I don't have enough money!"
                jump pharmacy
            else:
                $ money -= 130
                $ happiness += 50
                $ junkie += 25
                f "I feel so happy right now!"
                jump pharmacy

        "Corruption drug ($150)":
            if money < 150:
                f "I don't have enough money!"
                jump pharmacy
            else:
                $ money -= 150
                $ corruption -= 50
                $ junkie += 25
                f "I feel like myself again!"
                jump pharmacy

        "Cure addiction drug ($1500, needs full stamina)":
            if money < 1500:
                f "I don't have enough money!"
                jump pharmacy
            elif stamina < stamina_max:
                f "I'm too tired for the process."
            else:
                $ money -= 1500
                $ stamina = 0
                $ junkie = 0
                f "I feel tired but renewed!"
                jump pharmacy

        "Go back":
            jump map


label corruptionending:

    scene junkieending

    "Furina corruption led her through a dark path."
    "She got involved with bad people and sold her body for less and less"
    "She did unspeakable things just for the thrill of it."
    "At some point her mind broke in a unrepairable way and she became a mindless sex slave."
    jump gameover


label happyending:

    scene happyending

    "Furina finally found happiness with her new life."
    "She realized she didn't needed to be an archon to pursue happiness."
    "She eventually met and made amends with her former friends."
    jump gameover
    
label pornending:
    "Furina begins to enjoy more and more making porn movies."
    "She does more daring and explicit movies and makes her name in the industry."
    "Her former friends frown upon her decision, but she's happy with decision."
    jump gameover

label honestyending:

    scene happyending

    "After spending more time working and interacting with regular folk"
    "Furina begins to feel more and more fullfilled with the idea of honest work"
    "She's happy even if she isn't an archon anymore. Her former friends are happy by how she turned her life around."
    jump gameover

label junkieending:

    scene junkieending

    "Furina becomes too addicted to drugs."
    "She needs drugs to sleep, drugs to wake up. She only feels things when she's using them."
    "Her life was destroyed by the drugs and last time she was seem she was selling herself for drug money."
    jump gameover

label evictedEnding:

    scene junkieending

    "Furina didn't had money to pay her rent."
    "She was evicted and now roams the streets of Fontaine."
    "Her life was ruined and now she struggles to get back on her feet."
    jump gameover

label sadending:

    scene sadending

    "Furina sadness become too great for her to bear it."
    "All she can do is cry thinking about the state of her life."
    "She wastes away alone."
    jump gameover


label gameover:

    menu:

        "Try again?"

        "Yes":
            jump map
        "no":
            return



    return
