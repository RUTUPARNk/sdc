import csv

# Open a CSV file to record the data
with open('driving_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['image', 'input'])

    while True:
        # Capture the screen
        screen = capture_screen(driver)
        
        # Process the image
        contours = process_image(screen)
        
        # Decide the movement
        movement = Keys.UP  # Replace with actual key input you made
        
        # Save the screen and movement to the CSV
        writer.writerow([screen, movement])
        
        # Send the key press
        body.send_keys(movement)
        
        # Small delay to control the frequency of commands
        time.sleep(0.1)

