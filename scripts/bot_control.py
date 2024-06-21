def decide_movement(model, image):
    # Preprocess the image
    image = cv2.resize(image, (64, 64))
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    
    # Predict the input
    prediction = model.predict(image)
    
    # Convert the prediction to a key press
    if prediction < 0.5:
        return Keys.LEFT
    else:
        return Keys.RIGHT

# Main loop
while True:
    # Capture the screen
    screen = capture_screen(driver)
    
    # Decide the movement
    movement = decide_movement(model, screen)
    
    # Send the key press
    body.send_keys(movement)
    
    # Small delay to control the frequency of commands
    time.sleep(0.1)

