"""
Ques: User কাছ থেকে দুটি ইনপুট আনবে এবং ইনপুট দুটিকে গুনকরে গুনফলকে 2 দ্বারা গুন করবে এভাবে Loop চলতে থাকবে কিন্তু যখন
User ইনপুট দুটির মান -1 দিবে তখন terminal break করবে।
"""

start = 1
end = int(input("How Many times looping :"))

while start <= end:
    num1 = int(input("Enter Your First Number :"))
    num2 = int(input("Enter Your 2nd Number :"))
    result = num1 * num2 *2
    if(num1 == -1 & num2 == -1):
        break
    else:
        print(result)
