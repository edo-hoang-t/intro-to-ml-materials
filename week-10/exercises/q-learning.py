experience = [(0, 'b', 0), #t = 0
              (2, 'b', 0),
              (3, 'b', 2),
              (0, 'b', 0), #t = 3
              (2, 'b', 0),
              (3, 'c', 2),
              (0, 'c', 0), #t = 6
              (1, 'b', 1),
              (0, 'b', 0),
              (2, 'c', 0), #t = 9
              (3, 'c', 2),
              (0, 'c', 0),
              (1, 'c', 1), #t = 12
              (0, 'c', 0),
              (2, 'b', 0),
              (3, 'b', 2), #t = 15
              (0, 'b', 0),
              (2, 'c', 0),
              (3, '', 0), #t = 18
              ]

q_table = [[0, 0], [0, 0], [0, 0], [0, 0]]
alp = 0.5
gam = 0.9

def updateTable(from_id, to_id): # 0, 2
    print("Updated value: ")
    for i in range(to_id - from_id + 1):
        cur_exper = experience[from_id + i]
        cur_s = cur_exper[0]
        cur_action = 0 if cur_exper[1] == 'b' else 1

        next_s = experience[from_id + i + 1][0]

        max_Q_of_next_state = max(q_table[next_s][0], q_table[next_s][1])
        
        q_table[cur_s][cur_action] = q_table[cur_s][cur_action] * (1 - alp) + \
                                        alp * (cur_exper[2] + gam * max_Q_of_next_state)
        print(q_table[cur_s][cur_action])


                                    

