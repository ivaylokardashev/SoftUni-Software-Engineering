# snake_case = input().replace(' ', '_').lower()
# print(snake_case)
# import pandas as pd
# df = pd.read_clipboard(sep='\t')
# print(df)
# df.to_csv('data.py',index=False)
# df = pd.read_csv('data.csv')

# import pandas as pd
#
#
# df = pd.read_clipboard(sep="\t")
# print(df)
# df.to_csv('data.py',index=False)
# df = pd.read_csv('data.csv')
import win32clipboard

# set clipboard data
# win32clipboard.OpenClipboard()
# win32clipboard.EmptyClipboard()
# win32clipboard.SetClipboardText('testing 123')
# win32clipboard.CloseClipboard()

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData().replace(' ', '_').lower()
win32clipboard.CloseClipboard()

file = open(f"{data}.py", 'w')
file.close()
