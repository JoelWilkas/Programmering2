N = 12; pointer1 = 0; tempPointer = 0; pointer2 = 1; öar = 0;
while N > 0:
    öar += 1;
    tempPointer = pointer1;
    pointer1 = pointer2;
    pointer2 = tempPointer + pointer2;
    print(öar);
    N -= pointer2;