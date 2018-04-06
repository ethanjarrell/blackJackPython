import random
iterations = 10
sumValue = [["2: ", 0, 0, 0, 0, 0, 0, 0, 0], ["3: ", 0, 0, 0, 0, 0, 0, 0, 0], ["4: ", 0, 0, 0, 0, 0, 0, 0, 0], ["5: ", 0, 0, 0, 0, 0, 0, 0, 0], ["6: ", 0, 0, 0, 0, 0, 0, 0, 0], ["7: ", 0, 0, 0, 0, 0, 0, 0, 0], ["8: ", 0, 0, 0, 0, 0, 0, 0, 0], ["9: ", 0, 0, 0, 0, 0, 0, 0, 0], ["10: ", 0, 0, 0, 0, 0, 0, 0, 0], ["11: ", 0, 0, 0, 0, 0, 0, 0, 0], [
    "12: ", 0, 0, 0, 0, 0, 0, 0, 0], ["13: ", 0, 0, 0, 0, 0, 0, 0, 0], ["14: ", 0, 0, 0, 0, 0, 0, 0, 0], ["15: ", 0, 0, 0, 0, 0, 0, 0, 0], ["16: ", 0, 0, 0, 0, 0, 0, 0, 0], ["17: ", 0, 0, 0, 0, 0, 0, 0, 0], ["18: ", 0, 0, 0, 0, 0, 0, 0, 0], ["19: ", 0, 0, 0, 0, 0, 0, 0, 0], ["20: ", 0, 0, 0, 0, 0, 0, 0, 0], ["21: ", 0, 0, 0, 0, 0, 0, 0, 0], ["21+: ", 0, 0, 0, 0, 0, 0, 0, 0]]


