from MyExpression import MyExpression

def moduloReduction(mye=MyExpression(), fromTime="a"):
    # Now define mapping from a to b, b to c, and c to d
    a2b = 2
    b2c = 3
    c2d = 4
    a2c = a2b * b2c
    a2d = a2b * b2c * c2d
    b2d = b2c * c2d
    out = "("
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
    out += "("
    if (mye.opName == "U"):
      for  i  in range(param * mye.bounds[0], param * mye.bounds[1] + 1,param):
        for j in range(param * mye.bounds[0], i, param):
          out += "G[" + str(j) + "," + str(j) + "]" + "(" + mye.left + ")" + " & "
        out += "G[" + str(i) + "," + str(i) + "]" + "(" + mye.right + ")"
        out += ") | ("
      out = out[:-4]
    elif (mye.opName == "G"):
      for i in range(param * mye.bounds[0], param * mye.bounds[1] + 1, param):
        out += "G[" + str(i) + "," + str(i) + "]" +"(" + mye.right + ")"
        out += ") & ("
      out = out[:-4]
    elif (mye.opName == "F"):
      for i in range(param * mye.bounds[0], param * mye.bounds[1] + 1, param):
        out += "G[" + str(i) + "," + str(i) + "]" + "(" + mye.right + ")"
        out += ") | ("
      out = out[:-4]
    elif (mye.opName == "R"):
      temp = mye
      temp.opName = "R"
      temp.left = "!(" + temp.left + ")"
      temp.right = "!(" + temp.right + ")"
      out = "!" + moduloReduction(temp, fromTime)
    else:
      print("Unknown operator.\n")
    out += ")"
    return out

if __name__ == "__main__":
    ex = MyExpression(timeName="b",opName="U",left="a0",right="a1",bounds=[1,2])
    print(moduloReduction(ex,"a"))
