from tkinter import ttk, Tk, Toplevel, messagebox
import integral_equations

def get_input_data():
    try:
        k = str(input_equation_k.get())
        f = str(input_equation_f.get())
        l = int(lambda_input.get())
        a = int(a_input.get())
        b = int(b_input.get())
    except:
        messagebox.showerror("Ошибка!", "Пожалуйста, проверьте корректность данных!")
        return 0

    get_results(k, f, l, a, b)


def get_results(k, f, l, a, b):     
    try:
        main_eq1, diap, slau1, slau_answers1, result_equ1 = integral_equations.eq_Fredgolm(k, f, l, a, b)
        main_eq2, diap, slau2, slau_answers2, result_equ2 = integral_equations.eq_Volterr(k, f, l, a, b)
        main_eq_f = f'({k})*({result_equ1})'
        main_eq_v = f'({k})*({result_equ2})'
        fredgolm_rate, volterr_rate = integral_equations.grafic_create(result_equ1, result_equ2, main_eq_f, main_eq_v, l, f, a, b)
    except:
        messagebox.showerror("Ошибка!", "Невозможно завершить расчёт! Проверьте корректность введённых данных.")
        return 0
    
    output_window = Toplevel()
    output_window.geometry('%dx%d+%d+%d' % (1000, 950, (window.winfo_screenwidth()/2) - (1000/2), (window.winfo_screenheight()/2) - (950/2)))

    print_results(output_window, 'Фредгольма', main_eq1, diap, slau1, slau_answers1, result_equ1, f"{l}*∫[{a}, {b}]{main_eq_f}ds + {f}", fredgolm_rate, 15, 20)
    print_results(output_window, 'Вольтерра', main_eq2, diap, slau2, slau_answers2, result_equ2, f"{l}*∫[{a}, {b}]{main_eq_v}ds + {f}", volterr_rate, 15, 500)


def print_results(output_window, title, main_eq, diap, slau, slau_answers, result_equ, equation, rate, x, y):  
    output_fredgolm = ttk.Label(output_window, text=f'Уравнение {title}: ', font=('arial', 15, "bold"))
    output_fredgolm.place(x=x, y=y)
    output_fredgolm_equ = ttk.Label(output_window, text=main_eq, font=('arial', 10))
    output_fredgolm_equ.place(x=x, y=y+35)

    output_diap_title = ttk.Label(output_window, text='Интервальные значения:', font=('arial', 10))
    output_diap_title.place(x=x, y=y+55)
    output_diap = ttk.Label(output_window, text=str(diap), font=('arial', 10))
    output_diap.place(x=x+160, y=y+55)

    output_slau_title = ttk.Label(output_window, text='СЛАУ:', font=('arial', 10))
    output_slau_title.place(x=x, y=y+75)
    output_slau1_1 = ttk.Label(output_window, text=slau[0], font=('arial', 10))
    output_slau1_1.place(x=x+50, y=y+75)
    output_slau1_2 = ttk.Label(output_window, text=slau[1], font=('arial', 10))
    output_slau1_2.place(x=x+50, y=y+95)
    output_slau1_3 = ttk.Label(output_window, text=slau[2], font=('arial', 10))
    output_slau1_3.place(x=x+50, y=y+115)

    output_slau_answers_title = ttk.Label(output_window, text='Результаты решения СЛАУ:', font=('arial', 10))
    output_slau_answers_title.place(x=x, y=y+145)
    output_slau_answers_1 = ttk.Label(output_window, text=f'y0 = {slau_answers[0]}', font=('arial', 10))
    output_slau_answers_1.place(x=x+185, y=y+145)
    output_slau_answers_2 = ttk.Label(output_window, text=f'y1 = {slau_answers[1]}', font=('arial', 10))
    output_slau_answers_2.place(x=x+185, y=y+165)
    output_slau_answers_3 = ttk.Label(output_window, text=f'y2 = {slau_answers[2]}', font=('arial', 10))
    output_slau_answers_3.place(x=x+185, y=y+185)

    output_res_eq_title = ttk.Label(output_window, text='Результат:', font=('arial', 10, 'bold'))
    output_res_eq_title.place(x=x, y=y+205)
    output_res_eq = ttk.Label(output_window, text=f"y(x) = {result_equ}", font=('arial', 10))
    output_res_eq.place(x=x+80, y=y+205)

    rate_title = ttk.Label(output_window, text='Погрешность:', font=('arial', 10, 'bold'))
    rate_title.place(x=x, y=y+225)

    rate_eq1 = ttk.Label(output_window, text=f"y(x) = {result_equ}", font=('arial', 10))
    rate_eq1.place(x=x, y=y+245)
    rate_eq2 = ttk.Label(output_window, text=f"g(x) = {equation}", font=('arial', 10))
    rate_eq2.place(x=x, y=y+270)

    rate_formula = ttk.Label(output_window, text=f"||ψ|| = max[|yj - gj|]", font=('arial', 10))
    rate_formula.place(x=x, y=y+290)

    rate_ans = ttk.Label(output_window, text=f"||ψ|| = {round(rate, 5)}", font=('arial', 10))
    rate_ans.place(x=x, y=y+315)

window = Tk() 
window.title("Интегральные уравнения")
window.geometry('%dx%d+%d+%d' % (600, 400, (window.winfo_screenwidth()/2) - (600/2), (window.winfo_screenheight()/2) - (400/2)))

style_btn = ttk.Style()
style_btn.configure("TButton", font=('algerian', 10), foreground="#004524", background="#ACB78E")

style_label = ttk.Style()
style_label.configure("TLabel", font=('italic', 10))

style_check_btn = ttk.Style()
style_check_btn.configure("TCheckbutton", font=('algerian', 10))
    
frame = ttk.Frame(window)
frame.pack(expand=True)

quation_k_txt = ttk.Label(frame, text="k(x, s): ")
quation_k_txt.grid(row=2, column=1)
input_equation_k = ttk.Entry(frame, width=50)
input_equation_k.grid(row=2, column=2, pady=5)

equation_f_txt = ttk.Label(frame, text="f(x): ")
equation_f_txt.grid(row=3, column=1)
input_equation_f = ttk.Entry(frame, width=50)
input_equation_f.grid(row=3, column=2)

lambda_txt = ttk.Label(frame, text="lambda: ")
lambda_txt.grid(row=4, column=1)
lambda_input = ttk.Entry(frame, width=50)
lambda_input.grid(row=4, column=2, padx=5, pady=5)

a_txt = ttk.Label(frame, text="a: ")
a_txt.grid(row=5, column=1)
a_input = ttk.Entry(frame, width=50)
a_input.grid(row=5, column=2, pady=5)

b_txt = ttk.Label(frame, text="b: ")
b_txt.grid(row=6, column=1)
b_input = ttk.Entry(frame, width=50)
b_input.grid(row=6, column=2, padx=5)

start_btn = ttk.Button(frame, text='Решить', command=get_input_data)
start_btn.grid(row=8, column=2, pady=10)
exit_btn = ttk.Button(frame, text="Выйти", command=quit)
exit_btn.grid(row=9, column=2)

window.mainloop()