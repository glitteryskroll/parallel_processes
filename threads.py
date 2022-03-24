from tkinter import *
from tkinter.ttk import *
import tkinter as tk #библиотека для создания графического приложения
import threading
import random #для рандомайзера
import time

class root(tk.Frame):
    def __init__(self):
        #Создание окна
        self.root_ = tk.Tk()
        self.root_.geometry('600x400+500+300')
        self.f1 = tk.Frame(self.root_, height=100, bg='red', width=500)
        self.f1.pack()
        self.f2 = tk.Frame(self.root_, height=100, bg='blue', width=500)
        self.f2.pack(pady=10)
        self.f3 = tk.Frame(self.f1, bg='red')
        self.f3.place(x=0, y=0, width=500, height=100)
        # Верхний фрейм
        self.l2 = tk.Label(self.f3, text="Работа процессов").place(relx=0.4, rely=0)
        self.f4 = tk.Frame(self.f3, bg='red')
        self.f4.place(relx=0, rely=0.2)
        '''Создание надписей'''
        self.text1 = tk.Label(self.f3, text='A', bg='Yellow')
        self.text1.place(relx=0, rely=0.2)
        self.text2 = tk.Label(self.f3, text='B', bg='Yellow')
        self.text2.place(relx=0.2, rely=0.2)
        self.text3 = tk.Label(self.f3, text='C', bg='Yellow')
        self.text3.place(relx=0.4, rely=0.2)
        self.text4 = tk.Label(self.f3, text='D', bg='Yellow')
        self.text4.place(relx=0.6, rely=0.2)
        self.text5 = tk.Label(self.f3, text='E', bg='Yellow')
        self.text5.place(relx=0.8, rely=0.2)
        self.text6 = tk.Label(self.f2, text='F', bg='Yellow')
        self.text6.place(relx=0, rely=0.2)
        self.text7 = tk.Label(self.f2, text='G', bg='Yellow')
        self.text7.place(relx=0.2, rely=0.2)
        self.text8 = tk.Label(self.f2, text='H', bg='Yellow')
        self.text8.place(relx=0.4, rely=0.2)
        self.text9 = tk.Label(self.f2, text='K', bg='Yellow')
        self.text9.place(relx=0.6, rely=0.2)
        #Создание прогрессбаров
        self.progressbar_a = Progressbar(self.f1, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_a.place(relx=0, rely=0.4)
        self.progressbar_b = Progressbar(self.f1, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_b.place(relx=0.2, rely=0.4)
        self.progressbar_c = Progressbar(self.f1, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_c.place(relx=0.4, rely=0.4)
        self.progressbar_d = Progressbar(self.f1, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_d.place(relx=0.6, rely=0.4)
        self.progressbar_e = Progressbar(self.f1, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_e.place(relx=0.8, rely=0.4)
        self.progressbar_f = Progressbar(self.f2, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_f.place(relx=0, rely=0.4)
        self.progressbar_g = Progressbar(self.f2, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_g.place(relx=0.2, rely=0.4)
        self.progressbar_h = Progressbar(self.f2, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_h.place(relx=0.4, rely=0.4)
        self.progressbar_k = Progressbar(self.f2, orient=HORIZONTAL, length=100,
                                  mode="determinate")
        self.progressbar_k.place(relx=0.6, rely=0.4)
        # Дальнейшая настройка
        # Будем хранить значения массивов M1,M2,M3, чтобы в дальнейшем применять это в функциях
        self.M1 = []
        self.M2 = []
        self.M3 = []
        # Время начала программы
        self.timing_starting = time.perf_counter()
        # Блокировка тредов
        self.block = threading.RLock()
        self.running(0)
        self.root_.mainloop()
    #Функция для прогрессбаров
    def progressing_proccessing(self, name, finish):
        if name == 'a':
            if finish:
                self.progressbar_a['value'] = 100
            else:
                self.progressbar_a['value'] = 25
        elif name == 'b':
            if finish:
                self.progressbar_b['value'] = 100
            else:
                self.progressbar_b['value'] = 64
        elif name == 'c':
            if finish:
                self.progressbar_c['value'] = 100
            else:
                self.progressbar_c['value'] = 5
        elif name == 'd':
            if finish:
                self.progressbar_d['value'] = 100
            else:
                self.progressbar_d['value'] = 35
        elif name == 'e':
            if finish:
                self.progressbar_e['value'] = 100
            else:
                self.progressbar_e['value'] = 32
        elif name == 'f':
            if finish:
                self.progressbar_f['value'] = 100
            else:
                self.progressbar_f['value'] = 56
        elif name == 'g':
            if finish:
                self.progressbar_g['value'] = 100
            else:
                self.progressbar_g['value'] = 13
        elif name == 'h':
            if finish:
                self.progressbar_h['value'] = 100
            else:
                self.progressbar_h['value'] = 30
        elif name == 'k':
            if finish:
                self.progressbar_k['value'] = 100
            else:
                self.progressbar_k['value'] = 45
    #Функция для начала тредов, про приоритетности активируются треды
    def running(self, priority):
        if priority == 0:
            t1 = threading.Thread(target=self.A, name='A', args=(threading.currentThread().name,))
            t1.start()
        if priority == 1:
            self.block.acquire()  # Блокируем область
            t2 = threading.Thread(target=self.func1, name='B', args=(threading.currentThread().name,))  # Создание потока B
            t3 = threading.Thread(target=self.func2, name='C', args=(threading.currentThread().name,))  # Создание потока C
            t2.start()
            t3.start()
            self.block.release()  # Разблакируем область
        if priority == 2:
            self.block.acquire()
            try:
                if threading.enumerate()[1].is_alive() and not threading.enumerate()[2].is_alive():
                    pass
            except:
                if threading.enumerate()[1].is_alive():
                    t4 = threading.Thread(target=self.func3, name='D', args=(threading.currentThread().name,))  # Создание потока D
                    t5 = threading.Thread(target=self.func4, name='E', args=(threading.currentThread().name,))  # Создание потока E
                    t4.start()
                    t5.start()
            self.block.release()
        if priority == 3:
            self.block.acquire()
            try:
                if threading.enumerate()[1].is_alive() and not threading.enumerate()[2].is_alive():
                    print(threading.currentThread().name)
                    print('chilling')
                    print(threading.enumerate())
            except:
                if threading.enumerate()[1].is_alive():
                    t6 = threading.Thread(target=self.func5, name='F', args=(threading.currentThread().name,))
                    t7 = threading.Thread(target=self.func6, name='G', args=(threading.currentThread().name,))
                    t8 = threading.Thread(target=self.func7, name='H', args=(threading.currentThread().name,))
                    t6.start()
                    t7.start()
                    t8.start()
            self.block.release()

        if priority == 4:
            self.block.acquire()
            try:
                if threading.enumerate()[1].is_alive() and not threading.enumerate()[2].is_alive():
                    print(threading.currentThread().name)
                    print('chilling')
                    print(threading.enumerate())
            except:
                if threading.enumerate()[1].is_alive():
                    t9 = threading.Thread(target=self.func8, name='K', args=(threading.currentThread().name,))
                    t9.start()
            self.block.release()
    #Функция для вывода таблицы об времени и кто инициализировал поток
    def timings(self, time1, time2, initial, result):  # Будет давать нам возможность получить время
        self.block.acquire()
        print('t начала -', float('{:.5f}'.format(time1)),'|Кем инициирована -',initial , '|t конца - ', float('{:.5f}'.format(time2)), '|Имя потока - ', threading.currentThread().name, '|Результат - ', result)
        self.block.release()

    def A(self, initial):  # A
        time_start = time.perf_counter() - self.timing_starting
        self.progressing_proccessing(name='a', finish=0)
        time.sleep(1)
        for i in range(1, 4):
            self.M1.append(random.randint(1, 256))
            self.M2.append(random.randint(1, 256))
            self.M3.append(random.randint(1, 256))

        article = str(self.M1) + str(self.M2)  + str(self.M3)
        time_end = time.perf_counter() - self.timing_starting
        self.timings(time_start, time_end, initial, article)
        self.progressing_proccessing(name='a', finish=1)
        self.running(1)

    def func1(self, initial):  # B
        if threading.currentThread().name == 'B': #Если выполняется поток B, то...
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='b', finish=0)
        self.block.acquire()
        result = []
        for i in self.M1:
            result.append(int(i * 35 / 3))

        for i in self.M2:
            result.append(int(i * 15 / 2))

        for i in self.M3:
            result.append(int(i * 44 / 23))

        self.block.release()
        if threading.currentThread().name == 'B':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.timings(time_start, time_end, initial, result)
            self.progressing_proccessing(name='b', finish=1)
            self.running(2)
        return result

    def func2(self, initial):  # C
        if threading.currentThread().name == 'C': #Если выполняется поток C, то...
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='c',finish=0)
        self.block.acquire()
        result = []
        for i in self.M1:
            result.append(int(i * 35 / 3))

        for i in self.M2:
            result.append(int(i * 15 / 2))

        for i in self.M3:
            result.append(int(i * 44 / 23))

        self.block.release()
        if threading.currentThread().name == 'C':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.timings(time_start, time_end, initial, result)
            self.progressing_proccessing(name='c', finish=1)
            self.running(2)
        return result

    def func3(self, initial):  # D
        if threading.currentThread().name == 'D':
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='d', finish=0)
        self.block.acquire()
        result = []
        for i in self.M1:
            result.append(int(i * 35 / 3))

        for i in self.M2:
            result.append(int(i * 15 / 2))

        for i in self.M3:
            result.append(int(i * 44 / 23))

        time_end = time.perf_counter() - self.timing_starting
        self.block.release()
        if threading.currentThread().name == 'D':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.timings(time_start, time_end, initial, result)
            self.progressing_proccessing(name='d', finish=1)
            self.running(3)
        return result

    def func4(self, initial):  # E
        if threading.currentThread().name == 'E':
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='e', finish=0)
        self.block.acquire()
        result = []
        result = list(self.func1(0))
        for i in self.func2(0):
            result.append(i - 5)

        for i in self.func3(0):
            result.append(i - 50)

        self.block.release()
        if threading.currentThread().name == 'E':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.timings(time_start, time_end, initial, result)
            self.progressing_proccessing(name='e', finish=1)
            self.running(3)
        return result

    def func5(self, initial):  # F
        if threading.currentThread().name == 'F':
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='f', finish=0)
        self.block.acquire()
        result = []
        result = self.func1(0)
        for i in self.func2(0):
            result.append(i)

        for i in self.func3(0):
            result.append(i)

        self.block.release()
        if threading.currentThread().name == 'F':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.timings(time_start, time_end, initial, result)
            self.progressing_proccessing(name='f', finish=1)
            self.running(4)

        return result

    def func6(self, initial):  # G
        if threading.currentThread().name == 'G':
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='g', finish=0)
        self.block.acquire()
        result = []
        for i in self.func4(0):
            result.append(i * 2)

        self.block.release()
        if threading.currentThread().name == 'G':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.timings(time_start, time_end, initial, result)
            self.progressing_proccessing(name='g', finish=1)
            self.running(4)
        return result

    def func7(self, initial):  # H
        if threading.currentThread().name == 'H':
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='h', finish=0)
        self.block.acquire()
        result = []
        for i in self.func5(0):
            result.append(i / 2)
        self.block.release()
        if threading.currentThread().name == 'H':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.timings(time_start, time_end, initial, result)
            self.progressing_proccessing(name='h', finish=1)
            self.running(4)

        return result

    def func8(self, initial):  # K
        if threading.currentThread().name == 'K':
            time_start = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='k', finish=0)
        self.block.acquire()
        result = []
        for i in self.func6(0):
            for j in self.func7(0):
                result.append(i + j)
        self.block.release()
        if threading.currentThread().name == 'K':
            time.sleep(1)
            time_end = time.perf_counter() - self.timing_starting
            self.progressing_proccessing(name='k', finish=1)
            self.timings(time_start, time_end, initial, result)

        return result


G = root()
