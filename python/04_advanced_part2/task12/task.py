def generate_c_code(port, direction):

    print('void init_port(){\n')
     
    print('DDR' + port.capitalize() + ' = 0b', end='')
    
    for dir in reversed(direction):
        if dir == 'in':
            print('0', end='')
        elif dir == 'out':
            print('1', end='') 
    print(';\n\n}')

port = input("Enter the port: ")
direction = []
for i in range(8):
    dir = input(f"Enter the direction for pin {i}: ")
    if dir != 'in' and dir != 'out':
         print("Invalid direction. Please enter 'in' or 'out'.")
         break
    direction.append(dir)

generate_c_code(port, direction)


