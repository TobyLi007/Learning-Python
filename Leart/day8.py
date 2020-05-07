from time import sleep

class myTime(object):

    def __init__(self, hours = 0, mins = 0, seconds = 0):
        self.hours = hours
        self.mins = mins
        self.seconds = seconds


    def displayTime(self):
        print('%d hours, %d mins, %d secs' %(self.hours, self.mins, self.seconds))


    def ticTime(self):
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.mins += 1
            if self.mins == 60:
                self.mins = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0


def main():
    myClock = myTime(23, 59, 40)
    while True:
            myTime.displayTime(myClock)
            sleep(1) #1 sec sleep
            myTime.ticTime(myClock)
            

if __name__ == '__main__':
    main()

