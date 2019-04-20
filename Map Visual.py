#main call to run program
def main():
  intro = "---Welcome to the Testing123 House!---\n" # Using string concatenation to avoid strange triple quote behavior.
  intro += "In each room you will have "
  intro += "options of which direction you "
  intro += "would like to go. To win the "
  intro += "game find the audio tapes "
  intro += "and tape player, and play "
  intro += "the tapes to hear the clue. "
  intro += "Remember to first take off your shoes! "
  intro += "Type mission to redisplay this message. "
  actions = '''---Actions---\nType north, east, south, or west to move.
Type use to use an item.
Type climb up or climb down to use a ladder.
Type take to take an item.
Type drop to drop an item.
Type examine to check what items are in a room.
Type inventory to check what items you have.
Type look to reprint the description of the room.
Type exit or quit to quit at any time.
Type help to redisplay this message.\n'''

# Prints the welcome message.
  showInformation(intro)
  showInformation(actions)
  
# Initializing Room objects.
  Garage = Room("Garage",None, None, None, None, None, None, "one",  false, [])
  LivingRoom = Room("Living Room", None, None, None, None, None, None, "two", true, [])
  Kitchen = Room("Kitchen", None, None, None, None, None, None, "one", false, [])
  Bathroom = Room("Bathroom", None, None, None, None, None, None, "one", false, [])
  Bedroom = Room("Bedroom", None, None, None, None, None, None, "one", true, [])
  Attic = Room("Attic", None, None, None, None, None, None, "no", true, [])
  Basement = Room("Basement", None, None, None, None, None, None, "no", true, [])
  Pantry = Room("Pantry", None, None, None, None, None, None, "two", false, [])
  SecretRoom = Room("Secret Room", None, None, None, None, None, None, "no", false, []) 
  
# Creating Room neighbor connections.
  Garage.neighborWest = Pantry
  Pantry.neighborEast = Garage
  Pantry.neighborWest = LivingRoom
  LivingRoom.neighborEast = Pantry
  LivingRoom.neighborWest = Kitchen
  LivingRoom.neighborDown = Basement
  LivingRoom.neighborUp = Bedroom
  Bedroom.neighborWest = Bathroom
  Bedroom.neighborUp = Attic
  Bedroom.neighborDown = LivingRoom
  Attic.neighborDown = Bedroom
  Bathroom.neighborEast = Bedroom
  Kitchen.neighborEast = LivingRoom
  Basement.neighborUp = LivingRoom
  #Basement.neighborWest = SecretRoom
  SecretRoom.neighborEast = Basement

# Prompts user for name.
  name = requestString("What is your name?")
  
