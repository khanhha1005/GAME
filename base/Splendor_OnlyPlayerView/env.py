import numpy as np
import random as rd
from numba import njit

normal_cards_infor = np.array([[0, 2, 2, 2, 0, 0, 0], [0, 2, 3, 0, 0, 0, 0], [0, 2, 1, 1, 0, 2, 1], [0, 2, 0, 1, 0, 0, 2], [0, 2, 0, 3, 1, 0, 1], [0, 2, 1, 1, 0, 1, 1], [1, 2, 0, 0, 0, 4, 0], [0, 2, 2, 1, 0, 2, 0], [0, 1, 2, 0, 2, 0, 1], [0, 1, 0, 0, 2, 2, 0], [0, 1, 1, 0, 1, 1, 1], [0, 1, 2, 0, 1, 1, 1], [0, 1, 1, 1, 3, 0, 0], [0, 1, 0, 0, 0, 2, 1], [0, 1, 0, 0, 0, 3, 0], [1, 1, 4, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 4], [0, 0, 0, 0, 0, 0, 3], [0, 0, 0, 1, 1, 1, 2], [0, 0, 0, 0, 1, 2, 2], [0, 0, 1, 0, 0, 3, 1], [0, 0, 2, 0, 0, 0, 2], [0, 0, 0, 1, 1, 1, 1], [0, 0, 0, 2, 1, 0, 0], [0, 4, 0, 2, 2, 1, 0], [0, 4, 1, 1, 2, 1, 0], [0, 4, 0, 1, 0, 1, 3], [1, 4, 0, 0, 4, 0, 0], [0, 4, 0, 2, 0, 2, 0], [0, 4, 2, 0, 0, 1, 0], [0, 4, 1, 1, 1, 1, 0], [0, 4, 0, 3, 0, 0, 0], [0, 3, 1, 0, 2, 0, 0], [0, 3, 1, 1, 1, 0, 1], [1, 3, 0, 4, 0, 0, 0], [0, 3, 1, 2, 0, 0, 2], [0, 3, 0, 0, 3, 0, 0], [0, 3, 0, 0, 2, 0, 2], [0, 3, 3, 0, 1, 1, 0], [0, 3, 1, 2, 1, 0, 1], [1, 2, 0, 3, 0, 2, 2], [2, 2, 0, 2, 0, 1, 4], [1, 2, 3, 0, 2, 0, 3], [2, 2, 0, 5, 3, 0, 0], [2, 2, 0, 0, 5, 0, 0], [3, 2, 0, 0, 6, 0, 0], [3, 1, 0, 6, 0, 0, 0], [2, 1, 1, 0, 0, 4, 2], [2, 1, 0, 5, 0, 0, 0], [2, 1, 0, 3, 0, 0, 5], [1, 1, 0, 2, 3, 3, 0], [1, 1, 3, 2, 2, 0, 0], [3, 0, 6, 0, 0, 0, 0], [2, 0, 0, 0, 0, 5, 3], [2, 0, 0, 0, 0, 5, 0], [2, 0, 0, 4, 2, 0, 1], [1, 0, 2, 3, 0, 3, 0], [1, 0, 2, 0, 0, 3, 2], [3, 4, 0, 0, 0, 0, 6], [2, 4, 5, 0, 0, 3, 0], [2, 4, 5, 0, 0, 0, 0], [1, 4, 3, 3, 0, 0, 2], [1, 4, 2, 0, 3, 2, 0], [2, 4, 4, 0, 1, 2, 0], [1, 3, 0, 2, 2, 0, 3], [1, 3, 0, 0, 3, 2, 3], [2, 3, 2, 1, 4, 0, 0], [2, 3, 3, 0, 5, 0, 0], [2, 3, 0, 0, 0, 0, 5], [3, 3, 0, 0, 0, 6, 0], [4, 2, 0, 7, 0, 0, 0], [4, 2, 0, 6, 3, 0, 3], [5, 2, 0, 7, 3, 0, 0], [3, 2, 3, 3, 0, 3, 5], [3, 1, 3, 0, 3, 5, 3], [4, 1, 0, 0, 0, 0, 7], [5, 1, 0, 3, 0, 0, 7], [4, 1, 0, 3, 0, 3, 6], [3, 0, 0, 5, 3, 3, 3], [4, 0, 0, 0, 7, 0, 0], [5, 0, 3, 0, 7, 0, 0], [4, 0, 3, 3, 6, 0, 0], [5, 4, 0, 0, 0, 7, 3], [3, 4, 5, 3, 3, 3, 0], [4, 4, 0, 0, 0, 7, 0], [4, 4, 3, 0, 0, 6, 3], [3, 3, 3, 3, 5, 0, 3], [5, 3, 7, 0, 0, 3, 0], [4, 3, 6, 0, 3, 3, 0], [4, 3, 7, 0, 0, 0, 0]])
noble_cards_infor = np.array([[0, 4, 4, 0, 0], [3, 0, 3, 3, 0], [3, 3, 3, 0, 0], [3, 0, 0, 3, 3], [0, 3, 0, 3, 3], [4, 0, 4, 0, 0], [4, 0, 0, 4, 0], [0, 3, 3, 0, 3], [0, 4, 0, 0, 4], [0, 0, 0, 4, 4]])

