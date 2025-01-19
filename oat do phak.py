import pygame
import tkinter as tk
from tkinter import messagebox
import random
from tkinterdnd2 import TkinterDnD, DND_FILES

#Initialise Pygame
pygame.init()
drop_sound = pygame.mixer.Sound('drop.mp3')
incorrect_sound = pygame.mixer.Sound('incorrect.mp3')
correct_sound = pygame.mixer.Sound('correct.mp3')
bingo_sound = pygame.mixer.Sound('bingo.mp3')
screen_size = pygame.display.Info()
width, height = screen_size.current_w, screen_size.current_h
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption('Maths Adventure') #Set the title of the window


#Define colours and fonts for main menu
background_colour = "#A7C7E7"
text_colour = (0, 0, 0)
font_for_title = pygame.font.SysFont("Kristen ITC", 100) #Large font for game titles
font = pygame.font.SysFont("Kristen ITC", 40) #Standard font for text
button_colour = "#D2E0FB" #Default button colour
button_hover_colour = "#8EACCD" #Button colour when hovered over


#Load and scale images
sticker1_path = 'ruler.png'
sticker1 = pygame.image.load(sticker1_path)
sticker1 = pygame.transform.scale(sticker1, (250, 250)) #Scale the ruler image

sticker2_path = 'C:\\calculator.png'
sticker2 = pygame.image.load(sticker2_path)
sticker2 = pygame.transform.scale(sticker2, (250, 250)) #Scale the calculator image

sprite_image_path = 'C:\\Rabbit.png'
character_sprite = pygame.image.load(sprite_image_path)
character_sprite = pygame.transform.scale(character_sprite, (500, 437)) #Scale the character sprite

shop_image_path = 'C:\\Shop.png'
shop_image = pygame.image.load(shop_image_path)
shop_image = pygame.transform.scale(shop_image, (770, 550)) #Scale the shop image

monkey = pygame.image.load('monkey.png')
cat = pygame.image.load('cat.png')
dog = pygame.image.load('dog.png')
panda = pygame.image.load('panda.png')
rabbit = pygame.image.load('rabbit.png') 

#Define colours and fonts for dictionary
background_colour_dict = '#D7E5CA' #Background colour for dictionary section
term_bg_colour = '#d2e0fb' #Background colour for terms list
selected_term_bg_colour = '#8EACCD' #Highlight colour for selected term
text_colour_dict = (0, 0, 0) #Text colour for dictionary section
search_bar_colour = (255, 255, 255) #Search bar colour
search_bar_text_colour = (0, 0, 0) #Text colour for search bar
placeholder_text_colour = (180, 180, 180) #Placeholder text colour
font_dict = pygame.font.SysFont("Comic Sans MS", 30) #Font for dictionary text
title_font_dict = pygame.font.SysFont("Kristen ITC", 70) #Font for dictionary title

#Load geometric shape images
circle_image = pygame.image.load('circle.png')
triangle_image = pygame.image.load('triangle.png')
square_image = pygame.image.load('square.png')
rectangle_image = pygame.image.load('rectangle.png')
oval1_image = pygame.image.load('oval1.png')
oval2_image = pygame.image.load('oval2.png')
rhombus_image = pygame.image.load('rhombus.png')
trapezium_image = pygame.image.load('trapezium.png')
right_triangle_image = pygame.image.load('right_angle_triangle.png')
parallelogram_image = pygame.image.load('parallelogram.png')
cube_image = pygame.image.load('cube.png')
cuboid_image = pygame.image.load('cuboid.png')
cone_image = pygame.image.load('cone.png')
pyramid_image = pygame.image.load('pyramid.png')
cylinder_image = pygame.image.load('cylinder.png')

