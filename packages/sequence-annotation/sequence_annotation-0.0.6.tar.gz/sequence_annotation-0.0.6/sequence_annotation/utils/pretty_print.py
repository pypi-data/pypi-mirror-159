class PrettyPrint:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def ok_output(cls, message):
        print(cls.OKGREEN + message + cls.ENDC)

    @classmethod
    def warning_output(cls, message):
        print(cls.WARNING + message + cls.ENDC)

    @classmethod
    def fail_output(cls, message):
        print(cls.FAIL + message + cls.ENDC)