@njit()
def Reset():
    env_state = np.full(164, 0)
    env_state[:] = 0
    env_state[101:107] = np.array([7,7,7,7,7,5])
    lv1 = np.arange(40)
    lv2 = np.arange(40, 70)
    lv3 = np.arange(70, 90)
    nob = np.arange(90, 100)
    for lv in [lv1, lv2, lv3]:
        np.random.shuffle(lv)
        env_state[lv[:4]] = 5
    np.random.shuffle(nob)
    env_state[nob[:5]] = 5
    env_state[161] = lv1[4]
    env_state[162] = lv2[4]
    env_state[163] = lv3[4]

    return env_state, lv1, lv2, lv3

@njit()
def amount_action():
    return 42

@njit()
def amount_player():
    return 4

@njit()
def get_list_id_card_on_lv(lv):
    if len(lv) >= 4:return lv[:4]
    else: return lv[:len(lv)]

@njit()
def concatenate_all_lv_card(lv1, lv2, lv3):
    card_lv1 = normal_cards_infor[get_list_id_card_on_lv(lv1)]
    card_lv2 = normal_cards_infor[get_list_id_card_on_lv(lv2)]
    card_lv3 = normal_cards_infor[get_list_id_card_on_lv(lv3)]
    list_open_card = np.append(card_lv1, card_lv2)
    list_open_card = np.append(list_open_card, card_lv3)
    return list_open_card
    
@njit()
def get_id_card_normal_in_lv(lv1, lv2, lv3):
    list_card_normal_on_board = np.append(get_list_id_card_on_lv(lv1), get_list_id_card_on_lv(lv2))
    list_card_normal_on_board = np.append(list_card_normal_on_board, get_list_id_card_on_lv(lv3))
    return list_card_normal_on_board

