def towersHanoi(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return (towersHanoi(n-1) * 2) + 1

def main():
    while True:
        choice = input("Enter the value for number of disks in Towers of Hanoi game:")
        if not choice:
            print("No input recieved.")
        else:
            try:
                choice_int = int(choice)
                if choice_int > -1:
                    break
            except ValueError:
                print("Invalid input.")
                
    steps = towersHanoi(choice_int)
    print("The number of steps to most optimally finish a game of Towers of Hanoi with", choice, "disks is", steps)

main()
          
    
                
