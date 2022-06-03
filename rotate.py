nums = [
    [10, 20, 30, 40, 50],
    [10, 20, 30, 40],
    [10, 20, 30]
]

if __name__ == '__main__':
    z = 0
    total = 0
    for y in range(0, len(nums[z])):
        linha = 0
        for x in range(0, len(nums)):
            if y < len(nums[x]):
                linha += nums[x][y]
        total += linha
        print(f'line={linha}')
        z += 1
    print(f'total={total}')

    print('-------')
    total = 0
    for x in range(0, len(nums)):
        linha = 0
        for y in range(0, len(nums[x])):
            linha += nums[x][y]
        total += linha
        print(f'line={linha}')
    print(f'total={total}')
