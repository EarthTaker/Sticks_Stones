from time import sleep


# Function to get location text based on current location; Also, Function to get current investigate counter's text.
# Args is used as function will not always receive a location investigation counter.
def get_current_location_text(currentLoc, *args):
    # Call in global player selection to determine which text to display.
    global playerSelection
    global lastLocation

    # Intro text
    if currentLoc == 'Corroded Wagon' and playerSelection != 'INVESTIGATE':
        print('-----------------------------------------------------------------------------------------------------||')
        print(
            'Beneath your feet lies a thin road of gravel long blackened by years of travel. Along its path, fallen \n'
            'branches lay strewn in a chaotic pattern; large carved stakes stand spiked at intervals along the road. \n'
            'Each covered in a waxy film, the weathered limbs hold drooping fabrics of bruise-colored gradients. A \n'
            'moss-covered, dark wooden wagon lies in pieces, its form scattered by time and the humid, unwelcoming \n'
            'remains of the forest of Dammendrond. Though densely monochromatic vegetation stretch for miles, patches \n'
            'of grass touching the road’s perimeter are but dried, blackened husks.')
        print(
            '-----------------------------------------------------------------------------------------------------||\n')

    elif currentLoc == 'Corroded Wagon' and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print('---------------------------------------------------------------------------------------------||')
                print(
                    'Examining the environment, you look North to see a sturdy, overgrown structure. Though its rather \n'
                    'large exterior is obscured by heavy white fog, its roof still shimmers a muted green under the \n'
                    'canopies of massive sequoia. Trapped under these ancient giants, the roof appears as a helpless \n'
                    'entity, their outstretched limbs swarming over its rotting, yet glistening surface like \n'
                    'gnashing insects.')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)
                return

            elif eachVal == 1:
                print('---------------------------------------------------------------------------------------------||')
                print(
                    'Turning South, you see a colossal landmark jutting into the sky. Covered in the years of vegetative \n'
                    'overgrowth, vein-like vines have pierced the depths this jagged cliff, its colossal stone surface \n'
                    'scattered beneath their natural hues. Walking to its side of the road, you closely analyze its \n'
                    'distant appearance; stains of black, green, and muted red seem to trail from its peak in an \n'
                    'under-arcing motion. Moments later, the pungent aroma of decay pierces the natural ambiance as you \n'
                    'gag. Desperate, you cover your face under a mask of fabric, wood, and stone; though its primitive \n'
                    'filtration is barely more than a challenge for the acrid stench. Scanning for its source, your eyes \n'
                    'befall a horrific scene as they drop to the cliff’s base. In a circular array of reds and whites, \n'
                    'fattened corpse flowers dot the darkened grounds, their pervasive forms feasting on the litter of \n'
                    'the freshly decayed.\n\n')
                print(
                    'Tightly gripping your mask, you close your eyes as an odoriferous breeze brings a fresh deposit of \n'
                    'this horrid stench. Gathering your composure, you take a few steps back and raise your head to the \n'
                    'sky… though, immediately, notice a window of shimmering air at the cliff’s peak. ')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)
                return

            elif eachVal == 2:
                print('\n-------------------------------------------------------------------------------------------||')
                print(
                    'Panning your head to the East, you witness an incremental change in the road’s graveled surface. \n'
                    'Slowly, the grimy, mud-soaked surface dries into patches of sand and chipped mud leading your \n'
                    'eyes into the endless embrace of the arid Galuve Desert.')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)
                return
            else:
                return True

    if currentLoc == 'Jagged Cliffs' and playerSelection != 'INVESTIGATE':
        print('\n---------------------------------------------------------------------------------------------------||')
        print(
            'At your feet, stone lies scattered haphazardly; shattered from years of erosion and darkened by signs of \n'
            'weary travel. Each step feels like a triumph… but for the wrong reasons. Like succumbing to restrains of \n'
            'a malicious curse, you ascend the cliff’s warped incline; each step taking you closer to the cliff’s \n'
            'outstretched peak. Along with the light crunch of shattered stone, you hear a faint knocking behind you... \n'
            'and beneath you. Stopping quickly to analyze your surroundings, you look to see the source of this \n'
            'inconsistent noise…you watch rocks kicked up from each step collide with the stones below... Shaking your \n'
            'head, you continue your ascent as the vigilant awareness fades from your mind… alongside the gradual \n'
            'disappearance of the stink below. Replaced by the enormity of the vision, you reach the cliff’s peak \n'
            'and awe at its terrible resplendence. In all directions, the ancient trees of Dammendrond lie in patches \n'
            'of vivid and sickly growth cascading into sunken valleys, scarred plains, and ruined, but once hopeful \n'
            'settlements. ')
        print(
            '-----------------------------------------------------------------------------------------------------||\n')
        sleep(2)

    elif currentLoc == 'Jagged Cliffs' and playerSelection == 'INVESTIGATE':
        for eachVal in args:
            if eachVal == 0:
                print('---------------------------------------------------------------------------------------------||')
                print('Grabbing the tattered fabric from around your neck, you wipe the sweat from your brow. In the \n'
                      'distance, a stormy horizon bellows an ominous cry; its wrathful form mirrored in opposite of the \n'
                      'sight before you. Curious, misshapen piles of timeworn traveling equipment lay scattered across \n'
                      'the cliff’s peak; their inconsistent weathered appearances drawing your eyes along a disorganized \n'
                      'placement. Moving closer, you notice bags, banners, cloaks, and clothing all sewn with vastly \n'
                      'different sigils from powerfully monolithic civilizations. Of the luggage, you see seven bags, \n'
                      'each of muted colors, positioned in an erratic, but arcing pattern mimicking the peak’s tip. Back \n'
                      'and forth, your eyes scan the odd remnants... though, beneath your curiosity, a hollow whisper \n'
                      'tightens around the edges of your flesh...“A few more inches to the South… see for yourself...”')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)

            # Player Sigil Order for End Game Condition - VISION
            elif eachVal == 1:
                # Sigil Order: STRENGTH, GREED, FEAR, REGRET, FURY, DEPRESSION, SALVATION
                print('---------------------------------------------------------------------------------------------||')
                print(
                    'Warm wind thrashes at your clothing, though its soggy touch bears a refreshing comfort as white, \n'
                    'effervescent energy pools at the corners of your vision. Trying to shake your head free of the \n'
                    'living fog, you only manage to force it deeper into your visual awareness. Flooding inward, it \n'
                    'solidifies a path through the air and coagulates into an oval of intricate design. Staring into \n'
                    'its form, a thermogenic touch blankets your mind as a vision vice grips your consciousness. \n\n')
                print('...Crying... Endless crying... Lies and the suffering of untold millions... '
                      'Torn from a life of peace... A hero... Clad in the armor of white stone... '
                      'A great manipulator of the sunken souls... \n\n')
                print(
                    'Pulled from a state of suffocating intoxication, you stare breathlessly at the oval-shaped section \n'
                    'of living air. At its center, a message sears itself into your mind... \n')
                print('In Greed, you will find Fear... as in Regret, you will find Fury... \n')
                print(
                    'Matched only by the Final Promise of Salvation, we seek to understand the Darkest of Them all... \n')
                print('Though we must First seek the Strength to endure...')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)
            else:
                return True

    if currentLoc == "Trading Post" and playerSelection != 'INVESTIGATE':
        print('-----------------------------------------------------------------------------------------------------||')
        print('Traveling through lands never meant for man, you step off the patchy road onto a log-lined pathway. \n'
              'Walking up to the decaying remains of this once bustling center for commerce and festivities, you feel \n'
              'the fog envelope you... its moist touch like a stale breath as you reach the decorated exterior of this \n'
              'fallen Trading Post. Stepping closer to the structure’s downtrodden state, you see its passionate \n'
              'architecture. Beautiful, yet simplistic designs train your eyes up long corrugated pillars of Howlite; \n'
              'its marble-like appearance shaped by the hands of ambitious engineers. Analyzing the dark slabs of \n'
              'moss-covered walnut held above the vertically scaling detail, you hear light tapping sounds on the \n'
              'roof above. Distractingly gorgeous and even more so massive, you see the source of this noise; impossibly \n'
              'defined cerulean leaves, its white veins a swollen pattern topped with a large flower of cascading \n'
              'rainbow colors stretching out in all directions. Though amazed, you find yourself distracted; quickly \n'
              'adjusting, you scan the surroundings. \n\n'
              'To the East, through thick underbrush, you notice a large settlement littered with tens. Although... to \n'
              'the West, you can see the remains of what appears to be a logging camp... ')
        print(
            '-----------------------------------------------------------------------------------------------------||\n')
        sleep(2)

    elif currentLoc == "Trading Post" and playerSelection == 'INVESTIGATE':
        for eachVal in args:
            if eachVal == 0:
                print('---------------------------------------------------------------------------------------------||')
                print('Looking down the wide storefront, you notice the building’s edges wrap around implanted, yet \n'
                      'long overgrown trees. Placed at various intervals along its exterior, you see their limbs deeply \n'
                      'embedded in the shelves of architecture placed up and down their breadth. Walking but a few feet \n'
                      'forward, you stumble on a log raked out of its bordered placement. Slamming into the ground with \n'
                      'a thud, you pause against its surface to shake your head in disbelief... \n\n')
                print('Rolling back over, you stare towards the structure’s door and notice an odd patch of wood \n'
                      'completely devoid of moss. At its center, an amulet of burnt gold and stained silver lies \n'
                      'firmly implanted. As if trying to fight back some form of infection, it pulses with desperate \n'
                      'energy every few seconds, a faint blue and gold glow burns as emaciated black tendrils carve \n'
                      'at the wood around it. ')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)

            elif eachVal == 1:
                print('---------------------------------------------------------------------------------------------||')
                print('A shrill echo bounds from the gargantuan trees as the fog around you grows dense. A quick, \n'
                      'unannounced smell of sulfur strikes at your nostrils as the new vile stench fills your lungs. \n'
                      'Standing up, the echo pulses again as the wind coalesces into a far colder, more violent form. \n'
                      'Scanning the trees, a loud, bone chilling snap pierces the calm atmosphere as a massive tree \n'
                      'limb strikes into the decaying roof. Jolting from the sudden sound, you raise your head to the \n'
                      'cacophony above. Clad in a torn veil of flayed bark, you witness an ageless horror gaze down in \n'
                      'your direction, its ghostly white eyes vibrating in a furious curiosity. Emitting a harsh \n'
                      'cacophonous clicking noise, its attention suddenly jerks to the left. Following the sounds of \n'
                      'movement, the beast’s attention is drawn to the tree line. Descending from its jaw, grotesque \n'
                      'appendages ignite in purple brilliance as a volley of yellowed stone screams to the trees.\n'
                      'Kicking itself from the treetops, it dashes after the unfortunate prey; it’s terrifying change \n'
                      'in weather following suit. ')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)
            else:
                return True

    if currentLoc == "Worker\'s Tent City Section(1)" and playerSelection != 'INVESTIGATE':
        print('-----------------------------------------------------------------------------------------------------||')
        print(
            'Approaching the thick underbrush, you see more of the logs meant to line the pathway… You feel the air \n'
            'grow thick with moisture as you briefly stop to examine signs of a desperate struggle; deeply seated into \n'
            'the soggy wood, you see final hopes of frantic prayers. Nearing the settlement’s entrance as marked by two \n'
            'large stone columns, you see makeshift tents of various sizes lie scattered throughout its \n'
            'well-traveled perimeter... \n\n')
        print('A thunderclap batters the fresh silence, and you dart into the nearest tent. Tearing at a section of \n'
              'some old, well-worn fabric within, you stretch them over the dirt and sit to rest. Warm rain gathers \n'
              'at the corners of the tent as you hear another roar in the far distance, its voracious reverberation \n'
              'shaking you to your core... ')
        print(
            '-----------------------------------------------------------------------------------------------------||\n')
        sleep(2)

    elif currentLoc == "Worker\'s Tent City Section(1)" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print('---------------------------------------------------------------------------------------------||')
                print('Waiting as the storm passes, you lean over to look outside the tent. Rain batters the ruined \n'
                      'remains of this makeshift city; pooling over a nearby structure, the water splashes outward as \n'
                      'a tent collapses under its weight. A faint shimmer and your eyes narrow to the newly reveled \n'
                      'splintered column of wood. Purple scarred obsidian lay deeply infused in its ravaged form, \n'
                      'its voided surface glistening as rain stings and hisses with each impact.\n\n')
                print('Another reflection tears your attention beyond its corrosive manifestation to the North. \n'
                      'There you see the encampment continue outwards, though... it abruptly stops as a large, damaged \n'
                      'section of the camp takes its place.')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)

            elif eachVal == 1:
                print('---------------------------------------------------------------------------------------------||')
                print('Hammering the environment, the rain continues as confusion rakes at the corners of your mind. \n'
                      'Scratching your head, you decide to cautiously approach for a closer look at the mirrored stone; \n'
                      'each step a loud wet slop as the mud condenses around your leather wrapped shoes...\n\n')
                print('A bright purple light flashes at the left corner of your vision. Holding firm for but a few \n'
                      'moments, it sets the ground ablaze outside of the newly singed, yet large red filigreed fabric \n'
                      'tent nearby. Slowly dissipating under the relentless clouds above, you now cautiously navigate \n'
                      'towards this structure; ducking periodically into the remaining tents. Reaching its entrance, \n'
                      'you peer in... \n\n')
                print(
                    'Instantly, a motionless vision captures your eyes. Two figures, huddled against a burning lantern, \n'
                    'cower at something behind you... Darkness overtakes this visage, and you hear the terrified sounds \n'
                    'of hurried movement in all directions.\n\n')
                print('Gradually returning, you blink rapidly. Before you, the same lantern lies rusty and decayed, \n'
                      'its blackened interior now holding a desperate, dying ember. Shivering at the sounds and sights \n'
                      'once heard you steel yourself in an attempt to regain composure. Guarding your eyes, you slowly \n'
                      'approach the decrepit lantern. Dancing in an incoherent pattern, the flame’s shape promptly \n'
                      'changes, a seated, tarnished copper medallion finally consuming its illuminated form. The \n'
                      'medallion clanks to the dirty floor as you witness this old relic’s last warm embrace...')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)

            else:
                return True

    if currentLoc == "Worker\'s Tent City Section(2)" and playerSelection != 'INVESTIGATE':
        print('\n---------------------------------------------------------------------------------------------------||')
        print('Gathering yourself, you walk back to your makeshift tent to pack up. Grabbing the fabric above, you \n'
              'drape it over your head and gear. Heading out into the rain, you work your way past the intermittent \n'
              'signs of life towards the broader section of tents called “living quarters”. Amongst the remaining, you \n'
              'notice a thick groove passing under many of the more violated structures; denoted by their dotted fabric \n'
              'of running yellow, red, and purple colors. Following the groove, you find it ends in an unexpected, yet \n'
              'hastily dug pit. \n\n')
        print(
            'Moving closer, a fowl stench permeates the rain, and you retch at the horrid sights and smells before you. \n'
            'Large piles of dirt and shattered wood lay mixed along the sides of this freshly filled bowl of discordantly \n'
            'colored soup. On top of this fetid liquid, a frothy mixture pathetically digs at the piles, leaving oily \n'
            'stains... and purple scarred obsidian. \n\n')
        print(
            'Pulling your gaze away, you exhale a shuttering breath and peer towards the North. In the distance, you \n'
            'see the canopies gradually pull away revealing a large field of muted emerald and white flowers...\n'
            'Though, protruding into the horizon, you see icons of death amongst them...')
        print(
            '-----------------------------------------------------------------------------------------------------||\n')
        sleep(2)

    elif currentLoc == "Worker\'s Tent City Section(2)" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print('\n-------------------------------------------------------------------------------------------||')
                print(
                    'Lightning cracks at the air above you and shatters the illusion of safety under the thin blankets \n'
                    'of fabric. Pulling the fabric closer, you shamble away from of the abhorrent pool as thunder rouses \n'
                    'another wave of fear within...\n\n')
                print('Lightly lifting your head, you look to the West. There, hidden behind a wall of white stoned \n'
                      'brickwork, you see the remainders of a makeshift kitchen emitting a dull, but apparent shine. Oddly \n'
                      'untouched by the rampant corruption, you move to take a closer look. Stepping around the pockets \n'
                      'of virulent liquid, you greet the shrouded kitchen with surprise as while under the massive trees \n'
                      'above, the rain has ceased to reach its ancient form. Smiling, you look around the scene with \n'
                      'amazement and wonder how any of this could still be here after so many years...')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)

            elif eachVal == 1:
                print('\n-------------------------------------------------------------------------------------------||')
                print('After considering the art and act of ransacking, you reassess your morally dubious efforts; \n'
                      'after all, carrying more in this weather, not to mention this environment, might prove... unwise.\n\n')
                print(
                    'Rising to your feet after digging through a cabinet, you rummage through a pocket on your right \n'
                    'side and pull out a piece of bread rolled in a fabric napkin. Gleefully, you shove it in your \n'
                    'mouth... and instantly regret it. Drier than ash, you lean outside the tent and open your mouth \n'
                    'to catch some rain. Soothing relief passes over you as you gulp it down and smile. Though, after \n'
                    'your quick break, you see something... miraculous.\n\n')
                print(
                    'To the West, a shimmering gateway of pearlescent stone dominates your perception. On either side \n'
                    'of this large, sturdy gate, you see sigils of the Great Gravestone Father himself carved and in \n'
                    'lain with deep emerald and black opal lines. Though white pumice outlines the artful grooves, \n'
                    'your eyes descend to a section near the bottom. On one side, a large hand print lays within one \n'
                    'domed indentation... Its appearance seemingly awaiting a key...')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)
            else:
                return True

    if currentLoc == "Logging Camp Section(1)" and playerSelection != 'INVESTIGATE':
        print('\n---------------------------------------------------------------------------------------------------||')
        print('Moving along a narrow, log lined pathway, your pace quickens as you approach a section of overgrown \n'
              'vegetation. Stepping over a few fallen branches, you duck under a fallen tree. As your hand stumbles, \n'
              'you feel its impossibly cold surface and an unbearable fear… though as your hand leaves, reality seems \n'
              'to return… Though, after raising the hand in question to your eyes, you notice a large set of stairs \n'
              'leading down to a nearby bridge beyond your fingers. Covered in the long-standing growth of lilacs and \n'
              'roses, you step around each pocket of floral pattern and inch closer to the bridge below. \n\n')
        print('Upon reaching the entrance, you carefully step across the ancient wooden planks… each step a cautious \n'
              'stare at oily reflective river coursing below large, dark wooden columns jutting deep into the earth \n'
              'below. Though the floral arrangement entices you to stick around, you reluctantly move forward towards \n'
              'a large workshop across a large, flat courtyard.\n\n')
        print(
            'Walking to its entrance, you sample your surroundings and peer to the North. There, a grove of familiar \n'
            'vegetative patterns overtake more steps nearby a collection young spruce trees that lie in beautifully \n'
            'bone white contrast to the remarkably dark surroundings.')
        print(
            '-----------------------------------------------------------------------------------------------------||\n')
        sleep(2)

    elif currentLoc == "Logging Camp Section(1)" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print('\n-------------------------------------------------------------------------------------------||')
                print('Digging into a nearby workstation, you look for signs of a hammer and nails. Hoping to board \n'
                      'yourself up here for the night, you pick through the remnants just in case that... creature... \n'
                      'comes back. Pulling your hands from the drawer, you move from each one to the next but suddenly \n'
                      'stop as a loud clang echoes out from beyond the back of the shop. Falling to a couched position, \n'
                      'you slowly move to the doorway and peer outside.\n\n')
                print('In the distance, in an alternating pattern, you notice lanterns have been hung up on various \n'
                      'trees… and one has fallen to a stone stand just below it. You brush a hand across your face... \n'
                      'and step outside. Quickly scanning the area, you move to check the now dented metal lantern \n'
                      'laying at an open pathway into the dense forest. Curiously, you look around and notice an oddity... \n'
                      'the distinct lack of logs guiding this opened pathway. \n'
                      'Instead, you witness a scene of brutality... \n')
                print(
                    'Trees matted with rusting, rotting axe heads lay behind makeshift barriers covered with skeletal \n'
                    'remains. Strew like puppets on sinewy strings, long dead victims lay shattered... \n'
                    'their bones like broken teeth along the tree’s bark.')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)

            elif eachVal == 1:
                print('\n-------------------------------------------------------------------------------------------||')
                print('Saddened and disgusted, you reach to the ground beneath your feet. As if in response to your \n'
                      'movement, a flower, one of glistening emerald-colored leaves and sapphiric blue pedals rises from \n'
                      'the dirt and into your hand. Standing up, you press its form into the nearest free and it implants \n'
                      'itself. Though as you do so, the carvings dancing across each tree’s surface in a wave of panic, \n'
                      'suddenly forming into individual arcs. Loud, sharp cracks erupt from their surface as sharp stoned \n'
                      'grins form across each tree’s breadth. \n\n'
                      'You hear a deathless legion of voices echo deep into your mind...\n')
                print(
                    '...WE MEAN YOU NO HARM YOUNG EARTHTAKER... UNLESS YOU WISH TO REPAY RETRIBUTION... WITH REVENGE...')
                print(
                    '---------------------------------------------------------------------------------------------||\n')
                sleep(2)

            else:
                return True

    if currentLoc == "Logging Camp Section(2)" and playerSelection != 'INVESTIGATE':
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------||')
        print(
            'Approaching the steps into the overgrown valley, you spot the growth of Brould Fruit under a makeshift cover. Slowly moving down the \n'
            'staircase carved into the valley’s steep decline, you find yourself at the cusp of a large brick and stone worked courtyard. Stepping \n'
            'into the courtyard, you walk along its ceramic spiral pattern until reaching a small set of stairs leading into a large garden. Carefully \n'
            'stepping down the time worn wooden steps, you find ornate planters of wood and brass dotting the insides of the garden. Approaching the \n'
            'Brould Fruit’s grove, you lean down to examine this deliciously tasting yet rare berry. Gliding your hands over their surface, you gently \n'
            'pull oval shaped seeds from within the fruit without damaging the skin. Sliding a hand over to your left pauldron, you drop the seeds into \n'
            'a cylindrical hole; it closes as you pull your hand away. Moving back out of the garden area, you step back into the large courtyard. \n'
            'Scanning your surroundings, you notice the center of the area is topped with a slab of chlorite; its unique layered green cascading \n'
            'monochromatic colors outwards in all directions. Walking over its center you hear a light echo but continue onward towards the opposite \n'
            'side of the courtyard near a small patch of spruce trees. Stepping over a ring of dark red brickwork, you step down another set of stairs \n'
            'and head in their direction...\n\n')
        print(
            'Thunder booms overhead. You look up to see a virulent storm rolling into the area; its sudden rainfall blankets the area in a muted sea green.')
        print(
            '------------------------------------------------------------------------------------------------------------------------------------||')
        sleep(2)

    elif currentLoc == "Logging Camp Section(2)" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'Harsh grinding noises erupt from the center of the courtyard as a large, spherical object comprised of frantically shifting stones \n'
                    'rises to the surface. Quickly replacing the chlorite surface, the object is a deep nephrite; particles of cerulean blue following \n'
                    'each stone’s shift. Following its rise, a distinct whine seems to carve through the persistent sounds of rain as you move worriedly \n'
                    'into cover. Along the sides of the brickwork, you drop into a prone position and huddle beneath the engraved rim.\n\n')

                print(
                    'In one rapid motion, this living weapon’s focal point opens a forward-facing surface and turns to face South. Like a demon, a loud \n'
                    'disharmonic roar erupts as it fires long shards of jagged stone screaming into the forest nearby. As if already predicting its \n'
                    'acquisition, the sulfuric beast answers in kind by firing back a volley of yellowed stone. With animalistic ferocity, the weapon \n'
                    'carves at the creature and its surroundings. Dodging underneath the oncoming barrage, you hear the sounds of sickness from within \n'
                    'the beast\'s gullet as the creature darts at the weapon again. Firing a net like membrane around the structure, its sickly, mucus \n'
                    'like form in contrast to the purple veins extruding from the sides of its jaw. Pumping a violent stream of volatile chemicals of \n'
                    'some vile rancid form into the weapon, the jellied cocktail ignites inside the net disabling the weapon. In one swift motion, the \n'
                    'creature rips the sphere from its floating carriage and devours it whole. As you witness its digestion, the creature’s undulating \n'
                    'muscles collapse the weapon’s form from within but not before it could fire one last shot. Carved out of the creature’s stomach, \n'
                    'you watch a trail of bruised liquid form as it runs away to lick its wounds. Though, out of the corner of your eye, you see the \n'
                    'weapon’s shard of stone cemented against the brickwork; inside its grasp, a ring of amethyst.')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')
                sleep(2)

            elif eachVal == 1:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'Panic and fear surges throughout your mind as you slowly rise from your hiding place. Lifting yourself up and out of the mud, you \n'
                    'shamble away towards the embrace of the spruce trees. Beyond them, you see a pathway heading East. Upon closer inspection, you \n'
                    'notice stone patterns implanted with and surrounded by a legion of decayed remains. At its center, a door soaked in dried blood \n'
                    'lies motionless over the carnage just beyond its exterior. However, on one side of its portcullis shielded door, there is one \n'
                    'indentation for a key of sorts.')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')
                sleep(2)

            else:
                return True

    if currentLoc == "Tree House" and playerSelection != 'INVESTIGATE':
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------||')
        if lastLocation == 'Logging Camp Section(2)':
            print(
                'Walking up to the door, you quickly check your surroundings before reaching into your pack to look at your collection of sigils.\n'
                'Finding the ring of amethyst, you place it deep within the indentation... and, with sound of a grinding gears... the door opens!\n'
                'Walking forward, you venture into a dark cavern. Moments later, you hear a quick hiss and groan as lanterns along the pathway \n'
                'softly illuminate the shadows within. Carefully stepping your way over sharp stone cliffs and down steep drop offs, you find yourself \n'
                'exiting a cave\'s mouth overlooking an enormous tree containing a weathered, yet remarkably engineered tree house. Looking over the \n'
                'edge of the cliff, you notice it\'s not too far off the ground and jump down to the bottom. As you land firmly against the dirt, you \n'
                'grunt and gather yourself to continue moving. However, as you look to your right, you see a staircase leading up to the cave\'s entrance that \n'
                'was hidden behind a veil of thick vegetation... you sigh...')

        elif lastLocation == 'Worker\'s Tent City Section(2)':
            print(
                'Walking over to the pearlescent stone door, you lay a hand upon the surface and grin. To be in the presence of such an incredible piece \n'
                'of history was a wonderful experience that you wouldn\'t soon forget. Reaching into your pack, you rummage through until you find an \n'
                'object matching the domed indentations; the tarnished copper medallion ought to work you think as you reach up and firmly plant it \n'
                'into the stone\'s surface. Suddenly, an emerald, green energy pulses through the lines of black opal and the door opens!\n'
                'Moving through the door frame, you approach a long corridor leading into a cave system descending downwards and outwards. \n'
                'Jauntily striding through the rising and falling inclines, you laugh and listen to the echoes reverberating off the lower cave walls. \n'
                'After some time, you find yourself reaching the end of a cave mouth that spills directly out onto flat ground. Before you, a massive \n'
                'tree who\'s trunk is five feet thick stands jutting into the sky like a beacon of nature. Moving around the its area, you look up its \n'
                'breadth to see a beautiful tree house, though aged terribly by the erratic weather of the area...')

        sleep(3)
        print(
            '\n\nMoving closer to the tree house, you find a makeshift latter implanted in the wooden surface of the colossal tree. You feel like a kid again; \n'
            'your feet barely fitting on the rungs as you, with quite some effort, climb the latter and ascend to the top of this curious house in the middle \n'
            'of nowhere. Reaching the top after a minute, you hit a small hatch with the sign, "No losr" halfway erased by wear and tear after many years of use. \n'
            'You chuckle and reach up to unhook the makeshift appendage keeping it shut; stepping up, you find yourself within a small antechamber. Looking over to \n'
            'the next door, your eyes connect with a faded drawing of a small white and brown dog... you hear the faint bark of a friend lost long ago...')
        print(
            '------------------------------------------------------------------------------------------------------------------------------------||')

    elif currentLoc == "Tree House" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'Smiling at the rough, childish designs, you scan the tree’s first interior area. In the distant corner, a large bed of straw lay ruined \n'
                    'by years of disrepair and disuse; its hollow form shattered by a fallen limb. Adjoining the broken bed, a small workbench strewn with even \n'
                    'smaller tools lay next to piles of sawed limbs and logs. Nearby, a modest sized wrought iron furnace lay at the opposite end of the area; \n'
                    'nearby conjoined cabinets of various sizes providing abundant means for storage. Spilling out of the nearest cabinet, a bundle of emptied \n'
                    'sacks lay under a broken cabinet door; their emaciated forms clearly having held some form of vegetable as shown by the dark stains of rot \n'
                    'blackening the bottoms. Under foot, the floor is a white wooded composite, its deeply scarred and pitted surface surprisingly holding firm \n'
                    'after many years. \n\n'

                    'Making one final scan of the room, you notice two notched columns and an old, but sturdy table. On the right side of the table, an engraved \n'
                    'sign hangs over a leather-bound booklet suffering from extreme wear and tear. Moving closer, you pick up the booklet as pieces under your \n'
                    'loose grip break and fall to the floor. You sifting through the pages finding various scribbles and drawing; while some seem familial \n'
                    'in nature, others seem... extremely brutal... Setting the book back on the table, you look to the sign above; it reads, \n'
                    '"Welcome Home Gaedra!"')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')
                sleep(2)

            elif eachVal == 1:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'Wiping the sweat from your brow with the tattered fabric, you look to the area next to the table. Taking notice of a notch in the \n'
                    'paneling, you reach around and pull outwards. Hearing a soft thump and whirl of a counterweight, the door pops open to a small sectioned \n'
                    'off tunnel. Squeezing through the small entrance, you look to the opposite side of the hidden compartment and notice a small door within this \n'
                    'incredibly cramped space. Though attempting to stand up in the confined space provides far more difficult, you managed to cram your large frame \n'
                    'in as you see a small lantern hanging at eye level. Slowly, but deliberately, you inch closer to the lantern, reaching to see if it has any fuel. \n'
                    'Popping open the small compartment, you don\'t find any fuel; however, you see a rock tied to a rope that leads through the entire lantern. \n'
                    'Considering your options, you shrug and simply pull at the lantern; a sudden click and a smaller door along the wall opens revealing two keyed \n'
                    'indentations. ')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')
                sleep(2)
            else:
                return True

    if currentLoc == "Forsaken Camp" and playerSelection != 'INVESTIGATE':
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------||')
        if lastLocation == 'Tree House':
            print(
                'Tugging at your pack, you push its rugged strap off and down onto the ground below. Slumping over, you smack your head on the door whilst \n'
                'reaching for sigils within. Wincing and groaning, you inch closer; pressing your face against the surface, you finally reach into the bag \n'
                'and grab the ring of amethyst and the tarnished copper medallion... Slowly raising your hand up to the smaller door, you reach forward to \n'
                'implant the items one. Unfortunately, due to the humid conditions within the terribly small chamber, the ring slips from your sweaty hand. \n'
                'Smacking against the wooden floor, you watch with bated breath as its tiny form dances around a small crack in the wood. Settling against \n'
                'the floor, you sigh and once again squeeze your body downwards, this time making sure to ...softly... press your head to the door\'s surface. \n'
                'Picking up the ring... one more time... you place it in the second indentation. Hearing a faint click, the door suddenly swings open to reveal \n'
                'a zipline into the gulch below. \n')

            print(
                'Squeezing through to the other side of the door, you stretch on a balcony overlooking an awe inspiring scene. Large sequoias running perpendicular \n'
                'to a wide, glistening river lay at the center of a gorgeous valley; though further North, you notice a large encampment. You realize however, \n'
                'that to reach it, you must use the zipline and a sigh of disbelief washes over you... Reluctantly, you place your leather bound shoe on one of \n'
                'the rungs and, after clicking a release lever on the right, your sent flying over the gargantuan forest... Laughing, you bellow out a cry of glee; \n'
                'though you quickly realizing your mistake, you find its far too late. Advancing towards you, the horrid creature pounds at the ground below; its \n'
                'violent gallops following the noises you so generously provided...\n')

            print(
                'Finally nearing the end of the zipline, you brace yourself for a quick entry; however, unannounced to you, the contraption above your \n'
                'head clicks as the handles drop sending you quietly contemplating into the river below. A loud, wide splash erupts as you smack into the \n'
                'water\'s surface; Moments later, your head pops out and you swim over to a weathered dock. Reaching the river\'s edge, you notice a thick fog \n'
                'has flooded the area, though its dubious form helps conceal your movement, it further complicates visibility. Taking a second to gather yourself, \n'
                'you walk up the terrain fumbling for a something in a small bag tied to your waist. Quickly hiding behind a raised embankment, you pull a polished \n'
                'blue stone, drop it to the stone below, and crush it underfoot. Gradually, thin water-like tendrils of blue outstretch themselves until hovering over \n'
                'your gear. Absorbing the water within the soaked fabric, the tendrils use their newly bloated form to deposit the water back into the river. \n'
                'Grinning, you take a moment to admire your brother\'s creation, but hastily resume movement to reach the nearby encampment.\n')

        print(
            'Nearing the ancient encampment, you see battered walls stretching far off into the foggy distance. At intervals along its breadth, \n'
            'oval shaped towers provide sentinel over the nearby docks and forest region. Though some towers are still topped with bowed weaponry, most lay shattered \n'
            'as a clear sign of defeat. Quickly, you move into past the gateway, through the main checkpoint, and into the camp\'s central courtyard. \n'
            'Hoping to find cover before the creature arrives, you seek shelter in a nearby garrison. Jumping through a burned portion of the exterior, \n'
            'you immediately take cover as the sounds of rapid fire movement approach.')

        print('------------------------------------------------------------------------------------------------------------------------------------||')

    elif currentLoc == "Forsaken Camp" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'You look West to see a terrifying sight; cages, strewn with black laced beige covering appear stacked high into the sky. Next to each \n'
                    'a spiral staircase of ice provides immediate interaction with each cage\'s entrance. At intervals along the ice, spikes of solid white \n'
                    'appear to emit a pulse of cold air somehow maintaining its frozen state.\n\n'

                    'You look South, but only see the rivers contained within a vast valley of trees and wild overgrowth. Taking over the majority of your \n'
                    'perception, you can see the face of a colossal mountain, near its summit, a large Tree House lays in patient observation.')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')

            elif eachVal == 1:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'Moving inside the building, you are careful not to make a sound. You flinch suddenly as the creature dives through a nearby structure; '
                    'you hear the clang and sting of long rusted armor and weaponry shattered under its immense size. Firing a sudden volley of yellowed stone '
                    'into nearby building, it dashes into its interior but is instantly repulsed as a sonic boom detonates within. Cracking a door overlooking '
                    'the obliterated structure, you see a small orb of condensed, violent air. Jittery and unstable, it pulses again... however, this time... '
                    'the pulse lifts up the particles from the dirt in a sweeping motion. Sending it in all directions, it catches the door in front of you '
                    'and falls on your armor. As its particles gracefully flow over your right pauldron, it slowly retracts and the orb dissipates into a '
                    'star of carnelian laced with lightly colored orpiment embedded within an iron cage.')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')

            else:
                return True

    if currentLoc == "Underground Entrance" and playerSelection != 'INVESTIGATE':
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------||')
        print(
            'Just outside of the raging storm damaged lands, a large mossy structure lays dug into the ground; its exterior dripping wet from the '
            'recent rain storm passing through. Appearing as a giant half circle carved into the ground, you notice its brick exterior has struggled to '
            'keep its form as periodic whipping winds have stolen them over time. Scarred and time worn, much of the exterior has been forced to regrow.')
        print(
            '------------------------------------------------------------------------------------------------------------------------------------||')

    else:
        return True

    if currentLoc == 'Makeshift Slave Quarters Section(1)' and playerSelection != 'INVESTIGATE':
        print('\n----------------------------------------------------------------------------------------------------------------------------------||')
        print('Describe Makeshift Slave Quarters Section(1)')
        print('------------------------------------------------------------------------------------------------------------------------------------||')

    elif currentLoc == "Makeshift Slave Quarters Section(1)" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('Look North')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')

            elif eachVal == 1:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('Look East')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')
            else:
                return True

    if currentLoc == "Makeshift Slave Quarters Section(2)" and playerSelection != 'INVESTIGATE':
        print('\n----------------------------------------------------------------------------------------------------------------------------------||')
        print('Describe Makeshift Slave Quarters Section(2)')
        print('------------------------------------------------------------------------------------------------------------------------------------||')

    elif currentLoc == "Makeshift Slave Quarters Section(2)" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print('\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('You look South.')
                print('------------------------------------------------------------------------------------------------------------------------------------||')

            elif eachVal == 1:
                print('\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('You look East.')
                print('------------------------------------------------------------------------------------------------------------------------------------||')

            elif eachVal == 2:
                print('\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('You find the Fear Sigil.')
                print('------------------------------------------------------------------------------------------------------------------------------------||')
            else:
                return True

    if currentLoc == "Den of The Blind" and playerSelection != 'INVESTIGATE':
        print('\n----------------------------------------------------------------------------------------------------------------------------------||')
        print('You reach the Den of the Blind, its interior a vastly different environment from what you have seen thus far. Impacted from ceiling to floor \n'
            'lay thousands of skeletal structures. Bones of all manner of sizes lay in complex patterns, however, each appears to have congealed after years \n'
            'of water having washed into its decrepit pits. Deeper into its bowels, acidic growth forms large gullies of brightly colored yellow stone.')
        print('------------------------------------------------------------------------------------------------------------------------------------||')

    elif currentLoc == "Den of The Blind" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print('\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('Looking West, you see the remaining slave quarters; their appearance deeply unsettling, and truly depressive.')
                print('------------------------------------------------------------------------------------------------------------------------------------||')

            elif eachVal == 1:
                print('\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('You find a Secret Passage East. You see three indentations in a triangular pattern over an oval of black stone.')
                print('------------------------------------------------------------------------------------------------------------------------------------||')

            elif eachVal == 2:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'Carefully walking over the bridges of marred stone, you look to a island jutting into a deep section of the yellowed liquid lagoon. \n'
                    'Beyond its pitted surface, stalagtights appear as razor sharp teeth over a bright blue, tear drop shaped medallion flashing white in the \n'
                    'distance.')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')
            else:
                return True

    if currentLoc == "Splinter Gardens Section(1)" and playerSelection != 'INVESTIGATE':
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------||')
        print(
            'The clouds above clash with furious rage as you move further from the mired, noxious pools of dark liquid. The closer you draw to the \n'
            'plains beyond, the more diabolical its lightning strikes become. A sudden strike sends bolts of electricity scorching through a nearby \n'
            'tree, its surface instantly lit ablaze, but gradually smothered by the intense rain. Reaching the immediate threshold of the plains, \n'
            'you stare vacantly at the intense scene. Colossal columns of wind ravage the lands, splicing logs into spears in a matter of seconds as \n'
            'they splinter the ground with their natural ferocity. Ducking into a nearby hill cavity, you narrowly miss the high velocity impact of a \n'
            'large slab of stone as it slams into the hill behind you. Looking over the ridge, you examine the plain of desolation and destruction, \n'
            'its surface still deeply scarred by the uncontrollable desire for power long unchecked and dubiously unrivaled. \n\n'

            'Dashing out of the hillside, you run for the nearby tree line. Closer and closer, you bolt to the makeshift barricade carved from hastily \n'
            'cut down trees. Diving into cover, your heart rate intensifies as a large bundle of tree limbs barrels past you and pins itself into the \n'
            'perimeter\’s trees. ')
        print(
            '------------------------------------------------------------------------------------------------------------------------------------||')

    elif currentLoc == "Splinter Gardens Section(1)" and playerSelection == 'INVESTIGATE':
        for eachVal in args:

            if eachVal == 0:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'You look North and see a safe haven; a tunnel digging deep into the surface, surrounded by fields of whipped structures. '
                    'You look East and see more of the horrid conditions within these war torn lands. Though, upon closer inspection, you notice a brief '
                    'window of calmness closer to its end.')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')

            elif eachVal == 1:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print(
                    'Moving closer to the center, you lurch forward from around the barrier and dash again towards one closer to the enraged twister. Damage \n'
                    'marking wars of attrition stain the mismatched patches of areas of dried grass and scorched trees lying scattered across its surface. \n'
                    'Spikes of large, white stone blanket the area in randomized patterns; their shapes and colors alike shafts of faded, yet bloodied quartz. \n'
                    'Caking the special few, dried red smears lay deeply stained along its surface; nearby, graveyard\’s worth of bones lay in inconsistent, \n'
                    'yet shattered piles. Though picked clean of their flesh, the bodies have been sucked into these icons of death; their bones protruding \n'
                    'in horror. However, buried deep within the nearby crystalline statue, you see the remains of warrior clad in armor of rigid composition. \n'
                    'The individual appears mid war cry, but how he was not devastated by the impact of the stone, you cannot determine...\n')

                print(
                    'Nearby, you notice a shiny object hanging from a rusted weapon deeply impacted in the dirt. Though the wind around you howls, you try to \n'
                    'focus on its form. Squinting, you notice a band of red jasper, its small banners of cuprite swing furiously in the torrential wind, each \n'
                    'inscribed with black writing that glistens under the downpour. ')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')

            else:
                return True

    if currentLoc == "Splinter Gardens Section(2)" and playerSelection != 'INVESTIGATE':
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------||')
        print(
            'You work your way past the lethal winds of the nearby storm into another area of ravaged grounds. Though the dark skies have started to '
            'fade, you can still feel a frigid wind piercing your flesh beneath your armored carapace. However, looking to the North, you feel a sense '
            'of safety and security as looking past the blizzard like conditions, you notice a massive castle in the distance.')
        print(
            '------------------------------------------------------------------------------------------------------------------------------------||')

    else:
        return True

    if currentLoc == "Gravestone Father\'s Fortress" and playerSelection != 'INVESTIGATE':
        print(
            '\n----------------------------------------------------------------------------------------------------------------------------------||')
        print(
            'Crossing over from the war torn and weathered fields, you find yourself before a might fortress of stone. Large causways before its \n'
            'gargantuan walls create long stretches of ornate dark emerald and pearlescent stone. Nearby, fortified by colossal walls of rosewood, \n'
            'large braces of granite hold the causways aloft over an enormous patch of bioluminescent vegetation strewn along the edges of these \n'
            'roadways. Walking towards the main entrance, you notice large vines crawling up and down an interwoven mesh contiuting the gate\'s \n'
            'main structure. On either side of the battered gate, you can see mounds of stone and wood; each topped with flowing fountains of crystal clear \n'
            'water.')
        print(
            '------------------------------------------------------------------------------------------------------------------------------------||')

    elif currentLoc == "Gravestone Father\'s Fortress" and playerSelection == 'INVESTIGATE':
        for eachVal in args:
            if eachVal == 0:
                print(
                    '\n----------------------------------------------------------------------------------------------------------------------------------||')
                print('Look South & Find Door.')
                print(
                    '------------------------------------------------------------------------------------------------------------------------------------||')

            else:
                return True


# Pause Function
def pause():
    # Call to global game state and player selection
    global game_state
    global playerSelection

    # SET game to "off"
    game_state = 0

    # Text to show user game is "paused"
    print('Paused')
    sleep(1)

    # Grab user input
    user_msg = input('Ready to return? -> Y / N <- ')

    # WHILE game_state is zero or user message is N.
    while game_state == 0 or user_msg.upper() != 'Y':
        # investigate
        # Handle if user inputs Y to return to game; if Y, then reset player input to nothing.
        if user_msg.upper() == 'Y':
            game_state = 1
            playerSelection = ''
            return

        # Handle if user inputs incorrect value.
        elif user_msg.upper() != 'N':
            print('Incorrect Value -> {}. Please Input: Y / N.\n'.format(user_msg))
            continue


# End Function for end of game.
def endSequence(inv, move_opt):
    # GET Global variables
    global currentLocation
    global playerSelection
    global endOfGame

    # SET Default value for Death Counter
    deathCounter = 0

    # SET combination for combination lock.
    combination = ['STRENGTH', 'GREED', 'FEAR', 'REGRET', 'FURY', 'DEPRESSION', 'SALVATION']

    # Set End of Game global to True to enable HELP function showing combination format.
    endOfGame = True

    # End condition start
    if currentLocation == 'Gravestone Father\'s Fortress':

        # IF player has all 7 items in the game.
        while len(inv) == 7:

            # IF player reaches 3 death counters, then loss condition met.
            if deathCounter == 3:
                print('||==================================================================================================||')
                print('In your frustration, you slam a sigil into the battle-damaged gateway and roar at its preventative \n'
                      'measures keeping you from reaching the inner section of the mighty fortress. Your fists pound into \n'
                      'the white-stone-shaped shields in lain within the dark wooden panels of the once besieged doors. \n'
                      'Fury turns to malice as malice turns to carnivorous rage; each second, the hatred within you combusts \n'
                      'into a primordial rage. One blow after another, you hear the gradually growing sounds of cracking; \n'
                      'the air detonating through the sheer force of impact... \n\n')
                sleep(3)
                print('The door’s armor-plating buckles and snaps for the last time as a massive stone hand hit you with \n'
                      'enough force to lift you off the ground and pin you to the fortress’ walls. Without warning, it \n'
                      'launches yet another gargantuan fist into you; its velocity blowing a crater of dust away in all \n'
                      'directions. Your skull splinters into a paste against the siege-ready barriers… your lifeless corpse \n'
                      'drops to the dirt below; your last moments nothing but utterly total excruciating pain. You add yet \n'
                      'another stain to the colossal walls before the Gravestone Father’s Fortress...\n\n')
                sleep(3)
                print('Slumped over, the rapid movement of a creature bounds forward… its slender form bouncing between its \n'
                      'quadrupedal gaits. Closing the distance between it, the guardians, and you... it fires an accelerated \n'
                      'burst of yellowed stone as it tosses its full weight into a body slam. Crushing into the guardian, \n'
                      'it whips itself off of the befallen figure and lifts your corpse into its mouth. The second stone \n'
                      'guardian lifts its hand downwards and catapults a massive boulder towards the creature, but its \n'
                      'agility far outmatches the lumber giant’s form... \n\n')
                sleep(3)
                print('Your carcass is pulled into a pit of decrepit liquid… though, suddenly... you awake within... gulping down \n'
                      'its noxious ichor. Rising from the pool, you feel an instant state of dread… as you pull your hands \n'
                      'up and see your bruised flesh covered in purple scarred obsidian. A malicious voice turns your body \n'
                      'against you as you feel the putrid intoxication of The Shadow’s Will take over... \n\n')
                print('…RESURRECTION COMES AT A PRICE… AND I’VE COME TO COLLECT…')
                print('||==================================================================================================||')
                exit()

            # Start the end mini-game.
            print('||========================================================||')
            print('Place the Sigils upon the Gate in the correct order:')
            user_input = input().strip().upper()
            print('||========================================================||\n')

            # Handle if the user inputs a movement option; simply make them exit from the door interaction.
            if user_input in move_opt:
                user_input = 'EXIT'

            # Split user input from csv to list.
            userList = user_input.split(' ')

            # IF player input is EXIT, then return to main game loop.
            if user_input == 'EXIT':
                print('\n||====================================================================||')
                print('You\'re right... it might be time to take a step back and think...')
                print('||====================================================================||\n')
                playerSelection = ''

                # Set end of game back to false so user cannot see sigil format suggestion in the help function.
                endOfGame = False
                break

            if user_input == 'HELP':
                print('||==================================================================================================||')
                print('You feel a foreboding, malicious voice carve into you... its deeply apathetic, yet \n'
                      'apotheotic tone a cacophonous roar as it boils you alive in a roil of chaotic energies... ')
                print('||==================================================================================================||\n\n')
                sleep(3)
                print('||==================================================================================================||')
                print('Against the malevolent voice, a sudden, virtuous surge of energy strikes at the gathering void from \n'
                      'beyond a veil; its decisive lethality sheering away the encroaching darkness...\n'
                      'In a flurry of elemental combination, an orb of rapidly changing matter appears before you...\n'
                      'Looking closer, you hear calm, ethereal chanting...\n\n'
                      'They who\'s fury is beyond tectonic...\n'
                      'They who\'s retribution is deeper than the Abyss...\n'
                      'They who\'s volcanic anger is more potent than Olympus Mons...\n'
                      'They who\'s cyclonic temper scattered the stars...\n\n'
                      'Under these I find my charge!\n\n'
                      '...Find the help you need...')
                print('||==================================================================================================||')
                sleep(3)

                # Call Help Player Function, but have it return to end sequence.
                help_player(inv)
                continue

            # IF player input matches the correct door combination, then win condition met.
            if userList == combination:
                print('||==================================================================================================||')
                print('Placing the last sigil, you step back. Suddenly, two massive sets of stone armored hands reach up \n'
                      'from the ground on either side of you. Pushing hard against the dirt, two wooden golems rise to a \n'
                      'colossal stature. Staring down at you with expressionless masks of ancient form, they reach to the \n'
                      'massive iron rungs on each side of the door and pull. A smile creeps across your face as you stride \n'
                      'into the great fortress of Gaedra, the Gravestone Father...\n\n')
                sleep(4)
                print('Inside, you witness the aged, but immaculate architecture. Large courtyards of incredible design \n'
                      'stretch out and around ornate gardens of stunning composition. Stretched between large column, \n'
                      'beautifully blue and yellow bioluminescent vines shine a dazzling luminance providing safe passage \n'
                      'into the inner courtyard. Walking along their breadth, you reach a tower near the inner keep. Climbing \n'
                      'its wide and grandiose staircase, you reach a large antechamber overlooking the gateway below. As you \n'
                      'step into the antechamber, your overt sense of wonder wavers...\n\n')
                sleep(5)
                print('A large lake, seemingly hovering above, is wrapped in a massive veil of clear crystal. Upon closer \n'
                      'inspection though, you can see at its center, a violent and unstable object. A pylon of dark form \n'
                      'lays embedded deep crystal-clear lake’s bottom; its form transmuting incoming water and spewing out \n'
                      'a vile concoction of searing black liquid that rots at the floor below. A sudden sound of cracking \n'
                      'stone tears your attention away as you rush to the large balcony nearby to see the creature fighting \n'
                      'the golems at the gate’s entrance. Ready to end this charade, you prepare to jump off the balcony \n'
                      'and meet the creature below... \n\n')
                sleep(5)
                print('As you do, one of the golems lifts a massive rod of stone from the earth. In one momentous arc, \n'
                      'the column cracks into the creature with a booming force. Knocked down, you watch the golem move \n'
                      'to intercept its malicious foe as it lifts the vile creature up. Squirming and gnashing at its \n'
                      'sides, it almost breaks free as the second golem grabs its head and pulps it beneath its colossal \n'
                      'hands.\n\n')
                sleep(4)
                print('As the creature’s corpse topples to the dirt... an aetheric cry detonates from within. Agony erupts \n'
                      'within your mind as the very environment around you shakes with a violent current of condensed air. \n'
                      'Rising louder and louder, the screech begins to vibrate as the second golem steps back and places a \n'
                      'hand over the ground. Gradually, a massive dome of white stone erupts forth. Grabbing its wide berth \n'
                      'with both hands, it slams the vault down onto of the body. Though the cry dies down, moments later, a \n'
                      'phenomenally loud, bone crushing boom echoes in all directions and the air once again grows silent.\n\n')
                sleep(5)
                print('Though you now cry in victory, this jubilation is cut short as you hear a faint booming echo from \n'
                      'behind you. Swiftly turning, you look up to see the black liquid drain from the lake above. \n'
                      'However, as it descends, its form lurches for you. Blanketing your surroundings, it begins to \n'
                      'ignite the air in one last ditch effort… but is quickly cut short by the torrential waterspout \n'
                      'above. Dodging out of the way, you gather yourself and watch as the darkness subsides and is erased \n'
                      'from this plane. Victory has been achieved, Long Live the Great Gravestone Father!')
                print('||==================================================================================================||')
                quit()

            elif userList != combination and user_input != 'EXIT' or user_input != 'HELP':
                # IF player input does not match the correct door combination, then add one to the death counter.
                deathCounter += 1
                print('\n||===========================================================||')
                print('Careful... you can feel the rage building within... {} of 3'.format(deathCounter))
                print('||=============================================================||\n')

        else:
            print('||==================================================================================================||')
            print('The door stands as a silent guardian over you, its form a bastion of both strength, fortitude, and \n'
                  'resilience. Try as you might, you try to open its colossal gates, but nothing happens.')
            print('||==================================================================================================||')
            playerSelection = ''


# Function to check inventory for secret passages.
def getInventorySecretPassage(inv, args):
    # Create temporary list to hold current inventory.
    tmpList = []

    # For each item in the inventory, place it in a temporary list to compare against.
    for eachItem in range(len(inv)):
        tmpList.append(str(inv[eachItem]).upper())

    # Check if all elements in both lists match; if all elements match, return true, if not, false.
    if all(item in tmpList for item in args):
        return True
    else:
        return False


# Function to Check for Secret Passages.
def checkSecretPassages(playerSelect, locationsList, inv):
    # Get global current location
    global currentLocation
    global lastLocation

    # SET boolean default return value.
    canTravel = False

    # Create Lists containing "keys" required to open secret passages.
    blindDen = ['SALVATION', 'FEAR', 'FURY']
    logCamp2 = ['DEPRESSION']
    workTentCity2 = ['REGRET']
    treeHouse = ['DEPRESSION', 'REGRET']

    # Check for Secret Passages.
    for eachLoc in locationsList:

        # IF current location matches the iteration location value.
        if eachLoc == currentLocation:

            # CHECK each location option; find location's secret passage value.
            for movement in locationsList[eachLoc]:

                # IF location option SECRET is found.
                if movement.count('SECRET') == 1:

                    # Split dictionary option into 2 fields, set movement to the 2 value;
                    # this will always be a cardinal direction.
                    tmpList = movement.split(' ')
                    movement = tmpList[1]

                    # IF the player input matches the SECRET split value.
                    if playerSelect == movement:

                        # Enable Secret EAST Passage to Fortress if player has items: Salvation, Fear, Fury.
                        if currentLocation == 'Den of The Blind':

                            # Call to function to check if player can go through secret passage; return boolean.
                            canTravel = getInventorySecretPassage(inv, blindDen)

                            # IF True, set new location.
                            if canTravel:
                                lastLocation = currentLocation
                                currentLocation = 'Gravestone Father\'s Fortress'

                            # Return boolean and SECRET split value.
                            return canTravel, movement

                        # Enable Secret EAST Passage to Tree House if player has item: Depression.
                        elif currentLocation == 'Logging Camp Section(2)':

                            # Call to function to check if player can go through secret passage; return boolean.
                            canTravel = getInventorySecretPassage(inv, logCamp2)

                            # IF True, set new location.
                            if canTravel:
                                lastLocation = currentLocation
                                currentLocation = 'Tree House'

                            # Return boolean and SECRET split value.
                            return canTravel, movement

                        # Enable Secret WEST Passage to Tree House if player has item: Regret.
                        elif currentLocation == 'Worker\'s Tent City Section(2)':

                            # Call to function to check if player can go through secret passage; return boolean.
                            canTravel = getInventorySecretPassage(inv, workTentCity2)

                            # IF True, set new location.
                            if canTravel:
                                lastLocation = currentLocation
                                currentLocation = 'Tree House'

                            # Return boolean and SECRET split value.
                            return canTravel, movement

                        # Enable Secret NORTH Passage to Forsaken Camp if player has items: Depression & Regret.
                        elif currentLocation == 'Tree House':

                            # Call to function to check if player can go through secret passage; return boolean.
                            canTravel = getInventorySecretPassage(inv, treeHouse)

                            # IF True, set new location.
                            if canTravel:
                                lastLocation = currentLocation
                                currentLocation = 'Forsaken Camp'

                            # Return boolean and SECRET split value.
                            return canTravel, movement

                    # Else return False Boolean value and split value.
                    else:
                        # Return boolean and SECRET split value.
                        return canTravel, movement


# Function allowing player to move throughout the world.
def move_direction(playSelection, locationsList, inv):
    # Call to Global Current Location value.
    global currentLocation
    global lastLocation

    # SET default values for secret travel access and text back to player via direction and current location.
    canTravelSecret = False
    direction = ''

    # Create List containing Secret Passage Locations.
    secretPathwayLocations = ['Den of The Blind', 'Logging Camp Section(2)',
                              'Worker\'s Tent City Section(2)', 'Tree House']

    # Check if current location is a secret pathway location.
    if currentLocation in secretPathwayLocations:
        # Call to secret passage checker and see if the player has the correct inventory values.
        canTravelSecret, direction = checkSecretPassages(playSelection, locationsList, inv)

    # for each key in dictionary locations, get its sub-dictionary key.
    for eachLocation in locationsList:

        # IF the current location matches that within the list of locations.
        if eachLocation == currentLocation:

            # for each key (movement capability) inside each location.
            for movement in locationsList[eachLocation]:

                # IF boolean returns true, then set player input back to nothing and display their movement.
                if canTravelSecret:
                    print('\nYou\'ve taken a secret passage {} to the {}!'
                          .format(direction, currentLocation))

                    # Show player location text based on newly set location.
                    get_current_location_text(currentLocation)

                    # SET player input back to nothing and return out of this function.
                    playSelection = ''
                    return playSelection

                # If the movement capability is found as a value equal to what the player input, then
                # set current, set player input back to nothing, then display their movement.
                elif playSelection == movement:
                    print('\nYou\'ve moved {} to the {}.'.format(playSelection,
                                                                 locationsList[eachLocation][movement]))

                    lastLocation = currentLocation
                    currentLocation = locationsList[eachLocation][movement]

                    # Show player location text based on newly set location.
                    get_current_location_text(currentLocation)

                    # SET player input back to nothing and return out of this function.
                    playSelection = ''
                    return playSelection

                # IF player input movement is not in the list of location's movements.
                elif playSelection not in locationsList[eachLocation]:

                    # Special case for location Underground Entrance.
                    if playSelection == 'SOUTH' and currentLocation == 'Underground Entrance':
                        print('------------------------------------------------------------------------------------||')
                        print('Walking down through the cavern below, the ruined staircase\'s remains lie scattered\n'
                              'at your feet; each footfall a loud crunch and subsequent echo.\n\n'
                              'Suddenly, the light cascading down the steps begins to dim...\n\n'
                              'Turning around, you catch the last glimpse of light as \n'
                              'the horizon disappears behind a veil of impossibly black air covering the entrance.\n'
                              'A light stream of pebbles begins to fall as this chunk of foul air slams into the\n'
                              'door\'s threshold; desperate and bone-chilling wails echo into the new darkness\n'
                              'surrounding you. Holding up a makeshift lantern containing bioluminescent plants,\n'
                              'you watch as a maw of grinding stone tears at the entrance. A trap has been sprung.\n\n'
                              'Unable to turn back... you panic under the ear splitting cacophony, but quickly\n'
                              'begin to lose its howling sound as a voice echos in your mind...')
                        print('-----------------------------------------------------------------------------'
                              '-------||\n')
                        print('\n-----------------------------------------------------------------------'
                              '-------------||')
                        print('...Seek Salvation and you will find a Fear that binds it and a Fury to keep it alive...')
                        print('--------------------------------------------------------------------'
                              '---------------||\n')

                        # Reset Player input.
                        playSelection = ''
                        return playSelection

                    # Special Case for location Jagged Cliffs.
                    if playSelection == 'SOUTH' and currentLocation == 'Jagged Cliffs':
                        print('\n--------------------------------------------------------------------------------'
                              '----||')
                        print('Approaching the edge of the cliff, you once again smell the bloated stench of decay...\n'
                              'Though your mind begins to flood, you are met with a sense of righteousness...\n'
                              'Quickly, the repulsive odor is replaced... an alluring, floral odor calms the\n'
                              'cacophony of your mind...\n')
                        print('...It\'s only one more step...')
                        print('---------------------------------------------------------------------------------'
                              '---||\n')
                        sleep(2)
                        print('DON\'T DO THIS... PLEASE... NO! DON\'T!\n')
                        sleep(3)
                        print('As the muggy, slow breeze swiftly turns ferocious...\n'
                              'your eyes open to their last moments\n'
                              'before colliding with a dull crunch against '
                              'the pile of rotting flesh at the cliff\'s bottom...\n')
                        quit()
                    else:
                        # Handle player input location if it is neither a secret location, valid location, or special
                        # case.
                        print('\nGetting lost here isn\'t an option... {} is not a choice.'.format(playSelection))
                        playSelection = ''
                        sleep(1)
                        return playSelection


# Function that allows the player to investigate an area to retrieve the item.
def playerInvestigate(locList):
    # Call to global variables' player selection and current location investigation counter.
    global playerSelection
    global currentLocationInvestigationCounter

    # SET location counter as the end location counter in its location.
    endLocCounter = True

    # GET the current location's counter, return it as an int.
    locCounter = getCurrentLocationInvestigationCounter(locList)

    # IF the current location's counter is not greater than 3; there are between 1 and 3 options per area.
    if locCounter < 3:

        # GET the location's investigation text based on how many investigations have occurred.
        endLocCounter = get_current_location_text(currentLocation, locCounter)

        # IF the location still has more investigation encounters.
        if not endLocCounter:

            # For each location (investigate) in the locList (List of Locations).
            for investigate in locList:

                # IF the location is equal to the current location.
                if investigate == currentLocation:

                    # for each value inside the location.
                    for investigateCounter in locList[investigate]:

                        # IF the value is Investigated.
                        if investigateCounter == 'Investigated':
                            # Increase the investigation counter by 1.
                            locList[investigate][investigateCounter] += 1

                            # SET the global location counter equal to this new value.
                            currentLocationInvestigationCounter = locList[investigate][investigateCounter]

            # SET player input back to nothing and return out of this function.
            playerSelection = ''
            return

        # ELSE IF the location does not have any more investigation encounters.
        elif endLocCounter:
            print('\n---------------------------------------------------------------------------'
                  '---------||')
            print('...You find there is nothing left to investigate...')
            print('---------------------------------------------------------------------'
                  '---------------||\n')
            sleep(3)

            # SET player input back to nothing and return out of this function.
            playerSelection = ''
            return

    # ELSE IF the location has more than 3 investigation counters on it.
    elif endLocCounter:
        print('\n---------------------------------------------------------------------------'
              '---------||')
        print('...You find there is nothing left to investigate...')
        print('---------------------------------------------------------------------'
              '---------------||\n')
        sleep(3)

        # SET player input back to nothing and return out of this function.
        playerSelection = ''
        return


# Function to get the current location's investigation counter.
def getCurrentLocationInvestigationCounter(locList):
    # For each location in the list of locations.
    for investigate in locList:

        # IF the location equals the current location.
        if investigate == currentLocation:

            # For each of the location values within the location iteration
            for investigateCounter in locList[investigate]:

                # IF the location has the value of investigated.
                if investigateCounter == 'Investigated':
                    # SET the investigated count to this value.
                    investigateCount = locList[investigate][investigateCounter]

                    # RETURN the value back.
                    return investigateCount


# Function to check if the player has investigated the area enough to grab the item within that location.
def checkInvestigate(locationsList):
    # Grab current location global value; SET ability to grab item to false; function should handle this.
    global currentLocation
    grabItem = False

    # SET Required Investigation Counter to default value.
    requiredInvCounter = 1

    # Call to Get current location investigation counter and bring back it's # of investigations.
    investigateCount = getCurrentLocationInvestigationCounter(locationsList)

    # For each location in the list of locations.
    for investigate in locationsList:

        # IF the location equals the current location.
        if investigate == currentLocation:

            # For each of the location values within the location iteration
            for investigateCounter in locationsList[investigate]:

                # IF the location has a value of required investigation number.
                if investigateCounter == 'Required Investigate #':
                    # SET the required inventory counter equal to the value found in the dictionary.
                    requiredInvCounter = locationsList[investigate][investigateCounter]
                    break

    # IF the location's investigation count equals it's required investigation counter, then
    # allow the player to grab the item.
    if investigateCount >= requiredInvCounter:
        grabItem = True

    # RETURN the boolean value
    return grabItem


# Function to help player by displaying options, current location, and current inventory.
def help_player(inv):
    # Call to global variables
    global currentLocation
    global playerSelection
    global game_state
    global endOfGame

    # SET player selection back to nothing.
    playerSelection = ''

    # Display movement options, current location, and current inventory for player.
    print('\n||=========================================================================================||')
    print('|| Movement Controls: North, South, East, West                                             ||')
    print('|| Additional Actions: Help <-(Shows Inventory), Pause, Investigate, Retrieve              ||')
    print('||=========================================================================================||\n')

    print('You are currently located at the >--[{}]--<.\n'.format(currentLocation))

    print('=[]=Inventory=[]=')
    for eachItem in inv:
        tmp = '=||) Sigil - ' + ''.join(eachItem)
        print(tmp)
    print('=[]===========[]=\n')

    if endOfGame:
        print('Sigils Format: Greed Salvation')

    # SET game_state to 0 to mimic pause, then call to pause function.
    game_state = 0
    pause()

    # Return the reset player input.
    return playerSelection


# Function to retrieve item from Location
def item_retrieve(locationsList):
    # Grab global variables inventory and player selection
    global inventory
    global playerSelection

    # Set player selection back to nothing.
    playerSelection = ''

    # For each dictionary key location value.
    for eachLocation in locationsList:

        # IF the current location matches the current iteration location value.
        if eachLocation == currentLocation:

            # For each value within the current location iteration value.
            for itemKey in locationsList[eachLocation]:

                # IF Check to see that the current location iteration value is an item.
                if itemKey == 'Item':

                    # IF Check to see that the item value is not NONE.
                    if locationsList[eachLocation][itemKey] != 'NONE':

                        # IF Check to see if the player has the item in their inventory already.
                        if inventory.count(locationsList[eachLocation][itemKey]) == 0:

                            # Check whether player can retrieve item or not based on how many
                            # times they have investigated; returns boolean value.
                            grabItem = checkInvestigate(locationsList)

                            # IF returned boolean value is true; show player what they acquired
                            # and add item to their inventory.
                            if grabItem:
                                if len(inventory) != 6:
                                    print('\nSigil of {} Acquired... '.format(locationsList[eachLocation][itemKey]))
                                    return inventory.append(locationsList[eachLocation][itemKey])
                                else:
                                    print('\nSigil of {} Acquired... \n\n'
                                          '             ...Let\'s hope this is enough...'.format(
                                            locationsList[eachLocation][itemKey]))
                                    return inventory.append(locationsList[eachLocation][itemKey])

                            # Handle if they have not investigated the area per its required number of investigations
                            else:
                                print('\nYou can\'t seem to find anything...')

                        # Handle if player already has the item in their inventory.
                        else:
                            return print('\nYou have already retrieved Sigil - {}.'
                                         .format(locationsList[eachLocation][itemKey])), playerSelection

                    # Handle if the location does not have an item.
                    elif locationsList[eachLocation][itemKey] == 'NONE':
                        print('\nYou can\'t seem to find anything...')
                        sleep(3)
                        return playerSelection


# Function to check if the player input is a valid input.
def checkUserInput(playerSelect):
    # Set boolean to false; this function should check if the value is valid.
    isValid = False

    # Create dictionary of valid values.
    available_selection = {'OPTIONS': {'NORTH', 'SOUTH', 'EAST', 'WEST',
                                       'HELP', 'PAUSE', 'INVESTIGATE', 'RETRIEVE', 'OPEN'}}

    # IF the player input can be found amongst the dictionary of valid values, then return boolean value of true.
    for val in available_selection.values():
        if playerSelect in val:
            isValid = True

    return isValid


# SET Global Variables
currentLocation = 'Corroded Wagon'
lastLocation = ''
currentLocationInvestigationCounter = 0
inventory = []
playerSelection = ''
game_state = 0
endOfGame = False


# Start of Game
def main():
    # GET User Input (Display Game Intro Text).
    game_start = input('-------------------------\n'
                       '                         \n'
                       'S T I C K S & S T O N E S\n'
                       '                         \n'
                       '-------------------------\n'
                       '    A Production by      \n'
                       'Elements Of Entertainment\n'
                       '-------------------------\n'
                       '                         \n'
                       '-------------------------\n'
                       '    ...Start Game...     \n'
                       '           Y/N           \n'
                       '-------------------------\n')

    # Handle Invalid User Input Values.
    while game_start.upper() != 'N' and game_start.upper() != 'Y':
        print('Y / N')

        # GET User Input.
        game_start = input('-------------------------\n'
                           '    ...Start Game...     \n'
                           '           Y/N           \n'
                           '-------------------------\n')

    # Handle User Input for Quit before Game Start.
    while game_start.upper() == 'N':
        print('You\'re right...')
        sleep(1.5)
        print('It\'s better if you stay away...')
        sleep(2)
        exit()

    # Handle User Input for Start Game
    while game_start.upper() == 'Y':

        # GET & SET Global Variables for Game Start and current location (to show intro)
        global playerSelection
        global game_state
        global currentLocation
        game_state = 1

        # GET and Show current location text.
        get_current_location_text(currentLocation)

        # Dictionary of Valid Locations and their movement, items, and investigation counters.
        locations = {

            'Corroded Wagon': {'NORTH': 'Trading Post',
                               'SOUTH': 'Jagged Cliffs',
                               'Item': 'NONE',
                               'Investigated': 0},

            'Jagged Cliffs': {'NORTH': 'Corroded Wagon',
                              'Item': 'NONE',
                              'Investigated': 0,
                              'Required Investigate #': 2},

            'Trading Post': {'EAST': 'Worker\'s Tent City Section(1)',
                             'SOUTH': 'Corroded Wagon',
                             'WEST': 'Logging Camp Section(1)',
                             'Item': 'Greed',
                             'Investigated': 0,
                             'Required Investigate #': 2},

            'Worker\'s Tent City Section(1)': {'WEST': 'Trading Post',
                                               'NORTH': 'Worker\'s Tent City Section(2)',
                                               'Item': 'Regret',
                                               'Investigated': 0,
                                               'Required Investigate #': 2},

            'Worker\'s Tent City Section(2)': {'SECRET WEST': 'Tree House',
                                               'SOUTH': 'Worker\'s Tent City Section(1)',
                                               'NORTH': 'Splinter Gardens Section(1)',
                                               'Item': 'NONE',
                                               'Investigated': 0},

            'Logging Camp Section(1)': {'EAST': 'Trading Post',
                                        'NORTH': 'Logging Camp Section(2)',
                                        'Item': 'NONE',
                                        'Investigated': 0},

            'Logging Camp Section(2)': {'SOUTH': 'Logging Camp Section(1)',
                                        'SECRET EAST': 'Tree House',
                                        'Item': 'Depression',
                                        'Investigated': 0,
                                        'Required Investigate #': 1},

            'Tree House': {'WEST': 'Logging Camp Section(2)',
                           'EAST': 'Worker\'s Tent City Section(2)',
                           'SECRET NORTH': 'Forsaken Camp',
                           'Item': 'NONE',
                           'Investigated': 0},

            'Forsaken Camp': {'WEST': 'Makeshift Slave Quarters Section(1)',
                              'Item': 'Salvation',
                              'Investigated': 0,
                              'Required Investigate #': 2},

            'Underground Entrance': {'WEST': 'Makeshift Slave Quarters Section(2)',
                                     'Item': 'NONE',
                                     'Investigated': 0},

            'Makeshift Slave Quarters Section(1)': {'EAST': 'Forsaken Camp',
                                                    'NORTH': 'Makeshift Slave Quarters Section(2)',
                                                    'Item': 'NONE',
                                                    'Investigated': 0},

            'Makeshift Slave Quarters Section(2)': {'EAST': 'Den of The Blind',
                                                    'SOUTH': 'Makeshift Slave Quarters Section(1)',
                                                    'Item': 'Fear',
                                                    'Investigated': 0,
                                                    'Required Investigate #': 2},

            'Den of The Blind': {'WEST': 'Makeshift Slave Quarters Section(2)',
                                 'SECRET EAST': 'Gravestone Father\'s Fortress',
                                 'Item': 'Fury',
                                 'Investigated': 0,
                                 'Required Investigate #': 1},

            'Splinter Gardens Section(1)': {'NORTH': 'Underground Entrance',
                                            'SOUTH': 'Worker\'s Tent City Section(2)',
                                            'EAST': 'Splinter Gardens Section(2)',
                                            'Item': 'Strength',
                                            'Investigated': 0,
                                            'Required Investigate #': 2},

            'Splinter Gardens Section(2)': {'NORTH': 'Gravestone Father\'s Fortress',
                                            'WEST': 'Splinter Gardens Section(1)',
                                            'Item': 'NONE',
                                            'Investigated': 0},

            'Gravestone Father\'s Fortress': {'SOUTH': 'Splinter Gardens Section(2)',
                                              'Item': 'NONE',
                                              'Investigated': 0,
                                              'Required Investigate #': 1}

        }

        # Main Game Loop
        while game_state == 1:

            # GET Global Variables for Game Start
            global inventory
            global currentLocationInvestigationCounter

            inventory = ['STRENGTH', 'GREED', 'FEAR', 'REGRET', 'FURY', 'DEPRESSION', 'SALVATION']

            # SET valid movement options
            move_options = ['NORTH', 'SOUTH', 'EAST', 'WEST']

            # IF player input is empty
            if playerSelection == '':

                # Show player available options
                print('\n||=========================================================================================||')
                print('|| Movement Controls: North, South, East, West                                             ||')

                # IF current location is Gravestone Father\'s Fortress, show player Open option.
                if currentLocation == 'Gravestone Father\'s Fortress':
                    startEnd = checkInvestigate(locations)

                    if startEnd:
                        print('|| End Game Action: Open                                                              '
                              '     ||')

                # Show player available options
                print('|| Additional Actions: Help <-(Shows Inventory), Pause, Investigate, Retrieve              ||')
                print('||=========================================================================================||')

                # GET & SET the current investigation counter
                currentLocationInvestigationCounter = getCurrentLocationInvestigationCounter(locations)

                # Show current location to player.
                print('\nCurrent Location: >--[{}]--<.'.format(currentLocation))

                # Get player selection
                playerSelection = input('What\'s your next move?\n').upper()

            # Check that the player input is a valid option; call the check user input function.
            elif checkUserInput(playerSelection):

                # Move Function; Check that their move option is in the valid move option list,
                # not the entire valid option list.
                while playerSelection in move_options:
                    # Call to the movement function, return current location and player selection,
                    # break back to main loop
                    playerSelection = move_direction(playerSelection, locations, inventory)
                    break

                # Open Function (End Game)
                while playerSelection == 'OPEN':

                    # Ensure current location is Gravestone Father\'s Fortress.
                    if currentLocation == 'Gravestone Father\'s Fortress':

                        # Make sure user cannot access OPEN until they have investigated all of this location's options.
                        startEnd = checkInvestigate(locations)

                        # IF boolean returns true.
                        if startEnd:
                            endSequence(inventory, move_options)
                            break

                        else:
                            # Set player selection back to nothing.
                            playerSelection = ''
                            print('\n...You\'re speaking nonsense... ')
                            sleep(3)

                # Investigate Function
                while playerSelection == 'INVESTIGATE':
                    playerInvestigate(locations)
                    break

                # Pause Function
                while playerSelection == 'PAUSE':
                    pause()

                    if game_state == 1:
                        break

                # Help Function
                while playerSelection == 'HELP':
                    help_player(inventory)
                    break

                # Retrieve Function
                while playerSelection == 'RETRIEVE':
                    item_retrieve(locations)
                    break

                # Quit Function
                while playerSelection == 'QUIT':
                    print('You\'re right...')
                    sleep(1.5)
                    print('It\'s better if you stay away...')
                    sleep(2)
                    exit()
            else:
                playerSelection = ''
                print('\n...You\'re speaking nonsense... ')
                sleep(3)
                break


if __name__ == "__main__":
    main()
