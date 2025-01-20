import time
import threading

# Function to simulate checking notifications
def check_notification():
    print("John is checking his notifications...")

# Function to simulate eating the sandwich
def eat_sandwich():
    print("John is eating his sandwich...")
    time.sleep(8)  # 8 minutes to eat the sandwich

# Function to simulate drinking tea
def drink_tea():
    print("John is drinking his tea...")
    time.sleep(3)  # 3 minutes to drink tea
    check_notification()  # Multitasking: Checking notifications during tea

# Function to simulate eating the fruit
def eat_fruit():
    print("John is eating his fruit...")
    time.sleep(2)  # 2 minutes to eat fruit

# Function to simulate scrolling through social media
def scroll_social_media():
    print("John is scrolling through social media...")
    time.sleep(10)  # 10 minutes of social media time

# Function to run the entire breakfast routine with threads
def breakfast_routine_multithreading():
    # Create threads for each task
    sandwich_thread = threading.Thread(target=eat_sandwich)
    tea_thread = threading.Thread(target=drink_tea)
    fruit_thread = threading.Thread(target=eat_fruit)
    social_media_thread = threading.Thread(target=scroll_social_media)
    
    # Start all threads
    sandwich_thread.start()
    tea_thread.start()
    fruit_thread.start()
    social_media_thread.start()
    
    # Join the threads to ensure completion before exiting
    sandwich_thread.join()
    tea_thread.join()
    fruit_thread.join()
    social_media_thread.join()

# Run the breakfast routine with multithreading
breakfast_routine_multithreading()
