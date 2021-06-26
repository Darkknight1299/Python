line="*"
space="          "
total_len=1
while total_len<=10:
    print(space+line)
    line+="*"
    space=space[:-1]
    total_len+=1
