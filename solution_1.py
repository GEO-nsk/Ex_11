class AirConditioning:
    '''
    Class of conditioners

    properties:
        __status: True if conditioner is on, False if conditioner is off
        __temperature: number current temperature

    methods:
        switch_on: turns on conditioner
        switch_off: turns conditioner off
        reset: set temperature to 18
        get_temperature: prints current temperature status
        raise_temperature: increase temperature by 1 degree
        lower_temperature: decrease temperature by 1 degree
    '''

    def __init__(self):
        self.__status = False
        self.__temperature = None

    status = property()
    temperature = property()

    @status.setter
    def status(self, value):
        pass

    @status.getter
    def status(self):
        return self.__status

    @temperature.setter
    def temperature(self, value):
        pass

    @temperature.getter
    def temperature(self):
        return self.__temperature

    def switch_on(self):
        '''
        turns on conditioner
        '''
        self.__status = True
        self.__temperature = 18

    def switch_off(self):
        '''
        turns conditioner off
        '''
        self.__status = False
        self.__temperature = None

    def reset(self):
        '''
        set temperature to 18
        '''
        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        '''
        prints current temperature status

        return: temperature status
        '''
        if self.__status:
            return self.__temperature

    def raise_temperature(self):
        '''
        increase temperature by 1 degree
        '''
        if self.__status and 0 <= self.__temperature < 43:
            self.__temperature += 1

    def lower_temperature(self):
        '''
        decrease temperature by 1 degree
        '''
        if self.__status and 0 < self.__temperature <= 43:
            self.__temperature -= 1




    def __repr__(self):
        if self.__status:
            return f'Кондиционер включен. Температурный режим: {self.__temperature} градусов.'
        else:
            return 'Кондиционер выключен.'