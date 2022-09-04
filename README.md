# Game 2048 with gesture control

This project recreated the functionality of the game 2048.
Implemented the functions of undo last move, counting and saving the best score of the selected player.
The project uses OpenCV and Mediapipe for gesture recognition. 
To run the game without recognition, use the Game2048.py script. 
To run with recognition - Gesture_control.py. 

## Gesture control

To swap the playing field to the sides, use the index finger of your right hand.

![swapping](https://user-images.githubusercontent.com/112019541/187035116-6f8f3677-8171-4fd8-9b4c-41f2aabb27f3.png)

After the swap, there is a delay before the next move to avoid false positives. To undo a move, make a fist with your other fingers.

![undo](https://user-images.githubusercontent.com/112019541/187035314-ea15e242-4fa4-4dad-b0f7-942f0486810e.png)

To start a new game, squeeze your thumb.

![new_game](https://user-images.githubusercontent.com/112019541/187035450-f801cf10-cb99-4682-a8dd-dad0d318e42e.png)

## Video

![Game2048](https://user-images.githubusercontent.com/112019541/186515193-4edaa4ac-3388-4352-a538-23513f98f1a3.gif)

[![2048 with gesture control](https://user-images.githubusercontent.com/112019541/188335415-9409f2cc-e81f-436d-9232-51f418bbdaf7.jpg)](https://www.youtube.com/watch?v=AkxwrQtRAdE&ab_channel=%D0%98%D0%BB%D1%8C%D1%8F%D0%90%D0%B7%D0%B8%D0%BD)
[Full video](https://www.youtube.com/watch?v=AkxwrQtRAdE&ab_channel=%D0%98%D0%BB%D1%8C%D1%8F%D0%90%D0%B7%D0%B8%D0%BD)
