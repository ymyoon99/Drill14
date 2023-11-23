
from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(500, 500) # 실제코드에서는 하드코드 쓰지않도록
game_framework.run(start_mode)
close_canvas()

