def cheese_and_crackers(cheese_count, boxes_of_crackers):
    """
    Printing messages format crackers

    Parameters
    ----------
    cheese_count :

    boxes_of_crackers :


    Returns
    -------
    out :

    """

    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside tool:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


def unpacker(*args, **kwargs):

    res = [i for n, i in kwargs.items()]
    myl = []

    for i in args:
        myl.append(i)

    for i in res:
        myl.append(i)

    return myl


unpacker(1, 2, 3, 4, 1000, 1000, 1000, hey=20, income=50)