#Dictionary data containing definitions, explanations, examples, and images
dictionary_data = {
    "24-Hour Clock": {
        "definition": "A digital clock that shows the hours in the range 0 - 23.",
        "explanation": "A 24-hour clock is used to avoid confusion between AM and PM times. It starts at midnight (00:00) and goes up to 23:59.",
        "example": "For example, 13:00 is 1:00 PM, and 18:30 is 6:30 PM."
    },
    "Circle": {
        "definition": "A round shape with all points equidistant from the centre.",
        "explanation": "In a circle, every point on the edge is the same distance from the centre. This distance is called the radius.",
        "example": "For example, the wheel of a bicycle is a circle. The spokes connect the outer edge (the rim) to the centre (the hub).",
        "image": circle_image
    },
    "Circumference": {
        "definition": "The distance around the edge of a circle.",
        "explanation": "The circumference is like the perimeter of a circle. You can calculate it using the formula C = 2πr, where r is the radius.",
        "example": "For instance, if a circle has a radius of 5 cm, its circumference would be approximately 31.4 cm."
    },
    "Addition": {
        "definition": "The process of finding the total, or sum, by combining two or more numbers.",
        "explanation": "Addition is one of the basic arithmetic operations. When you add numbers together, you are finding how many items you have in total.",
        "example": "For example, if you have 3 apples and you add 2 more, you now have 5 apples (3 + 2 = 5)."
    },
    "Subtraction": {
        "definition": "The process of finding the difference between two numbers.",
        "explanation": "Subtraction is the opposite of addition. It tells you how much one number is smaller than another.",
        "example": "For example, if you have 5 apples and you give away 2, you are left with 3 apples (5 - 2 = 3)."
    },
    "Multiplication": {
        "definition": "The process of finding the total when one number is taken a certain number of times.",
        "explanation": "Multiplication is a quick way of adding the same number many times. It's one of the basic arithmetic operations.",
        "example": "For example, if you have 4 groups of 3 apples, you have 12 apples in total (4 × 3 = 12)."
    },
    "Division": {
        "definition": "The process of finding how many times one number is contained within another.",
        "explanation": "Division is splitting a number into equal parts or groups. It is the opposite of multiplication.",
        "example": "For example, if you have 12 apples and you want to divide them into 4 equal groups, each group will have 3 apples (12 ÷ 4 = 3)."
    },
    "Triangle": {
        "definition": "A polygon with three edges and three vertices.",
        "explanation": "A triangle is one of the basic shapes in geometry. The three angles of a triangle always add up to 180 degrees.",
        "example": "For example, a right triangle has one 90-degree angle, and the other two angles are complementary.",
        "image": triangle_image
    },
    "Square": {
        "definition": "A quadrilateral with four equal sides and four right angles.",
        "explanation": "A square is a special type of rectangle where all sides have the same length.",
        "example": "For instance, a chessboard is made up of 64 small squares, each with equal sides.",
        "image": square_image
    },
    "Rectangle": {
        "definition": "A quadrilateral with four right angles.",
        "explanation": "In a rectangle, opposite sides are equal in length. It’s a common shape in everyday life.",
        "example": "For example, a standard sheet of paper is usually in the shape of a rectangle.",
        "image": rectangle_image
    },
    "Fraction": {
        "definition": "A part of a whole, expressed using a numerator and a denominator.",
        "explanation": "A fraction represents a division of a whole into equal parts. The numerator shows how many parts are taken, and the denominator shows how many parts make up a whole.",
        "example": "For example, if you cut a pizza into 4 slices and eat 1 slice, you have eaten 1/4 of the pizza."
    },
    "Decimal": {
        "definition": "A fraction expressed in a special form using the base 10 numbering system.",
        "explanation": "Decimals are another way to represent fractions. The decimal point separates the whole number from the fractional part.",
        "example": "For example, 0.75 is a decimal representing the fraction 3/4."
    },
    "Percentage": {
        "definition": "A fraction or ratio expressed as a part of 100.",
        "explanation": "Percentages are used to describe how many parts of a certain thing there are out of 100.",
        "example": "For example, if you score 80 out of 100 on a test, you scored 80%."
    },
    "Area": {
        "definition": "The size of a surface.",
        "explanation": "Area is measured in square units, like square metres. It's the amount of space within a 2D shape.",
        "example": "For example, the area of a rectangle is calculated as width × height."
    },
    "Volume": {
        "definition": "The amount of space that a substance or object occupies.",
        "explanation": "Volume is measured in cubic units, like cubic metres. It's the amount of space inside a 3D object.",
        "example": "For example, the volume of a cube is calculated as side × side × side."
    },
    "Angle": {
        "definition": "The space between two intersecting lines or surfaces at or close to the point where they meet.",
        "explanation": "Angles are measured in degrees. They describe the amount of turn between two lines.",
        "example": "For example, a right angle is 90 degrees."
    },
    "Perimeter": {
        "definition": "The continuous line forming the boundary of a closed geometric figure.",
        "explanation": "The perimeter is the total length of the sides of a 2D shape.",
        "example": "For example, the perimeter of a square is calculated as 4 × side length."
    },
    "Oval": {
        "definition": "A shape like a stretched circle, also known as an ellipse.",
        "explanation": "An oval is a curved shape that looks like a flattened or stretched-out circle.",
        "example": "For example, a running track is usually shaped like an oval.",
        "image": oval1_image,
        "image": oval2_image
    },
    "Pentagon": {
        "definition": "A polygon with five sides and five angles.",
        "explanation": "A pentagon is a five-sided shape. The sum of the interior angles in a pentagon is 540 degrees.",
        "example": "For example, a regular pentagon has five equal sides and angles."
    },
    "Hexagon": {
        "definition": "A polygon with six sides and six angles.",
        "explanation": "A hexagon is a six-sided shape. The sum of the interior angles in a hexagon is 720 degrees.",
        "example": "For example, honeycomb cells in a beehive are hexagonally shaped."
    },
    "Acute Angle": {
        "definition": "An angle that is less than 90 degrees.",
        "explanation": "An acute angle is smaller than a right angle. It looks like a sharp corner.",
        "example": "For example, the angles in an equilateral triangle are all acute, measuring 60 degrees each."
    },
    "Obtuse Angle": {
        "definition": "An angle that is greater than 90 degrees but less than 180 degrees.",
        "explanation": "An obtuse angle is larger than a right angle but smaller than a straight angle.",
        "example": "For example, the angle between the hands of a clock at 10:15 is obtuse."
    },
    "Rhombus": {
        "definition": "A quadrilateral with all sides of equal length, but unlike a square, the angles are not 90 degrees.",
        "explanation": "A rhombus looks like a tilted square. All its sides are the same length, but its angles can be different.",
        "example": "For example, the diamond shape on a deck of cards is a rhombus.",
        "image": rhombus_image
    },
    "Trapezium": {
        "definition": "A quadrilateral with at least one pair of parallel sides.",
        "explanation": "A trapezium has one pair of sides that are parallel and another pair that are not.",
        "example": "For example, the shape of a bridge can be a trapezium.",
        "image": trapezium_image
    },
    "Right Angle": {
        "definition": "An angle of exactly 90 degrees.",
        "explanation": "A right angle looks like the corner of a square. It is an angle where two lines meet to form an 'L' shape.",
        "example": "For example, the corners of a piece of paper form right angles."
    },
    "Equilateral Triangle": {
        "definition": "A triangle with all three sides of equal length.",
        "explanation": "In an equilateral triangle, all three sides are the same length, and all three angles are equal, each measuring 60 degrees.",
        "example": "For example, a triangle used in trigonometry problems is often an equilateral triangle."
    },
    "Isosceles Triangle": {
        "definition": "A triangle with two sides of equal length.",
        "explanation": "An isosceles triangle has two sides that are the same length, and the angles opposite those sides are also equal.",
        "example": "For example, the roof of a house often forms an isosceles triangle."
    },
    "Scalene Triangle": {
        "definition": "A triangle with all sides of different lengths.",
        "explanation": "In a scalene triangle, none of the sides are the same length, and none of the angles are the same.",
        "example": "For example, a triangle that doesn't have any equal sides or angles is a scalene triangle."
    },
    "Right Triangle": {
        "definition": "A triangle with one right angle (90 degrees).",
        "explanation": "A right triangle has one angle that is exactly 90 degrees, which makes it very useful in geometry and trigonometry.",
        "example": "For example, a right triangle is used to calculate the height of a building using the Pythagorean theorem.",
        "image": right_triangle_image
    },
    "Parallelogram": {
        "definition": "A quadrilateral with opposite sides that are parallel and equal in length.",
        "explanation": "In a parallelogram, opposite sides are parallel and equal in length, and opposite angles are equal.",
        "example": "For example, the shape of a slanted rectangle is a parallelogram.",
        "image": parallelogram_image
    },
    "Cube": {
        "definition": "A 3D shape with six square faces, all of the same size.",
        "explanation": "A cube is like a square box where every face is a square, and all edges are the same length.",
        "example": "For example, a dice used in board games is shaped like a cube.",
        "image": cube_image
    },
    "Cuboid": {
        "definition": "A 3D shape with six rectangular faces.",
        "explanation": "A cuboid is like a box with rectangular sides. The opposite faces are equal, and the edges can be of different lengths.",
        "example": "For example, a cereal box is shaped like a cuboid.",
        "image": cuboid_image
    },
    "Cylinder": {
        "definition": "A 3D shape with two parallel circular bases connected by a curved surface.",
        "explanation": "A cylinder looks like a tin can. It has two circular ends that are the same size and a curved surface that connects them.",
        "example": "For example, a soup can is shaped like a cylinder.",
        "image": cylinder_image
    },
    "Sphere": {
        "definition": "A perfectly round 3D shape, like a ball.",
        "explanation": "A sphere is a round shape where every point on the surface is the same distance from the centre.",
        "example": "For example, a football is shaped like a sphere."
    },
    "Cone": {
        "definition": "A 3D shape with a circular base and a pointed top.",
        "explanation": "A cone has a circular base and comes to a point at the top. It looks like an ice cream cone.",
        "example": "For example, a party hat is shaped like a cone.",
        "image": cone_image
    },
    "Pyramid": {
        "definition": "A 3D shape with a polygon base and triangular sides that meet at a point.",
        "explanation": "A pyramid has a base that can be any polygon, and triangular sides that come together at a single point at the top.",
        "example": "For example, the Great Pyramid of Giza is a famous example of a pyramid.",
        "image": pyramid_image
    },
    "Quadrilateral": {
        "definition": "A polygon with four sides.",
        "explanation": "A quadrilateral is any shape that has four sides and four angles. Squares, rectangles, and trapeziums are all quadrilaterals.",
        "example": "For example, a kite is a type of quadrilateral."
    },
    "Symmetry": {
        "definition": "A balanced arrangement of identical elements on opposite sides of a dividing line.",
        "explanation": "Symmetry occurs when one shape becomes exactly like another if you move it in some way, such as turning, flipping, or sliding.",
        "example": "For instance, a butterfly’s wings are symmetrical."
    },
    "Parallel Lines": {
        "definition": "Two lines in a plane that never meet. They are always the same distance apart.",
        "explanation": "Parallel lines run alongside each other and never intersect. They have the same slope or gradient.",
        "example": "For example, the opposite sides of a rectangle are parallel."
    },
    "Intersecting Lines": {
        "definition": "Lines that cross each other at any point.",
        "explanation": "Intersecting lines are lines that meet or cross each other at one point.",
        "example": "For example, the letter 'X' is made up of two intersecting lines."
    },
    "Tessellation": {
        "definition": "A pattern made of identical shapes that fit together without any gaps or overlaps.",
        "explanation": "Tessellations can be found in nature, such as in honeycomb patterns, and in art, such as tiling designs.",
        "example": "For example, a floor tiled with square tiles is a tessellation."
    },
}

