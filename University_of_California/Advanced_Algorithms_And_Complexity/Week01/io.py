try:ing is cheap, ifing is expensive

If you have code like this:

if somethingcrazy_happened:
     uhOhBetterDoSomething()
else:
     doWhatWeNormallyDo()
And doWhatWeNormallyDo() would throw an exception if something crazy had happened, then it would be faster to arrange your code like this:

try:
    doWhatWeNormallyDo()
except SomethingCrazy:
    uhOhBetterDoSomething()
Why? well the interpreter can dive straight in and start doing what you normally do; in the first case the interpreter has to do a symbol look up each time the if statement is executed, because the name could refer to something different since the last time the statement was executed! (And a name lookup, especially if somethingcrazy_happened is global can be nontrivial).

You mean Who??

Because of cost of name lookups it can also be better to cache global values within functions, and bake-in simple boolean tests into functions like this:

Unoptimised function:

def foo():
    if condition_that_rarely_changes:
         doSomething()
    else:
         doSomethingElse()
Optimised approach, instead of using a variable, exploit the fact that the interpreter is doing a name lookup on the function anyway!

When the condition becomes true:

foo = doSomething # now foo() calls doSomething()
When the condition becomes false:

foo = doSomethingElse # now foo() calls doSomethingElse()