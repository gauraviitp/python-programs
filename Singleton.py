class Logger:
    _instance = None
    _startVal = 0

    def __init__(self):
        raise RuntimeError('call instance() method instead')

    @classmethod
    def instance(cls):
        if cls._instance == None:
            cls._instance = cls.__new__(cls)
        return cls._instance


class LoggerPythonic:
    _instance = None
    _startVal = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._startVal = 10

        return cls._instance


if __name__ == '__main__':
    loggerA = Logger.instance()
    loggerB = Logger.instance()

    if loggerA == loggerB:
        print('same')

    loggerA = LoggerPythonic()
    loggerB = LoggerPythonic()

    print(LoggerPythonic._startVal)

    if loggerA == loggerB:
        print('same')
