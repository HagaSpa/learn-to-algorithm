def binary_search(list, item):
    low = 0 # 最小インデックス
    high = len(list) - 1 # 最大インデックス

    while low <= high:
        mid = (low + high) // 2 # 2で除算して、余りは切り捨て。配列の中央のインデックスを取得
        guess = list[mid] # 配列の中央の値（推測値）
        if guess == item: # 配列の中央の値とitemが同じなら
            return mid
        if guess > item: # 配列の中央の値が、itemより大きければ（推測したが数字大きすぎた）
            high = mid - 1
        else:            # 配列の中央の値が、itemより小さければ（水即位した数字が小さすぎた）
            low = mid + 1
    return None # itemが存在しない

my_list = [1, 3, 5, 7, 9] # 要素が5つあるので、最も計算量が多くても2回でitemが見つけられる。log2x(x=5)

print(binary_search(my_list, 3))

print(binary_search(my_list, -1))