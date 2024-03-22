import os


ROOT = __file__
def get_full_path(*paths):
    root_dir = os.path.dirname(ROOT)
    print(f"Root: {root_dir}")
    full_path = os.path.join(root_dir, *paths)
    return full_path

fp=get_full_path('..\datasets\creditcard.csv')
print(f"fullPath:{fp}")