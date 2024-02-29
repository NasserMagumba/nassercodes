number_of_classes=int(input("Enter the number of classes attended: "))

attendance_percentage=0.75
percentage_of_classes_attended=0
medical_cause=""
percentage_of_classes_attended=int(number_of_classes*1.00)

if percentage_of_classes_attended>=0.75:
    print(f"percentage of classes attended: {percentage_of_classes_attended}")
    print("student is allowed to attend the exam")
    if medical_cause and percentage_of_classes_attended<0.75:
        medical_cause=input("Enter medical cause: ")
        print("student is allowed to attend the exam")
    else:
        print("student not allowed to attend the exam")
else:
    print("not allowed to attend the exam")