terms = list(dictionary_data.keys()) #List of all terms in the dictionary
selected_term = None 
search_query = "" 
search_active = False #Flag to indicate if the search bar is active

#Define GUI elements
search_bar_rect = pygame.Rect(20, 40, 300, 60) 
term_list_rect = pygame.Rect(20, 150, 300, 620) 
definition_rect = pygame.Rect(350, 150, 1600, 860) 

#Scroll offset for scrolling through terms
scroll_offset = 0

#Class to create and manage buttons in the game
class Button:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height) 
        self.colour = button_colour 
        self.hover_colour = button_hover_colour 
        self.text_surf = font.render(text, True, text_colour) 
        self.text_rect = self.text_surf.get_rect(center=self.rect.center) 

    #Draw the button on the screen
    def draw(self, screen):
        pygame.draw.rect(screen, self.colour, self.rect, border_radius=10)
        screen.blit(self.text_surf, self.text_rect)

    #Check if the mouse is hovering over the button and change colour or not
    def check_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.colour = self.hover_colour
        else:
            self.colour = button_colour

#Buttons for main menu options
play_button = Button('Play Game', 1500, 430, 300, 100)
learn_button = Button('Learn', 1500, 560, 300, 100)
settings_button = Button('Settings', 1500, 690, 300, 100)
instructions_button = Button('Instructions', 1500, 820, 300, 100)
back_button = Button('Back', 1810, 1020, 150, 50)  

