# hack by Alex Katzfey, Connor Runyan, & Jake Given

import pygame.camera
import pygame.image

# wait for button press here, when it happens call onPress

sudo apt-get install mercurial python3-dev python3-setuptools python3-numpy python3-opengl \
    libav-tools libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsmpeg-dev \
    libsdl1.2-dev libportmidi-dev libswscale-dev libavformat-dev libavcodec-dev \
    libtiff5-dev libx11-6 libx11-dev fluid-soundfont-gm timgm6mb-soundfont \
    xfonts-base xfonts-100dpi xfonts-75dpi xfonts-cyrillic fontconfig fonts-freefont-ttf


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
