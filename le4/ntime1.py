def function(i,x):
    if i>x:
        return
    print(i)
    function(i+1,x)
function(1,4)