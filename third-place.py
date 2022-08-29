def third_place(names, scores):
    nilai_urut = sorted(scores, reverse=True)
    nilai_urut = list(dict.fromkeys(nilai_urut))
    third_place = nilai_urut[2]
    winner = []
    for name, score in zip(names, scores):
        if third_place == score:
            winner.append(name)
    print(f"the third place are"," and ".join(winner))    
    print(winner)


names = ['andi', 'iman', 'budi', 'leo', 'grace']
scores = [90, 80, 80, 100, 90]

third_place(names, scores)