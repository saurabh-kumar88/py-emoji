import emoji
from time import sleep


emoji_list = [
  'cowboy_hat_face',
  'rolling_on_the_floor_laughing',
  'thumbs_up',
  'folded_hands',
  'face_blowing_a_kiss',
  'smiling_face_with_hearts',
  'smiling_face_with_heart-eyes',
  
]

def display():

  for _emoji in emoji_list:
    print(emoji.emojize("{} - :{}:".format(_emoji, _emoji)))
    sleep(0.5)
  print()
  print(emoji.emojize('Thanks for watching! :smiling_face_with_open_hands:'))


if __name__=="__main__":
  display()