import time
import sys
import curses
import threading

def animated_text(stdscr, stop_flag):
    curses.curs_set(0)  # Hide the cursor
    dot_count = 0

    while not stop_flag.is_set():
        stdscr.addstr(0, 0, 'Loading' + '.' * dot_count)
        stdscr.refresh()
        time.sleep(0.5)

        dot_count = (dot_count + 1) % 4  # Reset dot count after 3 dots
        stdscr.addstr(0, 0, ' ' * 10)  # Clear the line
        sys.stdout.flush()

    stdscr.addstr(0, 0, 'Animation stopped')
    stdscr.refresh()

def other_function(stop_flag):
    time.sleep(5)  # Simulating some work
    result = "Finished work!"
    stop_flag.set()  # Set the flag to stop the animation
    return result

def main(stdscr):
    stop_flag = threading.Event()

    # Start the animation thread
    animation_thread = threading.Thread(target=animated_text, args=(stdscr, stop_flag))
    animation_thread.start()

    # Run the other function
    result = other_function(stop_flag)

    # Wait for the animation thread to finish
    animation_thread.join()

    # Display the result
    stdscr.addstr(1, 0, result)
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
