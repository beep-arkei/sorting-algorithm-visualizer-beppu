# tutorials used:
# https://www.youtube.com/watch?v=twRidO-_vqQ&t=159s

# algorithms to implement: 
# Bubble Sort
# Selection Sort
# Insertion Sort
# Quick Sort
# Merge Sort
# Heap Sort
# Bogo Sort
# Cocktail Shaker Sort

import pygame
import random
import os
import math
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# change working directory to program's location
os.chdir(os.path.dirname(__file__))

pygame.init()

class DrawInformation:
    #basic colors
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    BLUE = 0, 0, 255
    GREY = 128, 128, 128

    #planned theme colors
    BACKGROUND = 15, 18, 34  
    HEADER = 10, 12, 28  
    DARK_GRAY = 30, 33, 50         
    MID_GRAY = 60, 65, 90          
    LIGHT_GRAY = 120, 130, 160    
    LIGHT_LIGHT_GRAY = 200, 210, 230

    BLUE = 100, 120, 255
    BLUE_LIGHT = 140, 170, 255
    BLUE_DARK = 40, 60, 140
    BLUE_PURPLE = 90, 70, 220

    PINK = 255, 100, 180
    PINK_LIGHT = 255, 140, 200
    PINK_DARK = 180, 60, 130
    PINK_PURPLE = 200, 80, 200

    VIOLET = 150, 90, 220
    CYAN = 80, 200, 255
    HOT_PINK = 255, 80, 160

    SWAP1 = PINK_DARK;
    SWAP2 = HOT_PINK;

    GRADIENTS = [
        BLUE,
        BLUE_PURPLE,
        BLUE_LIGHT
    ]

    TEXT_GRADIENTS = [
        WHITE,
        CYAN,
        VIOLET
   ]
    
    ROBOTO = "Roboto/Roboto-VariableFont_wdth,wght.ttf"
    VIGA = "Viga/Viga-Regular.ttf"
    ROBOTO_BOLD = "Roboto/Roboto-Bold.ttf"

    MICRO_FONT = pygame.font.Font(ROBOTO, 12)
    SMALL_FONT = pygame.font.Font(ROBOTO, 15)
    FONT = pygame.font.Font(ROBOTO, 20)
    BIG_FONT = pygame.font.Font(ROBOTO, 30)
    LARGE_FONT = pygame.font.Font(VIGA, 25)
    SEMI_FONT = pygame.font.Font(VIGA, 20)

    BACKGROUND_COLOR = BACKGROUND

    TOP_PAD = 150   
    SIDE_MENU_WIDTH = 250
    SIDE_PAD = SIDE_MENU_WIDTH + 50

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("beep's Sorting Algorithm Visualizer")
        self.icon = pygame.image.load("icon.png")
        self.icon = pygame.transform.scale(self.icon, (60, 60))
        self.set_list(lst)
        self.SIDE_MENU_WIDTH = DrawInformation.SIDE_MENU_WIDTH
        self.manual_mode = False

    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        self.block_width = round((self.width -self.SIDE_PAD) / len(lst))
        self.block_height = math.floor((self.height - self.TOP_PAD) / (self.max_val - self.min_val))
        self.start_x = self.SIDE_MENU_WIDTH + 25

