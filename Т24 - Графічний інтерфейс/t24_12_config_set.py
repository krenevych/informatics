#T24_12
# Зміна та збереження конфігураційного файлу

from T21.t21_21_config_dict import *

class ConfigDictSet(ConfigDict):
    '''Клас встановлює значення конфігураційного файлу та зберігає цей файл.

    Конфігураційний файл - це текстовий файл, рядки якого мають вигляд:
    <ім'я> = <значення>
    ім'я - це ідентифікатор
    значення може бути цілим або дійсним числом, або рядком.
    Цілі та дійсні числа задаються як звичайно. Рядки беруться у апострофи (')
    або подвійні лапки (").
    Допускаються коментарі (починаються символом '#') та порожні рядки.
    '''

    def setconfig(self, dct):
        '''Встановити змінені значення конфігураційного файлу.

           dct - словник зі значеннями параметрів
        '''
        self._dct = dct.copy()
        for key in self._dct:
            # пробуємо перетворити у ціле число
            try:
                self._dct[key] = int(self._dct[key])
            except:
                # пробуємо перетворити у дійсне число
                try:
                    self._dct[key] = float(self._dct[key])
                except:
                    # для рядків нічого не робимо
                    pass
                    
    def saveconfig(self):
        '''Зберегти конфігураційний файл.'''
        # формуємо список рядків конфігураціного файлу
        lines = []
        for key in self._dct:
            s = str(self._dct[key])
            if type(self._dct[key]) == str:
                # для рядків додаємо лапки '"'
                s = '"' + s + '"'
            lines.append('{} = {} \n'.format(key, s))

        with open(self._filename, 'w') as f:    #відкриваємо файл filename
            f.writelines(lines)                 # записуємо у файл список
        

if __name__ == '__main__':
    filename = input("Ім'я файлу: ")
    conf = ConfigDictSet(filename)
    dct = conf.getconfig()
    dct = {key:str(dct[key]) for key in dct}
    conf.setconfig(dct)
    conf.saveconfig()
    



