from sympy.plotting import plot, PlotGrid, plot_parametric
import sympy as sp
import numpy as np
import re

def eq_Fredgolm(k, f, l, a, b): 
    main_equation = f"yi - {l}*∫[{a}, {b}]({(k.replace('x', 'xi')).replace('s', 's0')})*y0 + 4*({(k.replace('x', 'xi').replace('s', 's1'))})*y1 + ({(k.replace('x', 'xi')).replace('s', 's1')})*y2]"  #само уравнение фредгольма 

    diap_parts = [a, a+((b-a)/2), b] 

    k1_s0 = eval(re.sub('s0', str(diap_parts[0]), re.sub('x0', str(diap_parts[0]), (k.replace('x', 'x0')).replace('s', 's0'))))         
    k1_s1 = eval(re.sub('s1', str(diap_parts[1]), re.sub('x0', str(diap_parts[0]), (k.replace('x', 'x0')).replace('s', 's1'))))         
    k1_s2 = eval(re.sub('s2', str(diap_parts[2]), re.sub('x0', str(diap_parts[0]), (k.replace('x', 'x0')).replace('s', 's2'))))         

    k2_s0 = eval(re.sub('s0', str(diap_parts[0]), re.sub('x1', str(diap_parts[1]), (k.replace('x', 'x1')).replace('s', 's0'))))         
    k2_s1 = eval(re.sub('s1', str(diap_parts[1]), re.sub('x1', str(diap_parts[1]), (k.replace('x', 'x1')).replace('s', 's1'))))         
    k2_s2 = eval(re.sub('s2', str(diap_parts[2]), re.sub('x1', str(diap_parts[1]), (k.replace('x', 'x1')).replace('s', 's2'))))         

    k3_s0 = eval(re.sub('s0', str(diap_parts[0]), re.sub('x2', str(diap_parts[2]), (k.replace('x', 'x2')).replace('s', 's0'))))         
    k3_s1 = eval(re.sub('s1', str(diap_parts[1]), re.sub('x2', str(diap_parts[2]), (k.replace('x', 'x2')).replace('s', 's1'))))         
    k3_s2 = eval(re.sub('s2', str(diap_parts[2]), re.sub('x2', str(diap_parts[2]), (k.replace('x', 'x2')).replace('s', 's2'))))         

    y0, y1, y2 = sp.symbols('y0 y1 y2')

    vector_b = [eval(re.sub(f'x{i}', str(diap_parts[i]), f.replace('x', f'x{i}'))) for i in range(len(diap_parts))]

    equation1 = eval(f"y0 + ({(-1)*l*round((b-a)/6, 5)*k1_s0})*y0 + ({(-1)*l*round((b-a)/6, 5)*4*k1_s1})*y1 + ({(-1)*l*round((b-a)/6, 5)*k1_s2})*y2") 
    equation2 = eval(f"y1 + ({(-1)*l*round((b-a)/6, 5)*k2_s0})*y0 + ({(-1)*l*round((b-a)/6, 5)*4*k2_s1})*y1 + ({(-1)*l*round((b-a)/6, 5)*k2_s2})*y2")   
    equation3 = eval(f"y2 + ({(-1)*l*round((b-a)/6, 5)*k3_s0})*y0 + ({(-1)*l*round((b-a)/6, 5)*4*k3_s1})*y1 + ({(-1)*l*round((b-a)/6, 5)*k3_s2})*y2")

    slau = [
        f"{equation1} = {vector_b[0]}", 
        f"{equation2} = {vector_b[1]}", 
        f"{equation3} = {vector_b[2]}"
    ]

    matrix = [
        [round(1+(-1)*l*round((b-a)/6, 5)*k1_s0, 5), round((-1)*l*round((b-a)/6, 5)*4*k1_s1, 5), round((-1)*l*round((b-a)/6, 5)*k1_s2, 5)],
        [round((-1)*l*round((b-a)/6, 5)*k2_s0, 5), round(1+(-1)*l*round((b-a)/6, 5)*4*k2_s1, 5), round((-1)*l*round((b-a)/6, 5)*k2_s2, 5)],
        [round((-1)*l*round((b-a)/6, 5)*k3_s0, 5), round((-1)*l*round((b-a)/6, 5)*4*k3_s1, 5), round(1+(-1)*l*round((b-a)/6, 5)*k3_s2, 5)]
    ]

    matrix_answers = np.linalg.inv(matrix).dot(vector_b)
    for i in range(len(matrix_answers)):
        matrix_answers[i] = round(matrix_answers[i], 5)   

    k1_s0_new = re.sub('s0', str(diap_parts[0]), re.sub('x0', str(diap_parts[0]), k.replace('s', 's0')))
    k1_s1_new = re.sub('s1', str(diap_parts[1]), re.sub('x0', str(diap_parts[0]), k.replace('s', 's1'))) 
    k1_s2_new = re.sub('s2', str(diap_parts[2]), re.sub('x0', str(diap_parts[0]), k.replace('s', 's2')))

    y = f"({f}) + {(l/6)}*({(k1_s0_new)})*({matrix_answers[0]}) + {(l/6)*4}*({(k1_s1_new)})*({matrix_answers[1]}) + {(l/6)}*({(k1_s2_new)})*({matrix_answers[2]})" 

    result = sp.trigsimp(y)

    return main_equation, diap_parts, slau, matrix_answers, result

