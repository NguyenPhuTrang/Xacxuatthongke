ten =(input("Nhập tên : "))
print(ten)
def ThuanNghich(n):
    str1 = str(n);  
    str2 = str1[::-1];  
    if (str1 == str2):
        return True;
    else:
        return False;

n = int(input("Nhập số nguyên dương n = "));
print("Check ", n, "là", ThuanNghich(n));
