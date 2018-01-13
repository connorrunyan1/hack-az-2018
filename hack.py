# hack by Alex Katzfey, Connor Runyan, & Jake Given

import pygame.camera
import pygame.image

# wait for button press here, when it happens call onPress

def onPress():
  pygame.camera.init()
  cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
  cam.start()
  img = cam.get_image()
  pygame.image.save(img, "image.png")
  pygame.camera.quit()





# send image to amazon recognition

# get back result ( display as text )

# send result to amazon polly

# get back speech from polly

# send to speaker