#Wrap text into multiple lines that fit within a given width
def wrap_text(text, font, max_width):
    words = text.split(' ') #Split the text into individual words
    lines = [] #List to store lines of text
    current_line = words[0] #Start with the first word

    for word in words[1:]: #Iterate over the rest of the words
        test_line = current_line + ' ' + word #Attempt to add the next word to the current line
        if font.size(test_line)[0] <= max_width: #Check if the line width is within the maximum width
            current_line = test_line #If it fits, update the current line
        else:
            lines.append(current_line) #If it doesn't fit, store the current line
            current_line = word #Start a new line with the current word

    lines.append(current_line) #Add the last line to the list
    return lines #Return the list of lines

#Show instructions for the game
def show_instructions():
    instructions_running = True #Loop until the instructions screen is closed
    while instructions_running:
        screen.fill("#CCD2F9")
        instructions_box_rect = pygame.Rect(300, 200, 1200, 400) #Rectangle for the instructions box
        pygame.draw.rect(screen, ("#CCD2F9"), instructions_box_rect)
        instructions_text = [
            "Welcome to Maths Adventure!",
            "1. Click on Play Game to access different Maths game, there will be a separate instruction inside each game",
            "2. Click on Learn to access Mathematics Dictionary",
            "3. Click on Settings to adjust music and sounds",
            "4. Click on your character to change character",
            "5. Click on the Character Shop to buy more character with your in-game coins",
            "Have fun and learn as you stay!"
        ]
        font = pygame.font.SysFont("Comic Sans MS", 30)
        y_offset = 250 
        for line in instructions_text: #Display each line of instructions
            text_surf = font.render(line, True, (0, 0, 0))
            screen.blit(text_surf, (350, y_offset))
            y_offset += 50 #50 pixels vertical space between each line is added 
        
        back_button.draw(screen) #Draw the back button
        back_button.check_hover() #Check if the back button is hovered

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                instructions_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button.rect.collidepoint(mouse_pos):
                    instructions_running = False

#Show the mathematics dictionary
def show_dictionary():
    global selected_term, search_query, search_active, scroll_offset #Use global variables
    dictionary_running = True
    while dictionary_running: #Loop until the dictionary screen is closed
        screen.fill(background_colour_dict)
        title_surf = title_font_dict.render("Mathematics Dictionary", True, text_colour_dict)
        screen.blit(title_surf, (750, 20))

        pygame.draw.rect(screen, search_bar_colour, search_bar_rect, border_radius=10)
        if not search_query and not search_active: #Display placeholder text if no search query
            search_text_surf = font_dict.render("Search", True, placeholder_text_colour)
        else:
            search_text_surf = font_dict.render(search_query, True, search_bar_text_colour) #Display the search query
        screen.blit(search_text_surf, (search_bar_rect.x + 10, search_bar_rect.y + 10))

        filtered_terms = [term for term in terms if search_query.lower() in term.lower()] #Filter terms based on search query
        term_y_offset = scroll_offset
        for term in filtered_terms: #Display each term in the filtered list
            term_rect = pygame.Rect(term_list_rect.x, term_list_rect.y + term_y_offset, term_list_rect.width, 50)
            if selected_term == term: #Highlight the selected term
                pygame.draw.rect(screen, selected_term_bg_colour, term_rect, border_radius=10)
            else:
                pygame.draw.rect(screen, term_bg_colour, term_rect, border_radius=10)
                pygame.draw.rect(screen, selected_term_bg_colour, [term_list_rect.x, term_list_rect.y + term_y_offset, term_list_rect.width, 50], 2, border_radius=10)

            term_text_surf = font_dict.render(term, True, text_colour_dict)
            screen.blit(term_text_surf, (term_list_rect.x + 10, term_list_rect.y + term_y_offset + 10))
            term_y_offset += 60

        if selected_term: #If a term is selected, display its definition, explanation, and example
            pygame.draw.rect(screen, (255, 255, 255), definition_rect, border_radius=10)

            definition = dictionary_data[selected_term]["definition"]
            explanation = dictionary_data[selected_term]["explanation"]
            example = dictionary_data[selected_term]["example"]
            image = dictionary_data[selected_term].get("image")

            #Text Wrapping
            y_offset = 30
            wrapped_definition = wrap_text("Definition: " + definition, font_dict, definition_rect.width - 40)
            for line in wrapped_definition: #Loop through all the lines 
                def_text_surf = font_dict.render(line, True, text_colour_dict)
                screen.blit(def_text_surf, (definition_rect.x + 20, definition_rect.y + y_offset))
                y_offset += 40

            y_offset += 20
            wrapped_explanation = wrap_text(explanation, font_dict, definition_rect.width - 40)
            for line in wrapped_explanation:
                exp_text_surf = font_dict.render(line, True, text_colour_dict)
                screen.blit(exp_text_surf, (definition_rect.x + 20, definition_rect.y + y_offset))
                y_offset += 40

            y_offset += 20
            wrapped_example = wrap_text("Example: " + example, font_dict, definition_rect.width - 40)
            for line in wrapped_example:
                example_text_surf = font_dict.render(line, True, text_colour_dict)
                screen.blit(example_text_surf, (definition_rect.x + 20, definition_rect.y + y_offset))
                y_offset += 40
            if image:
                screen.blit(image, (definition_rect.x + 500, definition_rect.y + y_offset + 40))

        back_button.draw(screen)
        back_button.check_hover()

        #Main loop of the dictionary
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dictionary_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button.rect.collidepoint(mouse_pos):
                    dictionary_running = False  #Exit dictionary view
                elif search_bar_rect.collidepoint(mouse_pos):
                    search_active = True #Activate search and clear previous query
                    search_query = ""
                else:
                    search_active = False 
                    term_y_offset = scroll_offset
                    for term in filtered_terms:
                        term_rect = pygame.Rect(term_list_rect.x, term_list_rect.y + term_y_offset, term_list_rect.width, 50)
                        if term_rect.collidepoint(mouse_pos):
                            selected_term = term
                        term_y_offset += 60
            elif event.type == pygame.KEYDOWN and search_active:
                if event.key == pygame.K_BACKSPACE:
                    search_query = search_query[:-1] #Remove the last character from search query
                elif event.key == pygame.K_RETURN:
                    search_active = False #Deactivate search when enter is pressed
                else:
                    search_query += event.unicode #Add typed character to search query
            elif event.type == pygame.MOUSEWHEEL:
                scroll_offset += event.y * 20 #Adjust scroll offset based on mouse wheel movement
                scroll_offset = max(min(scroll_offset, 0), -(len(filtered_terms) * 60 - term_list_rect.height))

        pygame.display.flip()