# Initializes items
  car = Item("car",isTakeable = false)
  car.use = "You cannot drive anywhere."
  Garage.items.append(car) # This is the garage items.
  
  chair = Item("chair",isTakeable = false)
  footstool = Item("footstool")
  tv = Item("tv",isTakeable = false)
  tv.use = "You look through the channels and there is nothing interesting."
  monitor = Item("monitor",isTakeable = false)
  monitor.use = "You do not know the password. You cannot use the computer."
  slidingDoor = Item("sliding door",isTakeable = false)
  slidingDoor.use = "You open the door and feel the gentle breeze on your face."
  LivingRoom.items.extend([chair,footstool,tv,monitor,slidingDoor]) # This is the living room items.
  
  sink = Item("sink",isTakeable = false)
  sink.use = "You wash your hands."
  fridge = Item("fridge",isTakeable = false)
  fridge.use = "You open the fridge. There is nothing intersting."
  cupboard = Item("cupboard",isTakeable = false)
  cupboard.use = ("You open the shelf, but there is nothing there.")
  keys = SecretItem("keys") # this is revealed when they open the cupboard
  banana = Item("banana")
  banana.use= "You eat the banana."
  Kitchen.items.extend([sink,fridge,cupboard,banana,keys]) # This is the kitchen items.
  
  washer = Item("washer",isTakeable=false)
  washer.use="You have no detergent to wash your clothes. You cannot use the washer"
  heater = Item("heater",isTakeable=false)
  heater.use="The house starts to get warmer. In a catastrophic scheme of events, the house explodes!"#Make this a lose condition
  Basement.items.extend([washer,heater]) # This is the basement items.
  
  lamp = Item("lamp",isTakeable=false)
  lamp.use="You turn the lamp on."
  bed = Item("bed",isTakeable=false)
  bed.use="You take a nap."
  nightstand = Item("nightstand",false,false)
  doubleWindow = Item("double window",isTakeable=false)
  doubleWindow.use = "You open the window and feel the gentle breeze on your face."
  Bedroom.items.extend([lamp,bed,nightstand,doubleWindow])
  
  bathtub = Item("bathtub",isTakeable=false)
  bathtub.use = "You take a bath."
  toilet = Item("toilet",isTakeable=false)
  toilet.use = "You use the toilet."
  bathroomSink = Item("bathroom sink",isTakeable=false)
  bathroomSink.use = "You wash your hands."
  window = Item("window",isTakeable=false)
  window.use = "You open the window and feel the gentle breeze on your face."
  mirror = Item("mirror",isTakeable=false)
  mirror.use = "You admire your reflection."
  Bathroom.items.extend([bathtub,toilet,bathroomSink,window,mirror])
  
  treasure = Item("treasure")
  SecretRoom.items.append(treasure)
  
  
  shoes = Item("shoes") # These are the players items.
  
# Initializing Player Object to start in Room MainHall.
# Prints out description of room and possible directions.
# Prints out items in the room and the player's inventory.
  myPlayer = Player(name, Garage)
  myPlayer.items.append(shoes)
  myPlayer.location.description()
  myPlayer.location.direction()
  myPlayer.location.displayItems()
  myPlayer.displayItems()
  
  # Initialize a counter for how many times they have moved rooms and how many allowed.
  maxcount = 20
  steps = 0 
  
# Accounts for the secret room.
  isAlreadyNoticed = false
  isUnlocked = false
  
# Continuously prompts the user to type a command.  
  while true:
# Lose conditions.
    if steps >= maxcount:
      showInformation("You ran out of time. You can only make so many moves. \n\n" + mPlayer.name.upper() + ", YOU LOSE!\n")
      break
    if myPlayer.location != Garage and myPlayer.contains(shoes): 
      showInformation("You can't enter with your shoes on.\n\n" + myPlayer.name.upper() + ", YOU LOSE!\n")
      break
# Win conditions.
    if treasure in myPlayer.items:
      showInformation(myPlayer.name.upper() + ", YOU WIN!")
      break 
# Secret room reveal condition.
    if myPlayer.contains(keys) and myPlayer.location == Basement and not isUnlocked and not isAlreadyNoticed:
      showInformation("You notice a door that is locked.\n")
      isAlreadyNoticed = true       
# Parse the command.
    command = requestString("What do you want to do?").strip().lower()
    if command == "exit" or command == "quit":
      showInformation("You are now exiting the game!")
      break
    elif command == "north" or command == "south" or command == "east" or command == "west":
      steps += myPlayer.move(command)
    elif command == "help":
      showInformation(actions)
      myPlayer.location.description()
      myPlayer.location.direction()
    elif command == "mission":
      showInformation(intro)
      myPlayer.location.description()
      myPlayer.location.direction()
    elif command == "climb up":
      steps += myPlayer.climbUp() 
    elif command == "climb down":
      steps += myPlayer.climbDown()
    elif command == "examine":
      myPlayer.location.displayItems()
    elif command == "inventory":
      myPlayer.displayItems()
    elif command == "look":
      myPlayer.location.description()
      myPlayer.location.direction()
    elif command == "take":
      item = requestString("What item do you want to take?")
      myPlayer.take(item)
    elif command == "drop":
      item = requestString("Which item do you want to drop?")
      myPlayer.dropItem(item)
    elif command == "use":
      item = requestString("What item do you want to use?")
      use = myPlayer.useItem(item, Basement, isUnlocked)
      if use == -1:
        showInformation(name.upper() + ", YOU LOSE!\n")
        break
      elif use == 1:
        isUnlocked = true
    else:
      printNow("Please type a valid command.\n")
  
  
