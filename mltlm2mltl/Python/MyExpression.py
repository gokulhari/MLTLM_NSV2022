import pytest

class MyExpression: 
    def __init__(self, opName="", left="", right="", timeName="", bounds=[], fromTimeName=""):
        self.opName = opName
        self.left = left
        self.right = right
        self.bounds = bounds
        self.timeName = timeName
        self.fromTimeName = fromTimeName
    def reconstruct2(self):
        if not self.bounds:
            return (self.left + " " + self.opName + " " + self.right)
        else:
            return (self.left + " " + self.opName + "[" + str(self.bounds[0]) + "," +
            str(self.bounds[1]) + "]" + " " + self.right)

    def reconstruct(self):
        if not self.bounds:
            return (self.left + " " + self.opName + " " + self.right)
        else:
            return (self.left + " " + self.opName + "[" + str(self.bounds[0]) + "," + str(self.bounds[1]) + "," + self.timeName + "]" +  " " +"(" + self.right + ")")

    def clear(self):
        self.opName = ""
        self.left = ""
        self.right = ""
        self.bounds.clear() 
        self.timeName = ""
        self.fromTimeName = ""
        
    def copy(self):
        you = MyExpression()
        you.opName = self.opName
        you.left = self.left
        you.right = self.right
        you.bounds = self.bounds.copy()
        you.timeName = self.timeName
        you.fromTimeName = self.fromTimeName
        return you

        

    def __repr__(self):
        return "MyExpression()"
    def __str__(self):
        return ("opName = " + self.opName + "\n bounds = [" + ','.join(str(e) for e in self.bounds) + "] \n" + "timeName: " + self.timeName + "\n left = " + self.left + "\n right = " + self.right + "\n fromTimeName: " + self.fromTimeName)


def test_reconstruct():
    exp = MyExpression(opName="U",left="a0",right="a1",timeName="c",bounds=[1,2])
    assert exp.reconstruct() == "a0 U[1,2,c] (a1)"


def test_reconstruct2():
    exp = MyExpression(opName="U", left="a0", right="a1",
                       timeName="c", bounds=[1, 2])
    assert exp.reconstruct2() == "a0 U[1,2] a1"



if __name__ == "__main__":
    ex = MyExpression(timeName="a")
    print(ex)