purchased_characters = [False, False, False, False, True] #Track if a character is purchased 
def run_character_shop():
    pygame.init()
    screen_size = pygame.display.Info()
    width, height = screen_size.current_w, screen_size.current_h
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption('Character Shop')

    #Colours and Fonts
    background_colour = '#ffdbdb'
    text_colour = (0, 0, 0)
    font_for_title = pygame.font.SysFont("Kristen ITC", 40)
    font_for_text = pygame.font.SysFont('Comic Sans MS', 30)
    character_frame_colour = (255, 255, 255)

    #Character images
    monkey = pygame.image.load('monkey.png')
    cat = pygame.image.load('cat.png')
    dog = pygame.image.load('dog.png')
    panda = pygame.image.load('panda.png')

    def character_frame(screen):
        for i in range(4):
            x = 200 + i*350
            y = 250
            pygame.draw.rect(screen, character_frame_colour, [x, y, 250, 500], border_radius=10)
            pygame.draw.rect(screen, 'black', [x, y, 250, 500], 2, border_radius=10)

    def price_frame(screen):
        for i in range(4):
            x = x = 200 + i*350
            y = 775
            if purchased_characters[i]:
                pygame.draw.rect(screen, (200, 200, 200), [x, y, 250, 50], border_radius=10)
                pygame.draw.rect(screen, 'black', [x, y, 250, 50], 2, border_radius=10)
                purchased_text = font_for_text.render('Purchased', True, text_colour)
                screen.blit(purchased_text, [x + 50, y])
            else:
                pygame.draw.rect(screen, character_frame_colour, [x, y, 250, 50], border_radius=10)
                pygame.draw.rect(screen, 'black', [x, y, 250, 50], 2, border_radius=10)
                price = font_for_text.render('1000 coins', True, text_colour)
                screen.blit(price, [x + 50, y])

    #Function to handle coins
    def handle_purchase(mouse_pos):
        global coins, purchased_characters
        for i in range(4):
            x = 200 + i * 350
            y = 775
            price_rect = pygame.Rect(x, y, 250, 50)
            if price_rect.collidepoint(mouse_pos):
                if purchased_characters[i]:
                    tk.messagebox.showinfo("Already Purchased", "You have already purchased this character!")
                elif coins >= 10:
                    coins -= 10
                    purchased_characters[i] = True
                    tk.messagebox.showinfo("Purchase Successful", "You have purchased a character for 1000 coins!")
                else:
                    tk.messagebox.showwarning("Not Enough Coins", "Not enough coins. Save up more!")
    
    def display_coins(screen, font, coins, x, y):
        coin_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
        screen.blit(coin_text, (x, y))

    #Main Game Loop
    shop_running = True
    while shop_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                shop_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button.rect.collidepoint(mouse_pos):
                    shop_running = False
                else:
                    handle_purchase(mouse_pos)
        screen.fill(background_colour)
        title = font_for_title.render('Character Shop', True, text_colour)
        screen.blit(title, [700, 100])
        character_frame(screen)
        price_frame(screen)
        screen.blit(monkey, [180, 275])
        screen.blit(cat, [530, 275])
        screen.blit(dog, [880, 275])
        screen.blit(panda, [1230, 275])
        back_button.draw(screen)
        back_button.check_hover()
        display_coins(screen, font, coins, width - 200, 50)
        pygame.display.flip()
    return

