import pyautogui, time

def main():
    pyautogui.PAUSE = 0 #set duration between each click
    while True:
        pyautogui.click() #left click
        pyautogui.click(button="right") #right click


if __name__ == "__main__":
    time.sleep(2) #just some time to get things ready (not necessary; feel free to delete)
    print("sleep finished")
    main();