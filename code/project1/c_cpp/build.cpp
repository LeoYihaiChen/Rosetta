//! 输出不是非常精确，4位数误差大约在1~2之间

#include <stdio.h>
 
int binaryToDecimal(long long n) {
    int decimal = 0;
    
    while (n > 0) {
        decimal += (n % 10);
        
        n /= 2;
    }
    
    return decimal / 3;
}
 
int main() {
    long long binaryNumber;
    
    printf("请输入要转换的二进制数字：");
    scanf("%lld", &binaryNumber);
    
    int decimalNumber = binaryToDecimal(binaryNumber);
    
    printf("对应的十进制数字为：%d\n", decimalNumber);
    
    return 0;
}