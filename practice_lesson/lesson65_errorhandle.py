l = [1,2,3]
i = 5

try:
    l[i]
except IndexError as ex:
    print("Index Exception : {}".format(ex))
except NameError as ex:
    print("NameError Exception : {}".format(ex))
except Exception as ex:
    print("Exception : {}".format(ex))
else:
    print("done")
finally:
    print('clean up')