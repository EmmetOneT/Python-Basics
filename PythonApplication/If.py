##change key press to see change
#key_press = 'l'
##if
#if key_press == 'r':
#    print('Move right')
##elif
#elif key_press == 'l':
#    print('Move Left')
##else
#else:
#    print('Invalid Key')

#command = 'Move right' if key_press == 'r' else 'Invalid Key'

num_lives = 3
health = 0
if health <= 0:
    num_lives -= 1
    print('You lost a life-')
    if num_lives <= 0:
        print ('You died')
elif health <= 10:
    print('Health Warning')
elif health <= 50:
    print ('Warning, less than 50% health')
