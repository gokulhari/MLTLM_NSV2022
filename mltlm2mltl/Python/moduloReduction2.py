from MyExpression import MyExpression

def moduloReduction2(mye=MyExpression(), fromTime="a"):
    # Now define mapping from a to b, b to c, and c to d
    a2b = 2
    b2c = 3
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

    out = "G[" + str(mye.bounds[0]*param) + "," + str(mye.bounds[0]*param) + "]" + "("

    if (mye.opName == "U"):
      out += mye.right + " | ("
      for  i  in range(param, param*(mye.bounds[1] - mye.bounds[0] + 1),param):
        out += mye.left + " & "
        for j in range(param, i, param):
          out += "G[" + str(j ) + "," + str(j) + "]" + "(" + mye.left + ")" + " & "
        out += "G[" + str(i) + "," + str(i) + "]" + "(" + mye.right + ")"
        out += ") | ("
      out = out[:-3]
      out += ")"
    elif (mye.opName == "G"):
      out += mye.right + " & "
      for i in range(param, param * (mye.bounds[1] - mye.bounds[0] + 1), param):
        out += "G[" + str(i) + "," + str(i) + "]" +"(" + mye.right + ")"
        out += " & "
      out = out[:-3]
      out += ")"
    elif (mye.opName == "F"):
      out += mye.right + " | "
      for i in range(param, param *( mye.bounds[1] - mye.bounds[0] + 1), param):
        out += "G[" + str(i) + "," + str(i) + "]" + "(" + mye.right + ")"
        out += " | "
      out = out[:-3]
      out += ")"
    elif (mye.opName == "R"):
      temp = mye
      temp.opName = "R"
      temp.left = "!(" + temp.left + ")"
      temp.right = "!(" + temp.right + ")"
      out = "!" + moduloReduction2(temp, fromTime)
    else:
      print("Unknown operator.\n")
    return out

if __name__ == "__main__":
    ex = MyExpression(timeName="c",opName="F",left="",right="a1",bounds=[3,5])
    print(moduloReduction2(ex,"a"))
