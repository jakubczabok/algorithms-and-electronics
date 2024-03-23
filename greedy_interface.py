# This project is simple app with interface which calculates change of coins using both greedy algorith and optimal solution (the least number of coins used)

import copy
import tkinter as tk
from tkinter import ttk

# Different sets of coins for tests
coins1 = [20, 10, 10, 5, 1, 1]
coins2 = [11, 11, 10, 5, 2, 1, 1]

root = tk.Tk()

label = tk.Label(root, text=("given change"), font=('Arial', 18), bg="black", fg="white")
label.pack()



def GiveChangeGreedy(coins,change):
    usedCoins = []
    copy = copy.deepcopy(coins)
    while (change > 0 and len(copy) > 0):
        if max(copy) <= change:
            usedCoins.append(max(copy))
            change -= max(copy)
            index = copy.index(max(copy))
        del copy[index]
    if len(copy) == 0 and change > 0:
        print("giving change failed")
        return
    else:
        return usedCoins

# using dynamic programming
def GiveChangeOptimal(accesible_coins, change):
    n = len(accesible_coins)
    if reszta > sum(accesible_coins):
        print("giving change failed")
        return
    dp = [float('inf')] * (change + 1)
    dp[0] = 0

    for i in range(1,change+ 1):
        for j in range(n):
            if accesible_coins[j] <= i:
                dp[i] = min(dp[i], dp[i - accesible_coins[j]] + 1)

    result = []
    i = coins
    while i > 0:
        for j in range(n):
            if i >= accesible_coins[j] and dp[i] == dp[i - accesible_coins[j]] + 1:
                result.append(accesible_coins[j])
                i -= accesible_coins[j]
                break
    return result


def update_label1():
    label1.config(text="change given greedy from 31 cents " + str(GiveChangeGreedy(coins1,31)))
def update_label2():
    label2.config(text="change given optimal from 31 cents " + str(GiveChangeOptimal(coins1,31)))
def update_label3():
    label3.config(text="change given greedy from 26 cents " + str(GiveChangeGreedy(coins2,26)))
def update_label4():
    label4.config(text="change given optimal from 26 cents " + str(GiveChangeOptimal(coins2,26)))


root.geometry("600x500")
root.configure(bg="black")
root.title("giving change")

style = ttk.Style()
style.configure('TButton', font=('Arial', 14), padding=5, foreground='green', background='green', borderwidth=4, relief="raised")

button_calculate1 = ttk.Button(root, text="Greedy from 31", command=update_label1)
button_calculate1.pack(pady=5)

button_calculate2 = ttk.Button(root, text="Optimal from 31", command=update_label2)
button_calculate2.pack(pady=5)

button_calculate3 = ttk.Button(root, text="Greedy from 26", command=update_label3)
button_calculate3.pack(pady=5)

button_calculate4 = ttk.Button(root, text="Optimal from 26", command=update_label4)
button_calculate4.pack(pady=5)


label1 = tk.Label(root, text="", font=('Arial', 18), bg="black", fg="white")
label1.pack()

label2 = tk.Label(root, text="", font=('Arial', 18), bg="black", fg="white")
label2.pack()

label3 = tk.Label(root, text="", font=('Arial', 18), bg="black", fg="white")
label3.pack()

label4 = tk.Label(root, text="", font=('Arial', 18), bg="black", fg="white")
label4.pack()


print("change from greedy algorithm")
print(GiveChangeGreedy(coins1, 31))
print(GiveChangeGreedy(coins2, 26))
print("optimal change")
print(GiveChangeOptimal(coins1, 31))
print(GiveChangeOptimal(coins2, 26))

root.mainloop()