def eq_Volterr(k, f, l, a, b):
    main_equation = f"yi - {l}*∫[{a}, {b}](k*ij)*y0 + 4*(k*ij)*y1 + (k*ij)*y2]"  

    diap_parts = [a, a+((b-a)/2), b]

    k1_s0 = eval(re.sub('s0', str(diap_parts[0]), re.sub('x0', str(diap_parts[0]), (k.replace('x', 'x0')).replace('s', 's0'))))         

    k2_s0 = eval(re.sub('s0', str(diap_parts[0]), re.sub('x1', str(diap_parts[1]), (k.replace('x', 'x1')).replace('s', 's0'))))         
    k2_s1 = eval(re.sub('s1', str(diap_parts[1]), re.sub('x1', str(diap_parts[1]), (k.replace('x', 'x1')).replace('s', 's1'))))         

    k3_s0 = eval(re.sub('s0', str(diap_parts[0]), re.sub('x2', str(diap_parts[2]), (k.replace('x', 'x2')).replace('s', 's0'))))         
    k3_s1 = eval(re.sub('s1', str(diap_parts[1]), re.sub('x2', str(diap_parts[2]), (k.replace('x', 'x2')).replace('s', 's1'))))         
    k3_s2 = eval(re.sub('s2', str(diap_parts[2]), re.sub('x2', str(diap_parts[2]), (k.replace('x', 'x2')).replace('s', 's2'))))         

    y0, y1, y2 = sp.symbols('y0 y1 y2')

    vector_b = [eval(re.sub(f'x{i}', str(diap_parts[i]), f.replace('x', f'x{i}'))) for i in range(len(diap_parts))]

    equation1 = eval(f"y0 + ({(-1)*l*round((b-a)/6, 5)*k1_s0})*y0 + ({(-1)*l*round((b-a)/6, 5)*4*0})*y1 + ({(-1)*l*round((b-a)/6, 5)*0})*y2")
    equation2 = eval(f"y1 + ({(-1)*l*round((b-a)/6, 5)*k2_s0})*y0 + ({(-1)*l*round((b-a)/6, 5)*4*k2_s1})*y1 + ({(-1)*l*round((b-a)/6, 5)*0})*y2")
    equation3 = eval(f"y2 + ({(-1)*l*round((b-a)/6, 5)*k3_s0})*y0 + ({(-1)*l*round((b-a)/6, 5)*4*k3_s1})*y1 + ({(-1)*l*round((b-a)/6, 5)*k3_s2})*y2")
    
    slau = [
        f"{equation1} = {vector_b[0]}", 
        f"{equation2} = {vector_b[1]}", 
        f"{equation3} = {vector_b[2]}"
    ]

    matrix = [
        [round(1+(-1)*l*round((b-a)/6, 5)*k1_s0, 5), round((-1)*l*round((b-a)/6, 5)*4*0, 5), round((-1)*l*round((b-a)/6, 5)*0, 5)],
        [round((-1)*l*round((b-a)/6, 5)*k2_s0, 5), round(1+(-1)*l*round((b-a)/6, 5)*4*k2_s1, 5), round((-1)*l*round((b-a)/6, 5)*0, 5)],
        [round((-1)*l*round((b-a)/6, 5)*k3_s0, 5), round((-1)*l*round((b-a)/6, 5)*4*k3_s1, 5), round(1+(-1)*l*round((b-a)/6, 5)*k3_s2, 5)]
    ]

    matrix_answers = np.linalg.inv(matrix).dot(vector_b)
    for i in range(len(matrix_answers)):
        matrix_answers[i] = round(matrix_answers[i], 5)     

    k1_s0_new = re.sub('s0', str(diap_parts[0]), re.sub('x0', str(diap_parts[0]), k.replace('s', 's0')))
    k1_s1_new = re.sub('s1', str(diap_parts[1]), re.sub('x0', str(diap_parts[0]), k.replace('s', 's1')))
    k1_s2_new = re.sub('s2', str(diap_parts[2]), re.sub('x0', str(diap_parts[0]), k.replace('s', 's2')))

    y = f"({f}) + {(l/6)}*({(k1_s0_new)})*({matrix_answers[0]}) + {(l/6)*4}*({(k1_s1_new)})*({matrix_answers[1]}) + {(l/6)}*({(k1_s2_new)})*({matrix_answers[2]})"  

    result = sp.trigsimp(y)

    return main_equation, diap_parts, slau, matrix_answers, result

def rate_result(y1, y2, a, b):
    results = []
    x = np.arange(a, b, 0.005)
    for i in range(len(x)):
        results.append(abs(eval(str(y1).replace('x', str(x[i]))) - eval(str(y2).replace('x', str(x[i])))))
    return max(results)

def func(x, y):
    return str(y).replace('s', str(x))

def grafic_create(y1, y2, y3, y4, l, f, a, b):
    x, s = sp.symbols("x s") 

    y3 = sp.expand(eval(y3))
    y4 = sp.expand(eval(y4))

    equation1 = sp.expand(eval(f"{l}*({sp.integrate(eval(func(s, y3)), (s, a, b))}) + ({f})"))
    equation2 = sp.expand(eval(f"{l}*({sp.integrate(eval(func(s, y4)), (s, a, b))}) + ({f})"))

    p1 = plot(y1, show=False, title='Уравнение Фредгольма')
    p2 = plot(y2, show=False, title='Уравнение Вольтерра')  
    p3 = plot(equation1, (x, a, b), show=False, title='g(x)')
    p3.append(plot(y1, (x, a, b), show=False)[0])
    p4 = plot(equation2, (x, a, b), show=False, title='g(x)')
    p4.append(plot(y2, (x, a, b), show=False)[0])
    PlotGrid(2, 2, p1, p2, p3, p4)     


    rate_res1 = rate_result(equation1, y1, a, b)
    rate_res2 = rate_result(equation2, y2, a, b)

    return rate_res1, rate_res2
