from typing import Union
import pygame
from pygame import Surface
from pygame.surface import SurfaceType

class Text:
    """专门用来显示文本(注意只能显示一行)"""
    message_image: Union[Surface, SurfaceType]
    message_image_rect: Union[Surface, SurfaceType]

    def __init__(self, screen, centerX, centerY, txt_color, message, font, font_size):
        self.screen = screen
        self.centerX = centerX
        self.centerY = centerY
        self.txt_color = txt_color
        self.message = message
        self.font = pygame.font.SysFont(font, font_size)
        self.prepare_message()# 放在__init__中，从而一开始就有

    def prepare_message(self):
        """把msg渲染成图像"""
        self.message_image = self.font.render(self.message, True, self.txt_color)# 把字体文件渲染成图像，第一个参数是文本信息，第二个是是否开启防锯齿，即是否让边缘平滑，第三个是字体颜色，第四个是背景的颜色，这个背景是刚好把文字包括起来的一个矩形，不填则为透明背景
        self.message_image_rect = self.message_image.get_rect()# 获取参数
        self.message_image_rect.center = (self.centerX, self.centerY)# 放在指定位置

    def draw_text(self):
        """绘制text的图片"""
        self.screen.blit(self.message_image, self.message_image_rect)
