#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7

alpha = ["A", "B", "C"]
alpha.append("D")
alpha.append("E")
print(alpha)

alpha = alpha + ["F"]
print(alpha)

indexofd = alpha.index("B")
print("The index of d is " + str(indexofd))

alpha.remove("B")
print(alpha)
