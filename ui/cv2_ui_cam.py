import cv2
import numpy as np
import math


def image_game_field(visual_field, current_score, max_score, game_over):

    height = 720
    width = 640

    font = cv2.FONT_HERSHEY_DUPLEX
    frame = np.zeros((height, width, 3), np.uint8)

    frame[:] = [255, 255, 255]

    for i in range(4):
        for j in range(4):
            coord = [i, j]
            value = visual_field[i][j]

            r = 255
            g = 255
            b = 255

            x1 = 10 + coord[1] * 150 + coord[1] * 10
            x2 = 150 + coord[1] * 150 + coord[1] * 10
            y1 = 10 + coord[0] * 150 + coord[0] * 10
            y2 = 150 + coord[0] * 150 + coord[0] * 10

            font_scale = 1
            text_coordinate = [x1 + 10, y2 + 10]

            if value > 0:
                step = math.log2(value)
                step = int(step)
            else:
                step = 0

            if step == 1:
                r = 255
                g = 217
                b = 217
            elif step == 2:
                r = 255
                g = 140
                b = 255
            elif step == 3:
                r = 255
                g = 0
                b = 255
            elif step == 4:
                r = 255
                g = 3
                b = 5
            elif step == 5:
                r = 255
                g = 139
                b = 105
            elif step == 6:
                r = 255
                g = 139
                b = 3
            elif step == 7:
                r = 255
                g = 255
                b = 3
            elif step == 8:
                r = 140
                g = 255
                b = 255
            elif step == 9:
                r = 140
                g = 85
                b = 255
            elif step == 10:
                r = 94
                g = 248
                b = 133
            elif step == 11:
                r = 140
                g = 85
                b = 52
            elif step == 12:
                r = 41
                g = 85
                b = 52
            elif step > 12:
                r = 41
                g = 85
                b = 239

            frame[y1:y2, x1:x2] = [b, g, r]

            str_value = str(value)
            nums = len(str_value)

            if nums == 1:
                font_scale = 5
                text_coordinate = [x1 + 19, y2 - 16]
            elif nums == 2:
                font_scale = 3.9
                text_coordinate = [x1 - 11, y2 - 30]
            elif nums == 3:
                font_scale = 2.5
                text_coordinate = [x1 - 6, y2 - 43]
            elif nums == 4:
                font_scale = 1.7
                text_coordinate = [x1, y2 - 50]
            elif nums >= 5:
                font_scale = 1.3
                text_coordinate = [x1 + 3, y2 - 55]

            if value > 0:
                cv2.putText(frame, str(value), text_coordinate, font, font_scale, (0, 0, 0), 1, cv2.LINE_AA)

            text = 'Press "Esc" to exit'
            cv2.putText(frame, text, (15, 665), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

            text = 'Score: ' + str(current_score) + '   Best score: ' + str(max_score)
            cv2.putText(frame, text, (15, 700), font, 1, (0, 0, 0), 1, cv2.LINE_AA)

    if game_over:
        original_alpha = 3
        frame = frame / original_alpha

        frame[frame > 255] = 255  # Обрезать до 255 для значений больше 255
        frame = frame.astype(np.uint8)  # Окончательно преобразовано в значение от 0 до 255

        text = 'GAME OVER'
        cv2.putText(frame, text, (50, 350), font, 3, (255, 255, 255), 3, cv2.LINE_AA)

        text = 'Press "Esc" to exit'
        cv2.putText(frame, text, (165, 400), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    cv2.imshow('2048', frame)

    return frame


if __name__ == '__main__':  # данная точка входа только для отладки функции выше

    game_field = np.zeros((4, 4), dtype=int)

    game_field[0][0] = 2
    game_field[0][1] = 4
    game_field[0][2] = 8
    game_field[0][3] = 16

    game_field[1][0] = 32
    game_field[1][1] = 64
    game_field[1][2] = 128
    game_field[1][3] = 256

    game_field[2][0] = 512
    game_field[2][1] = 1024
    game_field[2][2] = 2048
    game_field[2][3] = 4096

    game_field[3][0] = 8192
    game_field[3][1] = 16384
    game_field[3][2] = 32768
    game_field[3][3] = 0

    score = 68
    best_score = 222
    end_game = True
    img = image_game_field(game_field, score, best_score, end_game)

    while True:

        if cv2.waitKey(0) == 27:
            break

    cv2.destroyAllWindows()