@njit()
def get_player_state(env_state, lv1, lv2, lv3):
    p_id = env_state[100] % 4  #L???y ng?????i ??ang ch??i
    b_infor = env_state[101:107] # L???y 6 lo???i nguy??n li???u c???a b??n ch??i
    p_infor = env_state[107 + 12*p_id:119 + 12*p_id]  #L???y th??ng tin ng?????i ??ang ch??i, 6 nguy??n li???u tr??n b??n, 5 nguy??n li???u m???c ?????nh, ??i???m

    list_open_card = concatenate_all_lv_card(lv1, lv2, lv3) #L???y list th??? normal ??ang m??? tr??n b??n
    list_open_noble = noble_cards_infor[np.where(env_state[90:100] == 5)].flatten() #L???y list th??? Noble ??ang m??? tr??n b??n

    state_card_normal = np.full(84, 0)
    state_card_noble = np.full(25, 0)
    state_card_normal[:len(list_open_card)] = list_open_card
    state_card_noble[:len(list_open_noble)] = list_open_noble

    list_upside_down_card = normal_cards_infor[np.where(env_state[:90] == -(p_id+1))]
    p_upside_down_card = np.full(21, 0)
    if len(list_upside_down_card) > 0:
        array_hide_card = list_upside_down_card.flatten()
        p_upside_down_card[:len(array_hide_card)] = array_hide_card
    
    st_getting = env_state[155:160] #L???y th??ng tin 5 nguy??n li???u ??ang l???y trong turn
    other_scores = [env_state[118 + 12 * id_other_player] for id_other_player in range(4) if id_other_player != p_id] #L???y ??i???m c???a ng?????i ch??i kh??c

    p_state = np.append(b_infor, p_infor)
    p_state = np.append(p_state, state_card_normal) #L???y th??ng tin 12 th??? ??ang m??? ??? tr??n b??n
    p_state = np.append(p_state, state_card_noble)
    p_state = np.append(p_state, p_upside_down_card) #L???y th??ng tin 3 th??? ??ang ??p

    p_state = np.append(p_state, st_getting) #L???y th??ng tin 5 nguy??n li???u ??ang l???y trong turn
    p_state = np.append(p_state, other_scores) #L???y ??i???m c???a ng?????i ch??i kh??c
    p_state = np.append(p_state, (env_state[161:164] != 100)*1) #L???y th??ng tin c???a c??c th??? ???n c?? th??? ??p, n???u c?? th??? ??p th?? l?? 1
    p_state = np.append(p_state, len(np.where(env_state[:90] == 5)[0])) #S??? l?????ng th??? c?? th??? ??p trong b??n
    return p_state

@njit()
def check_victory(p_state):
    scores = p_state[153:156]
    owner_score = p_state[17]

    if owner_score >= 15 and max(scores) <= owner_score:
        return 1
    if max(scores) >= 15 and max(scores) > owner_score:
        return 0
    if owner_score < 15 and max(scores) < 15:
        return -1

