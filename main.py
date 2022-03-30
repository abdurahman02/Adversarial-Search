import numpy as np
import csv

with open("input.txt") as infile:
    infile = csv.reader(infile, delimiter=',')
    inputList = []
    for row in infile:
        inputList.append(np.array(row).reshape(3, 3).astype(int))


def printInputs():
    print("total inputs: ", len(inputList))
    for i in inputList:
        print(i)


def AllPossibleMoves(state, move):
    newMoves = []
    state = state.flatten()
    for i in range(len(state)):
        if int(state[i]) == 0:
            temp = state.copy()
            temp[i] = move
            newMoves.append(temp.reshape(3, 3))
    return newMoves


def whoseMove(state):
    if np.count_nonzero(state.flatten()) % 2:  # Turn of Second Player as condition will be true when nonzeros are odd
        # Turn of human if sum is > 0
        if state.sum() > 0:
            return -1
        return 1
    # turn of First Player as nonZeros are even
    mov = int(input("Please enter the first move: "))
    while not (int(mov) == -1 or int(mov) == 1):
        mov = int(input("please enter -1 or 1 for human or comp: "))
    return mov


def is_success(state):

    for i in range(3):
        if np.sum(state[:, i]) == 3 or np.sum(state[i, :]) == 3:
            return 1
        if np.sum(state[i, :]) == -3 or np.sum(state[:, i]) == -3:
            return -1
    a1 = np.array([state[0][0], state[1][1], state[2][2]])
    a2 = np.array([state[0][2], state[1][1], state[2][0]])
    if np.sum(a1) == 3 or np.sum(a2) == 3:
        return 1
    if np.sum(a1) == -3 or np.sum(a2) == -3:
        return -1
    return 0




def Agent(state, move):
    path = []
    if np.count_nonzero(state) == len(state.flatten()): #draw
        path.insert (0, state)
        lst = [is_success(state), path]
        return lst
    suc = is_success(state)
    if suc != 0:
        path.insert (0, state)
        lst = [suc, path]
        return lst
    que = AllPossibleMoves(state, move)
    maximum = [-1, []]
    minimum = [1, []]
    for tmp in que:
        var = Agent(tmp, (move)*-1)
        if var[0] >= maximum[0]:
            maximum[0] = int(var[0])
            maximum[1] = var[1]
        if var[0] <= minimum[0]:
            minimum[0] = int(var[0])
            minimum[1] = var[1]


    if move == 1:
        maximum[1].insert(0, state)
        return [maximum[0], maximum[1]]
    else:
        minimum[1].insert(0, state)
        return [minimum[0], minimum[1]]

# input is list stages to be computed


def main():
    state = inputList[5]

    v, p = Agent(state, whoseMove(state))
    print(p)

if __name__ == '__main__':
    main()
