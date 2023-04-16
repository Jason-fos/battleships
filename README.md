# Battleships
(Developer: Jason Foster)

![Mockup image](/docs/features/battleships-mockup.png)

[Live webpage](https://battleships-p.herokuapp.com/)

## Table of Content

1. [Project Goals](#project-goals)
    1. [User Goals](#user-goals)
    2. [Site Owner Goals](#site-owner-goals)
2. [User Experience](#user-experience)
    1. [Target Audience](#target-audience)
    2. [User Requirements and Expectations](#user-requirements-and-expectations)
    3. [User Stories](#user-stories)
3. [Design](#design)
    1. [Design Choices](#design-choices)
    2. [Colour](#colours)
    3. [Fonts](#fonts)
    4. [Structure](#structure)
    5. [Wireframes](#wireframes)
4. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Frameworks & Tools](#frameworks-&-tools)
5. [Features](#features)
6. [Testing](#validation)
    1. [HTML Validation](#HTML-validation)
    2. [CSS Validation](#CSS-validation)
    3. [Accessibility](#accessibility)
    4. [Performance](#performance)
    5. [Device testing](#performing-tests-on-various-devices)
    6. [Browser compatibility](#browser-compatability)
    7. [Testing user stories](#testing-user-stories)
8. [Bugs](#Bugs)
9. [Deployment](#deployment)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

## Project Goals 

### User Goals
- Play a strategy based guesssing game.
- A game that can be played against the computer.
- Create a username and password for logging into the game.
- Have fun.

### Site Owner Goals
- Increase the number of users it has.
- Relative information displayed to the user.
- New users to sign up and create a username and password.
- Fun easy intuitive easy to play game for all ages.

## User Experience

### Target Audience
- Anyone who wants to play the game.
- There is no specific target audience.

### User Requirements and Expectations
- A simple and easy to play game.
- Clear instructions for signing up.
- Relavent information clearly displayed.
- Simple easy to follow game instructions.
- Everything should function as expected.

### User Stories

#### Site User 
1. I want to be able to sign up and create a username.
2. I want to be able to log in as a returning user.
3. I want to see the game instructions before playing.
4. I want the option to play again when the game ends.

#### Site Owner 
5. I want new users to be able to sign up by creating a username and password.
6. I want returning users to be able to log in using their chosen information.
7. I want relative and constant feedback displayed to the user during the game.
8. I want all inut from the user to be validated to avoid errors.
9. I want the user to be presented with a win or lose message on game completion.
10. I want to provide a welcome message using the users chosen username. 
## Design

### How to play
- The game is played on a 10x10 board.
- Player and computer both get 6 ships each:
    - 2 destroyers (2 grid spaces per ship)
    - 2 subs (3 grid spaces per sub)
    - 1 carrier (4 grid spaces)
    - 1 battleship (5 grid spaces)
- Each board will have the 6 ships randomly placed on 
  them.
- The ships will be concealed from each other.
- Take in turns to choose X and Y coordinates to target 
  the oponents ships.
- You have unlimited amount of shots.
- When all the computers ships are sunk you win unless the computer sinks yours first then  you lose.

### Design Choices
- Battleships is a strategy based guessing game written in python and played 
  in a terminal window.
- As this game is played in a terminal window I have opted to keep things simple.
- The battleship logo prints to the screen using a fast typing effect that spells out 
  battleships.
- The background is black and text white by default which I have left as the white stands 
  out and makes the text easy to read. 
 
<br>


### Structure
- The structure of the game was designed to take turns between the player and computer.
- On arrival to the game the logo is printed and the user is asked if they are a returning 
  user and to enter Y or N.
- If N is entered then user is promted to sign up or if 
  Y is entered user is promted to log in to play.
- After log in/sign up is successful the game will start and ask the user if they have 
  played before, Y or N.
- If N is entered then instructions are shown or if Y 
  is entered the boards are printed to 
  the screen and the game begins.
- The user and computer now take turns guessing X and Y axis to target each others ships 
  and ultimatley sink them.
- The game finishes when user or computer has no ships 
  left.
- A win or lose message is printed to the screen and 
  asks if user wants to play again.
- If user wants to play again new boards are printed 
  with new ship positions
- If the user enters N the game ends and user is 
  displayed a goodbye message.

## Technical Design

### Flowchart


## Technologies Used

### Languages
-

### Frameworks & Tools
- Git
- GitHub
- Gitpod
- Python tutor

## Features


### Logo and Navigation Bar
- 
![]()

### Rules and Scoring section
- 

![rules and scoring section]()

### Rules and scoring toggle button
-

![rules and scoring toggle button]()

### Create Username
- 
![create username]()

### Right Or Wrong Answer Message To User
- 

![right or wrong answer message]()
![right or wrong answer message]()

### Current Score
- 

![current score]()

### Quiz Question Progress
-

![quiz question progress]()

### Game Over Or Win Display
- 

![game over or win display]()
![game over or win display]()


## Validation

### PEP8 Validation


### Performing tests on various devices 

### Browser compatability
The website was tested on the following browsers:
-
### Testing user stories
1.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navigation link | Click the Go To Quiz link from the navigation menu | Take user to the quiz page | Works as expected |

<details><summary>Screenshots</summary>
<img src=>
<img src=>
</details>

2. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Rules and Scoring section | Clearly displayed on the home page | Provide information on the rules and scoring | Works as expected |
| Toggle rules button in footer | Click rules button in footer | Toggle the rules from hidden to visible | Works as expected |

<details><summary>Screenshots</summary>
<img src=>

</details>

3.  
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| right/wrong message| click submit answer button in the quiz | Display right or wrong answer message to user | Works as expected |

<details><summary>Screenshots</summary>
<img src=>
</details>

4. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Current Score | Top left corner of the quiz area provides a score | Display the score to the user | Works as expected |

<details><summary>Screenshots</summary>
<img src=>
</details>

5.
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Create username | Click go to quiz in nav menu, enter username where prompted and click submit | Create a username | Works as expected |

<details><summary>Screenshots</summary>
<img src=>
</details>

6. 
| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Quiz progress | Top right corner of quiz area displays quiz progress | To display the quiz progress to the user | Works as expected |

<details><summary>Screenshots</summary>
<img src=>
</details>

7.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Navigation bar | Click links in nav menu | Navigate around the site | Works as expected |

<details><summary>Screenshots</summary>
<img src="docs/user-story-testing/user-story-7.png">
</details>

8. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Rules and scoring section | Clearly displayed on home page | Clearly display information to the user | Works as expected |
| Quiz area | go to quiz page and start quiz | Clearly display information to the user | Works as expected |

<details><summary>Screenshots</summary>
<img src=>
</details>

9. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game over/Win message | Lose or complete the quiz | Display game over or win message to user | Works as expected |

<details><summary>Screenshots</summary>
<img src>
</details>

10. 

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| 404 page | Click any link in navigation bar to return to site | Prevent user from using browser back arrows | Works as expected |

<details><summary>Screenshots</summary>
<img src=>
</details>

## Bugs

| **Bug** | **Fix** |
| ----------- | ----------- |
| None of the images load on page | Change all file paths to absolute |
| Home page image too big causing performance issues | Reduce size of images | 
| Text in quiz area overflowing on small screens | write media query to reduce font size on smaller screens |


## Deployment


## Credits


## Acknowledgements
I would like to take the opportunity to thank:
- My mentor Mo Shami for his advice, guidance and support during this project.
- My partner and friends for helping with testing and giving valuable feedback.
- Code Institute tutor support for their help and advice.
- The slack community as a whole for the support they provide.
 