@njit()
def get_list_action(p_state):
    b_stocks = p_state[:6] #C??c nguy??n li???u tr??n b??n ch??i
    p_st = p_state[6:11] #C??c nguy??n li???u c???a b???n th??n ??ang c??
    yellow_count = p_state[11] #S??? th??? v??ng ??ang c??
    normal_cards = p_state[18:102] #Th??ng tin 12 th??? ??ang m???
    p_upside_down_card =  p_state[127:148] #th??ng tin 3 th??? ??ang ??p
    taken = p_state[148: 153] #c??c nguy??n li???u ???? l???y trong turn
    p_count_st = p_state[12:17] #Nguy??n li???u m???c ?????nh c???a ng?????i ch??i
    list_action = np.array([0])

    #Tr??? nguy??n li???u
    p_st_have_auto = p_state[6:12]
    sum_p_st_have_auto = sum(p_st_have_auto)
    if sum_p_st_have_auto > 10:
        list_action_return_stock = [i_+36 for i_ in range(6) if p_st_have_auto[i_] != 0]
        list_action = np.array(list_action_return_stock)
        return list_action

    #L???y nguy??n li???u
    s_taken = np.sum(taken)
    temp_ = [i_ + 31 for i_ in range(5) if b_stocks[i_] != 0]
    if s_taken == 1:
        s_ = np.where(taken==1)[0][0]
        if b_stocks[s_] < 3: # C?? th??? l???y double
            if (s_+ 31) in temp_:
                temp_.remove(s_ + 31) #X??a action ???? l???y ??? file temp n???u nguy??n li???u kh??ng tr??n 4
        list_action = np.append(np.array([0]), temp_)
    elif s_taken == 2:
        lst_s_ = np.where(taken==1)[0]
        for s_ in lst_s_:
            if (s_+31) in temp_:
                temp_.remove(s_+31)
        list_action = np.append(np.array([0]), temp_)
    elif s_taken == 0:
        if len(temp_) > 0:
            list_action = np.array(temp_)
    if s_taken > 0:
        return list_action

    # Ki???m tra 15 th??? c?? th??? m???, action t??? [1:16]
    for id_card in range(12):
        card = normal_cards[7*id_card: 7+7*id_card]
        if sum(card) > 0:
            card_need = p_st + p_count_st - card[-5:]
            if -sum(card_need[np.where(card_need < 0)]) <= yellow_count or min(card_need) >= 0: #(x*x>0)
                # print('index_card:', id_card, 'The c???n:', card_need, 'th???',card)
                # print('t???ng nguy??n li???u c???n', -sum(card_need[np.where(card_need < 0)]), 'Nguy??n li???u v??ng:', yellow_count)
                list_action = np.append(list_action, id_card+1) # check c??c th??? c?? th??? l???y
    for id_card in range(3):
        card = p_upside_down_card[7*id_card: 7+7*id_card]
        if sum(card) > 0:
            # print(p_st, p_count_st, card[-5:], card)
            card_need = p_st + p_count_st -card[-5:]
            if sum(card_need) != 0:
                if -sum(card_need[np.where(card_need < 0)]) <= yellow_count or min(card_need) >= 0:
                    list_action = np.append(list_action, id_card+13) # check c??c th??? c?? th??? l???y

    #Ki???m tra v?? ??p th???, action t??? [16:31]
    list_card_upside_down = []
    count_upside_down = 0
    for id_card in range(3):
        card_upside_down = p_upside_down_card[7*id_card:7+7*id_card]
        if sum(card_upside_down) > 0:
            count_upside_down += 1
        else:
            break
    if count_upside_down < 3: # N???u ch??a c?? ????? 3 th??? ??p th?? c?? th??? ??p th??m m???t th???
        list_action_upside_down = [i+16 for i in range(0, p_state[159])]
        list_action = np.append(list_action, list_action_upside_down)
        list_card_hide = np.where(p_state[156:159] == 1)[0] + 28
        # print(list_card_hide)
        list_action = np.append(list_action, list_card_hide)
    
    if len(list_action) > 1 and list_action[0] == 0:
        list_action = np.delete(list_action, 0)
    return list_action

@njit
def get_remove_card_on_lv_and_add_new_card(env_state, lv,p_id, id_card_hide, type_action, card_id):
    if type_action == 2:
        env_state[lv[4]] = -(p_id+1)
        id_card_in_level = 4
    else:
        if len(lv) > 4:
            env_state[lv[4]] = 5
        id_card_in_level = np.where(lv == card_id)[0][0]
        if type_action == 1:
            env_state[card_id] = p_id+1

    lv = np.delete(lv, id_card_in_level)
    if len(lv) > 4:
        env_state[id_card_hide] = lv[4]
    else: 
        env_state[id_card_hide] = 100
    return env_state, lv

