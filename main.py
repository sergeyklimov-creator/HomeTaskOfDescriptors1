from datetime import datetime
import contextlib

@contextlib.contextmanager
def programm():
    try:
        now = datetime.now()
        print('Началo работы программы {}\n'.\
            format(now.strftime('%Y-%m-%d %H:%M:%S.%f')[:-5]))
        yield
    finally:
        then = datetime.now()
        print('\nОкончание работы программы {}'.\
            format(then.strftime('%Y-%m-%d %H:%M:%S.%f')[:-5]))
        print(f'Время работы программы {then-now}')

if __name__ == '__main__':

    with programm():
        print('Выполняем код ...')
        input('Для завершения программы нажмите Enter ...')
        