def hand():
    deck = []
    value = range(1, 14)
    for i in value:
        if i == 10 or i == 11 or i == 12 or i == 13:
            i = 10
        d = "D-"+str(i)
        c = "C-"+str(i)
        s = "S-"+str(i)
        h = "H-"+str(i)
        deck.append(d)
        deck.append(c)
        deck.append(s)
        deck.append(h)
        print deck
    hand = []
    hand2 = []
    card1 = random.choice(deck)
    hand.append(card1)
    if card1 in deck:
        deck.remove(card1)
    card2 = random.choice(deck)
    hand.append(card2)
    if card2 in deck:
        deck.remove(card2)

    value1 = int(hand[0].split("-")[1])
    value2 = int(hand[1].split("-")[1])
    if value1 == 1:
        value1 = 11
    if value2 == 1:
        value2 = 11
    sum1 = value1 + value2
    if sum1 > 21 and value2 == 11:
        value2 = 1
        sum1 = value1 + value2
    if sum1 > 21 and value1 == 11:
        value1 = 1
        sum1 = value1 + value2
    if sum1 == 2:
        sumValue[0][1] = sumValue[0][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[0][3] = sumValue[0][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[0][5] = sumValue[0][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[0][7] = sumValue[0][7] + 1
    if sum1 == 3:
        sumValue[1][1] = sumValue[1][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[1][3] = sumValue[1][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[1][5] = sumValue[1][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[1][7] = sumValue[1][7] + 1
    if sum1 == 4:
        sumValue[2][1] = sumValue[2][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[2][3] = sumValue[2][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[2][5] = sumValue[2][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[2][7] = sumValue[2][7] + 1
    if sum1 == 5:
        sumValue[3][1] = sumValue[3][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[3][3] = sumValue[3][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[3][5] = sumValue[3][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[3][7] = sumValue[3][7] + 1
    if sum1 == 6:
        sumValue[4][1] = sumValue[4][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[4][3] = sumValue[4][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[4][5] = sumValue[4][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[4][7] = sumValue[4][7] + 1
    if sum1 == 7:
        sumValue[5][1] = sumValue[5][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[5][3] = sumValue[5][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[5][5] = sumValue[5][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[5][7] = sumValue[5][7] + 1
    if sum1 == 8:
        sumValue[6][1] = sumValue[6][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[6][3] = sumValue[6][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[6][5] = sumValue[6][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[6][7] = sumValue[6][7] + 1
    if sum1 == 9:
        sumValue[7][1] = sumValue[7][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[7][3] = sumValue[7][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[7][5] = sumValue[7][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[7][7] = sumValue[7][7] + 1
    if sum1 == 10:
        sumValue[8][1] = sumValue[8][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[8][3] = sumValue[8][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[8][5] = sumValue[8][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[8][7] = sumValue[8][7] + 1
    if sum1 == 11:
        sumValue[9][1] = sumValue[9][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[9][3] = sumValue[9][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[9][5] = sumValue[9][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[9][7] = sumValue[9][7] + 1
    if sum1 == 12:
        sumValue[10][1] = sumValue[10][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[10][3] = sumValue[10][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[10][5] = sumValue[10][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[10][7] = sumValue[10][7] + 1
    if sum1 == 13:
        sumValue[11][1] = sumValue[11][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[11][3] = sumValue[11][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[11][5] = sumValue[11][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[11][7] = sumValue[11][7] + 1
    if sum1 == 14:
        sumValue[12][1] = sumValue[12][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[12][3] = sumValue[12][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[12][5] = sumValue[12][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[12][7] = sumValue[12][7] + 1
    if sum1 == 15:
        sumValue[13][1] = sumValue[13][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[13][3] = sumValue[13][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[13][5] = sumValue[13][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[13][7] = sumValue[13][7] + 1
    if sum1 == 16:
        sumValue[14][1] = sumValue[14][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[14][3] = sumValue[14][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[14][5] = sumValue[14][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[14][7] = sumValue[14][7] + 1
    if sum1 == 17:
        sumValue[15][1] = sumValue[15][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[15][3] = sumValue[15][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[15][5] = sumValue[15][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[15][7] = sumValue[15][7] + 1
    if sum1 == 18:
        sumValue[16][1] = sumValue[16][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[16][3] = sumValue[16][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[16][5] = sumValue[16][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[16][7] = sumValue[16][7] + 1
    if sum1 == 19:
        sumValue[17][1] = sumValue[17][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[17][3] = sumValue[17][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[17][5] = sumValue[17][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[17][7] = sumValue[17][7] + 1
    if sum1 == 20:
        sumValue[18][1] = sumValue[18][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[18][3] = sumValue[18][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[18][5] = sumValue[18][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[18][7] = sumValue[18][7] + 1
    if sum1 == 21:
        sumValue[19][1] = sumValue[19][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[19][3] = sumValue[19][3] + 1

        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[19][5] = sumValue[19][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[19][7] = sumValue[19][7] + 1
    if sum1 > 21:
        sumValue[20][1] = sumValue[20][1] + 1
        card3 = random.choice(deck)
        hand.append(card3)
        if card3 in deck:
            deck.remove(card3)
        value3 = int(hand[2].split("-")[1])
        sum2 = sum1 + value3
        if sum2 <= 21:
            sumValue[20][3] = sumValue[20][3] + 1
        card4 = random.choice(deck)
        hand.append(card4)
        if card4 in deck:
            deck.remove(card4)
        value4 = int(hand[3].split("-")[1])
        sum3 = sum2 + value4
        if sum3 <= 21:
            sumValue[20][5] = sumValue[20][5] + 1

        card5 = random.choice(deck)
        hand.append(card5)
        if card5 in deck:
            deck.remove(card5)
        value5 = int(hand[4].split("-")[1])
        sum4 = sum3 + value5
        if sum4 <= 21:
            sumValue[20][7] = sumValue[20][7] + 1
    return hand


myRange = range(0, iterations)

for i in myRange:
    hand()
for i in sumValue:
    percent = 100 * float(i[1])/float(iterations)
    i[2] = percent
    if i[1] != 0:
        percent2 = 100 * float(i[3])/float(i[1])
        i[4] = percent2
    if i[3] != 0:
        percent3 = 100 * float(i[5])/float(i[3])
        i[6] = percent3
    if i[5] != 0:
        percent4 = 100 * float(i[7])/float(i[5])
        i[8] = percent4
for i in sumValue:
    print i
