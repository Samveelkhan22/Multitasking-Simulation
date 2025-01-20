import time

# Function to simulate John's breakfast tasks with multitasking
def check_notification():
    print("John is checking his notifications...")

def breakfast_routine_with_multitasking():
    print("John is eating his sandwich...")
    time.sleep(8)  # 8 minutes to eat the sandwich
    
    # John waits for the tea to cool down and checks notifications
    print("John is drinking his tea...")
    time.sleep(3)  # John drinks tea for 3 minutes
    check_notification()  # Multitasking: Checking notifications during tea
    print("John is eating his fruit...")
    time.sleep(2)  # John eats his fruit
    
    print("John is scrolling through social media...")
    time.sleep(10)  # 10 minutes of social media time

# Run the breakfast routine with multitasking
breakfast_routine_with_multitasking()