#############################################################################
class Room(object):
# Creates a room object with attributes to account for "neighbor" rooms.
  def __init__(self, name, neighborUp, neighborDown, neighborNorth, neighborEast, neighborSouth, neighborWest, doors, ladder, items):
    self.name = name
    self.neighborUp = neighborUp
    self.neighborDown = neighborDown
    self.neighborNorth = neighborNorth
    self.neighborEast = neighborEast
    self.neighborSouth = neighborSouth
    self.neighborWest = neighborWest
    self.doors = doors
    self.ladder = ladder
    self.items = items

# Displays a message description of the room object.
  def description(self):
    if self.doors == "one":
      if self.ladder:
        printNow("---%s--- \nYou walk around a room called %s. You see %s door. There is a ladder in the room." % (self.name, self.name, self.doors))
      else:
        printNow("---%s--- \nYou walk around a room called %s. You see %s door." % (self.name, self.name, self.doors))
    elif self.ladder:
      printNow("---%s--- \nYou walk around a room called %s. You see %s doors. There is a ladder in the room." % (self.name, self.name, self.doors))
    else:
      printNow("---%s--- \nYou walk around a room called %s. You see %s doors." % (self.name, self.name, self.doors))
      
  #Informs the player which direction they can go    
  def direction(self):
    dir = ""
    if self.neighborNorth != None:
      dir += "You can go north. "
    if self.neighborEast != None:
      dir += "You can go east. "
    if self.neighborSouth != None:
      dir += "You can go south. "
    if self.neighborWest != None and (self.neighborWest.name != "Secret Room" or self.neighborWest.doors == "one"): # Don't reveal secret room.:
      dir += "You can go west. "
    if self.neighborUp != None:
      dir += "You can climb up. "
    if self.neighborDown != None:
      dir += "You can climb down. "
    printNow(dir)
    printNow("")
    
  def findItem(self, inputItemName):
    for item in self.items:
      if item.name == inputItemName:
        return item
    return None
    
  # Displays items in the room.
  def displayItems(self):
    if len(self.items) == 0:
      printNow("There are no items in the room.")
    else:
      printNow("The items in the room are:")
      for item in self.items:
        if not isinstance(item, SecretItem) or item.isRevealed == true:
          printNow(item)
      printNow("")
      
      
#############################################################################
#Creating the visual Map. This is NOT the Map class.
#Does not have to be defined to a class since it
#is not a use-able object and can simply be
#called in main() to update the visual map.
def createMap():
  setMediaPath()
  secretRoom = makePicture("hiddenroom.jpg")
  mainMap = makePicture("original map.jpg")
  winPlayer = makePicture("happy.png")
  winPlayerFlip = makePicture("happyflip.png")
  player = makePicture("neutral.png")
  playerFlip = makePicture("neutralflip.png")
  losePlayer = makePicture("upset.png")
  losePlayerFlip = makePicture("upsetflip.png")
  atticPlayer = makePicture("attic.png")
  atticPlayerFlip = makePicture("atticflip.png")
  
#Player coordinates. 
#Uncomment second call to see the flipped version.
#garage
  chromaKey(secretRoom, playerFlip, 770, 410)
  #chromaKey(secretRoom, player, 770, 410)
#basement
  chromaKey(secretRoom, playerFlip, 570, 525)
  #chromaKey(secretRoom, player, 570, 525)
#secretRoom
  chromaKey(secretRoom, playerFlip, 340, 525)
  #chromaKey(secretRoom, player, 340, 525)
