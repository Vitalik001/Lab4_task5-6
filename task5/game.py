class Room:

    def __init__(self, name):
        self.name = name
        self.rooms={}
        self.character=None
        self.item=None

    def set_description(self, description):
        self.description=description

    def link_room(self, room, direction):
        self.rooms[direction]=room

    def set_character(self, character):
        self.character=character

    def set_item(self, item):
        self.item=item

    def get_character(self):
        return self.character

    def get_item(self):
        return self.item

    def move(self, direction):
        return self.rooms[direction]

    def get_details(self):
        directions=''
        for item in self.rooms:
            directions+=f'The {self.rooms[item].name} is {item}\n'
        print(f'{self.name}\n--------------------\n{self.description}\n{directions[:-1]}')
class Enemy:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.weakness=None
        self.conversation=None
        self.defeated=0
        
    def set_conversation(self, conversation):
        self.conversation=conversation

    def set_weakness(self, weakness):
        self.weakness=weakness

    def talk(self):
        print(f'[{self.name} says]: {self.conversation}')

    def fight(self, item):
        if item==self.weakness:
            self.defeated+=1
            print(f'You fend {self.name} off with the {item}')
            return True
        print(f'{self.name} crushes you, puny adventurer!')

    def get_defeated(self):
        return self.defeated

    def describe(self):
        print(f"{self.name} is here!\n{self.description}")

class Item:
    def __init__(self, name):
        self.name = name
        self.description=None
        
    def set_description(self, description):
        self.description=description
    
    def describe(self):
        print(f"The [{self.name}] is here - {self.description}")

    def get_name(self):
        return self.name

    
    
        


        
