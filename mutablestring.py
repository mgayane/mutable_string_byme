from collections.abc import MutableSequence
from string import ascii_uppercase, ascii_lowercase, digits, punctuation
from re import compile, sub

class MutableString(MutableSequence):
    alphabet = f"{ascii_uppercase}{ascii_lowercase}"

    def __init__(self, item):
        self.item = item

    def __getitem__(self, item):
        return self.item

    def __setitem__(self, item, value):
        self.item = value

    def __delitem__(self, index):
        pass

    def __add__(self, string):
        return f"{self} {string}"

    def __str__(self):
        return str(self.item)

    def __len__(self):
        return len(self.item)

    def __iter__(self):
        self.i = 0
        yield self

    def __repr__(self):
        return f"Mutable string {self.item}"

    def insert(self, index, value):
        pass

    def ord(self, c):
        if not isinstance(c, str):
            raise TypeError(f'str expected {type(c)} found')

        dicts = {}
        v = 97
        u = 65

        for i, j in enumerate(ascii_lowercase):
            dicts[j] = v + i
        for i, j in enumerate(ascii_uppercase):
            dicts[j] = u + i

        res = int(dicts[c])
        if not isinstance(res, int):
            raise ValueError(f'{c} not found')
        else:
            return res

    def chr(self, d):
        if not isinstance(d, int):
            raise TypeError(f'int expected {type(d)} found')

        dicts = {}
        v = 97
        u = 65

        for i, j in enumerate(ascii_lowercase):
            dicts[j] = v + i
        for i, j in enumerate(ascii_uppercase):
            dicts[j] = u + i

        res = 0
        for key, val in dicts.items():
            if d == val:
                res = key

        if not isinstance(res, str):
            raise ValueError(f'{d} not found')
        else:
            return res

    def upper(self):
        result = ""
        for char in self.item:
            if char not in self.alphabet or char in ascii_uppercase:
                result += char
            else:
                result += self.chr(self.ord(char)-32)
        return result

    def lower(self):
        result = ""
        for char in self.item:
            if char not in self.alphabet or char in ascii_lowercase:
                result += char
            else:
                result += chr(ord(char)+32)
        return result

    def capitalize(self):
        f_item = self.item[0]

        if f_item in ascii_lowercase:
            result = f"{chr(ord(f_item)-32)}{self.item[1:]}"
        else:
            result = self.item
        return result

    def title(self):
        result = ""
        for char in self.item.split(' '):
            if char[0] in ascii_lowercase:
                res = f"{chr(ord(char[0])-32)}{char[1:]}"
            else:
                res = f"{char} "
            result += res
        return result

    def startswith(self, string):
        if not isinstance(string, str):
            raise TypeError(f"str expected {type(string)} found")

        len2 = len(string)

        if len(self.item) < len(string):
            return False

        for num in range(len2):
            if self.item[num] == string[num]:
                continue
            else:
                return False
        return True

    def endswith(self, string):
        if not isinstance(string, str):
            return False

        len2 = len(string)
        if len2 > len(self.item):
            return False

        rev_my = self.item[::-1]
        rev2 = string[::-1]
        for num in range(len2):
            if rev2[num] == rev_my[num]:
                continue
            else:
                return False
        return True

    def center(self, width, fill=None):
        if not isinstance(width, int):
            raise TypeError(f"int type expected, {type(width)} found")

        if fill is not None:
            if not isinstance(fill, str) or len(fill) == 0 or len(fill) > 1:
                raise TypeError("The fill character must be exactly one character long and str type")
            symb = fill
        else:
            symb = " "

        len_def = len(self.item)

        if width < len_def:
            return self.item

        x = len_def % 2
        y = width % 2

        if (x == 0 and y == 0) or (x != 0 and y != 0):
            x = int((width - len_def) / 2)
            return f"{symb*x}{self.item}{symb*x}"

        if x != 0 and y == 0:
            left_x = int((width - len_def - 1) / 2)
            right_x = left_x + 1
            return f"{symb*left_x}{self.item}{symb*right_x}"

        if x == 0 and y != 0:
            left_x = int((width - len_def + 1) / 2)
            right_x = left_x - 1
            return f"{symb*left_x}{self.item}{symb*right_x}"

    def count(self, string, start=None, end=None):
        if not isinstance(string, str):
            raise TypeError(f"type of {string} str expected {type(string)} found")

        s = start if isinstance(start, int) else 0
        f = end if isinstance(end, int) else 0

        count = 0
        len_sub = len(string)
        len_def = len(self.item)

        if len_def < len_sub or s > len_def or (f != 0 and s > f) or s < 0 or f < 0:
            return count

        stop = len_def if f == 0 else len_def - (len_def - f)

        for i in range(s, stop):
            if self.item[i:i + len_sub] == string:
                count += 1

        return count

    def find(self, string, start=None, end=None):
        if not isinstance(string, str):
            raise TypeError(f"string expected {type(string)} found")

        s = 0
        if start is not None:
            if isinstance(start, int):
                s = start
            else:
                raise TypeError(f"int expected {type(start)} found")

        f = 0
        if end is not None:
            if isinstance(end, int):
                f = end
            else:
                raise TypeError(f"int expected {type(start)} found")

        pos = -1
        j = len(string)
        len_def = len(self.item)

        if s > len_def or s < 0 or f < s or f < 0:
            return pos

        stop = f if f > s and f <= len_def else len_def
        sub_str = self.item[:stop]
        for i in range(len(sub_str)):
            if sub_str[i:i+j] == string:
                pos = i
                break

        return pos

    def rfind(self, s, start=None, end=None):
        if not isinstance(s, str):
            raise TypeError(f"string expected {type(s)} found")

        st = 0
        if start is not None:
            if isinstance(start, int):
                st = start
            else:
                raise TypeError(f"int expected {type(start)} found")

        f = 0
        if end is not None:
            if isinstance(end, int):
                f = end
            else:
                raise TypeError(f"int expected {type(start)} found")

        j = len(s)
        len_def = len(self.item)

        if st > len_def or st < 0 or f < st or f < 0:
            return -1

        stop = f if st < f <= len_def else len_def
        sub_str = self.item[:stop]
        res = []

        for i in range(len(sub_str)):
            if sub_str[i:i+j] == s:
                res.append(i)

        return res.pop() if len(res) > 0 else -1

    def index(self, string, start=None, end=None):
        if not isinstance(string, str):
            raise TypeError(f"string expected {type(string)} found")

        s = 0
        if start is not None:
            if isinstance(start, int):
                s = start
            else:
                raise TypeError(f"int expected {type(start)} found")

        f = 0
        if end is not None:
            if isinstance(end, int):
                f = end
            else:
                raise TypeError(f"int expected {type(start)} found")

        j = len(string)
        len_def = len(self.item)

        if s > len_def or s < 0 or f < s or f < 0:
            raise ValueError("substring not found")

        stop = f if f > s and f <= len_def else len_def
        sub_str = self.item[:stop]
        pos = ''

        for i in range(len(sub_str)):
            if sub_str[i:i+j] == string:
                pos = i
                break

        if isinstance(pos, int):
            return pos
        else:
            raise ValueError("substring not found")

    def rindex(self, string, start=None, end=None):
        if not isinstance(string, str):
            raise TypeError(f"string expected {type(string)} found")

        s = 0
        if start is not None:
            if isinstance(start, int):
                s = start
            else:
                raise TypeError(f"int expected {type(start)} found")

        f = 0
        if end is not None:
            if isinstance(end, int):
                f = end
            else:
                raise TypeError(f"int expected {type(start)} found")

        j = len(string)
        len_def = len(self.item)

        if s > len_def or s < 0 or f < s or f < 0:
            raise ValueError("substring not found")

        stop = f if s < f <= len_def else len_def
        sub_str = self.item[:stop]
        res = []

        for i in range(len(sub_str)):
            if sub_str[i:i+j] == string:
                res.append(i)

        if len(res) > 0:
            return res.pop()
        else:
            raise ValueError("substring not found")

    def split(self, symbol):
        if not isinstance(symbol, str):
            raise TypeError(f"must be str or None, {type(symbol)} found")

        if isinstance(symbol, str) and len(symbol) == 0:
            raise ValueError("empty separator")

        len_def = len(self.item)
        j = len(symbol)
        res = []
        l = 0
        for i in range(len_def):
            if self.item[i:i+j] == symbol:
                res.append(self.item[l:i])
                l = i+j

        last_pos = self.rfind(symbol)
        if last_pos < i:
            res.append(self.item[last_pos+j:])

        return res

    def replace(self, old, new):
        if self.find(old) == -1:
            raise ValueError('value not found')

        j = len(old)
        n = self.find(old)

        return f"{self.item[:n]}{new}{self.item[n+j:]}"

    def rreplace(self, old, new): # right_replace ?
        pass

    def istitle(self):
        count = 0
        checker = 0

        for char in self.item.split():
            if char[0] in self.alphabet:
                checker += 1
            if char[0] in ascii_uppercase and all(map(lambda x: x not in ascii_uppercase, filter(lambda x: x in self.alphabet, char[1:]))) :
                count += 1

        return True if count == checker else False

    def join(self, array):
        if not isinstance(array, (list, tuple, dict)):
            raise TypeError(f"list or tuple expected {type(array)} found")

        res = ''
        if isinstance(array, dict):
            items = array.values()
        else:
            items = array

        for i, item in enumerate(items):
            sep = " " if i+1 < len(items) else ""
            res += f'{item}{sep}'

        return res

    def format(self, *args, **kwargs):
        pass

    def lstrip(self, c=None):
        p = compile(r"^\s+")
        if c is not None:
            if not isinstance(c, str):
                raise TypeError(f"str expected {type(c)} found")
            else:
                p = compile(r"^"+c+"+")

        return sub(p, "", self.item)

    def rstrip(self, c=None):
        p = compile(r"\s+$")
        if c is not None:
            if not isinstance(c, str):
                raise TypeError(f"str expected {type(c)} found")
            else:
                p = compile(r""+c+"+$")

        return sub(p, "", self.item)

    def strip(self, c=None):
        p = compile(r"^\s+|\s+$")
        if c is not None:
            if not isinstance(c, str):
                raise TypeError(f"str expected {type(c)} found")
            else:
                p = compile(r"^" + c + "+|"+c+"+$")

        return sub(p, "", self.item)

    def isdigit(self):
        pass

    def isalpha(self):
        pass

    def isalnum(self):
        pass

    def islower(self):
        letters_set = set()
        for i in self.item:
            if i in digits or i in punctuation or i == " ":
                continue
            elif i in ascii_lowercase:
                letters_set.add(i)
                continue
            else:
                return False

        return True if len(letters_set) > 0 else False

    def isupper(self):
        letters_set = set()
        for i in self.item:
            if i in digits or i in punctuation or i == " ":
                continue
            elif i in ascii_uppercase:
                letters_set.add(i)
                continue
            else:
                return False

        return True if len(letters_set) > 0 else False

    def isspace(self):
        if len(self.item) > 0:
            counter = 0
            for i in self.item:
                if i == " ":
                    counter += 1
            return True if counter == len(self.item) else False
        else:
            return True if " " in self.item else False
