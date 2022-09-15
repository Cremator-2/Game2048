import cv2
import mediapipe as mp
from Game2048 import Game2048 as Game
from ui import cv2_ui_cam as vis


if __name__ == '__main__':  # данная точка входа для управления жестами

    x_previous = 320
    mark_x = 320
    y_previous = 240
    mark_y = 240
    dead_zone_left_right = 40
    dead_zone_up_down = 80
    chatter_protection = 20

    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles
    mp_hands = mp.solutions.hands

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    game = Game()

    player = input('Enter the username: ')
    try:
        best_score = Game.read_score(player)
    except IOError:
        best_score = 0
        Game.write_score(player, best_score)

    game_score = 0
    game_end = False
    game_end_lock = False

    with mp_hands.Hands(model_complexity=0,
                        max_num_hands=1,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5) as hands:

        count = 0

        while cap.isOpened():

            count = count + 1

            _, image = cap.read()

            results = hands.process(image)
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:

                    x, y = hand_landmarks.landmark[8].x, hand_landmarks.landmark[8].y
                    x = int(x * 640)
                    y = int(y * 480)

                    if y > (y_previous + dead_zone_up_down) and count > (chatter_protection - 5):
                        game_end, game_score = game.swap_down()
                        print('{} Down'.format(count))
                        count = 0
                        continue

                    if y < (y_previous - dead_zone_up_down) and count > (chatter_protection - 5):
                        game_end, game_score = game.swap_up()
                        print('{} Up'.format(count))
                        count = 0
                        continue

                    if x > (x_previous + dead_zone_left_right) and count > chatter_protection:
                        game_end, game_score = game.swap_left()
                        print('{} Left'.format(count))
                        count = 0
                        continue

                    if x < (x_previous - dead_zone_left_right) and count > chatter_protection:
                        game_end, game_score = game.swap_right()
                        print('{} Right'.format(count))
                        count = 0
                        continue

                    x_9, y_9 = hand_landmarks.landmark[9].x, hand_landmarks.landmark[9].y
                    y_9 = int(y_9 * 480)
                    x_9 = int(x_9 * 640)

                    _, y_12 = hand_landmarks.landmark[12].x, hand_landmarks.landmark[12].y
                    y_12 = int(y_12 * 480)

                    if y_9 < y_12 and count > chatter_protection:
                        print('Undo')
                        game.undo_step()

                    x_4, _ = hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y
                    x_4 = int(x_4 * 640)

                    if x_4 < x_9 and count > chatter_protection:
                        print('Reset')
                        del game
                        game_end_lock = game_end
                        game_end = False
                        game_score = 0
                        game = Game()

                    mp_drawing.draw_landmarks(image,
                                              hand_landmarks,
                                              mp_hands.HAND_CONNECTIONS,
                                              mp_drawing_styles.get_default_hand_landmarks_style(),
                                              mp_drawing_styles.get_default_hand_connections_style())

                    cv2.circle(image, (x, y), 6, (255, 255, 255), 3)

                    x_previous = x
                    y_previous = y

            if game_end:
                game_end_lock = game_end

            if game_score > best_score:
                Game.write_score(player, game_score)
                best_score = Game.read_score(player)

            vis.image_game_field(game.game_field, game_score, best_score, game_end_lock)
            cv2.imshow('Hands control', cv2.flip(image, 1))

            key = cv2.waitKey(10)
            if key == 27:
                break

    cv2.destroyAllWindows()
    cap.release()
