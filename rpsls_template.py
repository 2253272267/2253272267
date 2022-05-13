#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�����ɭ
���ڣ�2022/5/11
"""

import random



# 0 - ʯͷ  rock
# 1 - ʷ����  spock
# 2 - ֽ    paper
# 3 - ����   lizard
# 4 - ����   scissors

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if choice_name=="ʯͷ":
        choice_number=0
    elif choice_name=="ʷ����":
        choice_number=1
    elif choice_name=="ֽ":
        choice_number=2
    elif choice_name=="����":
        choice_number=3
    elif choice_name=="����":
        choice_number=4

    return choice_number

    # ʹ��if/elif/else��佫����Ϸ�����Ӧ����ͬ������
    # ��Ҫ���Ƿ��ؽ��

def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        comp_name="ʯͷ"
    elif number==1:
        comp_name="ʷ����"
    elif number==2:
        comp_name="ֽ"
    elif number==3:
        comp_name="����"
    else :
        comp_name="����"
    return comp_name

    # ʹ��if/elif/else��佫��ͬ��������Ӧ����Ϸ�Ĳ�ͬ����
    # ��Ҫ���Ƿ��ؽ��

     #��дִ�д���,������ɺ�passɾ��


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��
    """
    player_choice=choice_name

    player_choice_number=name_to_number(player_choice)

    comp_number=random.randrange(0,5)

    comp_choice=number_to_name(comp_number)

    print("�������ѡ��Ϊ",comp_choice)

    if player_choice_number==0:

        #�û�ѡ��Ϊʯͷ

        if comp_number==0:
            print("���ͼ��������һ����")
        elif comp_number== 3:
            print("��Ӯ��")
        elif comp_number== 4:
            print("��Ӯ��")
        elif comp_number== 2:
            print("�����Ӯ��")
        elif comp_number== 1:
            print("�����Ӯ��")


    elif player_choice_number==1:

        #�û�ѡ��Ϊʷ����

        if comp_number ==1:
            print("���ͼ��������һ����")
        elif comp_number == 4:
            print("��Ӯ��")
        elif comp_number == 0:
            print("��Ӯ��")
        elif comp_number == 3:
            print("�����Ӯ��")
        elif comp_number == 2:
            print("�����Ӯ��")

    elif player_choice_number==2:

        #�û�ѡ��Ϊֽ

        if comp_number ==2:
            print("���ͼ��������һ����")
        elif comp_number== 1:
            print("��Ӯ��")
        elif comp_number == 0:
            print("��Ӯ��")
        elif comp_number == 3:
            print("�����Ӯ��")
        elif comp_number == 4:
            print("�����Ӯ��")

    elif player_choice_number==3:

        #�û�ѡ��Ϊ����

        if comp_number ==3:
            print("���ͼ��������һ����")
        elif comp_number == 1:
            print("��Ӯ��")
        elif comp_number == 2:
            print("��Ӯ��")
        elif comp_number == 0:
            print("�����Ӯ��")
        elif comp_number == 4:
            print("�����Ӯ��")

    elif player_choice_number==4:

        #�û�ѡ��Ϊ����

        if comp_number==4:
            print("���ͼ��������һ����")
        elif comp_number == 3:
            print("��Ӯ��")
        elif comp_number == 2:
            print("��Ӯ��")
        elif comp_number == 0:
            print("�����Ӯ��")
        elif comp_number == 4:
            print("�����Ӯ��")






    # ���"-------- "���зָ�
    # ��ʾ�û�������ʾ���û�ͨ�����̽��Լ�����Ϸѡ��������룬�������player_choice

    # ����name_to_number()�������û�����Ϸѡ�����ת��Ϊ��Ӧ���������������player_choice_number

    # ����random.randrange()�Զ�����0-4֮��������������Ϊ��������ѡ�����Ϸ���󣬴������comp_number

    # ����number_to_name()����������������������ת��Ϊ��Ӧ����Ϸ����

    # ����Ļ����ʾ�����ѡ����������

    # ����if/elif/else ��䣬����RPSLS������û�ѡ��ͼ����ѡ������жϣ�������Ļ����ʾ�жϽ��

    # ����û��ͼ����ѡ��һ��������ʾ�����ͼ��������һ���ء�������û���ʤ������ʾ����Ӯ�ˡ�����֮����ʾ�������Ӯ�ˡ�




# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
if choice_name == "ʯͷ" or choice_name == "����" or choice_name == "ֽ" or choice_name == "ʷ����" or choice_name == "����":
    rpsls(choice_name)
else:
    print("Error: No Correct Name")