@njit
def step(action,env_state, lv1, lv2, lv3):
    p_id = env_state[100] % 4
    cur_p = env_state[107 + 12*p_id:119 + 12*p_id]
    b_stocks = env_state[101:107]

    if action == 0:
        env_state[100] += 1 #Sang turn m???i
        env_state[155:160] = [0,0,0,0,0]
    else:
        if 1 <= action and action < 16:#Mua th???
            if 1 <= action and action < 13:
                id_action = action - 1
                id_card_normal = get_id_card_normal_in_lv(lv1, lv2, lv3)
            else:
                id_action = action - 13
                id_card_normal = np.where(env_state[:90] == -(p_id+1))[0]
            card_id = id_card_normal[id_action]
            card_infor = normal_cards_infor[card_id]
            card_price = card_infor[-5:]
            nl_bo_ra = (card_price>cur_p[6:11]) * (card_price-cur_p[6:11])
            nl_bt = np.minimum(nl_bo_ra, cur_p[:5])
            nl_auto = np.sum(nl_bo_ra - nl_bt)
            
            # Tr??? nguy??n li???u
            cur_p[:5] -= nl_bt
            cur_p[5] -= nl_auto
            b_stocks[:5] += nl_bt
            b_stocks[5] += nl_auto

            x_ = env_state[card_id]
            env_state[card_id] = p_id+1
            if x_ == 5: #Type_action == 1
                if card_id < 40:
                    env_state, lv1 = get_remove_card_on_lv_and_add_new_card(env_state, lv1,p_id, 161, 1,card_id)
                elif card_id >= 40 and card_id < 70:
                    env_state, lv2 = get_remove_card_on_lv_and_add_new_card(env_state, lv2,p_id, 162, 1,card_id)
                    env_state[card_id] = p_id+1
                else:
                    env_state, lv3 = get_remove_card_on_lv_and_add_new_card(env_state, lv3,p_id, 163, 1,card_id)
                    
            cur_p[6:11][card_infor[1]] += 1  #const_stock
            cur_p[11] += card_infor[0] #Score

            # Check Noble
            noble_lst = []
            nobles = [i for i in range(90,100) if env_state[:100][i]==5]
            for noble_id in nobles:
                if (noble_cards_infor[noble_id-90][-5:] <= cur_p[6:11]).all():
                    noble_lst.append(noble_id)

            for noble_id in noble_lst:
                env_state[noble_id] = p_id+1
                cur_p[11] += 3
                
            env_state[100] += 1 # Sang turn m???i

        elif 16 <= action and action < 31:# ??p th??? c?? tr??n b??n
            id_action = action - 16
            # print('Chon lay the', id_action)
            if b_stocks[5] > 0:
                b_stocks[5] -= 1
                cur_p[5] += 1
            if id_action == 12: #??p th??? ???n c???p 1
                env_state, lv1 = get_remove_card_on_lv_and_add_new_card(env_state, lv1,p_id, 161, 2, 0)
            elif id_action == 13: #??p th??? ???n c???p 2
                env_state, lv2 = get_remove_card_on_lv_and_add_new_card(env_state, lv2,p_id, 162, 2, 0)
            elif id_action == 14: #??p th??? ???n c???p 3
                env_state, lv3 = get_remove_card_on_lv_and_add_new_card(env_state, lv3,p_id, 163, 2, 0)
            else: #??p th??? b??nh th?????ng tr??n b??n
                id_card_normal = get_id_card_normal_in_lv(lv1, lv2, lv3)
                card_id = id_card_normal[id_action]
                env_state[card_id] = -(p_id+1)
                if card_id < 40:
                    env_state, lv1 = get_remove_card_on_lv_and_add_new_card(env_state, lv1,p_id, 161, 3,card_id)
                elif card_id >= 40 and card_id < 70:
                    env_state, lv2 = get_remove_card_on_lv_and_add_new_card(env_state, lv2,p_id, 162, 3,card_id)
                else:
                    env_state, lv3 = get_remove_card_on_lv_and_add_new_card(env_state, lv3,p_id, 163, 3,card_id)

            if np.sum(cur_p[:6]) <= 10:
                env_state[100] += 1 # Sang turn m???i

        elif 31 <= action and action < 36: #L???y nguy??n li???u
            check_phase3 = False
            taken = env_state[155:160] #C??c nguy??n li???u ??ang l???y
            id_action = action - 31     #Id lo???i nguy??n li???u l???y trong turn
            b_stocks[id_action] -= 1   #Tr??? nguy??n li???u b??n ch??i
            cur_p[id_action] += 1      #th??m nguy??n li???u c???a ng?????i ch??i
            taken[id_action] += 1      # th??m nguy??n li???u l???y trong turn
            # print('L???y nguy??n li???u:', id_action, 'Taken:',taken)
            s_taken = np.sum(taken)

            if s_taken == 1: # Ch??? c??n ????ng lo???i nl v???a l???y nh??ng sl < 3
                if b_stocks[id_action] < 3 and (np.sum(b_stocks[:5]) - b_stocks[id_action]) == 0:
                    check_phase3 = True
            elif s_taken == 2: # L???y double, ho???c kh??ng c??n nl n??o kh??c 2 c??i v???a l???y
                if np.max(taken) == 2 or (np.sum(b_stocks[:5]) - np.sum(b_stocks[np.where(taken>0)[0]])) == 0:
                    check_phase3 = True
            else: # sum(taken) = 3
                check_phase3 = True

            if check_phase3:
                if np.sum(cur_p[:6]) < 10:
                    env_state[100] += 1 # Sang turn m???i
                    env_state[155:160] = [0,0,0,0,0]
            env_state[155:160] = taken

        elif 36 <= action and action < 42: #Tr??? nguy??n li???u
            st_ = action - 36
            cur_p[st_] -= 1
            b_stocks[st_] += 1

            if np.sum(cur_p[:6]) <= 10: # Th???a m??n ??i???u ki???n n??y th?? sang turn m???i
                env_state[100] += 1 # Sang turn m???i
                env_state[155:160] = [0,0,0,0,0]

    env_state[107 + 12*p_id:119 + 12*p_id] = cur_p
    env_state[101:107] = b_stocks
    return env_state, lv1, lv2, lv3

