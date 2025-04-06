import datetime

def today(print_today : bool) -> tuple:
    y = datetime.datetime.now().year
    m = datetime.datetime.now().month
    d = datetime.datetime.now().day

    if print_today:
        print(f"today is {y}/{m}/{d}")

    return ( y ,m ,d )


def calculate_age(birthday : tuple, today : tuple) -> int:
    agey = today[0] - birthday[0]
    agem = today[1] - birthday[1]
    aged = today[2] - birthday[2]

    if agem != 0 or aged != 0:
        agey += 1

    return agey


class Person:
    def __init__(self,
                 name : str,
                 birthday : tuple,
                 height : int,
                 job : str):
        self.name = name
        self.birthday = birthday
        self.height = height
        self.job = job
        self._age = calculate_age(birthday, today(True))


        #c self.dowrite(([self.name, self.year,
        #c              self.birthday, self.height,
        #c              self._age, self.job]))
        #c Person.find(10)


    def introduce(self) -> None:
        print(f"Hello, my name is {str(self.name)}. \n"
              f"I was born in Year {str(self.birthday[0])}. \n"
              f"My birthday is {str(self.birthday[1])}/{str(self.birthday[2])}. \n"
              f"I am {str(self._age)} years old. \n"
              f"I am {str(self.height)}cm tall. \n"
              f"I am a{str(self.job)}. \n"
              f"Nice to meet you! \n" )


    def find(self, num):
        global ind
        for i in range(1, num):
            text = open("/Users/yihaichen/Desktop/mycomputer/code/project1/python/Generatefiles/classes"+str(i)+".txt", "r")
            if text != None:
                if i == num:
                    print(" Warning: Memory is full.")
                    print(f"Memory:{i}/{num} |{self.summary(num+1)}| \n")
                    return 0
            else:
                suma = Person.summary(0+i+1, ">")
                sumb = Person.summary(num-i+1, " ")
                print(f" Memory:{i}/{num} "
                      f" |{suma + sumb}| \n")
                ind = i


    def summary(self, num, word):
        if num <= 0:
            print("wrong index")
            return "Error"
        if num == 1:
            return word

        o = o + self.summary(num - 1, word)
        return o



class DatabaseService:
    @classmethod
    def query(self, id: int) -> Person:
        if id <= 0:
            print("wrong index")
            return False

        try:
            file = open(f"/Users/yihaichen/Desktop/mycomputer/code/project1/python/Generatefiles/classes{id}.txt", "r")
            text = file.read()
        except:
            print("read text error")
            return False

        # print("[Leo] text: ", text, type(text))
        term1 = self.read(text)
        print(type(term1))

        term2 = id(term1)
        a = term2
        self.introduce(a)

    def introduce(self, input:list) -> None:
        print(f"Hello, my name is {input[0]}. "
              f"I was born in Year {input[1][0]}."
              f"My birthday is {input[1][1]}/{input[1][2]}."
              f"I am {input[2]} years old."
              f"I am {input[3]}cm tall ."
              f"My job is {input[4]}."
              f"Nice to meet you!")

    def read(line:str) -> list:
        long = len(line)
        numind = 1
        word = None
        output = []
        _term = ""
        for i in range(0, long, 1):
            word = line[i]
            if word == ",":
                output.append(_term)
            else:
                term = _term + word
                _term = term

        return output

    def change(line:list)->list:
        out = [None, None, None, None, None, None]
        for i in range(0, 6):
            line[i] = out[6-i]
        return out


    def register(self, person):
        try:
            change = input("Who do you want to change :\n>>> ")
            where = "/Users/yihaichen/Desktop/mycomputer/code/project1/python/Generatefiles/classes"+str(change)+".txt"
            self.write(where, person)
        except:
            print("read text error")
            return 0

    def write(where, thing):
        a = open(where, "w")
        a.write(str(thing))
        a.close()




def test_person():
    leo_chen = Person("Leo Chen", (2014, 8, 6), 145, "student")
    leo_chen.introduce()

    id = DatabaseService.register(leo_chen)
    person = DatabaseService.query(id)
    person.introduce()


test_person()