def draw(draw_info, sorting_algo_name, ascending):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR)
    
    HEADER_HEIGHT = 70

    pygame.draw.rect(draw_info.window, draw_info.HEADER, (0, 0, draw_info.width, HEADER_HEIGHT))

    draw_info.window.blit(draw_info.icon, (5, 5))
    title = draw_info.LARGE_FONT.render("beep's Sorter", 1, draw_info.WHITE)
    draw_info.window.blit(title, (70, HEADER_HEIGHT//2 - title.get_height()//2))

    title = draw_info.LARGE_FONT.render(f"{sorting_algo_name}", 1, draw_info.PINK_LIGHT)
    draw_info.window.blit(title, (draw_info.width/2 - title.get_width()/2 , 2))

    ascending_text = draw_info.SEMI_FONT.render("Ascending" if ascending else "Descending", 1, draw_info.CYAN if ascending else draw_info.PINK_PURPLE)
    draw_info.window.blit(ascending_text, (draw_info.width/2 - ascending_text.get_width()/2, 35))

    credits_text = draw_info.FONT.render("credits to Tech With Tim", 1, draw_info.LIGHT_GRAY)
    credits_rect = credits_text.get_rect(right=draw_info.width-20, centery=HEADER_HEIGHT//2)
    draw_info.window.blit(credits_text, credits_rect)

    clickable_buttons, slider_rects = draw_sidebar(draw_info, offset = HEADER_HEIGHT)
    draw_list(draw_info, offset = HEADER_HEIGHT)
    pygame.display.update()

    return clickable_buttons, slider_rects, credits_rect


def draw_list(draw_info, color_positions={}, clear_bg=False, offset=100):
    lst = draw_info.lst

    if clear_bg:
        clear_rect = (
            draw_info.SIDE_MENU_WIDTH,
            offset,
            draw_info.width - draw_info.SIDE_MENU_WIDTH - 10,
            draw_info.height - offset
        )
        pygame.draw.rect(draw_info.window, draw_info.BACKGROUND_COLOR, clear_rect)

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        color = draw_info.GRADIENTS[i % 3]

        if i in color_positions:
            color = color_positions[i]
        if draw_info.numbers_state == 1:
            pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width - 1, draw_info.height - y - 40))
        else:
            pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width - 1, draw_info.height - y))

        if (draw_info.numbers_state == 2):
            continue
        else:
            text_color = draw_info.TEXT_GRADIENTS[i % 3]

            if i in color_positions:
                text_color = color_positions[i]
            if len(lst) >90:
                number_text = draw_info.MICRO_FONT.render(str(val), 1, text_color)
            elif len(lst) >50:
                number_text = draw_info.SMALL_FONT.render(str(val), 1, text_color)
            elif len(lst) >30:
                number_text = draw_info.FONT.render(str(val), 1, text_color)
            else:
                number_text = draw_info.BIG_FONT.render(str(val), 1, text_color)

            if draw_info.numbers_state == 0:
                number_rect = number_text.get_rect(center=(x + draw_info.block_width // 2, ((y - 10) if len(lst) > 30 else (y - 30))))
                draw_info.window.blit(number_text, number_rect)
            elif draw_info.numbers_state == 1:
                number_rect = number_text.get_rect(center=(x + draw_info.block_width // 2, (y + (val - draw_info.min_val) * draw_info.block_height) - 20))
                draw_info.window.blit(number_text, number_rect)
    if clear_bg:
        pygame.display.update()

def draw_sidebar(draw_info, offset=100):
    pygame.draw.rect(draw_info.window, draw_info.MID_GRAY, (0, offset, draw_info.SIDE_MENU_WIDTH, draw_info.height - offset))

    controls = [
        ("Reset (R)", "reset"),
        ("Start Sorting (SPACE)", "start"),
        ("Sort Ascending (A)", "ascending"),
        ("Sort Descending (D)", "descending"),
        ("Toggle Numbers (N)", "toggle"),
        ("Mode (M) - " + ("Manual" if draw_info.manual_mode else "Auto"), "mode"),
        ("Exit (ESC)", "exit")
    ]

    algorithms = [
        ("Bubble Sort (1)", bubble_sort, "Bubble Sort"),
        ("Selection Sort (2)", selection_sort, "Selection Sort"),
        ("Insertion Sort (3)", insertion_sort, "Insertion Sort"),
        ("Quick Sort (4)", quick_sort, "Quick Sort"),
        ("Merge Sort (5)", merge_sort, "Merge Sort"),
        ("Heap Sort (6)", heap_sort, "Heap Sort"),
        ("Cocktail Sort (7)", cocktail_shaker_sort, "Cocktail Shaker Sort"),
        ("Bogo Sort (8)", bogo_sort, "Bogo Sort")
    ]

    top = offset + 20
    clickable_buttons = []
    slider_rects = []

    control_header = draw_info.SEMI_FONT.render("Controls", True, draw_info.WHITE)
    draw_info.window.blit(control_header, (20, top))
    top += control_header.get_height() + 15

    mouse_pos = pygame.mouse.get_pos()
    for text_str, action in controls:
        text = draw_info.FONT.render(text_str, True, draw_info.WHITE)
        button_rect = pygame.Rect(20, top, draw_info.SIDE_MENU_WIDTH - 40, text.get_height() + 10)

        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(draw_info.window, draw_info.LIGHT_GRAY, button_rect, border_radius=5)
        else:
            pygame.draw.rect(draw_info.window, draw_info.DARK_GRAY, button_rect, border_radius=5)

        text_rect = text.get_rect(center=button_rect.center)
        draw_info.window.blit(text, text_rect)
        
        clickable_buttons.append((button_rect, action, None))
        top += button_rect.height + 15
    
    slider_label1 = draw_info.FONT.render("Array Size - " + f"{len(draw_info.lst)}", True, draw_info.WHITE)
    draw_info.window.blit(slider_label1, (20, top))
    top += slider_label1.get_height() + 10

    #Sliders for array size and speed (tbh mostly copy pasted)

    # Calculate slider handle positions based on current values
    size_value = getattr(draw_info, 'size_value', 0.5)
    speed_value = getattr(draw_info, 'speed_value', 0.5)

    slider_rect1 = pygame.Rect(20, top, draw_info.SIDE_MENU_WIDTH - 40, 15)
    pygame.draw.rect(draw_info.window, draw_info.DARK_GRAY, slider_rect1, border_radius=7)
    slider_handle1 = pygame.Rect(
        slider_rect1.left + (slider_rect1.width - 20) * size_value,
        slider_rect1.top - 5,
        20,
        25
    )
    pygame.draw.rect(draw_info.window, draw_info.PINK_LIGHT, slider_handle1, border_radius=5)
    slider_rects.append((slider_rect1, slider_handle1, "size"))
    top += 30

    if not draw_info.manual_mode:
        slider_label2 = draw_info.FONT.render("Sort Speed - " + f"{int(5 + draw_info.speed_value * 95)}" + " FPS", True, draw_info.WHITE)
        draw_info.window.blit(slider_label2, (20, top))
        top += slider_label2.get_height() + 10

        slider_rect2 = pygame.Rect(20, top, draw_info.SIDE_MENU_WIDTH - 40, 15)
        pygame.draw.rect(draw_info.window, draw_info.DARK_GRAY, slider_rect2, border_radius=7)
        slider_handle2 = pygame.Rect(
            slider_rect2.left + (slider_rect2.width - 20) * speed_value,
            slider_rect2.top - 5,
            20,
            25
        )
        pygame.draw.rect(draw_info.window, draw_info.PINK_LIGHT, slider_handle2, border_radius=5)
        slider_rects.append((slider_rect2, slider_handle2, "speed"))
        top += 40

    pygame.draw.line(draw_info.window, draw_info.LIGHT_GRAY, (20, top), (draw_info.SIDE_MENU_WIDTH - 20, top), 1)
    top += 20

    algo_header = draw_info.SEMI_FONT.render("Algorithms", True, draw_info.WHITE)
    draw_info.window.blit(algo_header, (20, top))
    top += algo_header.get_height() + 15

    for text_str, func, name in algorithms:
        text = draw_info.FONT.render(text_str, True, draw_info.WHITE)
        button_rect = pygame.Rect(20, top, draw_info.SIDE_MENU_WIDTH - 40, text.get_height() + 10)
        
        if (button_rect.collidepoint(mouse_pos) or name == draw_info.sorting_algo_name):  
            pygame.draw.rect(draw_info.window, draw_info.LIGHT_GRAY, button_rect, border_radius=5)
        else:
            pygame.draw.rect(draw_info.window, draw_info.DARK_GRAY, button_rect, border_radius=5)
        
        if name == draw_info.sorting_algo_name:
            pygame.draw.rect(draw_info.window, draw_info.BLUE_PURPLE, button_rect, border_radius=5, width=2)
        
        text_rect = text.get_rect(center=button_rect.center)
        draw_info.window.blit(text, text_rect)
        
        clickable_buttons.append((button_rect, func, name))
        top += button_rect.height + 15

    return clickable_buttons, slider_rects

def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst

def bubble_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            num1 = lst[j]
            num2 = lst[j + 1]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(draw_info, {j: draw_info.SWAP1, j + 1: draw_info.SWAP2}, True)
                yield True
    return lst


def selection_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range(len(lst)):
        min_index = i

        for j in range(i + 1, len(lst)):
            num1 = lst[min_index]
            num2 = lst[j]

            if (num1 > num2 and ascending) or (num1 < num2 and not ascending):
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]
        draw_list(draw_info, {i: draw_info.SWAP1, min_index: draw_info.SWAP2}, True)
        yield True

    return lst

def insertion_sort(draw_info, ascending=True):
    lst = draw_info.lst

    for i in range (1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1] > current and ascending
            descending_sort = i > 0 and lst[i - 1] < current and not ascending
            if not ascending_sort and not descending_sort:
                break
            lst[i] = lst[i - 1]
            i -= 1
            lst[i] = current
            draw_list(draw_info, {i - 1: draw_info.SWAP1, i: draw_info.SWAP2}, True)
            yield True

    return lst

def quick_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def partition(low, high):
        pivot = lst[high]
        i = low - 1

        for j in range(low, high):
            if (lst[j] < pivot and ascending) or (lst[j] > pivot and not ascending):
                i += 1
                lst[i], lst[j] = lst[j], lst[i]
                draw_list(draw_info, {i: draw_info.SWAP1, j: draw_info.SWAP2}, True)
                yield True

        lst[i + 1], lst[high] = lst[high], lst[i + 1]
        draw_list(draw_info, {i + 1: draw_info.SWAP1, high: draw_info.SWAP2}, True)
        yield True
        return i + 1

    def quick_sort_helper(low, high):
        if low < high:
            pi = yield from partition(low, high)
            yield from quick_sort_helper(low, pi - 1)
            yield from quick_sort_helper(pi + 1, high)

    yield from quick_sort_helper(0, len(lst) - 1)
    return lst

def merge_sort(draw_info, ascending=True):
    lst = draw_info.lst
    
    def merge_sort_helper(start, end):
        if end - start > 1:
            mid = (start + end) // 2
            yield from merge_sort_helper(start, mid)
            yield from merge_sort_helper(mid, end)
            
            left = lst[start:mid]
            right = lst[mid:end]
            i = j = 0
            k = start
            
            while i < len(left) and j < len(right):
                if (left[i] < right[j] and ascending) or (left[i] > right[j] and not ascending):
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                draw_list(draw_info, {k: draw_info.SWAP1}, True)
                yield True
                k += 1
                
            while i < len(left):
                lst[k] = left[i]
                draw_list(draw_info, {k: draw_info.SWAP1}, True)
                yield True
                i += 1
                k += 1
                
            while j < len(right):
                lst[k] = right[j]
                draw_list(draw_info, {k: draw_info.SWAP1}, True)
                yield True
                j += 1
                k += 1
    
    yield from merge_sort_helper(0, len(lst))
    return lst

def heap_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def heapify(n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and ((lst[left] > lst[largest] and ascending) or (lst[left] < lst[largest] and not ascending)):
            largest = left

        if right < n and ((lst[right] > lst[largest] and ascending) or (lst[right] < lst[largest] and not ascending)):
            largest = right

        if largest != i:
            lst[i], lst[largest] = lst[largest], lst[i]
            draw_list(draw_info, {i: draw_info.SWAP1, largest: draw_info.SWAP2}, True)
            yield True
            yield from heapify(n, largest)

    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(n, i)

    for i in range(n - 1, 0, -1):
        lst[i], lst[0] = lst[0], lst[i]
        draw_list(draw_info, {0: draw_info.SWAP1, i: draw_info.SWAP2}, True)
        yield True
        yield from heapify(i, 0)

    return lst

def cocktail_shaker_sort(draw_info, ascending=True):
    lst = draw_info.lst
    n = len(lst)
    swapped = True
    start = 0
    end = n - 1

    while swapped:
        swapped = False

        for i in range(start, end):
            if (lst[i] > lst[i + 1] and ascending) or (lst[i] < lst[i + 1] and not ascending):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                draw_list(draw_info, {i: draw_info.SWAP1, i + 1: draw_info.SWAP2}, True)
                yield True
                swapped = True

        if not swapped:
            break

        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if (lst[i] > lst[i + 1] and ascending) or (lst[i] < lst[i + 1] and not ascending):
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                draw_list(draw_info, {i: draw_info.SWAP1, i + 1: draw_info.SWAP2}, True)
                yield True
                swapped = True

        start += 1

    return lst

def bogo_sort(draw_info, ascending=True):
    lst = draw_info.lst

    def is_sorted(lst):
        for i in range(len(lst) - 1):
            if (lst[i] > lst[i + 1] and ascending) or (lst[i] < lst[i + 1] and not ascending):
                return False
        return True

    while not is_sorted(lst):
        random.shuffle(lst)
        color_positions = {i: (draw_info.SWAP1 if i % 2 == 0 else draw_info.SWAP2) for i in range(len(lst))}
        draw_info.SWAP1, draw_info.SWAP2 = draw_info.SWAP2, draw_info.SWAP1
        draw_list(draw_info, color_positions, True)
        yield True

    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    screen_info = pygame.display.Info()
    screen_width, screen_height = screen_info.current_w, screen_info.current_h

    lst = generate_starting_list(n, min_val, max_val)

    draw_info = DrawInformation(screen_width, screen_height, lst)
    draw_info.window = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    draw_info.sorting_algo_name = "Bubble Sort"
    draw_info.size_value = 0.5  # Initialize slider values
    draw_info.speed_value = 0.5
    draw_info.numbers_state = 0

    sorting = False
    ascending = True
    dragging_slider = False #Again, copied lang

    sorting_algorithm = bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None

    while run:
        current_speed = int(5 + draw_info.speed_value * 95)
        clock.tick(current_speed)

        if sorting and not draw_info.manual_mode:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
                draw_list(draw_info, clear_bg=True)
        else:
            clickable_buttons, slider_rects, credits_rect = draw(draw_info, sorting_algo_name, ascending)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for rect, action_or_func, name in clickable_buttons:
                        if rect.collidepoint(pos) and action_or_func == "reset":
                                    n = int(5 + draw_info.size_value * 95)
                                    lst = generate_starting_list(n, min_val, max_val)
                                    draw_info.set_list(lst)
                                    sorting = False
                        break   
                
            if event.type == pygame.MOUSEBUTTONDOWN and not sorting:
                pos = pygame.mouse.get_pos()

                if credits_rect.collidepoint(pos):
                    import webbrowser
                    webbrowser.open("https://www.youtube.com/@TechWithTim")
                    continue

                for slider_rect, handle_rect, slider_type in slider_rects:
                    if handle_rect.collidepoint(pos) or slider_rect.collidepoint(pos):
                        dragging_slider = slider_type
                        mouse_x = max(slider_rect.left, min(pos[0], slider_rect.right))
                        normalized_value = (mouse_x - slider_rect.left) / slider_rect.width
                        setattr(draw_info, f"{slider_type}_value", normalized_value)
                        break
                
                
                else:
                    for rect, action_or_func, name in clickable_buttons:
                        if rect.collidepoint(pos):
                            if name:  
                                sorting_algorithm = action_or_func
                                sorting_algo_name = name
                                draw_info.sorting_algo_name = name
                            else:
                                if action_or_func == "start":
                                    if draw_info.manual_mode and sorting:
                                        try:
                                            next(sorting_algorithm_generator)
                                        except StopIteration:
                                            sorting = False
                                            draw_list(draw_info, clear_bg=True)
                                    elif not sorting:
                                        sorting = True
                                        sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                                elif action_or_func == "mode":
                                    draw_info.manual_mode = not draw_info.manual_mode
                                    if draw_info.manual_mode:
                                        sorting = False
                                        draw_list(draw_info, clear_bg=True)
                                elif action_or_func == "ascending":
                                    ascending = True
                                elif action_or_func == "descending":
                                    ascending = False
                                elif action_or_func == "toggle":
                                    draw_info.numbers_state = (draw_info.numbers_state + 1) % 3
                                elif action_or_func == "exit":
                                    run = False
                            break
            
            

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_slider = None

            elif event.type == pygame.MOUSEMOTION and dragging_slider:
                for slider_rect, handle_rect, slider_type in slider_rects:
                    if slider_type == dragging_slider:
                        mouse_x = max(slider_rect.left, min(event.pos[0], slider_rect.left + slider_rect.width))
                        normalized_value = (mouse_x - slider_rect.left) / slider_rect.width
                        normalized_value = min(max(normalized_value, 0), 1)  # Clamp value between 0 and 1
                        setattr(draw_info, f"{slider_type}_value", normalized_value)
                        
                        if slider_type == "size" and not sorting:
                            n = int(5 + normalized_value * 95)
                            lst = generate_starting_list(n, min_val, max_val)
                            draw_info.set_list(lst)
                            draw_list(draw_info, clear_bg=True)
                        break

            if event.type != pygame.KEYDOWN:
                continue
            else:
                if event.key == pygame.K_r:
                    n = int(5 + draw_info.size_value * 95)
                    lst = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(lst)
                    sorting = False
                elif event.key == pygame.K_SPACE:
                    if draw_info.manual_mode and sorting:
                        try:
                            next(sorting_algorithm_generator)
                        except StopIteration:
                            sorting = False
                            draw_list(draw_info, clear_bg=True)
                    elif not sorting:
                        sorting = True
                        sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
                elif event.key == pygame.K_m:
                    draw_info.manual_mode = not draw_info.manual_mode
                    if draw_info.manual_mode:
                        sorting = False
                        draw_list(draw_info, clear_bg=True)
                elif event.key == pygame.K_a and not sorting:
                    ascending = True
                elif event.key == pygame.K_d and not sorting:
                    ascending = False
                elif event.key == pygame.K_n:
                    draw_info.numbers_state = (draw_info.numbers_state + 1) % 3

                elif event.key == pygame.K_1 and not sorting:
                    sorting_algorithm = bubble_sort
                    sorting_algo_name = "Bubble Sort"
                    draw_info.sorting_algo_name = "Bubble Sort"
                elif event.key == pygame.K_2 and not sorting:
                    sorting_algorithm = selection_sort
                    sorting_algo_name = "Selection Sort"
                    draw_info.sorting_algo_name = "Selection Sort"
                elif event.key == pygame.K_3 and not sorting:
                    sorting_algorithm = insertion_sort
                    sorting_algo_name = "Insertion Sort"
                    draw_info.sorting_algo_name = "Insertion Sort"
                elif event.key == pygame.K_4 and not sorting:
                    sorting_algorithm = quick_sort
                    sorting_algo_name = "Quick Sort"
                    draw_info.sorting_algo_name = "Quick Sort"
                elif event.key == pygame.K_5 and not sorting:
                    sorting_algorithm = merge_sort
                    sorting_algo_name = "Merge Sort"
                    draw_info.sorting_algo_name = "Merge Sort"
                elif event.key == pygame.K_6 and not sorting:
                    sorting_algorithm = heap_sort
                    sorting_algo_name = "Heap Sort"
                    draw_info.sorting_algo_name = "Heap Sort"
                elif event.key == pygame.K_7 and not sorting:
                    sorting_algorithm = cocktail_shaker_sort
                    sorting_algo_name = "Cocktail Shaker Sort"
                    draw_info.sorting_algo_name = "Cocktail Shaker Sort"
                elif event.key == pygame.K_8 and not sorting:
                    sorting_algorithm = bogo_sort
                    sorting_algo_name = "Bogo Sort"
                    draw_info.sorting_algo_name = "Bogo Sort"

                elif event.key == pygame.K_ESCAPE:
                    run = False
    pygame.quit()

if __name__ == "__main__":
    main()