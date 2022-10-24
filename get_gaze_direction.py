import numpy as np
import math
import matplotlib.pyplot as plt
import cv2

def get_gaze_direction(a_vector, b_vector, target_vector,
                       img_width, img_height):
    
    # the midpoint between two points
    middle_x_coord = (a_vector[0] + b_vector[0]) / 2 
    middle_y_coord = (a_vector[1] + b_vector[1]) / 2
    
    gradient_x = middle_x_coord - target_vector[0]
    gradient_y = middle_y_coord - target_vector[1]
    
    gradient = gradient_y / gradient_x
    
    # coordinates tangent to the axis
    if target_vector[0]-middle_x_coord < 0:
        y_value = 'gradient * (0 - target_vector[0]) + target_vector[1]'
        if eval(y_value) >= img_height:
            x_value = '((img_height - target_vector[1] / gradient) + target_vector[0])'
            x = eval(x_value)
            y = img_height
        elif eval(y_value) < 0:
            x_value = '((0 - target_vector[1]) / gradient) + target_vector[0]'
            x = eval(x_value)
            y = 0
        else:
            x = 0
            y = eval(y_value)  
    else:
        x_value = '((img_height - target_vector[1] / gradient) + target_vector[0])'
        x = eval(x_value)
        y = img_height
        if eval(x_value) >= img_width:
            y_value = 'gradient * (img_width - target_vector[0]) + target_vector[1]'
            x = img_width
            y = eval(y_value)
            
    return x, y

def gaze_direction_visualization(a_vector, b_vector, target_vector, img_width, img_height):
    
    # set image size
    x_size = [0, img_width]
    y_size = [0, img_height]
    
    # plot points
    plt.figure(figsize = (100,100))
    plt.xlim(0, img_width)
    plt.ylim(0, img_height)
    plt.xticks(ticks=np.arange(0, img_width, step = 30))
    plt.yticks(ticks=np.arange(0, img_height, step = 30))
    
    # draw dots
    plt.scatter(a_vector[0], a_vector[1], edgecolor = 'blue')
    plt.scatter(b_vector[0], b_vector[1], edgecolor = 'green')
    plt.scatter(target_vector[0], target_vector[1], edgecolor = 'red')
    
    # the midpoint between two points
    middle_x_coord = (a_vector[0] + b_vector[0]) / 2
    middle_y_coord = (a_vector[1] + b_vector[1]) / 2
    
    x_array = np.array(range(0, img_width))
    
    draw_a = [a_vector[0], b_vector[0]]
    draw_b = [a_vector[1], b_vector[1]]
    
    gradient_x = middle_x_coord - target_vector[0]
    gradient_y = middle_y_coord - target_vector[1]
    gradient = gradient_y / gradient_x
    
    equation = 'gradient * (x_array - target_vector[0]) + target_vector[1]'
    
    # coordinates tangent to the axis
    if target_vector[0]-middle_x_coord < 0:
        y_value = 'gradient * (0 - target_vector[0]) + target_vector[1]'
        if eval(y_value)>=img_height:
            x_value = '((img_height - target_vector[1] / gradient) + target_vector[0])'
            plt.scatter(eval(x_value), img_height, edgecolor='yellow')
            x = eval(x_value)
            y = img_height
        elif eval(y_value) < 0:
            x_value = '((0 - target_vector[1]) / gradient) + target_vector[0]'
            plt.scatter(eval(x_value), 0, edgecolor='yellow')
            x = eval(x_value)
            y = 0
        else:
            plt.scatter(0,eval(y_value), edgecolor='yellow')
            x = 0
            y = eval(y_value)
    else:
        x_value = '((img_height - target_vector[1] / gradient) + target_vector[0])'
        plt.scatter(eval(x_value), img_height, edgecolor='purple')
        x = eval(x_value)
        y = img_height
        if eval(x_value) >= img_width:
            y_value = 'gradient * (img_width - target_vector[0]) + target_vector[1]'
            plt.scatter(img_width,eval(y_value), edgecolor = 'purple')
            x = img_width
            y = eval(y_value)
    
    # made plot
    plt.plot(x_array, eval(equation), label = 'y={}'.format(equation))
    plt.plot(draw_a, draw_b)
    plt.arrow(middle_x_coord, middle_y_coord, target_vector[0] - middle_x_coord, target_vector[1] - middle_y_coord, head_width = 10, head_length = 10, color = 'red')
    
    plt.axhline(0, color = 'gray', alpha = 0.3)
    plt.axvline(0, color = 'gray', alpha = 0.3)
    plt.title("Vector")
    plt.grid()
    plt.show()
    
    return x, y


if __name__ == "__main__":

    path = '/home/addd/Desktop/study/get_gaze_direction/jellyfish.jpeg'
    img = cv2.imread(path)
    img_height, img_width, img_channel = img.shape
    
    # set vector
    a_vector = [300, 200]
    b_vector = [120, 100]
    target_vector = [10, 20]
    
    print(gaze_direction_visualization(a_vector,b_vector,target_vector, img_width, img_height))
    print(get_gaze_direction(a_vector, b_vector, target_vector, img_width, img_height))
    
 