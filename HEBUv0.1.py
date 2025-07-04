import random

# 定義希伯來文和英文配對
hebrew_cards = {
    'א': 'aleph',
    'ב': 'bet',
    'ג': 'gimel',
    'ד': 'dalet',
    'שלום': 'peace',
    'תודה': 'thank you',
    'כן': 'yes',
    'לא': 'no'
}

# 準備卡片列表並打亂順序
cards = list(hebrew_cards.keys()) + list(hebrew_cards.values())
random.shuffle(cards)

# 建立 4x4 遊戲板
board_size = 4
board = [cards[i:i + board_size] for i in range(0, len(cards), board_size)]
revealed = [[False for _ in range(board_size)] for _ in range(board_size)]

# 遊戲參數
matches = 0
total_matches = len(hebrew_cards)

# 遊戲主循環
while matches < total_matches:
    # 顯示當前遊戲板
    for i in range(board_size):
        row = []
        for j in range(board_size):
            if revealed[i][j]:
                row.append(board[i][j])
            else:
                row.append('?')
        print(' '.join(row))
    
    # 玩家輸入選擇
    print("請選擇第一張卡片 (行 列，例如 '0 1'): ")
    row1, col1 = map(int, input().split())
    print("請選擇第二張卡片 (行 列，例如 '1 2'): ")
    row2, col2 = map(int, input().split())

    # 顯示玩家選擇的卡片
    card1 = board[row1][col1]
    card2 = board[row2][col2]
    print(f"你翻開了: {card1} 和 {card2}")

    # 檢查是否匹配
    if (card1 in hebrew_cards and hebrew_cards[card1] == card2) or (card2 in hebrew_cards and hebrew_cards[card2] == card1):
        print("匹配成功！")
        revealed[row1][col1] = True
        revealed[row2][col2] = True
        matches += 1
    else:
        print("不匹配，請再試一次。")

    print("----------------")

# 遊戲結束
print("恭喜！你完成了所有配對！")
