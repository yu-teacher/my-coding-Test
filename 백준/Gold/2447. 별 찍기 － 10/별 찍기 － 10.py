def del_star(s_list, i_start, i_end, j_start, j_end):
    i_term = i_end - i_start
    j_term = j_end - j_start
    if i_term < 3 or j_term < 3:
        return

    for i in range(i_start + i_term // 3, i_start + 2 * i_term // 3):
        for j in range(j_start + j_term // 3, j_start + 2 * j_term // 3):
            s_list[i][j] = ' '

    del_star(s_list, i_start, i_start + i_term // 3, j_start, j_start + j_term // 3)
    del_star(s_list, i_start, i_start + i_term // 3, j_start + j_term // 3, j_start + 2 * j_term // 3)
    del_star(s_list, i_start, i_start + i_term // 3, j_start + 2 * j_term // 3, j_end)

    del_star(s_list, i_start + i_term // 3, i_start + 2 * i_term // 3, j_start, j_start + j_term // 3)
    del_star(s_list, i_start + i_term // 3, i_start + 2 * i_term // 3, j_start + 2 * j_term // 3, j_end)

    del_star(s_list, i_start + 2 * i_term // 3, i_end, j_start, j_start + j_term // 3)
    del_star(s_list, i_start + 2 * i_term // 3, i_end, j_start + j_term // 3, j_start + 2 * j_term // 3)
    del_star(s_list, i_start + 2 * i_term // 3, i_end, j_start + 2 * j_term // 3, j_end)


N = int(input())

star_list = [['*' for _ in range(N)] for _ in range(N)]

del_star(star_list, 0, N, 0, N)

for i in star_list:
    re_str = ''.join(i)
    print(re_str)