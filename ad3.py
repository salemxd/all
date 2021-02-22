
import sys
ans = []
counter = 1
def atMost(k, list):
    global counter
    if (len(list)<=1):
        return ""

    string = ""
    matrix = [[0 for i in range(len(list))] for j in range(k)]

    for x in range(k):
        for y in range(len(list)):
            matrix[x][y] = str(counter)
            counter += 1

    string += "-"+str(list[0]) + " " + matrix[0][0] + " 0 "
    for x in range(1, k):
        string += "-"+matrix[x][1] + " 0 "

    for x in range(1, len(list)-1):
        string += "-"+str(list[x]) + " " + matrix[0][x] + " 0 "
        string += "-"+matrix[0][x-1] + " " + matrix[0][x] + " 0 "
        for y in range(1, k):
            string += "-"+str(list[x])+ " -" + matrix[y-1][x-1] + " " + matrix[y][x] + " 0 "
            string += "-"+ matrix[y][x-1] + " " + matrix[y][x] + " 0 "

        string += "-"+ str(list[x]) + " -" + matrix[k-1][x-1] + " 0 "
    string += "-"+ str(list[len(list)-1]) + " -" + matrix[k-1][len(list)-1] + " 0 "
    return string

def atLeast(list):
    test = ""
    for x in list:
        test += str(x) + " "
    test += "0 "
    return test

def orImply(b, list):
    if list == []:
        return ""
    result = ""
    for x in range(1, len(list)+1):
        result += "-" + str(x) + " "+ str(b) + " 0 "
    last_clause = ""
    for x in range(1, len(list)+1):
        last_clause += str(x) + " "
    last_clause += "-"+str(b) + " 0 "
    result += last_clause
    return result

def andImply(b, list):
    if list == []:
        return ""
    result = ""
    for x in list:
        result += "-"+str(x) + " "
    result += str(b) + " 0 "
    return result

def main(d, c, e):
    global counter
    world = [[[0 for k in range(d)] for j in range(int(d/c))] for i in range(e)]

    for x in range(e):
        for y in range(int(d/c)):
            for z in range(d):
                world[x][y][z] = counter
                counter += 1
    result = ""
    for x in range(e):
        for y in range(d):
            string = []
            for z in range(int(d/c)):
                string.append(world[x][z][y])
            result += atLeast(string)
    result2= ""
    for x in world:
        for y in x:
            string = []
            for z in range(len(y)):
                string.append(str(y[z]))
            result2 += atMost(c, string)
    result3 = ""
    for x in range(d):
        for y in range(d):
            if x == y:
                break
            list_of_i = []
            for z in range(e):
                for w in range(int(d/c)):
                    temp = [world[z][w][x], world[z][w][y]]
                    result3 += andImply(counter, temp)
                    list_of_i.append(counter)
                    counter+=1
            hej = atMost(1, list_of_i)
            result3 += hej
            counter+=1

    tot = result + result2 + result3
    answer = "p cnf " + str(counter-2) + " "+ str(tot.count(" 0 "))+ " \n"  + tot

    f = open("sat.txt", "w")
    f.write(answer)
    f.close()
    print(answer)


main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
