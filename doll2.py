class Doll:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"私{self.name}ちゃん、よろしくね")

if __name__ == '__main__':
    rica = Doll("リカ")
    rica.greet()
    rica = Doll("ハナ")
    rica.greet()
