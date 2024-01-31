def outer():
    x=1

    def inner():
        x=2
        return 2
    
    inner()
    return x

print(outer())