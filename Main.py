import Screen, Space
    
def main():
    space = Space.space(500,500)
    user_interface = Screen.screen(space)
    user_interface.running()

if __name__ == '__main__' : 
    main()