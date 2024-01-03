import cylindrical_body as cb
import incompressible_cylindrical_body as icb
import spherical_body as sb
import plots as plt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # внутр.
    a = 24
    # внешняя
    b = 64

    # нагрузки интенсивности
    qa = 0
    qb = 3654

    # коэффицент пуассона
    v = 0.3

    # модуль упругости
    E = 200000

    # параметры ламме
    l1 = cb.l1(v, E)
    h1 = cb.h1(v, E)


    # радиус
    r = range(a, b + 1)

    C1 = cb.C1(a, b, qa, qb, l1, h1)
    C2 = cb.C2(a, b, qa, qb, h1)

    u = cb.U_r(r, C1, C2)

    Or = cb.Or_r(r, a, b, qa, qb)

    Oo = cb.Oo_r(r, a, b, qa, qb)

    args1 = (r, u)
    args2 = (r, Or)
    args3 = (r, Oo)

    path1 = r'C:\Users\User\PycharmProjects\MKM_6\solutionA\решениеU.xlsx'
    path2 = r'C:\Users\User\PycharmProjects\MKM_6\solutionA\решениеQr.xlsx'
    path3 = r'C:\Users\User\PycharmProjects\MKM_6\solutionA\решениеOo.xlsx'

    plt.show_plot(a, args1, path1)
    plt.show_plot(a, args2, path2)
    plt.show_plot(a, args3, path3)


    #
    # # внутр.
    # a = 15
    # # внешняя
    # b = 45
    #
    # # нагрузки интенсивности
    # qa = 1500
    # qb = 0
    #
    # # коэффицент пуассона
    # v = 0.3333
    #
    # # модуль упругости
    # E = 62100
    #
    # # параметры ламме
    # h1 = icb.h1(v, E)
    #
    # # радиус
    # r = range(a, b + 1)
    #
    # u = icb.U_r(r, a, b, qa, qb, h1)
    #
    # Or = icb.Or_r(r, a, b, qa, qb)
    #
    # Oo = icb.Oo_r(r, a, b, qa, qb)
    #
    # args1 = (r, u)
    # args2 = (r, Or)
    # args3 = (r, Oo)
    # print(args1)
    #
    # path1 = r'C:\Users\User\PycharmProjects\MKM_6\solutionB\1.xlsx'
    # path2 = r'C:\Users\User\PycharmProjects\MKM_6\solutionB\2.xlsx'
    # path3 = r'C:\Users\User\PycharmProjects\MKM_6\solutionB\3.xlsx'
    #
    # plt.show_plot(a, args1, path1)
    # plt.show_plot(a, args2, path2)
    # plt.show_plot(a, args3, path3)





    # # внутр.
    # a = 55
    # # внешняя
    # b = 95
    #
    # # нагрузки интенсивности
    # qa = 0
    # qb = 4320
    #
    # # коэффицент пуассона
    # v = 0.3
    #
    # # модуль упругости
    # E = 120000
    #
    # # параметры ламме
    # l1 = sb.l1(v, E)
    # h1 = sb.h1(v, E)
    #
    # # радиус
    # r = range(a, b + 1)
    #
    # C1 = sb.C1(a, b, qa, qb, l1, h1)
    # C2 = sb.C2(a, b, qa, qb, h1)
    #
    # u = sb.U_r(r, C1, C2)
    #
    # Or = sb.Or_r(r, a, b, qa, qb)
    #
    # Oo = sb.Oo_r(r, a, b, qa, qb)
    #
    # args1 = (r, u)
    # args2 = (r, Or)
    # args3 = (r, Oo)
    #
    # path1 = r'C:\Users\User\PycharmProjects\MKM_6\solutionC\1.xlsx'
    # path2 = r'C:\Users\User\PycharmProjects\MKM_6\solutionC\2.xlsx'
    # path3 = r'C:\Users\User\PycharmProjects\MKM_6\solutionC\3.xlsx'
    #
    # plt.show_plot(a, args1, path1)
    # plt.show_plot(a, args2, path2)
    # plt.show_plot(a, args3, path3)