#pantry (room next to garage)
  chromaKey(secretRoom, playerFlip, 645, 390)
  #chromaKey(secretRoom, player, 645, 390)
#living room
  chromaKey(secretRoom, playerFlip, 320, 390)
  #chromaKey(secretRoom, player, 320, 390)
#kitchen
  chromaKey(secretRoom, playerFlip, 100, 390)
  #chromaKey(secretRoom, player, 100, 390)
#bedroom
  chromaKey(secretRoom, playerFlip, 450, 215)
  #chromaKey(secretRoom, player, 450, 215)
#bathroom
  chromaKey(secretRoom, playerFlip, 300, 215)
  #chromaKey(secretRoom, player, 300, 215)
#attic
  chromaKey(secretRoom, atticPlayerFlip, 460, 120)
  #chromaKey(secretRoom, atticPlayer, 460, 120)   

#This is required to insert image of player into map image.    
def chromaKey(background, pic, xloc, yloc):
  width = getWidth(pic)
  height = getHeight(pic)
  comparator = getColor(getPixel(pic,0,0))
  for x in range(width):
    for y in range(height):
      pix = getPixel(pic, x,y)
      color = getColor(pix)
      if color != comparator:
      	setColor(getPixel(background,x+xloc,y+yloc), color)
  repaint(background) 
 
###################################################################################
class Player(object):
  def __init__(self, name, room):
    self.name = name
    self.location = room
    self.items = []
    
  def move(self, direction):
    if direction == "north" and self.location.neighborNorth != None:
      self.location = self.location.neighborNorth
      self.location.description()
      self.location.direction()
      self.location.displayItems()
    elif direction == "east" and self.location.neighborEast != None:
      self.location = self.location.neighborEast
      self.location.description()
      self.location.direction()
      self.location.displayItems()
    elif direction == "south" and self.location.neighborSouth != None:
      self.location = self.location.neighborSouth
      self.location.description()
      self.location.direction()
      self.location.displayItems()
    elif direction == "west" and self.location.neighborWest != None \
    and (self.location.neighborWest.name != "Secret Room" or self.location.neighborWest.doors == "one"): # Don't let them go into the secret room until unlocked with door set to "one":
      self.location = self.location.neighborWest
      self.location.description()
      self.location.direction()
      self.location.displayItems()
    else:
      printNow("Please provide a valid direction.\n")
      return 0
    return 1
   
# Action to climb up, returns 1 if succeful and 0 if not.
  def climbUp(self):
    if not self.location.ladder:
      printNow("There is no ladder to climb in this room.\n")
      return 0  
    elif self.location.neighborUp != None:
      printNow("You are climbing up the ladder.\n")
      self.location = self.location.neighborUp
      self.location.description()
      self.location.direction()
      self.location.displayItems()
      return 1
    else:
      printNow("You cannot climb that direction.\n") 
      return 0
      
