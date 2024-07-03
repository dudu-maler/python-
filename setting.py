class Settings:
    """存储游戏《《外星人入侵》》中的所有设置类"""

    def __init__(self):
        self.width = 1200
        self.height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.alien_speed = 0.1
        self.fleet_drop_speed = 4.0
        # fleet_direction为1表示向右移，为-1表示向左移
        self.fleet_direction = 1


