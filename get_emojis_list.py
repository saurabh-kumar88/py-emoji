from emoji.unicode_codes import data_dict

EMOJI_DICT = data_dict.EMOJI_DATA
def supported_emoji_names():
  with open("emoji_list.txt", "w") as file:
    for key in EMOJI_DICT.keys():
      print(EMOJI_DICT.get(key).get('en') + "  " + key + "\n")
      # file.write(str(EMOJI_DICT.get(key).get('en') + "  " + key + "\n"))
      
if __name__=="__main__":
  supported_emoji_names()

  