v1 = "first string"
v2 = "second string"
method1 = "use two temporary variables to refer to v1 and v2 Then use v1 and v2 to represent to the new variables"
method2  = "use one temporary variable to assign v1. Then switch v1 with v2. Finally, use the temporary variable to replace v2"

print ("Exercise:")
print ("find a way to switch the value of two given variables \n")

print ("Solutions:\n")
print ("Solution #1:", method1,"\n")
print ("Given: \nv1=", v1, "\nv2=", v2, "\n")


temp1 = v1
temp2 = v2
print (temp1)
print (temp2, "\n")

v1 = temp2
v2 = temp1
print (v1)
print (v2, "\n")

print ("Solution #2:", method2,"\n")
print ("Given: \nv1=", v1, "\nv2=", v2, "\n")

v1 = "first string"
v2 = "second string"
print (v1)
print (v2, "\n")

temp1 = v1
v1 = v2
v2 = temp1
print (v1)
print (v2)
