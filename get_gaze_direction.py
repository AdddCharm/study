import numpy as np
import math
import matplotlib.pyplot as plt
import cv2

def get_gaze_direction(a_vector, b_vector, target_vector, img_width, img_height):
    
    # the midpoint between two points
    middle_x = (a_vector[0]+b_vector[0])/2 
    middle_y = (a_vector[1]+b_vector[1])/2
    
    x = np.array(range(0, img_width))
    
    gradient = (middle_y-target_vector[1])/(middle_x-target_vector[0])
    
    # coordinates tangent to the axis
    if target_vector[0]-middle_x < 0:
        y_value = '{}*({}-{})+{}'.format(gradient,0,int(target_vector[0]),int(target_vector[1]))
        if eval(y_value)>=img_height:
            x_value = '(({}-{})/{})+{}'.format(img_height,int(target_vector[1]),gradient,int(target_vector[0]))
            plt.scatter(eval(x_value), img_height, edgecolor='yellow')
            print('(x, y) = ({}, {})'.format(eval(x_value), img_height))
        elif eval(y_value)<0:
            x_value = '(({}-{})/{})+{}'.format(0,int(target_vector[1]),gradient,int(target_vector[0]))
            plt.scatter(eval(x_value), 0, edgecolor='yellow')
            print('(x, y) = ({}, {})'.format(eval(x_value), 0))
        else:
            plt.scatter(0,eval(y_value), edgecolor='yellow')
            print('(x, y) = ({}, {})'.format(0, eval(y_value)))
            
    if target_vector[0]-middle_x > 0:
        x_value = '(({}-{})/{})+{}'.format(img_height,int(target_vector[1]),gradient,int(target_vector[0]))
        plt.scatter(eval(x_value), img_height, edgecolor='purple')
        print('(x, y) = ({}, {})'.format((eval(x_value), img_height)))
        if eval(x_value)>=img_width:
            y_value = '{}*({}-{})+{}'.format(gradient,img_width,int(target_vector[0]),int(target_vector[1]))
            plt.scatter(img_width,eval(y_value), edgecolor='purple')
            print('(x, y) = ({}, {})'.format(img_width,eval(y_value)))

def gaze_direction_visualization(a_vector, b_vector, target_vector, img_width, img_height):
    
    # set image size
    x_size = [0, img_width]
    y_size = [0, img_height]
    
    # plot points
    plt.figure(figsize=(100,100))
    plt.xlim(0, img_width)
    plt.ylim(0, img_height)
    plt.xticks(ticks=np.arange(0, img_width, step=30))
    plt.yticks(ticks=np.arange(0, img_height, step=30))
    
    # draw dots
    plt.scatter(a_vector[0], a_vector[1], edgecolor='blue')
    plt.scatter(b_vector[0], b_vector[1], edgecolor='green')
    plt.scatter(target_vector[0], target_vector[1], edgecolor='red')
    
    # the midpoint between two points
    middle_x = (a_vector[0]+b_vector[0])/2
    middle_y = (a_vector[1]+b_vector[1])/2
    
    
    x = np.array(range(0, img_width))
    
    draw_a = [a_vector[0], b_vector[0]]
    draw_b = [a_vector[1], b_vector[1]]
    gradient = (middle_y-target_vector[1])/(middle_x-target_vector[0])
    equation = '{}*(x-{})+{}'.format(gradient,int(target_vector[0]),int(target_vector[1]))
    
    # coordinates tangent to the axis
    if target_vector[0]-middle_x < 0:
        y_value = '{}*({}-{})+{}'.format(gradient,0,int(target_vector[0]),int(target_vector[1]))
        if eval(y_value)>=img_height:
            x_value = '(({}-{})/{})+{}'.format(img_height,int(target_vector[1]),gradient,int(target_vector[0]))
            plt.scatter(eval(x_value), img_height, edgecolor='yellow')
            print('(x, y) = ({}, {})'.format(eval(x_value), img_height))
        elif eval(y_value)<0:
            x_value = '(({}-{})/{})+{}'.format(0,int(target_vector[1]),gradient,int(target_vector[0]))
            plt.scatter(eval(x_value), 0, edgecolor='yellow')
            print('(x, y) = ({}, {})'.format(eval(x_value), 0))
        else:
            plt.scatter(0,eval(y_value), edgecolor='yellow')
            print('(x, y) = ({}, {})'.format(0, eval(y_value)))
        
    if target_vector[0]-middle_x > 0:
        x_value = '(({}-{})/{})+{}'.format(img_height,int(target_vector[1]),gradient,int(target_vector[0]))
        plt.scatter(eval(x_value), img_height, edgecolor='purple')
        print('(x, y) = ({}, {})'.format((eval(x_value), img_height)))
        if eval(x_value)>=img_width:
            y_value = '{}*({}-{})+{}'.format(gradient,img_width,int(target_vector[0]),int(target_vector[1]))
            plt.scatter(img_width,eval(y_value), edgecolor='purple')
            print('(x, y) = ({}, {})'.format(img_width,eval(y_value)))
    
    # made plot
    plt.plot(x, eval(equation), label='y={}'.format(equation))
    plt.plot(draw_a, draw_b)
    plt.arrow(middle_x,middle_y, target_vector[0] - middle_x, target_vector[1]- middle_y, head_width = 10, head_length = 10, color = 'red')
    
    plt.axhline(0, color='gray', alpha = 0.3)
    plt.axvline(0, color='gray', alpha = 0.3)
    plt.title("Vector")
    plt.grid()
    plt.show()
    
    return target_vector[0] - middle_x, target_vector[1] - middle_y # value of vector

if __name__ == "__main__":

    path = '/home/addd/Desktop/jellyfish.jpeg'
    img = cv2.imread(path)
    img_height, img_width, img_channel = img.shape
    
    # set vector
    a_vector = [300, 200]
    b_vector = [120, 320]
    target_vector = [40, 40]
    
    gaze_direction_visualization(a_vector,b_vector,target_vector, img_width, img_height)
    get_gaze_direction(a_vector, b_vector, target_vector, img_width, img_height)