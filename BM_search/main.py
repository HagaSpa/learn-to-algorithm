
"""
BM法

https://algoful.com/Archive/Algorithm/BMSearch
"""


def main():
    # 検索対象
    t = "aaaaa"  
    # 検索パターン
    p = "baa"

    table = create_pt_dict(p)

    # t用ポインタ
    i = len(p) - 1

    # tの長さを超えるまで
    while i < len(t):
        j = len(p) - 1 # p用ポインタ
        
        while j >= 0 and i < len(t):
            if p[j] == t[i]:
                i -= 1
                j -= 1
            else:
                break
        # jが0未満（jはpに対するインデックスのため0もあり得る）なら、「pを最後までデクリメントできている＝pがtに存在している」
        if j < 0:
            return print(i+1)

        # 検索パターンに含まないなら 「パターンの長さ」を入れる
        shift_num_1 = len(p) if t[i] not in table else table[t[i]]
        # TODO: ここのロジックがよくわからない
        shift_num_2 = len(p) - j
        i += max(shift_num_1, shift_num_2)

    
    print("見つからない")
        

def create_pt_dict(p: str):
    pt = dict()
    # 後ろからの文字と距離をk,vにする。重複した場合距離が近い（後方文字列）を優先させるため、setdefaultで先勝にする
    for i, v in enumerate(p[::-1]):
        pt.setdefault(v, i)
    print(pt)
    return pt


main()