@njit
def close_game(env_state):
    score_arr = np.array([env_state[118 + 12*p_id] for p_id in range(4)])
    max_score = np.max(score_arr)
    if max_score >= 15 and env_state[100] % 4 == 0:
        lst_p = np.where(score_arr==max_score)[0] + 1
        if len(lst_p) == 1:
            return lst_p[0]
        else:
            lst_p_c = []
            for p_id in lst_p:
                lst_p_c.append(np.count_nonzero(env_state[:90]==p_id))
            
            lst_p_c = np.array(lst_p_c)
            min_p_c = np.min(lst_p_c)
            lst_p_win = np.where(lst_p_c==min_p_c)[0]
            if len(lst_p_win) == 1:
                return lst_p[lst_p_win[0]]
            else:
                id_max = -1
                a = -1
                for i in lst_p_win:
                    b = max(np.where(env_state[:90]==lst_p[i])[0])
                    if b > a:
                        id_max = lst_p[i]
                        a = b

                return id_max
    
    else:
        return 0


def one_game(list_player, per_file):
    env, lv1, lv2, lv3 = Reset()
    temp_file = [[0],[0],[0],[0]]
    _cc = 0
    while env[100] <= 400 and _cc <= 10000:
        p_idx = env[100]%4
        p_state = get_player_state(env, lv1, lv2, lv3)
        act, temp_file[p_idx], per_file = list_player[p_idx](p_state, temp_file[p_idx], per_file)
        env, lv1, lv2, lv3 = step(act, env, lv1, lv2, lv3)

        if close_game(env) != 0:
            break

        _cc += 1
    
    turn = env[100]
    for i in range(4):
        env[100] = i
        act, temp_file[i], per_file = list_player[i](get_player_state(env, lv1, lv2, lv3), temp_file[i], per_file)
    
    env[100] = turn
    return close_game(env), per_file

def normal_main(list_player, num_game,per_file):
    if len(list_player) != 4:
        print('Game ch??? cho ph??p c?? ????ng 4 ng?????i ch??i')
        return [-1,-1,-1,-1,-1], per_file
    
    num_won = [0,0,0,0,0]
    p_lst_idx = [0,1,2,3]
    for _n in range(num_game):

        # Shuffle ng?????i ch??i
        rd.shuffle(p_lst_idx)
        winner, per_file = one_game(
            [list_player[p_lst_idx[0]], list_player[p_lst_idx[1]], list_player[p_lst_idx[2]], list_player[p_lst_idx[3]]], per_file,
        )

        if winner != 0:
            num_won[p_lst_idx[winner-1]] += 1
        else:
            num_won[4] += 1

    return num_won, per_file

