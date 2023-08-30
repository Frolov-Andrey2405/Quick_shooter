import random
import sys
import time


class FastDrawGame:
    def __init__(self):
        print('''
Fast Draw
\nTime to test your reflexes and see if you are the fastest draw in the west!
When you see "DRAW", you have 0.3 seconds to press Enter.
But you lose if you press Enter before "DRAW" appears
\nPress Enter to begin...
''')
        input()

    def run(self):
        while True:
            print()
            print('It is high noon...')
            time.sleep(random.uniform(2.0, 5.0))
            print('DRAW!')
            draw_time = time.time()
            # This function call doesn't return until Enter is pressed.
            input()
            time_elapsed = time.time() - draw_time

            if time_elapsed < 0.01:
                print('You drew before "DRAW" appeared! You lose.')
            elif time_elapsed > 0.3:
                time_elapsed = round(time_elapsed, 4)
                print(f'You took {time_elapsed} seconds to draw. Too slow!')
            else:
                time_elapsed = round(time_elapsed, 4)
                print(f'You took {time_elapsed} seconds to draw.')
                print('You are the fastest draw in the west! You win!')

            response = input(
                '\nEnter QUIT to stop, or press Enter to play again: ').upper()
            if response == 'QUIT':
                print('Thanks for playing!')
                sys.exit()


if __name__ == '__main__':
    game = FastDrawGame()
    game.run()