# Action to climb down, returns 1 if succeful and 0 if not.
  def climbDown(self,):
    if not self.location.ladder:
      printNow("There is no ladder to climb in this room.\n")  
      return 0
    elif self.location.neighborDown != None:
      printNow("You are climbing down the ladder.\n")
      self.location = self.location.neighborDown
      self.location.description()
      self.location.direction()
      self.location.displayItems()
      return 1
    else:
      printNow("You cannot climb that direction.\n") 
      return 0 
      
  def useItem(self, inputItemName, basement, unlocked):
    inputItem = self.findItem(inputItemName) # Get the item of that name.
    
    # Check if trying to unlock the secret room.
    if inputItemName == "keys" and self.contains(inputItem) and self.location == basement and not unlocked:
      showInformation("You opened the Secret Room with the " + inputItem + ".\nYou can now go south to enter.\n")
      self.location.neighborSouth.doors = "one"
      self.location.doors = "one"
      return 1
    elif inputItemName == "keys" and self.contains(inputItem) and self.location == basement and unlocked:
      printNow("You have already unlocked the Secret Room. You can go south to enter.\n")
    elif inputItemName == "keys" and not self.contains(inputItem) and self.location == basement and unlocked:
      printNow("You do not have the " + inputItem + " but you have already opened this door.\n")
      
    # Checks if item exists in player's inventory then room's.  
    if inputItem == None:
      inputItem = self.location.findItem(inputItemName)
      if inputItemName == "cupboard":
        # Reveal keys
        inputItem.isRevealed = true
        printNow("You discover a set of keys.\n")
    if inputItem == None:
      printNow("You cannot use the " + inputItemName + " becasue it is not in your inventory or in the room.\n")
    elif inputItem.isUsable:
      printNow(inputItem.use)
      if inputItemName == "heater":
        return -1
      elif inputItemName == "banana":
        self.items.remove(inputItem)
    else:
      printNow("You cannot use the " + inputItemName + " because it does not do anything./n")
      
  def take(self, inputItemName):
    inputItem = self.location.findItem(inputItemName) # !!!!!!!!!!!!! NEED TO IMPLEMENT ROOM.FINDITEMS !!!!!!!!!!!!!
    if inputItem == None:
      printNow("You cannot take the " + inputItemName + " because it is not in the room with you.\n")
    elif inputItem.isTakeable:
      self.items.append(inputItem)
      self.location.items.remove(inputItem)
      printNow("You have taken the " + inputItemName + ".\n")
    else:
      printNow("You cannot take the " + inputItemName + ". How did you expect to carry it?")
  
  def dropItem(self, inputItemName):
    inputItem = self.findItem(inputItemName)
    if inputItem == None:
      printNow("You cannot take the " + inputItemName + " because it is not in your inventory.\n")
    elif inputItem.isTakeable:
      self.location.items.append(inputItem)
      self.items.remove(inputItem)
      printNow("You have dropped the " + inputItemName + ".\n")
    else:
      printNow("You cannot take the " + inputItemName + ". How did you expect to carry it?")
  
  def findItem(self, inputItemName):
    for item in self.items:
      if item.name == inputItemName:
        return item
    return None
    
  # Checks if an item is in inventory.
  def contains(self, inputItem):
     return inputItem in self.items
     
  # Displays items in the player's inventory.
  def displayItems(self):
    if len(self.items) == 0:
      printNow("There are no items in your inventory.")
    else:
      printNow("The items in your inventory are:")
      for item in self.items:
        printNow(item)
      printNow("")
    
class Item(object):
  def __init__(self, name, isUsable = true, isTakeable = true):
    self.name = name
    self.isUsable = isUsable
    self.use = "You use the " + self.name + " and nothing interesting happens."
    self.isTakeable = isTakeable
    
  def __repr__(self):
    return self.name
    
class SecretItem(object):
  # An item that is only revealed if the player does something
  
  def __init__(self, name, isUsable = true, isTakeable = true, isRevealed=false):
    self.name = name
    self.isUsable = isUsable
    self.use = "You use the " + self.name + " and nothing interesting happens."
    self.isTakeable = isTakeable
    self.isRevealed = isRevealed
    
def testPlayer():
  me = Player("me","Kitchen")
  print "Player me is in the " + me.location
  print "Player me is named " + me.name
  print "Player me has " + str(me.items)
  print
  you = Player("you","Bedroom")
  print "Player you is in the " + you.location
  print "Player you is named " + you.name
  print "Player you has " + str(you.items)
  print
  you.items.append("banana")
  print "Now player you has " + str(you.items)
  print "Checking player me has " + str(me.items)
  
def testFindItems():
  me = Player("me","Kitchen")
  banana = Item("banana")
  me.items.append(banana)
  print "The player has the items: " + str(me.items)
  inputItem = me.findItem("banana")
  print "Using the findItem method returns the item " + str(inputItem)
  