def one_game_test(list_player, per_file_temp):
    env, lv1, lv2, lv3 = Reset()
    temp_file = [[0],[0],[0],[0]]
    _cc = 0
    while env[100] <= 400 and _cc <= 10000:
        p_idx = env[100]%4
        p_state = get_player_state(env, lv1, lv2, lv3)
        act, temp_file[p_idx], per_file_temp[p_idx] = list_player[p_idx](p_state, temp_file[p_idx], per_file_temp[p_idx])
        env, lv1, lv2, lv3 = step(act, env, lv1, lv2, lv3)

        if close_game(env) != 0:
            break

        _cc += 1
    
    turn = env[100]
    for i in range(4):
        env[100] = i
        act, temp_file[i], per_file_temp[i] = list_player[i](get_player_state(env, lv1, lv2, lv3), temp_file[i], per_file_temp[i])
    
    env[100] = turn
    return close_game(env), per_file_temp

def normal_main_test(list_player, num_game,per_file):
    if len(list_player) != 4:
        print('Game ch??? cho ph??p c?? ????ng 4 ng?????i ch??i')
        return [-1,-1,-1,-1,-1], per_file
    
    num_won = [0,0,0,0,0]
    p_lst_idx = [0,1,2,3]
    per_file = [[0],[0],[0],[0]]
    for _n in range(num_game):

        # Shuffle ng?????i ch??i
        rd.shuffle(p_lst_idx)
        # print()
        # print(p_lst_idx)
        per_file_temp = [per_file[p_lst_idx[0]], per_file[p_lst_idx[1]], per_file[p_lst_idx[2]], per_file[p_lst_idx[3]]]
        print(per_file_temp)
        winner, per_file_temp = one_game_test(
            [list_player[p_lst_idx[0]], list_player[p_lst_idx[1]], list_player[p_lst_idx[2]], list_player[p_lst_idx[3]]], 
            per_file_temp,
        )
        # print(per_file_temp)
        for ii in range(4):
            per_file[ii] = per_file_temp[p_lst_idx[ii]]

        # print(per_file)
        if winner != 0:
            num_won[p_lst_idx[winner-1]] += 1
        else:
            num_won[4] += 1

    return num_won, per_file


def get_id_card(card_id):
    if card_id < 40: return 'I', card_id +1
    if 40 <= card_id < 70: return 'II', card_id - 39
    if 70 <= card_id < 90: return 'III', card_id - 69
    
