import math

def get_bit_length(n):
    return math.floor(math.log2(n)) + 1

n = int(input("请输入模数 n: "))

bit_length = get_bit_length(n)
print(f"模数n的比特数是: {bit_length}")