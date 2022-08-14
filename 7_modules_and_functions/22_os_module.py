"""
os module recursively

nonlocal keyword
"""
import os


def list_directories(s):

    def dir_list(d):
        nonlocal tab_stop
        files = os.listdir(d)
        for f in files:
            current_dir = os.path.join(d, f)
            if os.path.isdir(current_dir):
                print("\t" * tab_stop + "Directory " + f)
                tab_stop += 1
                dir_list(current_dir)
                tab_stop -= 1
            else:
                print("\t" * tab_stop + f)

    tab_stop = 0
    if os.path.exists(s):
        print("Directory listing of " + s)
        dir_list(s)
    else:
        print(s + " does not exist")


def spam1():

    def spam2():

        def spam3():
            z = " even"
            z += y
            print("In spam3,locals are {}".format(locals()))
            return z

        y = " more " + x  # y must exist before spam3 is called
        y += spam3()  # do not combine these assignments
        print("In spam2, locals are {}".format(locals()))
        return y

    x = "spam"  # x must exist before spam2 is called
    x += spam2()  # do not combine these assignments
    print("In spam1, locals are {}".format(locals()))
    return x


list_directories('.')

print(spam1())
print(locals())
print(globals())


# listing = os.walk('.')
# for root, directories, files in listing:
#     print(root)
#     for d in directories:
#         print(d)
#     for file in files:
#         print(file)

