from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
stuff_to_be_removed = list(stopwords.words("english"))+list(punctuation)
import enchant, difflib
import pandas as pd
import numpy as np
import re
import pickle
import random
import nltk

file_path = "words.txt"
dictionary = enchant.request_pwl_dict(file_path)

data = pd.read_excel("data/sampledata_v2.xlsx", encoding="latin1")
for i in data.columns:
    data[i] = data[i].str.lower()




class color:
    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"

negative_list = ["not", "no", "without", "dont", "wont", "other than"]
greeting_keywords = [
    "hi",
    "hiee",
    "hie",
    "hey",
    "heyy",
    "hello",
    "good morning",
    "good afternoon",
    "good evening",
    "gm",
]



pack = list(data["Package"].str.lower().dropna().unique())
pack = [x.strip() for x in pack]  # removing leading and trailing spaces

sub_pack = list(data["Sub-package"].str.lower().dropna().unique())
sub_pack = [x.strip() for x in sub_pack]

yoga_pack = list(data["Yoga_package"].str.lower().dropna().unique())
yoga_pack = [
    x.strip() for x in yoga_pack
]  # removing leading and trailing spaces

massage_pack = list(data["Massage_package"].str.lower().dropna().unique())
massage_pack = [
    x.strip() for x in massage_pack
]  # removing leading and trailing spaces

meditation_pack = list(
    data["Meditation_package"].str.lower().dropna().unique()
)
meditation_pack = [
    x.strip() for x in meditation_pack
]  # removing leading and trailing spaces

naturopathy_pack = list(
    data["Naturopathy_package"].str.lower().dropna().unique()
)
naturopathy_pack = [
    x.strip() for x in naturopathy_pack
]  # removing leading and trailing spaces

ayurvedic_pack = list(data["Ayurvedic_package"].str.lower().dropna().unique())
ayurvedic_pack = [
    x.strip() for x in ayurvedic_pack
]  # removing leading and trailing spaces

therapies_pack = list(data["Therapies_package"].str.lower().dropna().unique())
therapies_pack = [
    x.strip() for x in therapies_pack
]  # removing leading and trailing spaces

facials_pack = list(data["Facials_package"].str.lower().dropna().unique())
facials_pack = [
    x.strip() for x in facials_pack
]  # removing leading and trailing spaces

adventure_pack = list(data["Adventure_package"].str.lower().dropna().unique())
adventure_pack = [
    x.strip() for x in adventure_pack
]  # removing leading and trailing spaces

local_pack = list(data["Local_package"].str.lower().dropna().unique())
local_pack = [
    x.strip() for x in local_pack
]  # removing leading and trailing spaces

prop_type = list(data["Prop Type"].str.lower().dropna().unique())
prop_type = [
    x.strip() for x in prop_type
]  # removing leading and trailing spaces

prop_fac = list(data["Prop Facilities"].str.lower().dropna().unique())
prop_fac = [
    x.strip() for x in prop_fac
]  # removing leading and trailing spaces

benefits = list(data["Benefits"].str.lower().dropna().unique())
benefits = [
    x.strip() for x in benefits
]  # removing leading and trailing spaces

meal = list(data["Meal Type"].str.lower().dropna().unique())
meal = [x.strip() for x in meal]  # removing leading and trailing spaces

diff_level = list(data["Difficulty Level"].str.lower().dropna().unique())
diff_level = [
    x.strip() for x in diff_level
]  # removing leading and trailing spaces

budget = list(data["Budget&Currency"].str.lower().dropna().unique())
budget = [x.strip() for x in budget]  # removing leading and trailing spaces

places = list(data["Places"].str.lower().dropna().unique())
places = [x.strip() for x in places]  # removing leading and trailing spaces

