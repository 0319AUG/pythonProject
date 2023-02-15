students_data = []
filename = "学生成绩录入汇总.txt"


def main():
    n = open(filename, "a+")
    n.close()
    with open(filename, "r") as f:
        gather = f.readlines()
        for msg in gather:
            students_data.append(eval(msg))

    while True:
        # 开始选择界面
        print("进入管理系统\n1:录入\n2:删除\n3:修改\n4:统计总数\n5:显示所有\n6：排序\n7:查找\n8:退出")
        choice = input("请输入选择数字：")

        # 选择录入
        if choice == "1":
            enter()

            while True:
                choice = input("是否继续录入：(y/n):")
                if choice == "y":
                    enter()
                elif choice == "n":
                    print("退出录入")
                    break
                else:
                    print("无效字符")

        # 选择删除
        elif choice == "2":
            delete()

            while True:
                choice = input("是否继续删除：（y/n）")
                if choice == "y":
                    delete()
                elif choice == "n":
                    print("退出删除")
                    break
                else:
                    print("无效字符")

        # 选择修改
        elif choice == "3":
            change()

            while True:
                choice = input("是否继续修改（y/n）：")
                if choice == "y":
                    change()
                elif choice == "n":
                    print("退出修改")
                    break
                else:
                    print("无效字符")

        elif choice == "4":
            count()

        # 显示全部
        elif choice == "5":
            show_all()

        # 选择排序
        elif choice == "6":
            sort()

        # 选择查找
        elif choice == "7":
            find()

            while True:
                choice = input("是否继续查询（y/n）")
                if choice == "y":
                    find()
                elif choice == "n":
                    print("退出查找")
                    break
                else:
                    print("无效字符")

        # 退出系统
        elif choice == "8":
            with open(filename, "w") as f:
                for msg in students_data:
                    f.write(str(msg) + "\n")
            print("退出程序")
            break
        else:
            print("请输入有效数字")


# 录入函数
def enter():
    student_id = input("输入ID：")
    student_name = input("输入姓名：")
    student_english_score = input("输入英语成绩：")
    student_math_score = input("输入数学成绩：")
    student_data = {"student_id": student_id, "student_name": student_name,
                    "student_english_score": student_english_score, "student_math_score": student_math_score}
    students_data.append(student_data)


# 删除函数
def delete():
    method = input("选择ID删除/姓名删除（1/2）：")

    if method == "1":
        del_id = input("请输入要删除的ID：")
        for index, student in enumerate(students_data):
            if student["student_id"] == del_id:
                students_data.pop(index)
    elif method == "2":
        del_name = input("请输入要删除的学生姓名：")
        for index, student in enumerate(students_data):
            if student["student_name"] == del_name:
                students_data.pop(index)


# 修改函数
def change():
    method = input("选择ID/姓名（1/2）：")

    if method == "1":
        change_id = input("输入ID：")
        for index, student in enumerate(students_data):
            if student["student_id"] == change_id:
                modification_item = input("选择修改项目1：ID，2：姓名，3：英语成绩，4：数学成绩：")
                modification_result = input("输入修改后内容：")
                if modification_item == "1":
                    students_data[index]["student_id"] = modification_result
                elif modification_item == "2":
                    students_data[index]["student_name"] = modification_result
                elif modification_item == "3":
                    students_data[index]["student_english_score"] = modification_result
                elif modification_item == "4":
                    students_data[index]["student_math_score"] = modification_result
            # else:
            #     print("无效ID")
    elif method == "2":
        change_name = input("输入姓名：")
        for index, student in enumerate(students_data):
            if student["student_name"] == change_name:
                modification_item = input("选择修改项目1：ID，2：姓名，3：英语成绩，4：数学成绩：")
                modification_result = input("输入修改后内容：")
                if modification_item == "1":
                    students_data[index]["student_id"] = modification_result
                elif modification_item == "2":
                    students_data[index]["student_name"] = modification_result
                elif modification_item == "3":
                    students_data[index]["student_english_score"] = modification_result
                elif modification_item == "4":
                    students_data[index]["student_math_score"] = modification_result
            # else:
            #     print("姓名无效")


def count():
    print(len(students_data))


def show_all():
    for msg in students_data:
        print(msg)


def find():
    method = input("ID/姓名：（1/2）")

    if method == "1":
        find_id = input("输入查找的ID：")
        for student in students_data:
            if student["student_id"] == find_id:
                print(student)
    elif method == "2":
        find_name = input("输入查找姓名：")
        for student in students_data:
            if student["student_name"] == find_name:
                print(student)


def sort():
    sorted_subject = input("选择排序依据（1：ID，2：姓名，3：英语成绩，4：数学成绩）：")
    if sorted_subject == "1":
        print(sorted(students_data, key=lambda x: x["student_id"]))
    elif sorted_subject == "2":
        print(sorted(students_data, key=lambda x: x["student_name"]))
    elif sorted_subject == "3":
        print(sorted(students_data, key=lambda x: x["student_english_score"], reverse=True))
    elif sorted_subject == "4":
        print(sorted(students_data, key=lambda x: x["student_math_score"], reverse=True))


if __name__ == '__main__':
    main()
