# クイックソートを行う
def quick_sort(array):
    if len(array) < 2:   # 基本ケース（配列の要素が空か、一つしかない場合はソート不要のため。）
        return array
    else:
        pivot = array[0] # 再帰ケース（クイックソートを行う。）
        
        # ピボットの値以下の要素をすべて含んだ部分配列
        less = [i for i in array[1:] if i <= pivot]

        # ピボットの値よりも大きい要素をすべて含んだ部分配列
        greater = [i for i in array[1:] if i > pivot]

        # 再帰的にこの関数を呼び出し、部分配列とピボットを結合
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([10, 5, 2, 3])) # [2, 3, 5, 10]を出力