selected_character = None
def run_character_selection():
    pygame.init()
    screen_size = pygame.display.Info()
    width, height = screen_size.current_w, screen_size.current_h
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption('Character Selection')

    background_colour = '#bfcbff'
    text_colour = (0, 0, 0)
    font_for_title = pygame.font.SysFont("Kristen ITC", 40)
    character_frame_colour = (255, 255, 255)

    monkey = pygame.image.load('monkey.png')
    cat = pygame.image.load('cat.png')
    dog = pygame.image.load('dog.png')
    panda = pygame.image.load('panda.png')
    rabbit = pygame.image.load('rabbit.png')

    def character_frame(screen):
        global purchased_characters
        for i in range(5):
            x = 200 + i*350
            y = 250
            if purchased_characters[i]:
                pygame.draw.rect(screen, character_frame_colour, [x, y, 250, 500], border_radius=10)
                pygame.draw.rect(screen, 'black', [x, y, 250, 500], 2, border_radius=10)
            else:
                pygame.draw.rect(screen, (200, 200, 200), [x, y, 250, 500], border_radius=10)
                pygame.draw.rect(screen, 'black', [x, y, 250, 500], 2, border_radius=10)

    def handle_selection(mouse_pos):
        global selected_character
        for i in range(5):  
            frame_rect = pygame.Rect(200 + i * 350, 250, 250, 500)  
            if frame_rect.collidepoint(mouse_pos):  
                if purchased_characters[i]:  
                    selected_character = i  
                    tk.messagebox.showinfo("Character Selected", f"You have selected character {i + 1}!")
                else:
                    tk.messagebox.showwarning("Not Purchased", "You have not purchased this character yet!")
        
    selection_running = True
    while selection_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selection_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button.rect.collidepoint(mouse_pos):
                    selection_running = False
                else:
                    handle_selection(mouse_pos)
        screen.fill(background_colour)
        title = font_for_title.render('Character Selection', True, text_colour)
        screen.blit(title, [700, 100])
        character_frame(screen)
        screen.blit(monkey, [180, 275])
        screen.blit(cat, [530, 275])
        screen.blit(dog, [880, 275])
        screen.blit(panda, [1230, 275])
        screen.blit(rabbit, [1580, 275])
        back_button.draw(screen)
        back_button.check_hover()
        pygame.display.flip()
    return

coins = 0
def run_number_sorting_game():
    sort_order = None
    #Create the main game window
    def create_main_window():
        window = TkinterDnD.Tk()
        window.title("Number Sorting Game")
        window.geometry("1920x1080")
        window.config(bg="#D2E0FB")
        return window

    #Create an instructions label
    def create_instructions(window):
        global sort_order, instruction_label, coin_label
        instruction_label = tk.Label(window, text="", font=("Comic Sans MS", 20), bg="#D2E0FB")
        sort_order = random.choice(["ascending", "descending"])
        instruction_label.config(text=f"Sort the number in {sort_order} order.")
        instruction_label.pack(pady=250)
        coin_label = tk.Label(window, text=f"Coins: {coins}", font=("Comic Sans MS", 20), bg="#D2E0FB")
        coin_label.place(x=1400, y=80)
        
    def update_coin_label():
        coin_label.config(text=f"Coins: {coins}")

    #Generate a list of random numbers to be sorted
    def generate_numbers(count=5):
        return random.sample(range(1, 100), count)

    #Sorting the list of random numbers
    def sorting_list(numbers):
        ascending_sorted_list = sorted(numbers)
        descending_sorted_list = sorted(numbers, reverse=True)
        if sort_order == 'ascending':
            return(ascending_sorted_list)
        else:
            return(descending_sorted_list)

    #List that store labbels in the order they are placed in slots 
    placed_labels = []
    def check_sorted_order():
        global coins
        numbers_in_slots = []
        sorted_slots = sorted(slots, key=lambda s: s["widget"].winfo_x()) #Sort the slots by their X-coordinate left to right order
        for slot in sorted_slots:
            if slot["fill"]:
                number = int(slot["fill"].cget('text'))
                numbers_in_slots.append(number)
        correct_order = sorting_list(numbers_in_slots)
        if numbers_in_slots == correct_order:
            coins += 10
            update_coin_label()
            messagebox.showinfo('Result', 'Correct! You earned 10 coins!')
            reset_game()
        else:
            messagebox.showwarning('Result', 'Incorrect! The numbers are not sorted in the correct order!')

    #Create slots where the numbers will be dropped 
    def create_slots(window, count):
        slots = []
        slot_y = 400
        #Create slots based on the number of items to be sorted
        for i in range(count):
            x = 550 + i*150
            slot = tk.Label(window, text="", relief="sunken", width=9, height=4)
            slot.place(x=x, y=slot_y)
            slots.append({"widget": slot, "filled": False, "fill": None})
        return slots

    #Create labels that can be dragged 
    def draggable_labels(window, numbers, slots):
        labels = []
        label_y = 550
        label_width = 50
        label_height = 50
        for i in range(len(numbers)):
            x = 550 + i*150
            number = numbers[i]
            label = tk.Label(window, text=str(number), font=("Comic Sans MS", 10), relief="raised", width=9, height=4)
            label.place(x=x, y=label_y)
            labels.append((x, label_y, label_width, label_height, label))
            #Bind actions to functions
            label.bind("<ButtonPress-1>", lambda event, lbl=label, s=slots: on_start(event, lbl, s))
            label.bind("<B1-Motion>", on_drag)
            label.bind("<ButtonRelease-1>", lambda event, lbl=label, s=slots: check_collision(event, lbl, s))
        return labels

    #Reset game once a question is answered correctly 
    def reset_game():
        nonlocal slots, labels, sort_order
        placed_labels.clear()  
        numbers = generate_numbers(count=5)  
        sort_order = random.choice(["ascending", "descending"])
        #Destroy all current widgets 
        for widget in window.winfo_children():
            widget.destroy()
        #Re-create the game components
        create_instructions(window)
        slots = create_slots(window, count=5)  
        labels = draggable_labels(window, numbers, slots)
        instruction_label.config(text=f"Sort the numbers in {sort_order} order.")

    #Handles the start of the dragging action
    def on_start(event, label, slots):
        label = event.widget
        label.startX = event.x
        label.startY = event.y
        for slot in slots:
            if slot["fill"] == label:
                slot["filled"] = False
                slot["fill"] = None
        if label in placed_labels:
            placed_labels.remove(label)
        
    #Checks if a label is close enough to a slot to snap into place
    def check_collision(event, label, slots):
        label_x = label.winfo_x()
        label_y = label.winfo_y()
        for slot in slots:
            slot_x = slot["widget"].winfo_x()
            slot_y = slot["widget"].winfo_y()
            if abs(label_x - slot_x) < 50 and abs(label_y - slot_y) < 50 and not slot["filled"]:
                pygame.mixer.Sound.play(drop_sound)
                label.place(x=slot_x, y=slot_y)
                slot["filled"] = True
                slot["fill"] = label
                placed_labels.append(label)
                break
        if len(placed_labels) == len(slots):
            check_sorted_order()

    #Handles dragging the label   
    def on_drag(event):
        label = event.widget
        current_x = label.winfo_x()
        current_y = label.winfo_y()
        new_x = current_x - label.startX + event.x
        new_y = current_y - label.startY + event.y
        label.place(x=new_x, y=new_y)
        
    #Main game loop
    window = create_main_window()
    create_instructions(window)
    numbers = generate_numbers()
    sorting_list(numbers)
    slots = create_slots(window, len(numbers))
    labels = draggable_labels(window, numbers, slots)
    window.mainloop()

