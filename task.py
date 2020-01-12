
# s - креветка, f - рыба, r - скала, e - пустое место
def main():
    # Input
    n = int(input())
    a = []
    for i in range(n):
        row = input().split()
        a.append(row)
    #


    # Output
    for i in range(n):
        for elem in a[i]:
            print(elem, end='')
        print('\n', end='')

if __name__ == '__main__':
    main()
