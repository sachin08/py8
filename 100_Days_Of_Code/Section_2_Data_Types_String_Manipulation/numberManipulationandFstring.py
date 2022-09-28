print(8/3)
print(int(8/3))
print(round(8/3))
print(round(8/3, 2))
print(8 // 3) #// -> floor division, whole number ignoring after decimal
print(type(8 // 3))

result = 4 / 2
result /= 2
print(result) 
print(type(result)) # type() -> float

score = 0
#User scores a point
score += 1 ## short hand operators -=, *=, /=
print(score)

## F Strings
#print("Your score is " + score) ## o/p : error - TypeError: can only concatenate str (not "int") to str
print("Your score is " + str(score)) ## correct but painful way of doing

score = 0
height = 1.8
isWinning = True
#f-String -> in front of " or '
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}") ## notice : no conversion needed now between different data formats :)