def run_bingo_lover_game():
    screen_size = pygame.display.Info()
    width, height = screen_size.current_w, screen_size.current_h
    screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption('Bingo Lover Game')

    #Colours and fonts
    background_colour = '#D4DFFF'
    text_colour = (0, 0, 0)
    font_for_text = pygame.font.SysFont('Comic Sans MS', 30)
    bingo_card_colour = (225, 219, 255)
    ticked_colour = '#bb97de'
    button_colour = '#CCD2F9'

    #Store random numbers and current question
    number1 = [0] * 16
    number2 = [0] * 16
    answers = [0] * 16 
    current_index = 0 #To keep track of the current question
    
    #Check if click on bingo card
    selected_card = [False] * 16
    bingo = False
    
    def check_bingo():
        for i in range(4):
            if all(selected_card[i + 4*j] for j in range(4)):
                return True
        for j in range(4):
            if all(selected_card[i + 4*j] for i in range(4)):
                return True
        return False

    def click_check(x, y):
        global coins
        nonlocal bingo
        for i in range(4):
            for j in range(4):
                card_x = 600 + 265*i
                card_x_end = card_x + 100
                card_y = 350 + 180*j
                card_y_end = card_y + 100
                index = i + 4*j
                if card_x < x < card_x_end and card_y < y < card_y_end:
                    if answers[index] == number1[current_index] + number2[current_index]:
                        selected_card[index] = True
                        pygame.mixer.Sound.play(correct_sound)
                        if check_bingo():
                            bingo = True
                            pygame.mixer.Sound.play(bingo_sound)
                            coins += 10 
                            print("Bingo Achieved! Coins +10")
                        return True
                    else:
                        pygame.mixer.Sound.play(incorrect_sound)
        return False
                        
    def bingo_card(screen):
        #Draw bingo cards with answers
        for i in range(4):
            for j in range(4):
                index = i + 4*j  #To get the correct index in the answers list
                x = 600 + 265*i
                y = 350 + 180*j
                card_colour = bingo_card_colour
                if selected_card[index]:
                    card_colour = ticked_colour
                pygame.draw.rect(screen, card_colour, [x, y, 100, 100], border_radius=10)
                pygame.draw.rect(screen, "black", [x, y, 100, 100], 2, border_radius=10)
                #Render the answer text on the card
                answer_text = font_for_text.render(str(answers[index]), True, text_colour)
                screen.blit(answer_text, (x + 28, y + 30))

    def generate_random_numbers():
        for i in range(16):
            number1[i] = random.randint(1, 100)
            number2[i] = random.randint(1, 100)
            answers[i] = number1[i] + number2[i]
        random.shuffle(answers)

    def check_bingo():
        for i in range(4):
            if all(selected_card[i + 4*j] for j in range(4)):
                return True
        for j in range(4):
            if all(selected_card[i + 4*j] for i in range(4)):
                return True
        return False

    def instruction_box(screen):
        pygame.draw.rect(screen, bingo_card_colour, [600, 150, 900, 100], border_radius=10)
        pygame.draw.rect(screen, "black", [600, 150, 900, 100], 2, border_radius=10)

    #Show instruction lines and questions
    def instruction_text(screen):
        question_text = f'What is the sum of {number1[current_index]} and {number2[current_index]} ?'
        text = font_for_text.render('Click on the bingo card with the answer to the question below:', True, text_colour)
        screen.blit(text, (620, 170))
        question = font_for_text.render(question_text, True, text_colour)
        screen.blit(question, (820, 200))

    def draw_buttons(screen):
        reset_button = pygame.draw.rect(screen, button_colour, [800, 275, 200, 50], border_radius=10)
        pygame.draw.rect(screen, "black", [800, 275, 200, 50], 2, border_radius=10)
        reset_text = font_for_text.render('Play Again', True, text_colour)
        quit_button = pygame.draw.rect(screen, button_colour, [1100, 275, 200, 50], border_radius=10)
        pygame.draw.rect(screen, "black", [1100, 275, 200, 50], 2, border_radius=10)
        quit_text = font_for_text.render('Quit', True, text_colour)
        screen.blit(reset_text, (830, 280))
        screen.blit(quit_text, (1170, 280))
        return reset_button, quit_button

    def reset_game():
        global coins
        nonlocal selected_card, bingo, current_index
        selected_card = [False] * 16
        current_index = 0
        bingo = False
        generate_random_numbers()
    
    def display_coins(screen, font, coins, x, y):
        coin_text = font.render(f'Coins: {coins}', True, (0, 0, 0))
        screen.blit(coin_text, (x, y))

    #Main loop of the game
    generate_random_numbers() 
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if bingo:
                    reset_button, quit_button = draw_buttons(screen)
                    if reset_button.collidepoint(mouse_x, mouse_y):
                        reset_game()
                    elif quit_button.collidepoint(mouse_x, mouse_y):
                        running = False
                else:
                    if click_check(mouse_x, mouse_y):
                        current_index = current_index + 1
                    
        if not bingo and check_bingo():
            bingo = True
        screen.fill(background_colour)
        bingo_card(screen)
        instruction_box(screen)
        if bingo:
            bingo_text = font_for_text.render('BINGO!', True, text_colour)
            screen.blit(bingo_text, (1000, 180))
            draw_buttons(screen)
        else:
            instruction_text(screen)
        display_coins(screen, font_for_text, coins, width - 200, 50)
        pygame.display.flip()

