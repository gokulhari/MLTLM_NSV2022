#from typing import _Collection
from MyExpression3 import MyExpression3
from MyExpression3 import addPrefactors

def moduloReduction4(mye=MyExpression3(), fromTime="a"):
    # Now define mapping from a to b, b to c, and c to d
    a2b = 24
    b2c = 7
    c2d = 4
    a2c = a2b * b2c
    a2d = a2b * b2c * c2d
    b2d = b2c * c2d
    
    if (fromTime == "a" and mye.timeName == "b"):
        param = a2b
    elif (fromTime == "b" and mye.timeName == "c"):
        param = b2c 
    elif (fromTime == "c" and mye.timeName == "d"):
        param = c2d
    elif (fromTime == "a" and mye.timeName == "c"):
        param = a2c
    elif (fromTime == "a" and mye.timeName == "d"):
        param = a2d
    elif (fromTime == "b" and mye.timeName == "d"):
        param = b2d
    else:
        print("Unknown time conversion \n")
    class Container(object):
      prefactor = ""
      string = ""
      num = 0
    out = Container()
    out.prefactor = "G[" + str(mye.bounds[0]*param) + "," + str(mye.bounds[0]*param) + "]"
    out.prefactor = addPrefactors(out.prefactor,mye.prefactor)
    out.string = "("

    if (mye.opName == "U"):
      out.string += mye.right + " | ("
      for  i  in range(param, param*(mye.bounds[1] - mye.bounds[0] + 1),param):
        out.string += mye.left + " & "
        for j in range(param, i, param):
          out.string += "G[" + str(j ) + "," + str(j) + "]" + "(" + mye.left + ")" + " & "
        out.string += "G[" + str(i) + "," + str(i) + "]" + "(" + mye.right + ")"
        out.string += ") | ("
      out.string = out.string[:-3]
      out.string += ")"
    elif (mye.opName == "G"):
      out.string += mye.right + " & "
      for i in range(param, param * (mye.bounds[1] - mye.bounds[0] + 1), param):
        out.string += "G[" + str(i) + "," + str(i) + \
            "]" + "(" + mye.right + ")"
        out.string += " & "
      out.string = out.string[:-3]
      out.string += ")"
    elif (mye.opName == "F"):
      out.string += mye.right + " | "
      for i in range(param, param *( mye.bounds[1] - mye.bounds[0] + 1), param):
        out.string += "G[" + str(i) + "," + str(i) + \
            "]" + "(" + mye.right + ")"
        out.string += " | "
      out.string = out.string[:-3]
      out.string += ")"
    elif (mye.opName == "R"):
      temp = mye
      temp.opName = "R"
      temp.left = "!(" + temp.left + ")"
      temp.right = "!(" + temp.right + ")"
      out.string = "!" + moduloReduction3(temp, fromTime)
    else:
      print("Unknown operator.\n")
      out.string = ""
      out.prefactor = ""
    
    if out.prefactor:
      val1 = out.prefactor[2:]
      val1 = val1.split(",")
      val1 = int(val1[0])
      out.num = val1
    return out

if __name__ == "__main__":
    ex = MyExpression(timeName="c",opName="F",left="",right="a1",bounds=[3,5])
    out = moduloReduction3(ex, "a")
    print(out.prefactor)
    print(out.string)
