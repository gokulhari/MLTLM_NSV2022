import pytest
import sys

def addPrefactors(prefactora, prefactorb):

    if (prefactora and prefactorb):
        valas = prefactora[2:]
        valas = valas.split(",")
        vala1 = int(valas[0])
        vala2 = valas[1].split("]")
        vala2 = int(vala2[0])

        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
    elif (not prefactora) and (not prefactorb):
        vala1 = 0
        vala2 = 0
        valb1 = 0
        valb2 = 0
    elif not prefactora:
        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
        vala1 = 0
        vala2 = 0
    else:
       valas = prefactora[2:]
       valas = valas.split(",")
       vala1 = int(valas[0])
       vala2 = valas[1].split("]")
       vala2 = int(vala2[0])
       valb1 = 0
       valb2 = 0
    val1 = vala1 + valb1
    val2 = vala2 + valb2
    if (val1 is 0) and (val2 is 0):
        return ""
    else:
        return "G[" + str(val1) + "," + str(val2) + "]"


def minusPrefactors(prefactora, prefactorb):
    if (prefactora and prefactorb):
        valas = prefactora[2:]
        valas = valas.split(",")
        vala1 = int(valas[0])
        vala2 = valas[1].split("]")
        vala2 = int(vala2[0])

        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
    elif (not prefactora) and (not prefactorb):
        vala1 = 0
        vala2 = 0
        valb1 = 0
        valb2 = 0
    elif (not prefactora):
        valbs = prefactorb[2:]
        valbs = valbs.split(",")
        valb1 = int(valbs[0])
        valb2 = valbs[1].split("]")
        valb2 = int(valb2[0])
        vala1 = 0
        vala2 = 0
    elif (not prefactorb):
        valas = prefactora[2:]
        valas = valas.split(",")
        vala1 = int(valas[0])
        vala2 = valas[1].split("]")
        vala2 = int(vala2[0])
        valb1 = 0
        valb2 = 0
    val1 = vala1 - valb1
    val2 = vala2 - valb2

    if (val1 < 0) or (val2 < 0):
        sys.exit("Internal indices are negative")
    elif (val1 is 0) and (val2 is 0):
        return ""
    else:
        return "G[" + str(val1) + "," + str(val2) + "]"
class MyExpression3: 
    def __init__(self, opName="", left="", right="", timeName="", bounds=[], fromTimeName="",prefactor=""):
        self.opName = opName
        self.left = left
        self.right = right
        self.bounds = bounds
        self.timeName = timeName
        self.fromTimeName = fromTimeName
        self.prefactor = prefactor
    def reconstruct2(self):
        if self.opName is "G":
            return (addPrefactors(self.prefactor, "G[" + str(self.bounds[0]) + "," + str(self.bounds[1]) + "]") + " " + self.right  )
        elif not self.bounds:
            return (self.prefactor + "(" + self.left + " " + self.opName + " " + self.right + ")" )
        else:
            return (self.prefactor + "(" + self.left + " " + self.opName + "[" + str(self.bounds[0]) + "," + str(self.bounds[1]) + "]" + " " + self.right + ")")

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
        self.prefactor = ""

    def copy(self):
        you = MyExpression3()
        you.opName = self.opName
        you.left = self.left
        you.right = self.right
        you.bounds = self.bounds.copy()
        you.timeName = self.timeName
        you.fromTimeName = self.fromTimeName
        you.prefactor = self.prefactor
        return you

        

    def __repr__(self):
        return "MyExpression()"
    def __str__(self):
        return ("opName = " + self.opName + "\n bounds = [" + ','.join(str(e) for e in self.bounds) + "] \n" + "timeName: " + self.timeName + "\n left = " + self.left + "\n right = " + self.right + "\n fromTimeName: " + self.fromTimeName)


def test_reconstruct():
    exp = MyExpression3(opName="U",left="a0",right="a1",timeName="c",bounds=[1,2])
    assert exp.reconstruct() == "a0 U[1,2,c] (a1)"


def test_reconstruct2():
    exp = MyExpression3(opName="U", left="a0", right="a1",
                       timeName="c", bounds=[1, 2])
    assert exp.reconstruct2() == "a0 U[1,2] a1"



if __name__ == "__main__":
    ex = MyExpression3(timeName="a")
    print(ex)