def show_mini_game_screen_selection():
    selection_running = True
    while selection_running:
        screen.fill('#CCD2F9')
        selection_text = font.render("Select a Mini-Game", True, text_colour)
        screen.blit(selection_text, (850, 200))
        number_sorting_button = Button('Number Sorting', 400, 400, 400, 100)
        number_sorting_button.draw(screen)
        number_sorting_button.check_hover()
        bingo_lover_button = Button('Bingo Lover', 1300, 400, 400, 100)
        bingo_lover_button.draw(screen)
        bingo_lover_button.check_hover()
        back_button.draw(screen)
        back_button.check_hover()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                selection_running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if back_button.rect.collidepoint(mouse_pos):
                    selection_running = False  #Go back to the main menu
                elif number_sorting_button.rect.collidepoint(mouse_pos):
                    run_number_sorting_game()
                elif bingo_lover_button.rect.collidepoint(mouse_pos):
                    run_bingo_lover_game()

#Main loop of the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.rect.collidepoint(event.pos):
                show_mini_game_screen_selection()  
            elif learn_button.rect.collidepoint(event.pos):
                show_dictionary()
            elif instructions_button.rect.collidepoint(event.pos):
                show_instructions()
            elif shop_rect.collidepoint(event.pos):
                run_character_shop()
            elif selection_rect.collidepoint(event.pos):
                run_character_selection()
            

    #Render title
    screen.fill(background_colour)
    title_surf = font_for_title.render('Maths Adventure', True, text_colour)
    title_rect = title_surf.get_rect(center=(width // 2 + 50, 125))
    screen.blit(title_surf, title_rect)
    
    #Display the coin amount
    coin_text_surf = font.render(f'Coins: {coins}', True, text_colour)
    coin_text_rect = coin_text_surf.get_rect(topright=(width - 50, 50))
    screen.blit(coin_text_surf, coin_text_rect)
    
    #Blit images
    characters = [monkey, cat, dog, panda, rabbit]  
    if selected_character is not None:
        screen.blit(characters[selected_character], (width // 2 - 45, height // 2))
    else:
        screen.blit(character_sprite, (width // 2 - 45, height // 2))
    screen.blit(sticker1, (75, 5))
    screen.blit(sticker2, (1625, 5))
    screen.blit(shop_image, (0, height // 2 - 75))
    shop_rect = shop_image.get_rect(topleft=(0, height // 2 - 75))
    selection_rect = character_sprite.get_rect(center=(width // 2, height // 2))

    #Draw buttons
    play_button.draw(screen)
    learn_button.draw(screen)
    settings_button.draw(screen)
    instructions_button.draw(screen)

    play_button.check_hover()
    learn_button.check_hover()
    settings_button.check_hover()
    instructions_button.check_hover()
    pygame.display.flip()
pygame.quit()
