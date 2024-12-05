import time
import os
import sys
import argparse
from plyer import notification
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

if os.name == 'nt':
    import msvcrt
else:
    import select
    import termios
    import tty

class NonBlockingConsole:
    def __enter__(self):
        if os.name != 'nt':
            self.fd = sys.stdin.fileno()
            self.old_settings = termios.tcgetattr(self.fd)
            tty.setcbreak(self.fd)
        return self

    def __exit__(self, type, value, traceback):
        if os.name != 'nt':
            termios.tcsetattr(self.fd, termios.TCSADRAIN, self.old_settings)

    def get_char(self):
        if os.name == 'nt':
            # Windows
            if msvcrt.kbhit():
                ch = msvcrt.getch()
                try:
                    return ch.decode('utf-8')
                except UnicodeDecodeError:
                    return ''
            else:
                return None
        else:
            # Unix-like system
            dr, dw, de = select.select([sys.stdin], [], [], 0)
            if dr:
                return sys.stdin.read(1)
            return None

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown(minutes, message):
    """Starts the countdown timer with pause and resume functionality."""
    total_seconds = minutes * 60
    paused = False

    with NonBlockingConsole() as nbc:
        while total_seconds >= 0:
            if not paused:
                mins, secs = divmod(total_seconds, 60)
                timer = f"{mins:02}:{secs:02}"
                print(f"{Fore.CYAN}{message}: {timer}  Press 'p' to pause/resume, 'q' to quit.", end="\r")
                total_seconds -= 1
                time.sleep(1)
            else:
                mins, secs = divmod(total_seconds, 60)
                print(f"{Fore.YELLOW}{message} paused at {mins:02}:{secs:02}. Press 'p' to resume, 'q' to quit.     ", end="\r")
                time.sleep(1)

            # Check for user input
            user_input = nbc.get_char()
            if user_input:
                user_input = user_input.lower()
                if user_input == 'p':
                    paused = not paused
                    if paused:
                        print(f"\n{Fore.YELLOW}{message} paused. Press 'p' to resume, 'q' to quit.     ")
                    else:
                        print(f"\n{Fore.GREEN}{message} resumed.     ")
                elif user_input == 'q':
                    print(f"\n{Fore.RED}{message} stopped by user.")
                    return

        # When the countdown finishes
        print(f"\n{Fore.GREEN}{message} complete! Time's up!                               ")
        # Notification sound
        if os.name == 'nt':
            os.system('echo \a')
        else:
            sys.stdout.write('\a')
            sys.stdout.flush()

        # Desktop notification
        notification.notify(
            title="Pomodoro Timer",
            message=f"{message} complete! Time's up!",
            timeout=10
        )

def prompt_user_to_start(message):
    """Prompts the user to start the next session."""
    input(f"\n{Style.BRIGHT}Press Enter to start {message} session...")

def pomodoro_timer(work_duration, short_break, long_break):
    """Runs the Pomodoro timer indefinitely."""
    session_count = 0   # Tracks the number of work sessions

    try:
        while True:
            clear_screen()
            session_count += 1
            print(f"{Style.BRIGHT}{Fore.MAGENTA}Session {session_count}: Work for {work_duration} minutes.")
            prompt_user_to_start("Work")
            countdown(work_duration, "Work")

            if session_count % 4 == 0:
                print(f"\n{Fore.BLUE}Take a long break for {long_break} minutes.")
                prompt_user_to_start("Long Break")
                countdown(long_break, "Long Break")
            else:
                print(f"\n{Fore.BLUE}Take a short break for {short_break} minutes.")
                prompt_user_to_start("Short Break")
                countdown(short_break, "Short Break")

    except KeyboardInterrupt:
        clear_screen()
        print(f"{Fore.RED}Pomodoro timer stopped. Stay productive!")

def main():
    parser = argparse.ArgumentParser(description="A simple Pomodoro timer.")
    parser.add_argument('-w', '--work', type=int, default=25,
                        help='Work duration in minutes (default: 25)')
    parser.add_argument('-s', '--short_break', type=int, default=5,
                        help='Short break duration in minutes (default: 5)')
    parser.add_argument('-l', '--long_break', type=int, default=15,
                        help='Long break duration in minutes (default: 15)')

    args = parser.parse_args()

    pomodoro_timer(args.work, args.short_break, args.long_break)

if __name__ == "__main__":
    main()
