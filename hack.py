# hack by Alex Katzfey, Connor Runyan, & Jake Given

import pygame.camera
import pygame.image
import base64
import boto3

# wait for button press here, when it happens call onPress

def onPress():
  pygame.camera.init()
  cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
  cam.start()
  img = cam.get_image()
  pygame.image.save(img, "image.png")
  pygame.camera.quit()

  image = open("image.png", "rb")
  image_read = image.read()
  image_64_encode = base64.encodestring(image_read)
  
  print(image_64_encode)
  
  client = boto3.client('rekognition')
  
  response = client.detect_labels(
    Image = {
      "Bytes": image_64_encode
    },
    MaxLabels=100,
    MinConfidence=50.0
  )
  
  print(response)

# send image to amazon recognition

# get back result ( display as text )

# send result to amazon polly

# get back speech from polly

# send to speaker

onPress()
