#version 1.0

import random
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'


englishParts = ['wordForms', 'wordForms2', 'wordForms3']

wordForms = {
    "beat": "beat beaten", "become": 'became become', "begin": 'began begun', "bite": 'bit bitten', "blow": 'blew blown',
    "break": "broke broken", "bring": "brought brought", "build": "built built", "burn": 'burnt burnt', "buy": 'bought bought',
    "catch": 'caught caught', "choose": 'chose chosen', "come": 'came come', "cost": "cost cost", "cut": 'cut cut', "do": 'did done',
    "draw": 'drew drawn', "dream": 'dreamt dreamt', "drink": 'drank drunk', "drive": 'drove driven', "eat": 'ate eaten', "fall": 'fell fallen',
    "feed": "fed fed", "feel": 'felt felt', "fight": "fought fought", "find": "found found", "fly": "flew flown", "forget": 'forgot forgotten',
    "forgive": 'forgave forgiven', "freeze": 'froze frozen', "get": "got got", "give": "gave given", "go": "went gone", "grow": 'grew grown',
    "hang": "hung hung", "have": "had had"
}

wordForms2 = {
    "hear": 'heard heard', 'hide': 'hid hidden', 'hit': 'hit hit', 'hold': 'held held', 'hurt': 'hurt hurt', 'keep': 'kept kept', 'know': 'knew known',
    'lay': 'laid laid', 'lead': 'led led', 'learn': 'learnt learnt', 'leave': 'left left', 'lend': 'lent lent', 'let': 'let let', 'lie': 'lay lain',
    'lose': 'lost lost', 'make': 'made made', 'mean': 'meant meant', 'meet': 'met met', 'pay': 'paid paid', 'put': 'put put', 'read': 'read read',
    'ring': 'rang rung', 'rise': 'rose risen', 'run': 'ran run', 'say': 'said said', 'see': 'saw seen', 'sell': 'sold sold', 'send': 'sent sent',
    'set': 'set set', 'shake': 'shook shaken', 'shave': 'shaved shaved', 'shine': 'shone shone', 'shoot': 'shot shot', 'show': 'showed shown',
    'shut': 'shut shut', 'sing': 'sang sung', 'sit': 'sat sat', 'sit': 'sat sat', 'sleep': 'slept slept', 'smell': 'smelt smelt', 'speak': 'spoke spoken',
    'spend': 'spent spent', 'spill': 'spilt spilt', 'spoil': 'spoilt spoilt', 'spread': 'spread spread', 'stand': 'stood stood', 'steal': 'stole stolen',
    'sweep': 'swept swept', 'swim': 'swam swum', 'take': 'took taken', 'teach': 'taught taught', 'tell': 'told told', 'think': 'thought thought',
    'throw': 'threw thrown', 'understand': 'understood understood', 'upset': 'upset upset', 'wake': 'woke woken', 'wear': 'wore worn', 'win': 'won won', 'write': 'wrote written'
}

words2 = list(wordForms2.keys())

wordForms3 = {
    'arise': 'arose arisen', 'awake': 'awoke awoken', 'bear': 'bore born', 'bend': 'bent bent', 'bind': 'bound bound', 'bleed': 'bled bled', 'breed': 'bred bred',
    'broadcast': 'broadcast broadcast', 'burst': 'burst burst', 'cast': 'cast cast', 'creep': 'crept crept', 'deal': 'dealt dealt', 'dig': 'dug dug', 'dwell': 'dwellt dwelt',
    'flee': 'fled fled', 'forbid': 'forbad forbidden', 'forecast': "forecast forecast", 'forsake': 'forsook forsaken', 'forsee': "forsaw forseen", 'fortell': 'foretold foretold',
    'grind': 'ground ground', 'kneel': 'knelt knelt', 'lean': 'leant leant', 'leap': 'leapt leapt', 'light': 'lit lit', 'mislay': 'mislaid mislaid', 'mislead': 'misled misled',
    'mistake': 'mistook mistaken', 'misunderstand': 'misunderstood misunderstood', 'outdo': 'outdid outdone', 'outrun': 'outran outrun', 'overcome': 'overcame overcome',
    'overdo': 'overdid overdone', 'overhear': 'overheard overheard', 'oversleep': 'overslept overslept', 'overtake': 'overtook overtaken', 'overthrow': 'overthrew overthrown',
    'partake': 'partook partaken', 'plead': 'pled pled', 'rid': 'rid rid', 'ride': 'rode ridden', 'saw': 'sawed sawn', 'seek': 'sought sought', 'sew': 'sewed sewn',
    'shed': 'shed shed', 'shrink': 'shrank shrunk', 'sink': 'sank sunk', 'slide': "slid slid", 'smell': 'smelt smelt', 'sow': 'sowed sown', 'speed': 'sped sped',
    'spell': 'spelt spelt', 'spill': 'spilt spilt', 'spin': 'span span', 'spit': 'spat spat', 'split': 'split split', 'spring': 'sprang sprung', 'stick': 'stuck stuck', 'sting': 'stung stung',
    'strike': 'struck struck', 'string': 'strung strung', 'strive': 'strove striven', 'swear': 'swore sworn', 'swell': 'swelled swollen', 'swing': 'swung swung',
    'tear': 'tore torn', 'thrive': 'throve thriven', 'unbind': 'unbound unbound', 'undergo': 'underwent undergone', 'undertake': 'undertook undertaken', 'undo': 'undid undone', 'weep': 'wept wept',
    'wind': 'wound wound', 'withdraw': 'withdrew withdrawn', 'withstand': 'withstood withstood', 'wring': 'wrung wrung'
}

words = ['beat', 'become', 'begin', 'bite', 'blow', 'break', 'bring', 'build', 'build', 'burn', 'buy', 'catch', 'choose', 'come', 'cost', 'cut',
         'do', 'draw', 'dream', 'drink', 'drive', 'eat', 'fall', 'feed', 'feel', 'fight', 'find', 'fly',
         'forget', 'forgive', 'freeze', 'get', 'give', 'go', 'grow', 'hang', 'have']

count = 0
wordsLen = len(words2) - 1

# print('Hello, which part you want to learn?\n Write number from 1 to 3')
# selectedNumber = int(input())
# selectedPast = englishParts[selectedNumber - 1]
print(bcolors.HEADER + "Let's start!")
while (wordForms2):
    currentWord = words2[random.randint(0, len(words2) - 1)]
    print(bcolors.OKGREEN + currentWord)
    words2.remove(currentWord)
    answer = input()
    if (wordForms2[currentWord] == answer):
        count += 1
    else:
        print(bcolors.WARNING + 'Incorrect! Your score is', count, '/', wordsLen)
        print('Right forms of', currentWord, 'are', wordForms2[currentWord])
        sys.exit()
    print(count, '/', wordsLen)