def one_game_print(list_player, per_file, *print_mode):
    env, lv1, lv2, lv3 = Reset()
    list_color = ['red', 'blue', 'green', 'black', 'white', 'auto_color']
    def _print_():
        print('----------------------------------------------------------------------------------------------------')
        print('L?????t c???a ng?????i ch??i:', env[100]%4 + 1, list_color)
        print('B_stocks:', env[101:107], 'Turn:', env[100], )
        print('Th??? 1:', [i_+1 for i_ in get_list_id_card_on_lv(lv1)], list(lv1+1))
        print('Th??? 2:', [i_-39 for i_ in get_list_id_card_on_lv(lv2)], list(lv2-39))
        print('Th??? 3:', [i_-69 for i_ in get_list_id_card_on_lv(lv3)], list(lv3-69))
        print('Noble:', [i_-89 for i_ in range(90,100) if env[:100][i_] == 5])
        print('P1:', env[107:113], env[113:118], env[118], [get_id_card(i_) for i_ in range(90) if env[i_] == -1], [get_id_card(i_) for i_ in range(90) if env[i_] == 1],
            '\nP2:', env[119:125], env[125:130], env[130], [get_id_card(i_) for i_ in range(90) if env[i_] == -2], [get_id_card(i_) for i_ in range(90) if env[i_] == 2],
            '\nP3:', env[131:137], env[137:142], env[142], [get_id_card(i_) for i_ in range(90) if env[i_] == -3], [get_id_card(i_) for i_ in range(90) if env[i_] == 3],
            '\nP4:', env[143:149], env[149:154], env[154], [get_id_card(i_) for i_ in range(90) if env[i_] == -4], [get_id_card(i_) for i_ in range(90) if env[i_] == 4],)
        print('Nl ???? l???y:', env[155:160],'Th??? ???n:', get_id_card(env[161]), get_id_card(env[162]), get_id_card(env[163]))
        print('-------')

    def _print_action_(act):
        if act == 0:
            print(f'Ng?????i ch??i {p_idx+1} k???t th??c l?????t:', act)
        elif act in range(1,13):
            id_action = act-1
            id_card_normal = get_id_card_normal_in_lv(lv1, lv2, lv3)
            print(f'Ng?????i ch??i {p_idx+1} m??? th??? tr??n b??n:', get_id_card(id_card_normal[id_action]),id_action,id_card_normal)
        elif act in range(13,16):
            id_action = act-13
            id_card_normal = np.where(env[:90] == -(p_idx+1))[0]
            print(f'Ng?????i ch??i {p_idx+1} ch???n m??? th??? ??ang ??p:', get_id_card(id_card_normal[id_action]),id_action,id_card_normal)
        elif act in range(16,28):
            id_action = act-16
            id_card_normal = get_id_card_normal_in_lv(lv1, lv2, lv3)
            print(f'Ng?????i ch??i {p_idx+1} ch???n ??p th??? tr??n b??n:', get_id_card(id_card_normal[id_action]), id_action,id_card_normal)
        elif act in range(28, 31):

            print(f'Ng?????i ch??i {p_idx+1} ch???n ??p th??? ???n:', get_id_card(env[161 + act-28]))
        elif act in range(31, 36):
            id_action = act-31
            print(f'Ng?????i ch??i {p_idx+1} l???y nguy??n li???u:', list_color[id_action])
        elif act in range(36, 42):
            id_action = act-36
            print(f'Ng?????i ch??i {p_idx+1} tr??? nguy??n li???u:', list_color[id_action])


    temp_file = [[0],[0],[0],[0]]
    _cc = 0
    while env[100] <= 400 and _cc <= 10000:
        p_idx = env[100]%4
        p_state = get_player_state(env, lv1, lv2, lv3)
        act, temp_file[p_idx], per_file = list_player[p_idx](p_state, temp_file[p_idx], per_file)
        print('day la action he thong', act)
        list_action = get_list_action(p_state)
        if print_mode:
            _print_()
            for act_test in list_action:
                print(act_test, end = ' ')
                _print_action_(act_test)
            print('________')
            _print_action_(act)
        env, lv1, lv2, lv3 = step(act, env, lv1, lv2, lv3)
        # print('D??y l?? lv1', lv1)
        if close_game(env) != 0:
            break

        _cc += 1
    

    turn = env[100]
    for i in range(4):
        env[100] = i
        act, temp_file[i], per_file = list_player[i](get_player_state(env, lv1, lv2, lv3), temp_file[i], per_file)
    
    env[100] = turn
    return close_game(env), per_file

def normal_main_print(list_player, num_game=1, print_mode=False):
    per_file = [0]
    if len(list_player) != 4:
        print('Game ch??? cho ph??p c?? ????ng 4 ng?????i ch??i')
        return [-1,-1,-1,-1,-1], per_file
    
    num_won = [0,0,0,0,0]
    p_lst_idx = [0,1,2,3]
    for _n in range(num_game):

        # Shuffle ng?????i ch??i
        rd.shuffle(p_lst_idx)
        if print_mode:
            print('Th??? t??? ng?????i ch??i (th??? t??? n??y s??? ???ng v???i P1,P2,P3,P4):', p_lst_idx)
            print('L??u ??: kh??ng ph???i ng?????i ch??i index 0 l?? P1')

        winner, per_file = one_game_print(
            [list_player[p_lst_idx[0]], list_player[p_lst_idx[1]], list_player[p_lst_idx[2]], list_player[p_lst_idx[3]]], per_file, print_mode
        )

        if winner != 0:
            num_won[p_lst_idx[winner-1]] += 1
        else:
            num_won[4] += 1

    return num_won, per_file

def player_random(p_state, temp_file, per_file):
    arr_action = get_list_action(p_state)
    act_idx = np.random.randint(0, len(arr_action))
    return arr_action[act_idx], temp_file, per_file