def filter_data(key, value, df2):
    if len(value) == 2:
        key = key
        value1 = value[0]
        value2 = value[1]
        # print('entities detected: ',key,value1,value2)
        df2 = df2[(df2[key] == value1) | (df2[key] == value2)]
        return df2, key

    elif len(value) == 3:
        key = key
        value1 = value[0]
        value2 = value[1]
        value3 = value[2]
        # print('entities detected: ',key,value1,value2,value3)
        df2 = df2[
            (df2[key] == value1) | (df2[key] == value2) | (df2[key] == value3)
        ]
        return df2, key

    else:

        key = key
        value = value[0]
        df2 = df2[df2[key] == value]
        # print('entities detected: ',key, value)
        return df2, key



def generate_response_v2(key, value):
    print('key',key)
    print('value',value)
        
    psearch = {
        "Package":
        
        random.choice([
            "Which package would you like ?",
            "What kind of holiday are you looking for ?",
            "Which is your preferred choice of holiday ?"
        ]),
        
        "Sub_package":
        random.choice([
            "Which {} package would you like to go for ?".format(value),
            "Amazing, what type of {} are you interested in ?".format(value),
            "Cool, what type of {} package would you like to try ?".format(value)
        ]),
        
        "Difficulty_level":
        random.choice([
            "Okay, provide me with your level of expertise ?",
            "Fine, what is your proficiency level in this ?",
            "Great, please select your level of expertise"
        ]),
        
        "Prop_type": 
        random.choice([
            "Okay noted! What kind of stay would you like?",
            "Nice! What is your preferred property choice of stay?",
            "Great! Please select your preferred stay type"
        ]),
        
        "Prop_Facilities":
        random.choice([
            "Alright, any additional facility with your stay?",
            "Okay, would there be any additional facilities with your stay?",
            "Are there any preffered choice of facilities?"
        ]),
        
        "Benefits":
        random.choice([
            "Noted, what health related problems are you trying to heal?",
            "Noted, can you provide me with the health issues you are trying to aid?",
            "Do you have any health problems?"
        ]),
        
        "Meal_type":
        random.choice([
            "Got it ! thanks for letting us know. What kind of meal would you prefer",
            "Choose from the given meal types"
        ]),
        
        "Places":
        random.choice([
            "Noted. Where would you like to travel to?"
        ]),
        
        "Budget":
        random.choice([
            "Noted. what would be your budget(kindly specify the currency)?"
        ])
        }

    

    showlist = {
        "Package": pack,
        "Yoga_package": yoga_pack,
        "Massage_package": massage_pack,
        "Meditation_package": meditation_pack,
        "Naturopathy_package": naturopathy_pack,
        "Ayurvedic_package": ayurvedic_pack,
        "Therapies_package": therapies_pack,
        "Facials_package": facials_pack,
        "Adventure_package": adventure_pack,
        "Local_package": local_pack,
        "Difficulty_level": diff_level,
        "Prop_type": prop_type,
        "Prop_Facilities": prop_fac,
        "Benefits": benefits,
        "Meal_type": meal,
        "Places": places,
        "Budget": budget,
    }

    if value == "yoga":
        print('key',key)
        print('value',value)
        return "{} \n \n Please select anyone: \n{}".format(psearch[key],showlist["Yoga_package"])
    elif value == "massage":
        return str("""{}
        Please select anyone:

        {}""".format(psearch[key],showlist["Massage_package"]))
    elif value == "meditation":
        return str("""{}
        Please select anyone: 

        {}""".format(psearch[key],showlist["Meditation_package"]))
    elif value == "naturopathy":
        return str("""{}
        Please select anyone: 

        {}""".format(psearch[key],showlist["Naturopathy_package"]))
    elif value == "ayurvedic":
        return str("""{}
        Please select anyone: 

        {}""".format(psearch[key],showlist["Ayurvedic_package"]))
    elif value == "therapy":
        return str("""{}
        Please select anyone: 

        {}""".format(psearch[key],showlist["Therapies_package"]))
    elif value == "facials":
        return str("""{}
        Please select anyone: 

        {}""".format(psearch[key],showlist["Facials_package"]))
    elif value == "adventure":
        return str("""{}
        Please select anyone: 

        {}""".format(psearch[key],showlist["Adventure_package"]))
    elif value == "local":
        return str("""{}
        Please select anyone: 

        {}""".format(psearch[key],showlist["Local_package"]))
    else:
        return str("{} \n Please select anyone: {}".format(psearch[key],showlist[key]))




