import requests

def compose_question(passage):
    resp = requests.post("https://api.ai21.com/studio/v1/j1-jumbo/complete",
        headers={"Authorization": "Bearer 5ORlDMHctx05Hqa9rhV4gMgMY4QAmiDG"},
        json={
            "prompt": f"Write test questions based on the information in these passages.\n\nPassage: The primary exporters of fresh pineapples are Costa Rica, Côte d'Ivoire, and the Philippines. \nQuestion: Which countries export pineapples?\n\nPassage: A skunk's smell can be detected by a human a mile away. \nQuestion: From how far away can you smell a skunk? \n\nPassage: Peter Minuit purchased the island of Manhattan from Native Americans on May 24, 1626 for goods valued at 60 Dutch guilders, which in the 19th century was estimated to be the equivalent of US$24 (or $680 today).\nQuestion: For how much was Manhattan island bought?\n\nPassage: Alfred Pennyworth is a former agent of MI-6, along with being Bruce Wayne's butler and bodyguard.\nQuestion: Who is Batman's butler?\n\nPassage: There was a man named Elkonoh from the land of Ephrayim. He had two wives; the name of one was Chana and the name of the second was Penina. \nQuestion: Who were Elkonoh's two wives?\n\nPassage: And the man Elqana, and all his house, went up to offer to the Lord his yearly sacrifice, and vow. But Hanna did not go up; for she said to her husband, I will not go up until the child is weaned, and then I will bring him, that he may appear before the Lord, and there abide for ever. \nQuestion: Who did not go up?\n\nPassage: {passage}\nQuestion:",
            "numResults": 1,
            "maxTokens": 207,
            "temperature": 0.3,
            "topKReturn": 0,
            "topP":1,
            "countPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "frequencyPenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
            },
            "presencePenalty": {
                "scale": 0,
                "applyToNumbers": False,
                "applyToPunctuations": False,
                "applyToStopwords": False,
                "applyToWhitespaces": False,
                "applyToEmojis": False
        },
        "stopSequences":["Jargon:","↵↵"]
        }
    )
    return resp.json()['completions'][0]['data']['text'][1:]

if __name__ == '__main__':

    passage = 'Balak son of Zippor saw all that Israel had done to the Amorites. Moab was alarmed because that people was so numerous. Moab dreaded the Israelites, and Moab said to the elders of Midian, “Now this horde will lick clean all that is about us as an ox licks up the grass of the field.” Balak son of Zippor, who was king of Moab at that time, sent messengers to Balaam son of Beor in Pethor, which is by the Euphrates,* in the land of his kinsfolk, to invite him, saying, “There is a people that came out of Egypt; it hides the earth from view, and it is settled next to me. Come then, put a curse upon this people for me, since they are too numerous for me; perhaps I can thus defeat them and drive them out of the land. For I know that whomever you bless is blessed indeed, and whomever you curse is cursed.” The elders of Moab and the elders of Midian, versed in divination,* set out. They came to Balaam and gave him Balak’s message.'
    
    print(compose_question(passage))
    
    pass