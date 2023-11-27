import re

Units = ["нула", "един ", "два ", "три ", "четири ", "пет ", "шест ", "седем ", "осем ", "девет ", "десет ",
         "единадесет ", "дванадесет ", "тринадесет ", "четиринадесет ", "петнадесет ", "шестнадесет ",
         "седемнадесет ", "осемнадесет ", "деветнадесет "]

Units1 = ["", "една ", "две ", "три ", "четири ", "пет ", "шест ", "седем ", "осем ", "девет ", "десет ",
          "единадесет ", "дванадесет ", "тринадесет ", "четиринадесет ", "петнадесет ", "шестнадесет ",
          "седемнадесет ", "осемнадесет ", "деветнадесет "]

Decim = ["", "двадесет ", "тридесет ", "четиридесет ", "петдесет ", "шестдесет ", "седемдесет ",
         "осемдесет ", "деведесет "]

Hundr = ["", "", "сто ", "двеста ", "триста ", "четиристотин ", "петстотин ", "шестстотин ",
         "седемстотин ", "осмстотин ", "деветстотин "]

Thous = ["", "", "хиляди ", "милиона ", "милиарда "]

Thous1 = ["", "", "хиляда ", "милион ", "милиард "]

def is_cents_have_one(cents):
    for current_cent in range(1, 92, 10):
        if current_cent == cents and current_cent != 11:
            return True


def Spell(NumStr, i):
    RetStr = ""
    Num = int(NumStr)

    if Num == 0:
        return RetStr

    if Num == 1:
        if i == 1:
            RetStr = "и " + Units[1] + Thous1[1]
        elif i == 2:
            RetStr = Thous1[2]
        else:
            RetStr = Units[1] + Thous1[i]
        return RetStr

    RetStr = RetStr + "" + Hundr[int(NumStr[0]) + 1]
    if int(NumStr[1:]) == 0:
        return RetStr + Thous[i]

    if NumStr[1] == "0" or NumStr[1] == "1":
        if i == 2:
            return RetStr + "и " + Units1[int(NumStr[1:])] + Thous[i]
        else:
            return RetStr + "и " + Units[int(NumStr[1:])] + Thous[i]

    if NumStr[2] == "0":
        RetStr = RetStr + Decim[int(NumStr[1]) - 1]
    else:
        if i == 2:
            RetStr = RetStr + Decim[int(NumStr[1]) - 1] + "и " + Units1[int(NumStr[2])]
        else:
            RetStr = RetStr + Decim[int(NumStr[1]) - 1] + "и " + Units[int(NumStr[2])]

    return RetStr + Thous[i]


def Slov(Num):
    c = [None] * 6
    NumStr = str(Num)

    if Num == 0:
        return "нула лева и нула стотинки"

    Buf = "минус " if Num < 0 else ""
    Frac = abs(Num - int(Num))
    if Num < 0 or Frac != 0 or Frac == 0:
        Num = abs(int(Num))

    AtLeastOne = Num >= 1
    i = 1
    NumStr = str(Num)

    while len(NumStr) > 3:
        c[i] = NumStr[-3:]
        NumStr = NumStr[:-3]
        i += 1

    c[i] = "0" * (3 - len(NumStr)) + NumStr
    NumStr = ""

    for k in range(i, 0, -1):
        NumStr = NumStr + Spell(c[k], k)

    if NumStr == '':
        NumStr = "нула "
    if NumStr[:2] == "и ":
        NumStr = NumStr[2:]
    if NumStr[:2] == "и ":
        NumStr = NumStr[2:]

    # Process the digits after the decimal point (cents)
    FracStr = ""
    if Frac != 0:
        cents = int(round(Frac * 100))
        if is_cents_have_one(cents):
            FracStr = f" {Slov(cents)}и една стотинка"
            if " и един" or "леви" in FracStr:
                split_part = re.split(" и един|стотинка|един лев", FracStr)
                if split_part[1] != "и една ":
                    FracStr = " и" + ''.join(split_part) + "стотинки"
                    if "и и" in FracStr:
                        FracStr = ''.join(split_part) + "стотинки"
                else:
                    FracStr = " и" + ''.join(split_part) + "стотинка"
                    if "и и" in FracStr:
                        FracStr = ''.join(split_part) + "стотинкa"
        elif cents == 2:
            FracStr = f" и две стотинки"
        else:
            FracStr = f" и {Slov(cents)}стотинки"
    if FracStr:
        if (Num >= 2 or Num == 0) and Frac != 0:
            return f"{Buf}{NumStr}лева{FracStr}"
        elif Num == 1:
            return f"{Buf}{NumStr}лев{FracStr}"
        else:
            return f"{NumStr}"

    else:
        if Num >= 2 and Frac == 0.0:
            return f"{Buf}{NumStr}"
        else:
            if Num == 1 and Frac == 0:
                return f"{NumStr}лев"
            else:
                return f"{Buf}{NumStr}лева"


# num = 1.01
num = float(input())
result = Slov(num)

if ("лев" in result and "стотинки" not in result and " стотинкa " not in result):
    if "стотинкa" not in result:
        print(f"{result} и нула стотинки")
    else:
        print(f"{result}")
elif "лева" not in result and "стотинки" not in result and "стотинка" not in result:
    print(f"{result}лева и нула стотинки")
elif "лева и една" in result:
    split_result = result.split(" стотинки")
    result = ''.join(split_result)
    print(f"{result}")
else:
    print(result)
