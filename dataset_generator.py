
import json
import random
from copy import deepcopy
from itertools import combinations
from typing import Dict, List, Any, Tuple, Set


class SlotDatasetGenerator:
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

        self.slots = {
            "country": {
                "open_user": ["country"],
                "open_assistant": ["What country do you live in?"],
                "values": ["Ukraine", "Poland", "Italy", "Japan", "France", "Germany", "Spain", "Canada"],
                "fill_user_templates": [
                    "I am from {value}.",
                    "{value}.",
                    "I live in {value}.",
                    "My country is {value}."
                ],
                "fill_assistant_templates": [
                    "Got it, you are from {value}.",
                    "Got it, you live in {value}.",
                    "Got it, your country is {value}."
                ],
                "update_user_templates": [
                    "Now I am from {value}.",
                    "Now I live in {value}.",
                    "Now my country is {value}."
                ],
                "update_assistant_templates": [
                    "Got it, now you are from {value}.",
                    "Got it, now you live in {value}.",
                    "Got it, now your country is {value}."
                ],
                "retrieve_user": ["knowledge: country"],
                "retrieve_assistant": "country: {value}",
            },
            "name": {
                "open_user": ["name"],
                "open_assistant": ["What is your name?"],
                "values": ["Anna", "Olena", "Iryna", "John", "Mark", "Sophia", "Maria", "Daniel"],
                "fill_user_templates": [
                    "My name is {value}.",
                    "I am {value}.",
                    "{value}."
                ],
                "fill_assistant_templates": [
                    "Got it, your name is {value}.",
                    "Got it, you are {value}."
                ],
                "update_user_templates": [
                    "Now my name is {value}.",
                    "Now I am {value}."
                ],
                "update_assistant_templates": [
                    "Got it, now your name is {value}.",
                    "Got it, now you are {value}."
                ],
                "retrieve_user": ["knowledge: name"],
                "retrieve_assistant": "name: {value}",
            },
            "action": {
                "open_user": ["action"],
                "open_assistant": ["What are you doing right now?"],
                "values": [
                    "watch TV",
                    "drive by car",
                    "working",
                    "drink tea",
                    "drink coffee",
                    "watch YouTube",
                    "listen music",
                    "play online game",
                    "order underwear in clothing store",
                    "vacuum",
                    "eat apple",
                    "eat pizza",
                    "peel potatoes",
                    "cook pasta",
                    "wash dishes",
                    "cook breakfast",
                    "cook lunch",
                    "cook dinner",
                    "check email",
                    "read book",
                    "watch movie",
                    "talk on the phone",
                    "brush teeth",
                    "repair desk lamp",
                    "set up laptop",
                    "water flowers",
                    "open the window",
                    "close the window",
                    "make the bed",
                    "fold clothes",
                    "iron clothes",
                    "charge phone",
                    "change bed sheets",
                    "wipe the table",
                    "take out the trash",
                    "feed the cat",
                    "feed the dog",
                    "write a post",
                    "talk with a friend",
                    "talk with mother",
                    "talk with father",
                    "think about the past",
                    "air the room",
                    "wash the floor",
                    "wash the window",
                    "walk the dog",
                    "wipe glasses",
                    "fry beefsteak",
                    "put on lipstick",
                    "wash hair",
                    "take a bath",
                    "make coffee",
                    "read news",
                    "hang clothes to dry",
                    "fix the chair",
                    "replace the light bulb",
                    "clean the keyboard",
                    "organize the desk",
                    "pack a bag",
                    "unpack groceries",
                    "comb hair",
                    "apply makeup",
                    "do manicure",
                    "have an online meeting with colleagues",
                ],
                "fill_map": {
                    "watch TV": [
                        "I am watching TV.",
                        "watching TV",
                        "I watch TV now."
                    ],
                    "drive by car": [
                        "I am driving by car.",
                        "driving by car",
                        "I drive a car now."
                    ],
                    "working": [
                        "I am working.",
                        "working",
                        "I work now."
                    ],
                    "drink tea": [
                        "I am drinking tea.",
                        "drink tea",
                        "I drink tea now."
                    ],
                    "drink coffee": [
                        "I am drinking coffee.",
                        "drink coffee",
                        "I drink coffee now."
                    ],
                    "watch YouTube": [
                        "I am watching YouTube.",
                        "watch YouTube",
                        "I watch YouTube now."
                    ],
                    "listen music": [
                        "I am listening to music.",
                        "listen music",
                        "I listen to music now."
                    ],
                    "play online game": [
                        "I am playing an online game.",
                        "playing an online game",
                        "I play an online game now."
                    ],
                    "order underwear in clothing store": [
                        "I am ordering underwear in a clothing store.",
                        "ordering underwear in a clothing store"
                    ],
                    "vacuum": [
                        "I am vacuuming.",
                        "vacuuming"
                    ],
                    "eat apple": [
                        "I am eating an apple.",
                        "eating an apple"
                    ],
                    "eat pizza": [
                        "I am eating pizza.",
                        "eating pizza"
                    ],
                    "peel potatoes": [
                        "I am peeling potatoes.",
                        "peeling potatoes"
                    ],
                    "cook pasta": [
                        "I am cooking pasta.",
                        "cooking pasta"
                    ],
                    "wash dishes": [
                        "I am washing dishes.",
                        "washing dishes"
                    ],
                    "cook breakfast": [
                        "I am cooking breakfast.",
                        "cooking breakfast"
                    ],
                    "cook lunch": [
                        "I am cooking lunch.",
                        "cooking lunch"
                    ],
                    "cook dinner": [
                        "I am cooking dinner.",
                        "cooking dinner"
                    ],
                    "check email": [
                        "I am checking email.",
                        "checking email",
                        "I am checking my email."
                    ],
                    "read book": [
                        "I am reading a book.",
                        "reading a book"
                    ],
                    "watch movie": [
                        "I am watching a movie.",
                        "watching a movie"
                    ],
                    "talk on the phone": [
                        "I am talking on the phone.",
                        "talking on the phone"
                    ],
                    "brush teeth": [
                        "I am brushing my teeth.",
                        "brushing teeth"
                    ],
                    "repair desk lamp": [
                        "I am repairing a desk lamp.",
                        "repairing a desk lamp"
                    ],
                    "set up laptop": [
                        "I am setting up a laptop.",
                        "setting up a laptop"
                    ],
                    "water flowers": [
                        "I am watering the flowers.",
                        "watering flowers"
                    ],
                    "open the window": [
                        "I am opening the window.",
                        "opening the window"
                    ],
                    "close the window": [
                        "I am closing the window.",
                        "closing the window"
                    ],
                    "make the bed": [
                        "I am making the bed.",
                        "making the bed"
                    ],
                    "fold clothes": [
                        "I am folding clothes.",
                        "folding clothes"
                    ],
                    "iron clothes": [
                        "I am ironing clothes.",
                        "ironing clothes"
                    ],
                    "charge phone": [
                        "I am charging my phone.",
                        "charging the phone"
                    ],
                    "change bed sheets": [
                        "I am changing the bed sheets.",
                        "changing bed sheets"
                    ],
                    "wipe the table": [
                        "I am wiping the table.",
                        "wiping the table"
                    ],
                    "take out the trash": [
                        "I am taking out the trash.",
                        "taking out the trash"
                    ],
                    "feed the cat": [
                        "I am feeding the cat.",
                        "feeding the cat"
                    ],
                    "feed the dog": [
                        "I am feeding the dog.",
                        "feeding the dog"
                    ],
                    "write a post": [
                        "I am writing a post.",
                        "writing a post"
                    ],
                    "talk with a friend": [
                        "I am talking with a friend.",
                        "talking with a friend"
                    ],
                    "talk with mother": [
                        "I am talking with my mother.",
                        "talking with my mother"
                    ],
                    "talk with father": [
                        "I am talking with my father.",
                        "talking with my father"
                    ],
                    "think about the past": [
                        "I am thinking about the past.",
                        "thinking about the past"
                    ],
                    "air the room": [
                        "I am airing the room.",
                        "airing the room"
                    ],
                    "wash the floor": [
                        "I am washing the floor.",
                        "washing the floor"
                    ],
                    "wash the window": [
                        "I am washing the window.",
                        "washing the window"
                    ],
                    "walk the dog": [
                        "I am walking the dog.",
                        "walking the dog"
                    ],
                    "wipe glasses": [
                        "I am wiping my glasses.",
                        "wiping glasses"
                    ],
                    "fry beefsteak": [
                        "I am frying a beefsteak.",
                        "frying a beefsteak"
                    ],
                    "put on lipstick": [
                        "I am putting on lipstick.",
                        "putting on lipstick"
                    ],
                    "wash hair": [
                        "I am washing my hair.",
                        "washing my hair"
                    ],
                    "take a bath": [
                        "I am taking a bath.",
                        "taking a bath"
                    ],
                    "make coffee": [
                        "I am making coffee.",
                        "making coffee"
                    ],
                    "read news": [
                        "I am reading the news.",
                        "reading the news"
                    ],
                    "hang clothes to dry": [
                        "I am hanging clothes to dry.",
                        "hanging clothes to dry"
                    ],
                    "fix the chair": [
                        "I am fixing the chair.",
                        "fixing the chair"
                    ],
                    "replace the light bulb": [
                        "I am replacing the light bulb.",
                        "replacing the light bulb"
                    ],
                    "clean the keyboard": [
                        "I am cleaning the keyboard.",
                        "cleaning the keyboard"
                    ],
                    "organize the desk": [
                        "I am organizing the desk.",
                        "organizing the desk"
                    ],
                    "pack a bag": [
                        "I am packing a bag.",
                        "packing a bag"
                    ],
                    "unpack groceries": [
                        "I am unpacking groceries.",
                        "unpacking groceries"
                    ],
                    "comb hair": [
                        "I am combing my hair.",
                        "combing my hair"
                    ],
                    "apply makeup": [
                        "I am applying makeup.",
                        "doing makeup"
                    ],
                    "do manicure": [
                        "I am doing a manicure.",
                        "doing a manicure"
                    ],
                    "have an online meeting with colleagues": [
                        "I am in an online meeting with my colleagues.",
                        "I am having an online meeting with my colleagues.",
                        "I am in a video meeting with my colleagues."
                    ],
                },
                "fill_assistant_map": {
                    "watch TV": ["Got it, you are watching TV.", "Got it, you are watching TV now."],
                    "drive by car": ["Got it, you are driving by car.", "Got it, you are driving a car now."],
                    "working": ["Got it, you are working.", "Got it, you are working now."],
                    "drink tea": ["Got it, you are drinking tea.", "Got it, you are drinking tea now."],
                    "drink coffee": ["Got it, you are drinking coffee.", "Got it, you are drinking coffee now."],
                    "watch YouTube": ["Got it, you are watching YouTube.", "Got it, you are watching YouTube now."],
                    "listen music": ["Got it, you are listening to music.", "Got it, you are listening to music now."],
                    "play online game": ["Got it, you are playing an online game.", "Got it, you are playing an online game now."],
                    "order underwear in clothing store": ["Got it, you are ordering underwear in a clothing store."],
                    "vacuum": ["Got it, you are vacuuming."],
                    "eat apple": ["Got it, you are eating an apple."],
                    "eat pizza": ["Got it, you are eating pizza."],
                    "peel potatoes": ["Got it, you are peeling potatoes."],
                    "cook pasta": ["Got it, you are cooking pasta."],
                    "wash dishes": ["Got it, you are washing dishes."],
                    "cook breakfast": ["Got it, you are cooking breakfast."],
                    "cook lunch": ["Got it, you are cooking lunch."],
                    "cook dinner": ["Got it, you are cooking dinner."],
                    "check email": ["Got it, you are checking email.", "Got it, you are checking your email."],
                    "read book": ["Got it, you are reading a book."],
                    "watch movie": ["Got it, you are watching a movie."],
                    "talk on the phone": ["Got it, you are talking on the phone."],
                    "brush teeth": ["Got it, you are brushing your teeth."],
                    "repair desk lamp": ["Got it, you are repairing a desk lamp."],
                    "set up laptop": ["Got it, you are setting up a laptop."],
                    "water flowers": ["Got it, you are watering the flowers."],
                    "open the window": ["Got it, you are opening the window."],
                    "close the window": ["Got it, you are closing the window."],
                    "make the bed": ["Got it, you are making the bed."],
                    "fold clothes": ["Got it, you are folding clothes."],
                    "iron clothes": ["Got it, you are ironing clothes."],
                    "charge phone": ["Got it, you are charging your phone."],
                    "change bed sheets": ["Got it, you are changing the bed sheets."],
                    "wipe the table": ["Got it, you are wiping the table."],
                    "take out the trash": ["Got it, you are taking out the trash."],
                    "feed the cat": ["Got it, you are feeding the cat."],
                    "feed the dog": ["Got it, you are feeding the dog."],
                    "write a post": ["Got it, you are writing a post."],
                    "talk with a friend": ["Got it, you are talking with a friend."],
                    "talk with mother": ["Got it, you are talking with your mother."],
                    "talk with father": ["Got it, you are talking with your father."],
                    "think about the past": ["Got it, you are thinking about the past.", "Got it, now you are thinking about the past."],
                    "air the room": ["Got it, you are airing the room."],
                    "wash the floor": ["Got it, you are washing the floor."],
                    "wash the window": ["Got it, you are washing the window."],
                    "walk the dog": ["Got it, you are walking the dog."],
                    "wipe glasses": ["Got it, you are wiping your glasses."],
                    "fry beefsteak": ["Got it, you are frying a beefsteak."],
                    "put on lipstick": ["Got it, you are putting on lipstick."],
                    "wash hair": ["Got it, you are washing your hair."],
                    "take a bath": ["Got it, you are taking a bath."],
                    "make coffee": ["Got it, you are making coffee."],
                    "read news": ["Got it, you are reading the news."],
                    "hang clothes to dry": ["Got it, you are hanging clothes to dry."],
                    "fix the chair": ["Got it, you are fixing the chair."],
                    "replace the light bulb": ["Got it, you are replacing the light bulb."],
                    "clean the keyboard": ["Got it, you are cleaning the keyboard."],
                    "organize the desk": ["Got it, you are organizing the desk."],
                    "pack a bag": ["Got it, you are packing a bag."],
                    "unpack groceries": ["Got it, you are unpacking groceries."],
                    "comb hair": ["Got it, you are combing your hair."],
                    "apply makeup": ["Got it, you are applying makeup."],
                    "do manicure": ["Got it, you are doing a manicure."],
                    "have an online meeting with colleagues": [
                        "Got it, you are in an online meeting with your colleagues.",
                        "Got it, you are having an online meeting with your colleagues."
                    ],
                },
                "update_user_templates": [
                    "Now I am {user_value}.",
                ],
                "retrieve_user": ["knowledge: action"],
                "retrieve_assistant": "action: {value}",
            },
            "mood": {
                "open_user": ["mood"],
                "open_assistant": ["How are you feeling right now?"],
                "values": ["happy", "sad", "tired", "calm", "angry", "excited", "worried", "relaxed"],
                "fill_user_templates": [
                    "I feel {value}.",
                    "I am {value}."
                ],
                "fill_assistant_templates": [
                    "Got it, you feel {value}.",
                    "Got it, you are {value}."
                ],
                "update_user_templates": [
                    "Now I feel {value}.",
                    "Now I am {value}."
                ],
                "update_assistant_templates": [
                    "Got it, now you feel {value}.",
                    "Got it, now you are {value}."
                ],
                "retrieve_user": ["knowledge: mood"],
                "retrieve_assistant": "mood: {value}",
            },
            "month": {
                "open_user": ["month"],
                "open_assistant": ["What month is it for you now?"],
                "values": [
                    "January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"
                ],
                "fill_user_templates": [
                    "It is {value}.",
                    "{value}."
                ],
                "fill_assistant_templates": [
                    "Got it, it is {value} for you now.",
                    "Got it, it is {value}."
                ],
                "update_user_templates": [
                    "Now it is {value}.",
                ],
                "update_assistant_templates": [
                    "Got it, now it is {value} for you.",
                    "Got it, now it is {value}."
                ],
                "retrieve_user": ["knowledge: month"],
                "retrieve_assistant": "month: {value}",
            },
            "weather": {
                "open_user": ["weather"],
                "open_assistant": ["What is the weather like for you now?"],
                "values": [
                    "sunny",
                    "foggy",
                    "cloudy",
                    "rainy",
                    "drizzling",
                    "snowy",
                    "windy",
                    "hot",
                    "warm",
                    "cool",
                    "frosty",
                    "damp"
                ],
                "fill_user_templates": [
                    "It is {value}.",
                    "{value}."
                    "The weather is {value}.",
                ],
                "fill_assistant_templates": [
                    "Got it, it is {value} for you now.",
                    "Got it, it is {value}."
                ],
                "update_user_templates": [
                    "Now the weather is {value}."
                ],
                "update_assistant_templates": [
                    "Got it, now it is {value} for you.",
                    "Got it, now it is {value}."
                ],
                "retrieve_user": ["knowledge: weather"],
                "retrieve_assistant": "weather: {value}",
            },
            "favorite_city": {
                "open_user": ["favorite city"],
                "open_assistant": ["What is your favorite city?"],
                "values": ["Kyiv", "Odesa", "Warsaw", "Rome", "Tokyo", "Paris", "Berlin", "Lviv"],
                "fill_user_templates": [
                    "My favorite city is {value}.",
                    "{value}."
                ],
                "fill_assistant_templates": [
                    "Got it, your favorite city is {value}."
                ],
                "update_user_templates": [
                    "Now my favorite city is {value}.",
                ],
                "update_assistant_templates": [
                    "Got it, now your favorite city is {value}."
                ],
                "retrieve_user": ["knowledge: favorite_city"],
                "retrieve_assistant": "favorite_city: {value}",
            },
            "color": {
                "open_user": ["color"],
                "open_assistant": ["What is your favorite color?"],
                "values": ["blue", "green", "red", "black", "white", "orange", "purple", "yellow"],
                "fill_user_templates": [
                    "My favorite color is {value}.",
                    "{value}."
                ],
                "fill_assistant_templates": [
                    "Got it, your favorite color is {value}."
                ],
                "update_user_templates": [
                    "Now my favorite color is {value}.",
                ],
                "update_assistant_templates": [
                    "Got it, now your favorite color is {value}."
                ],
                "retrieve_user": ["knowledge: color"],
                "retrieve_assistant": "color: {value}",
            },
        }

    def _choice(self, arr: List[str]) -> str:
        return self.rng.choice(arr)

    def _make_sample(self, knowledge_in: Dict[str, str], user_text: str, assistant_text: str,
                     knowledge_out: Dict[str, str]) -> Dict[str, Any]:
        return {
            "knowledge_in": deepcopy(knowledge_in),
            "dialog": [
                {"role": "user", "content": user_text},
                {"role": "assistant", "content": assistant_text}
            ],
            "knowledge_out": deepcopy(knowledge_out),
        }

    def _sample_context(self, exclude_slot: str, max_other_slots: int = 3) -> Dict[str, str]:
        other_slots = [s for s in self.slots.keys() if s != exclude_slot]
        count = self.rng.randint(0, min(max_other_slots, len(other_slots)))
        chosen = self.rng.sample(other_slots, count)
        ctx = {}
        for slot in chosen:
            value = self._choice(self.slots[slot]["values"])
            ctx[slot] = value
        return ctx


    def _iter_action_fill_pairs(self):
        action_cfg = self.slots["action"]
        for canonical in action_cfg["values"]:
            for user_variant in action_cfg["fill_map"][canonical]:
                for assistant_variant in action_cfg["fill_assistant_map"][canonical]:
                    yield canonical, user_variant, assistant_variant

    def generate_opening_samples(self) -> List[Dict[str, Any]]:
        samples = []
        for slot, cfg in self.slots.items():
            # empty context
            for user_text in cfg["open_user"]:
                for assistant_text in cfg["open_assistant"]:
                    knowledge_out = {slot: "unknown"}
                    samples.append(self._make_sample({}, user_text, assistant_text, knowledge_out))

            # with cross-slot context
            for _ in range(16):
                ctx = self._sample_context(slot, max_other_slots=3)
                user_text = self._choice(cfg["open_user"])
                assistant_text = self._choice(cfg["open_assistant"])
                knowledge_out = deepcopy(ctx)
                knowledge_out[slot] = "unknown"
                samples.append(self._make_sample(ctx, user_text, assistant_text, knowledge_out))
        return samples


    def generate_fill_samples(self) -> List[Dict[str, Any]]:
        samples = []
        for slot, cfg in self.slots.items():
            if slot == "action":
                # unknown -> value
                for canonical, user_text, assistant_text in self._iter_action_fill_pairs():
                    samples.append(
                        self._make_sample(
                            {"action": "unknown"},
                            user_text,
                            assistant_text,
                            {"action": canonical}
                        )
                    )
                # cross-slot unknown -> value
                for canonical, user_text, assistant_text in self._iter_action_fill_pairs():
                    ctx = self._sample_context("action", max_other_slots=3)
                    knowledge_in = deepcopy(ctx)
                    knowledge_in["action"] = "unknown"
                    knowledge_out = deepcopy(ctx)
                    knowledge_out["action"] = canonical
                    samples.append(self._make_sample(knowledge_in, user_text, assistant_text, knowledge_out))
            else:
                for value in cfg["values"]:
                    for user_t in cfg["fill_user_templates"]:
                        for assistant_t in cfg["fill_assistant_templates"]:
                            user_text = user_t.format(value=value)
                            assistant_text = assistant_t.format(value=value)
                            samples.append(
                                self._make_sample(
                                    {slot: "unknown"},
                                    user_text,
                                    assistant_text,
                                    {slot: value}
                                )
                            )
                    # cross-slot
                    ctx = self._sample_context(slot, max_other_slots=3)
                    knowledge_in = deepcopy(ctx)
                    knowledge_in[slot] = "unknown"
                    knowledge_out = deepcopy(ctx)
                    knowledge_out[slot] = value

                    user_text = self._choice(cfg["fill_user_templates"]).format(value=value)
                    assistant_text = self._choice(cfg["fill_assistant_templates"]).format(value=value)
                    samples.append(self._make_sample(knowledge_in, user_text, assistant_text, knowledge_out))
        return samples


    def generate_update_samples(self) -> List[Dict[str, Any]]:
        samples = []
        for slot, cfg in self.slots.items():
            if slot == "action":
                vals = cfg["values"]
                # random pair transitions
                pairs = set()
                while len(pairs) < min(500, len(vals) * 6):
                    old_v = self._choice(vals)
                    new_v = self._choice(vals)
                    if old_v != new_v:
                        pairs.add((old_v, new_v))
                for old_v, new_v in pairs:
                    # use fill variants as update payload
                    user_base = self._choice(cfg["fill_map"][new_v])
                    # rewrite to "Now I am..." when possible
                    if user_base.startswith("I am "):
                        user_text = "Now " + user_base[2:] # TODO: 2-?
                    elif user_base.startswith("I "):
                        user_text = "Now " + user_base
                    else:
                        user_text = "Now I am " + user_base.rstrip(".") + "."
                    assistant_text = self._choice(cfg["fill_assistant_map"][new_v])
                    if assistant_text.startswith("Got it, you are "):
                        assistant_text = "Got it, now you are " + assistant_text[len("Got it, you are "):]
                    elif assistant_text.startswith("Got it, you are"):
                        assistant_text = assistant_text.replace("Got it, you are", "Got it, now you are", 1)
                    elif assistant_text.startswith("Got it, you "):
                        assistant_text = "Got it, now " + assistant_text[len("Got it, "):]
                    else:
                        assistant_text = "Got it, now " + assistant_text[len("Got it, "):] if assistant_text.startswith("Got it, ") else "Got it, now " + assistant_text

                    samples.append(
                        self._make_sample(
                            {"action": old_v},
                            user_text,
                            assistant_text,
                            {"action": new_v}
                        )
                    )
                    # cross-slot
                    ctx = self._sample_context("action", max_other_slots=3)
                    k_in = deepcopy(ctx)
                    k_in["action"] = old_v
                    k_out = deepcopy(ctx)
                    k_out["action"] = new_v
                    samples.append(self._make_sample(k_in, user_text, assistant_text, k_out))
            else:
                vals = cfg["values"]
                for old_v in vals:
                    for new_v in vals:
                        if old_v == new_v:
                            continue
                        user_text = self._choice(cfg["update_user_templates"]).format(value=new_v)
                        assistant_text = self._choice(cfg["update_assistant_templates"]).format(value=new_v)
                        samples.append(
                            self._make_sample(
                                {slot: old_v},
                                user_text,
                                assistant_text,
                                {slot: new_v}
                            )
                        )
                        # cross-slot
                        ctx = self._sample_context(slot, max_other_slots=3)
                        k_in = deepcopy(ctx)
                        k_in[slot] = old_v
                        k_out = deepcopy(ctx)
                        k_out[slot] = new_v
                        samples.append(self._make_sample(k_in, user_text, assistant_text, k_out))
        return samples


    def generate_retrieval_samples(self) -> List[Dict[str, Any]]:
        samples = []
        for slot, cfg in self.slots.items():
            # unknown retrieval
            samples.append(
                self._make_sample(
                    {slot: "unknown"},
                    self._choice(cfg["retrieve_user"]),
                    cfg["retrieve_assistant"].format(value="unknown"),
                    {slot: "unknown"}
                )
            )

            for value in cfg["values"]:
                samples.append(
                    self._make_sample(
                        {slot: value},
                        self._choice(cfg["retrieve_user"]),
                        cfg["retrieve_assistant"].format(value=value),
                        {slot: value}
                    )
                )
                # cross-slot retrieval
                ctx = self._sample_context(slot, max_other_slots=3)
                k_in = deepcopy(ctx)
                k_in[slot] = value
                k_out = deepcopy(k_in)
                samples.append(
                    self._make_sample(
                        k_in,
                        self._choice(cfg["retrieve_user"]),
                        cfg["retrieve_assistant"].format(value=value),
                        k_out
                    )
                )
        return samples


    def generate_cross_slot_disambiguation(self) -> List[Dict[str, Any]]:
        samples = []
        slot_names = list(self.slots.keys())

        # opening target slot while another slot already exists
        for target_slot in slot_names:
            cfg = self.slots[target_slot]
            for other_slot in slot_names:
                if other_slot == target_slot:
                    continue
                other_value = self._choice(self.slots[other_slot]["values"])
                knowledge_in = {other_slot: other_value}
                knowledge_out = {other_slot: other_value, target_slot: "unknown"}
                samples.append(
                    self._make_sample(
                        knowledge_in,
                        self._choice(cfg["open_user"]),
                        self._choice(cfg["open_assistant"]),
                        knowledge_out
                    )
                )

        # retrieval of one slot while others exist
        for target_slot in slot_names:
            cfg = self.slots[target_slot]
            for other_slots_n in [1, 2, 3, 4]:
                others = [s for s in slot_names if s != target_slot]
                if len(others) < other_slots_n:
                    continue
                picked = self.rng.sample(others, other_slots_n)
                knowledge_in = {target_slot: self._choice(cfg["values"])}
                for s in picked:
                    knowledge_in[s] = self._choice(self.slots[s]["values"])
                samples.append(
                    self._make_sample(
                        knowledge_in,
                        self._choice(cfg["retrieve_user"]),
                        cfg["retrieve_assistant"].format(value=knowledge_in[target_slot]),
                        knowledge_in
                    )
                )
        return samples

    def dedupe(self, samples: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        seen: Set[str] = set()
        result = []
        for sample in samples:
            key = json.dumps(sample, ensure_ascii=False, sort_keys=True)
            if key not in seen:
                seen.add(key)
                result.append(sample)
        return result

    def generate_all(self) -> List[Dict[str, Any]]:
        samples = []
        samples.extend(self.generate_opening_samples())
        samples.extend(self.generate_fill_samples())
        samples.extend(self.generate_update_samples())
        samples.extend(self.generate_retrieval_samples())
        samples.extend(self.generate_cross_slot_disambiguation())
        samples = self.dedupe(samples)
        self.rng.shuffle(samples)
        return samples


def save_dataset_json(path: str, data: List[Dict[str, Any]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    gen = SlotDatasetGenerator(seed=42)
    data = gen.generate_all()
    print(f"Generated samples: {len(data)}")
    save_dataset_json("slot-dataset-8-gen.json", data)
    print("Saved to slot-dataset-8-gen.json")


if __name__ == "__main__":
    main()
