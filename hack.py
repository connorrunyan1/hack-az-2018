# hack by Alex Katzfey, Connor Runyan, & Jake Given

import pygame.camera
import pygame.image
import pygame
import base64
import boto3

# wait for button press here, when it happens call onPress

def onPress():
  pygame.init()
  pygame.mixer.init()
  pygame.mixer.music.load('taking.mp3')
  pygame.mixer.music.play()
  pygame.camera.init()
  cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
  cam.start()
  img = cam.get_image()
  print('Picture Taken.')

  pygame.image.save(img, "image.png")
  pygame.camera.quit()
  
  image = open("image.png", "rb")
  image_read = image.read()
  #image_64_encode = base64.encodestring(image_read)
  b = bytearray(image_read)
  
  # send image to amazon recognition
  print('Sending to AWS Rekognition.')
  client = boto3.client('rekognition')
  
  response = client.detect_labels(
    Image = {
      "Bytes": b
    },
    MaxLabels=100,
    MinConfidence=80.0
  )
  
  # get back result ( display as text )
  
  #print(response)
  
  labels = response['Labels']
  
  text = ""
  
  if(len(labels) != 0):
    for label in labels:
      #print(str(label['Name']) + " " + str(label['Confidence']) + "%")
      text = text + str(label['Name']) + ", "
  
    # send result to amazon polly
    print('Sending to AWS Polly.')
    client2 = boto3.client('polly')

    voice = client2.synthesize_speech(
      OutputFormat='mp3',
      SampleRate='22050',
      Text=text,
      TextType='text',
      #VoiceId='Geraint'|'Gwyneth'|'Mads'|'Naja'|'Hans'|'Marlene'|'Nicole'|'Russell'|'Amy'|'Brian'|'Emma'|'Raveena'|'Ivy'|'Joanna'|'Joey'|'Justin'|'Kendra'|'Kimberly'|'Matthew'|'Salli'|'Conchita'|'Enrique'|'Miguel'|'Penelope'|'Chantal'|'Celine'|'Mathieu'|'Dora'|'Karl'|'Carla'|'Giorgio'|'Mizuki'|'Liv'|'Lotte'|'Ruben'|'Ewa'|'Jacek'|'Jan'|'Maja'|'Ricardo'|'Vitoria'|'Cristiano'|'Ines'|'Carmen'|'Maxim'|'Tatyana'|'Astrid'|'Filiz'|'Vicki'|'Takumi'|'Seoyeon'|'Aditi'
      VoiceId='Matthew'
    )

    # get back speech from polly

    voiceBytes = voice['AudioStream'].read()  

    #print(voiceBytes)

    with open('output.mp3', 'wb') as w:
      w.write(voiceBytes)

    pygame.mixer.music.load('output.mp3')
    print('Playing Audio.')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(1) 
      
  else:
    pygame.mixer.music.load('nothing.mp3')
    print('Nothing Found.')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
      pygame.time.Clock().tick(1)   
  
  

onPress()
