# Please write the main file for this algorithm
# A demo is:
from arguments import parameters
from arguments import outputs

fi = open("{}/data.txt".format(outputs["in"]))
with open("{}/data.txt".format(outputs["out"]), "w") as f:
    n = parameters["n"]
    for i in range(n):
        x = int(fi.readline())
        if (x % 2 == 0)
            f.write("{}".format(x))