def correct(string):
    dict = {}
    max = 0
    word_list = []
    words = word_tokenize(string.lower())
    for word in words:
        if word not in stuff_to_be_removed:
            word_set = set(dictionary.suggest(word))
            for option in word_set:
                max = 0
                word_prob = difflib.SequenceMatcher(None, word, option).ratio()
                dict[word_prob] = option
                if word_prob > max:
                    max = word_prob
            word_list.append(dict[max])

    return word_list     


def find_entity(string2):

    #string2 = " ".join(correct(string))

    ent = {
        "Package": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in pack
            ]
            if j != []
        ],
        "Sub_package": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in sub_pack
            ]
            if j != []
        ],
        "Difficulty_level": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in diff_level
            ]
            if j != []
        ],
        "Prop_type": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in prop_type
            ]
            if j != []
        ],
        "Prop_Facilities": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in prop_fac
            ]
            if j != []
        ],
        "Benefits": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in benefits
            ]
            if j != []
        ],
        "Meal_type": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in meal
            ]
            if j != []
        ],
        "Budget": [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string2.lower())
                for i in budget
            ]
            if j != []
        ],
    }

    return ent

def get_user_info(string,data_fill,features,df2):
    
    response_key = "blank"
    entities = find_entity(string.lower())
    

    present = sum(map(lambda x: len(x), entities.values()))
    data_fill_empty = sum(map(lambda x: len(x),data_fill.values()))

    if present == 0:

        greeting_entitiy = [
            j[0]
            for j in [
                re.findall(re.compile(rf"\b{i}\b", re.I), string.lower())
                for i in greeting_keywords
            ]
            if j != []
        ]
        if greeting_entitiy:
            return str(
                random.choice(
                    [
                        "hi",
                        "hello",
                        "hi! how may i help you",
                        "hey! how can i help you",
                    ]
                )
            ), data_fill,features,df2

        elif data_fill_empty!=0:

            return str('I did not understand, can you repeat?'),data_fill,features,df2

        else:
            return str(
                "Which package would you like?? "+"\n"+" Please select anyone: {}".format(pack)
                
            ),data_fill,features,df2


    else:

        entities = find_entity(string)

        key_values = [(k, v) for k, v in entities.items() if v] 
        for i in key_values:
            data_fill[i[0]] = i[1]

        neg = [
            j[0]
            for j in [re.findall(i, string.lower()) for i in negative_list]
            if j != []
        ]


        if neg != []:
            word = string.split(neg[0])[1].strip()
            data_fill["dont want"] = word



        
        for filter_key_values in key_values:
            if filter_key_values[0] in features:
                features.remove(filter_key_values[0])
                df2, key = filter_data(
                    filter_key_values[0], filter_key_values[1], df2
                )

        response_key, blank_value = next(
            (k, v) for k, v in data_fill.items() if not v
        )
        print('response_key',response_key)
        if response_key == "Budget":
            no_packages = df2.shape[0]
            pack_recommend = " ".join(df2["Holiday Package"].to_list())
            return str(
                "\n \n We have the packages tailored to your need !! Here are your {} best packages \n {} \n i hope that helps !! bye".format(no_packages,pack_recommend)),data_fill,features,df2

        if response_key == "Sub_package":
            
            for value in key_values[0][1]:
                return generate_response_v2(response_key, value),data_fill,features,df2
        else:
            return generate_response_v2(response_key, blank_value),data_fill,features,df2